#!/usr/bin/env python
#coding=utf8

"""
General utility functions.
"""
import wx


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


def mix_colours(colour1, colour2, mix):
    """
    Mixes two colours together.
    
    @param colour1: the first colour to mix.
    @param colour2: the second colour to mix.
    @param mix: the mix factor. 0.0 is only colour1, 1.0 is only colour2, 0.5 is an even mix.  
    """
    
    colour = wx.Colour(
        int(colour1.Red() * (1.0 - mix) + colour2.Red() * mix),
        int(colour1.Green() * (1.0 - mix) + colour2.Green() * mix),
        int(colour1.Blue() * (1.0 - mix) + colour2.Blue() * mix)
    )
    
    return colour


def get_map_name(episode_index, map_index):
    """
    Returns a map name from an episode and map index.
    
    @param episode_index: the index of the episode. If this is 0, a Doom 2 style MAPxx name is returned.
    @param map_index: the index of the map.
    
    @return: a ExMx map name if episode_index is non-zero, a MAPxx name otherwise.
    """  
    
    if episode_index == 0:
        return 'MAP{:0>2}'.format(map_index)
    else:
        return 'E{}M{}'.format(episode_index, map_index)
    

def seconds_to_minutes(seconds):
    """
    Returns a number of seconds formatted as minutes:seconds.
    """
    
    return '{}:{:0>2}'.format(int(seconds / 60), seconds % 60)


def file_dialog(parent, message=wx.FileSelectorPromptStr, default_dir=wx.EmptyString, default_file=wx.EmptyString,
                     wildcard=wx.FileSelectorDefaultWildcardStr, style=wx.FD_DEFAULT_STYLE, pos=wx.DefaultPosition):
    """
    Wrapper around the wxWidgets file dialog class.
    
    @return: the selected file path, or None if the user cancelled.
    
    @see: http://www.wxpython.org/docs/api/wx.FileDialog-class.html
    """
    
    dialog = wx.FileDialog(parent, message, default_dir, default_file, wildcard, style, pos)

    result = dialog.ShowModal()
    if result == wx.ID_OK:
        return dialog.GetPath()
    else:
        return None