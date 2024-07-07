"""
String editor UI.
"""

from typing import Optional

import wx
from wx import Window, CommandEvent, ActivateEvent

from whacked4 import config
from whacked4.ui import windows


class StringDialog(windows.StringDialogBase):
    """
    This dialog displays a string to be edited by the user.
    """

    def __init__(self, parent: Window):
        windows.StringDialogBase.__init__(self, parent)

        self.SetEscapeId(windows.STRING_CANCEL)

        self.Original.SetFont(config.FONT_MONOSPACED)
        self.New.SetFont(config.FONT_MONOSPACED)

        self.engine_string: Optional[str] = None
        self.old_string: Optional[str] = None
        self.new_string: Optional[str] = None
        self.extended: bool = False
        self.max_length: int = 0

    def set_state(
        self,
        engine_string: str,
        old_string: str,
        extended: bool,
        name: str,
        cheat: bool = False
    ):
        """
        Sets a new state for this string dialog.
        """

        self.engine_string = engine_string
        self.old_string = old_string
        self.extended = extended

        # Set displayed text.
        self.Original.ChangeValue(engine_string)
        self.New.ChangeValue(old_string)

        if cheat:
            self.SetLabel(f'Cheat - {name}')
            self.New.SetWindowStyleFlag(wx.TE_DONTWRAP)
        else:
            self.SetLabel(f'String - {name}')
            self.New.SetWindowStyleFlag(
                wx.TE_MULTILINE |
                wx.TE_DONTWRAP |
                wx.TE_PROCESS_ENTER |
                wx.TE_PROCESS_TAB
            )

        if extended:
            self.max_length = 0
            self.CharsLeft.Hide()
        else:
            # Non-extended string lengths are limited by the padding room in the executable.
            # Rounded to the next multiple of 4, excluding the terminating NULL character.
            if cheat:
                self.max_length = len(engine_string)
            else:
                self.max_length = self.get_max_string_length(len(engine_string))

            self.CharsLeft.Show()

        self.update_length()

        self.New.SelectAll()
        self.New.SetFocus()

    def get_max_string_length(self, original_len: int) -> int:
        """
        Calculate the maximum allowed string length.

        Source: Chocolate Doom

        :param original_len: length in the original engine string

        :return: maximmum allowed length that can be stored inside the executable
        """

        # Enough bytes for the string and the NUL terminator
        max_len = original_len + 1

        # All strings in doom.exe are on 4-byte boundaries, so we may be able
        # to support a slightly longer string. Extend up to the next 4-byte boundary
        max_len += (4 - (max_len % 4)) % 4

        # Less one for the NUL terminator.
        return max_len - 1

    def text_enter(self, event: CommandEvent):
        """
        Called when text is entered.
        """

        self.update_length()
        event.Skip()

    def update_length(self):
        """
        Updates the amount of characters left.
        """

        if self.extended:
            return

        text = self.New.GetValue()
        chars_left = self.max_length - len(text)

        # Plural formatting.
        if abs(chars_left) == 1:
            plural = ''
        else:
            plural = 's'

        if chars_left < 0:
            chars_left = abs(chars_left)
            label = f'{chars_left} character{plural} too many'
        else:
            if chars_left == 0:
                chars_left = 'No more'
            label = f'{chars_left} character{plural} left'

        self.CharsLeft.SetLabel(label)
        self.ButtonOk.Enable(self.is_new_length_valid())

    def activate(self, event: ActivateEvent):
        self.New.SetFocus()

    def is_new_length_valid(self) -> bool:
        """
        Returns if a new text control length is a valid length.
        """

        if self.extended:
            return True

        text = self.New.GetValue()
        return len(text) <= self.max_length

    def ok(self, event: CommandEvent):
        if not self.is_new_length_valid():
            return

        self.new_string = self.New.GetValue()
        self.EndModal(0)

    def cancel(self, event: CommandEvent):
        self.new_string = None
        self.EndModal(0)
