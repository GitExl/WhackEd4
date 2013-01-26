#!/usr/bin/env python
#coding=utf8

"""
General utility functions.
"""


def validate_numeric(window):
    """
    Validates the contents of a window (usually a text control), to make sure it is numeric.
    
    The window's contents are altered if the user entered any non-numeric input. 0 is returned if only a minus sign
    is present in the control, to allow the user to enter negative numbers.

    @return: the validated integer value that is present in the control.
    """
    
    value = window.GetValue()
    
    if len(value) == 0:
        return 0

    # Handle negative values.        
    if value.startswith('-') == True:
        # If the value contains more than just a minus sign, attempt to get the integer value.
        if len(value) > 1:
            if value[1:].isnumeric() == False:
                value = 0
            else:
                value = int(value)
        
        # Otherwise directly return 0 as a temporary value until the user finishes entering a valid value.
        else:
            return 0
    
    else:
        # Non-numeric values are set to 0.
        if value.isnumeric() == False:
            value = 0
        
        # Others are parsed.
        else:
            value = int(value)
    
    # Update the text control if the validated value is now different.
    if str(value) != window.GetValue():
        window.ChangeValue(str(value))
        
    return value


def focus_text(event, parent):
    """
    Selects the entire contents of a text control so that the user can immediately type to replace it.
    """
    
    window = parent.FindWindowById(event.GetId())
    window.SetSelection(-1, -1)
    
    
def sound_play(name, pwads):
    """
    Plays back a sound.
    """
    
    if pwads is None:
        return
    
    name = 'DS' + name.upper()
    sound_data = pwads.get_sound(name)
    if sound_data != None:
        sound_data.play()
