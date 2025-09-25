"""
General utility functions.
"""

import sys
import wx

from whacked4.doom.wadlist import WADList


def validate_numeric(window: wx.TextCtrl) -> int:
    """
    Validates the contents of a window (usually a text control), to make sure it
    is numeric.

    The window's contents are altered if the user entered any non-numeric input. 0 is
    returned if only a minus sign is present in the control, to allow the user to
    enter negative numbers.

    @return: the validated integer value that is present in the control.
    """

    value = window.GetValue()

    if len(value) == 0:
        return 0

    # Handle negative values.
    if value.startswith('-'):
        # If the value contains more than just a minus sign, attempt to get the integer value.
        if len(value) > 1:
            if not value[1:].isnumeric():
                value = 0
            else:
                value = int(value)

        # Otherwise directly return 0 as a temporary value until the user finishes entering
        # a valid value.
        else:
            return 0

    else:
        # Non-numeric values are set to 0.
        if not value.isnumeric():
            value = 0

        # Others are parsed.
        else:
            value = int(value)

    # Update the text control if the validated value is now different.
    if str(value) != window.GetValue():
        window.ChangeValue(str(value))

    return value


def validate_numeric_float(window: wx.TextCtrl) -> float:
    """
    Validates the contents of a window (usually a text control), to make sure it is
    numeric, and floating point.

    The window's contents are altered if the user entered any non-numeric input. 0 is
    returned if only a minus sign is present in the control, to allow the user to
    enter negative numbers.

    @return: the validated floating point value that is present in the control.
    """

    value = window.GetValue()

    if len(value) == 0:
        return 0
    if '.' not in value:
        return validate_numeric(window)
    if value[-1] == '.':
        return 0

    # Handle negative values.
    if value.startswith('-'):

        # If the value contains more than just a minus sign, attempt to get the integer value.
        if len(value) > 1:
            try:
                temp = float(value)
            except ValueError:
                value = 0
            else:
                value = temp

        # Otherwise directly return 0 as a temporary value until the user finishes
        # entering a valid value.
        else:
            return 0

    else:
        try:
            temp = float(value)
        except ValueError:
            value = 0
        else:
            value = temp

    # Update the text control if the validated value is now different.
    if str(value) != window.GetValue():
        window.ChangeValue(str(value))

    return value


def focus_text(event, parent: wx.Window):
    """
    Selects the entire contents of a text control so that the user can immediately
    type to replace it.
    """

    ctrl: wx.TextCtrl = parent.FindWindowById(event.GetId())

    # Select all text if clicked at the end of the text.
    selfrom, selto = ctrl.GetSelection()
    if selfrom == selto == len(ctrl.GetValue()):
        ctrl.SetSelection(-1, -1)


def sound_play(name: str, wadlist: WADList):
    """
    Plays back a sound.
    """

    if wadlist is None:
        return

    app = wx.GetApp()
    if app is None:
        return

    name = 'DS' + name.upper()
    sound_data = wadlist.get_sound(name)
    if sound_data is not None:
        sound_data.play(app.pyaudio_instance)


def mix_colors(color1: wx.Colour, color2: wx.Colour, mix: float) -> wx.Colour:
    """
    Mixes two colors together.

    @param color1: the first color to mix.
    @param color2: the second color to mix.
    @param mix: the mix factor. 0.0 is only color1, 1.0 is only color2, 0.5 is an even mix.
    """

    return wx.Colour(
        int(color1.Red() * (1.0 - mix) + color2.Red() * mix),
        int(color1.Green() * (1.0 - mix) + color2.Green() * mix),
        int(color1.Blue() * (1.0 - mix) + color2.Blue() * mix)
    )


def get_map_name(episode_index: int, map_index: int) -> str:
    """
    Returns a map name from an episode and map index.

    @param episode_index: the index of the episode. If this is 0, a Doom 2 style
    MAPxx name is returned.

    @param map_index: the index of the map.

    @return: a ExMx map name if episode_index is non-zero, a MAPxx name otherwise.
    """

    if episode_index == 0:
        return f'MAP{map_index:0>2}'
    return f'E{episode_index}M{map_index}'


def seconds_to_minutes(seconds: int) -> str:
    """
    Returns a number of seconds formatted as minutes:seconds.
    """

    minutes = int(seconds / 60)
    seconds_left = seconds % 60
    return f'{minutes}:{seconds_left:0>2}'


def file_dialog(
    parent,
    message=wx.FileSelectorPromptStr,
    default_dir=wx.EmptyString,
    default_file=wx.EmptyString,
    wildcard=wx.FileSelectorDefaultWildcardStr,
    style=wx.FD_DEFAULT_STYLE,
    pos=wx.DefaultPosition
):
    """
    Wrapper around the wxWidgets file dialog class.

    @return: the selected file path, or None if the user cancelled.

    @see: http://www.wxpython.org/docs/api/wx.FileDialog-class.html
    """

    dialog = wx.FileDialog(parent, message, default_dir, default_file, wildcard, style, pos)

    result = dialog.ShowModal()
    if result == wx.ID_OK:
        return dialog.GetPath()
    return None


def load_toolbar_bitmap(path: str, target_size: wx.Size = None) -> wx.Bitmap:
    """
    Loads a toolbar bitmap, scaling to target size on Mac to work around
    SetToolBitmapSize limitations.

    @param path: path to the bitmap file
    @param target_size: target size to scale to on Mac (if None, uses original size)
    @return: wx.Bitmap object, potentially scaled on Mac
    """

    bitmap = wx.Bitmap(path, wx.BITMAP_TYPE_ANY)

    # On Mac, scale toolbar icons to target size to work around SetToolBitmapSize issues
    if sys.platform == 'darwin' and target_size is not None:
        new_width = target_size.width
        new_height = target_size.height

        if new_width > 0 and new_height > 0:
            # Create a scaled image
            image = bitmap.ConvertToImage()
            scaled_image = image.Scale(new_width, new_height, wx.IMAGE_QUALITY_HIGH)
            bitmap = wx.Bitmap(scaled_image)

    return bitmap
