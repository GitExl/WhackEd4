#!/usr/bin/env python
#coding=utf8

from whacked4.ui import windows

import whacked4.config as config

import wx


class StringDialog(windows.StringDialogBase):
    """
    This dialog displays a string to be edited by the user.
    """

    def __init__(self, parent):
        windows.StringDialogBase.__init__(self, parent)

        self.SetEscapeId(windows.STRING_CANCEL)

        self.Original.SetFont(config.FONT_MONOSPACED)
        self.New.SetFont(config.FONT_MONOSPACED)

        self.engine_string = None
        self.old_string = None
        self.new_string = None
        self.extended = False
        self.max_length = 0

    def set_state(self, engine_string, old_string, extended, name, cheat=False):
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
            self.SetLabel('Cheat - {}'.format(name))
            self.New.SetWindowStyleFlag(wx.TE_DONTWRAP)
        else:
            self.SetLabel('String - {}'.format(name))
            self.New.SetWindowStyleFlag(wx.TE_MULTILINE | wx.TE_DONTWRAP | wx.TE_PROCESS_ENTER | wx.TE_PROCESS_TAB)

        if extended:
            self.max_length = 0
            self.CharsLeft.Hide()
        else:
            # Non-extended string lengths are limited by the padding room in the executable.
            # Rounded to the next multiple of 4, excluding the terminating NULL character.
            if cheat:
                self.max_length = len(engine_string)
            else:
                self.max_length = len(engine_string) + (4 - (len(engine_string) % 4)) - 1

            self.CharsLeft.Show()

        self.update_length()

        self.New.SelectAll()
        self.New.SetFocus()

    def text_enter(self, event):
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
            label = '{} character{} too many'.format(abs(chars_left), plural)
        else:
            if chars_left == 0:
                chars_left = 'No more'
            label = '{} character{} left'.format(chars_left, plural)

        self.CharsLeft.SetLabel(label)
        self.ButtonOk.Enable(self.is_new_length_valid())

    def activate(self, event):
        self.New.SetFocus()

    def is_new_length_valid(self):
        if self.extended:
            return True

        text = self.New.GetValue()
        return len(text) <= self.max_length

    def ok(self, event):
        if not self.is_new_length_valid():
            return

        self.new_string = self.New.GetValue()
        self.EndModal(0)

    def cancel(self, event):
        self.new_string = None
        self.EndModal(0)
