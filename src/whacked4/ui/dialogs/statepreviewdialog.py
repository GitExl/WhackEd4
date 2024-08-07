"""
State preview UI.
"""

from typing import Optional

import time
import random

import wx
from wx import KeyEvent, ActivateEvent, TimerEvent, CloseEvent

from whacked4 import config
from whacked4.dehacked.entry import Entry
from whacked4.dehacked.patch import Patch
from whacked4.doom.wadlist import WADList
from whacked4.ui import windows
from whacked4.utils import sound_play


class StatePreviewDialog(windows.StatePreviewDialogBase):
    """
    This dialog displays an animated preview of a state.
    """

    TICK_INTERVAL: float = 1000 / 35

    def __init__(self, parent):
        windows.StatePreviewDialogBase.__init__(self, parent)

        self.patch: Optional[Patch] = None
        self.pwads: Optional[WADList] = None

        # Thing for sound references.
        self.ref_thing_index: Optional[int] = None
        self.ref_thing: Optional[Entry] = None

        # Weapon for sound\offset references.
        self.ref_weapon_index: Optional[int] = None
        self.ref_weapon: Optional[Entry] = None

        self.first_state_index: int = -1
        self.state_index: int = -1

        # Precise timer data.
        self.timer_prev: int = 0
        self.elapsed: int = 0
        self.ticks: int = 0

        self.Sprite.set_baseline_factor(0.85)
        self.Sprite.set_scale(2)

        self.StateInfo.SetFont(config.FONT_MONOSPACED_BOLD)
        self.StateAction.SetFont(config.FONT_MONOSPACED_BOLD)
        self.StateSound.SetFont(config.FONT_MONOSPACED_BOLD)
        self.SpawnSound.SetFont(config.FONT_MONOSPACED_BOLD)

        self.SetEscapeId(windows.PREVIEW_CLOSE)

        self.Bind(wx.EVT_CHAR_HOOK, self.key_hook)

    def update(self, pwads: WADList):
        """
        Updates the preview WADList for sprites to render from.

        :param pwads: WADList
        """
        self.pwads = pwads

        self.Sprite.set_source(self.pwads)
        self.Sprite.Refresh()

    def key_hook(self, event: KeyEvent):
        """
        Intercepts all key presses.
        """

        # Tilde restarts the animation from the state this dialog was called with.
        if event.GetKeyCode() == 96:
            self.begin_playback(self.first_state_index)
            self.anim_start()
        else:
            event.Skip()

    def begin_playback(self, state_index: int):
        """
        Starts playback from a state. Takes care of moving over 0 duration starting states.
        """

        self.set_state(state_index)
        while self.ticks == 0:
            state = self.patch.states[self.state_index]
            self.set_state(state['nextState'])

    def prepare(
        self,
        pwads: WADList,
        patch: Patch,
        state_index: int,
        thing_index: Optional[int] = None,
        weapon_index: Optional[int] = None
    ):
        """
        Used to prepare a new animation to preview.
        """

        self.pwads = pwads
        self.patch = patch
        self.first_state_index = state_index

        self.ref_thing_index = thing_index
        if thing_index is not None:
            self.ref_thing = patch.things[thing_index]
        else:
            self.ref_thing = None

        if weapon_index is not None:
            self.ref_weapon = patch.weapons[weapon_index]
        else:
            self.ref_weapon = None

        self.Sprite.set_source(pwads)
        self.set_title()
        self.begin_playback(state_index)

    def set_title(self):
        """
        Sets the title based on what is being previews.
        """

        if self.ref_thing is not None:
            title = f'Preview thing - {self.ref_thing.name}'
        elif self.ref_weapon is not None:
            title = f'Preview weapon - {self.ref_weapon.name}'
        else:
            title = 'Preview'

        self.SetLabel(title)

    def activate(self, event: ActivateEvent):
        """
        Window activation event.
        """

        self.anim_start()

    def anim_start(self):
        """
        Starts animation playback from the current state.
        """

        self.timer_prev = time.time()
        self.Timer.Start(1)

    def anim_stop(self):
        """
        Stops animation playback.
        """

        self.Timer.Stop()

    def set_state(self, state_index: int):
        """
        Sets a new state index.
        """

        if state_index <= 1 or state_index >= len(self.patch.states):
            self.ticks = -1
            self.anim_stop()
            return

        state = self.patch.states[state_index]
        sprite_index = state['sprite']
        sprite_name = self.patch.sprite_names[sprite_index]
        sprite_frame = state['spriteFrame'] & 0x3FFF

        offset_x = 0
        offset_y = 0

        # Weapons are rendered offset from the center.
        if self.ref_weapon and state['unused1'] != 0:
            offset_x = state['unused1'] / 65536
            offset_y = state['unused2'] / 65536

        self.Sprite.show_sprite(sprite_name, sprite_frame, offset_x, offset_y)

        frame_name = chr(65 + sprite_frame)
        self.StateIndex.SetLabel(str(state_index))
        self.StateInfo.SetLabel(f'{sprite_name}{frame_name}')

        self.do_state_action(state)

        self.state_index = state_index
        self.ticks = state['duration']

    def do_state_action(self, state):
        """
        Execute actions for a state such as playing sounds.

        :param state:
        """

        action_label = ''

        sound_label = ''
        sound_index = None

        spawn_sound_label = ''
        spawn_sound_index = None

        if state['action'] is not None:
            action_key = state['action']
            action = self.patch.engine.actions[action_key]
            action_label = action.name

            # Support for RandomJump action that takes parameters to jump to a random next state.
            if state['action'] == 'RandomJump' and random.randint(0, 255) < state['unused2']:
                self.set_state(state['unused1'])
                return

            # Queue a sound for this action.
            if action.sound is not None:
                parts = action.sound.split(':')
                if len(parts) != 2:
                    raise RuntimeError(f'Invalid sound for action "{action_key}".')

                if parts[0] == 'sound':
                    sound_index = int(parts[1])

                elif parts[0] == 'thing':
                    if self.ref_thing_index is not None:
                        sound_index = self.ref_thing[parts[1]]
                    else:
                        sound_label = f'{parts[0]}:{parts[1]}'

                elif parts[0] == 'state':
                    sound_index = state[parts[1]]

            # Action spawns a thing.
            if action.spawns is not None:
                thing = self.patch.things[action.spawns]
                spawn_sound_index = thing['soundAlert']

            # Playback sounds for this action. Any specific sound overrides a spawned thing sound.
            if sound_index is not None:
                sound_play(self.patch.sounds[sound_index - 1].name, self.pwads)
                sound_label = self.patch.sounds[sound_index - 1].name
            elif spawn_sound_index is not None:
                sound_play(self.patch.sounds[spawn_sound_index - 1].name, self.pwads)
                spawn_sound_label = self.patch.sounds[spawn_sound_index - 1].name

        self.StateAction.SetLabel(action_label)
        self.SpawnSound.SetLabel(spawn_sound_label.upper())
        self.StateSound.SetLabel(sound_label.upper())

    def timer(self, event: TimerEvent):
        """
        Timer event.
        """

        # Figure out the exact time that has passed since the last call to this event.
        # The Timer control may not be precise enough in it's timing, so we rely on Python's
        # time.time() for more accurate time accounting.
        self.elapsed += (time.time() - self.timer_prev) * 1000
        self.timer_prev = time.time()

        # If too much time has passed since the previous event, just do a single tick to
        # prevent needless updating.
        if self.elapsed > 3000:
            self.elapsed = self.TICK_INTERVAL

        # Keep ticking until all elapsed time has been ticked through.
        while self.elapsed >= self.TICK_INTERVAL:
            self.elapsed -= self.TICK_INTERVAL
            self.advance_tick()

    def advance_tick(self):
        """
        Advances the animation a single tick.
        """

        self.ticks -= 1
        while self.ticks == 0:
            state = self.patch.states[self.state_index]
            self.set_state(state['nextState'])

    def close(self, event: CloseEvent):
        """
        Close event.
        """

        self.anim_stop()
        self.EndModal(0)
