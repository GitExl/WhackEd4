#!/usr/bin/env python
#coding=utf8

from ui import windows


class StringDialog(windows.StringDialogBase):
    """
    This dialog displays a string to be edited by the user.
    """

    def __init__(self, parent):
        windows.StringDialogBase.__init__(self, parent)

        self.engine_string = None
        self.old_string = None
        self.new_string = None
        self.extended = False
        self.max_length = 0


    def set_state(self, engine_string, old_string, extended):
        """
        Sets a new state for this string dialog.
        """
        
        self.engine_string = engine_string
        self.old_string = old_string
        self.extended = extended
        
        # Set displayed text.
        self.Original.ChangeValue(engine_string)
        self.New.ChangeValue(old_string)
        
        if extended == True:
            self.max_length = 0
            self.New.SetMaxLength(0)
            self.CharsLeft.Hide()
        else:
            # Non-extended string lengths are limited by the padding room in the executable.
            self.max_length = int((len(old_string) / 4.0) * 4) + 3
            self.New.SetMaxLength(self.max_length)
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
        
        if self.extended == True:
            return
        
        text = self.New.GetValue()
        chars_left = self.max_length - len(text)
        
        # Plural formatting.
        if chars_left == 1:
            plural = ''
        else:
            plural = 's'
        if chars_left == 0:
            chars_left = 'No'
            
        self.CharsLeft.SetLabel('{} character{} left'.format(chars_left, plural))

        
    def ok(self, event):
        self.new_string = self.New.GetValue()
        self.Hide()
        
    def cancel(self, event):
        self.new_string = None
        self.Hide()