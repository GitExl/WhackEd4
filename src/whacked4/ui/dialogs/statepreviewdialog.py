#!/usr/bin/env python
#coding=utf8

from whacked4.ui import windows

import wx
import time


class StatePreviewDialog(windows.StatePreviewDialogBase):
    """
    This dialog displays an animated preview of a state.
    """

    TICK_INTERVAL = 1000 / 35

    def __init__(self, parent, pwads):
        windows.StatePreviewDialogBase.__init__(self, parent)

        self.patch = None

        self.first_state_index = -1
        self.state_index = -1

        # Precise timer data.
        self.timer_prev = time.time()
        self.elapsed = 0
        self.ticks = 0

        self.Sprite.set_source(pwads)
        self.Sprite.set_baseline_factor(0.75)
        self.Sprite.set_scale(2)

        self.SetEscapeId(windows.PREVIEW_CLOSE)

        self.Bind(wx.EVT_CHAR_HOOK, self.key_hook)

    def key_hook(self, event):
        """
        Intercepts all key presses.
        """

        # Tilde restarts the animation from the state this dialog was called with.
        if event.GetKeyCode() == 96:
            self.set_state(self.first_state_index)
            self.anim_start()
        else:
            event.Skip()

    def prepare(self, patch, state_index):
        """
        Used to prepare a new animation to preview.
        """

        self.patch = patch
        self.first_state_index = state_index
        self.set_state(state_index)

    def activate(self, event):
        """
        Window activation event.
        """

        self.anim_start()

    def anim_start(self):
        """
        Starts animation playback from the current state.
        """

        self.timer_prev = time.time()
        self.ticks = 0
        self.Timer.Start(1)
        self.update_tick_info()

    def anim_stop(self):
        """
        Stops animation playback.
        """

        self.Timer.Stop()

    def set_state(self, state_index):
        """
        Sets a new state index.
        """

        if state_index <= 1 or state_index >= len(self.patch.states):
            self.anim_stop()

        else:
            state = self.patch.states[state_index]
            sprite_index = state['sprite']
            sprite_name = self.patch.sprite_names[sprite_index]
            sprite_frame = state['spriteFrame'] & 0x3FFF

            self.Sprite.show_sprite(sprite_name, sprite_frame)
            self.StateInfo.SetLabel('{}{}'.format(sprite_name, chr(65 + sprite_frame)))

            # States with negative duration play forever, so stop.
            if state['duration'] < 0:
                self.anim_stop()

        self.state_index = state_index

    def timer(self, event):
        """
        Timer event.
        """

        # Figure out the exact time that has passed since the last call to this event.
        # The Timer control may not be precise enough in it's timing, so we rely on Python's time.time() for
        # more accurate time accounting.
        self.elapsed += (time.time() - self.timer_prev) * 1000
        self.timer_prev = time.time()

        # If too much time has passed since the previous event, just do a single tick to prevent needless updating.
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

        state = self.patch.states[self.state_index]

        self.ticks += 1
        if self.ticks >= state['duration']:
            next_state_index = state['nextState']
            self.set_state(next_state_index)
            self.ticks = 0

        self.update_tick_info()

    def update_tick_info(self):
        """
        Update tick info label.
        """

        self.Time.SetLabel('tick {}'.format(self.ticks))

    def close(self, event):
        """
        Close event.
        """

        self.anim_stop()
        self.EndModal(0)
