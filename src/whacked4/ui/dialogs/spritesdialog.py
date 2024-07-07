from whacked4 import utils, config
from whacked4.ui import windows
import wx


class SpritesDialog(windows.SpritesDialogBase):
    """
    This dialog displays a list of sprites and sprite frames, and lets the user select one of them.
    """

    def __init__(self, parent):
        windows.SpritesDialogBase.__init__(self, parent)

        self.SetEscapeId(windows.SPRITES_CANCEL)

        self.selected_sprite = None
        self.selected_frame = None

        self.patch = None
        self.pwads = None

        self.SpritePreview.set_baseline_factor(0.85)
        self.SpritePreview.set_scale(2)

        self.SpriteNames.SetFont(config.FONT_MONOSPACED)

        self.filter_list = None

    def activate(self, event):
        """
        Called when the dialog is activated.
        """

        self.Filter.SetFocus()

    def ok(self, event):
        """
        Called when the user clicks the Ok button.
        """

        # Store selected details.
        selection = self.SpriteNames.GetFirstSelected()
        if selection == -1:
            return

        else:
            self.selected_sprite = self.filter_list[selection]

            # Store the frame index if one was selected.
            frame_index = self.FrameIndex.GetValue()
            if frame_index == '':
                self.selected_frame = -1
            else:
                self.selected_frame = int(frame_index)

        self.EndModal(0)

    def sprite_select_list(self, event):
        """
        Called when a sprite name is selected in the list.
        """

        if self.FrameIndex.GetValue() != '':
            self.FrameIndex.SetValue('0')

        self.update_preview()

    def sprite_select_index(self, list_index):
        """
        Selects a sprite name from the list based on a list index.
        """

        if list_index < 0:
            list_index = 0
        elif list_index >= self.SpriteNames.GetItemCount():
            list_index = self.SpriteNames.GetItemCount() - 1

        self.SpriteNames.Select(list_index, True)
        self.update_preview()

    def update_preview(self):
        """
        Updates the displayed sprite.
        """

        selected = self.SpriteNames.GetFirstSelected()
        if selected != wx.NOT_FOUND:
            sprite_name = self.SpriteNames.GetItemText(selected, 0)
            sprite_frame = self.FrameIndex.GetValue()
            if sprite_frame != '':
                sprite_frame = int(sprite_frame)
            else:
                sprite_frame = 0

            self.SpritePreview.show_sprite(sprite_name, sprite_frame)

    def set_state(self, patch, pwads, sprite_index=None, frame_index=None):
        """
        Sets this dialog's user interface state.
        """

        self.patch = patch
        self.pwads = pwads

        self.selected_sprite = -1
        self.selected_frame = -1

        self.filter_list = None
        self.Filter.ChangeValue('')
        self.filter_build('')

        if sprite_index is not None:
            self.SpriteNames.Select(sprite_index, True)
            self.SpriteNames.EnsureVisible(sprite_index)

        # Set the right frame index, or leave it blank if none was specified.
        if frame_index is not None:
            self.FrameIndex.ChangeValue(str(frame_index))
            self.FrameIndexSpinner.SetValue(frame_index)
        else:
            self.FrameIndex.ChangeValue('')
            self.FrameIndexSpinner.SetValue(0)

        self.Filter.SetFocus()

        self.SpritePreview.set_source(self.pwads)
        self.update_preview()

    def update(self, pwads):
        self.pwads = pwads

        self.SpritePreview.set_source(self.pwads)
        self.update_preview()

    def update_frame(self, event):
        """
        Called when the frame index text control is updated.

        Updates the frame index value, ensuring it is a valid integer.
        """

        window_id = event.GetId()
        window = self.FindWindowById(window_id)

        if window.GetValue() == '':
            return

        value = utils.validate_numeric(window)

        if value < 0:
            value = 0
        elif value >= config.MAX_SPRITE_FRAME:
            value = config.MAX_SPRITE_FRAME - 1

        if str(value) != window.GetValue():
            window.ChangeValue(str(value))

        self.update_preview()

    def filter_key(self, event):
        """
        Called when a key is pressed in the filter text control.

        Catches up and down keys to move through the filter list without giving the names list focus.
        """

        key = event.GetKeyCode()
        list_index = self.SpriteNames.GetFirstSelected()
        if list_index == -1:
            event.Skip()
            return

        # Move selection up.
        if key == wx.WXK_UP:
            self.sprite_select_index(list_index - 1)

        # Move selection down.
        elif key == wx.WXK_DOWN:
            self.sprite_select_index(list_index + 1)

        event.Skip()

    def filter_build(self, filter_string):
        """
        Builds a newly filtered sprite list.
        """

        # Create a filtered list of sprite name indices.
        self.filter_list = []
        for index, name in enumerate(self.patch.sprite_names):
            if name.startswith(filter_string):
                self.filter_list.append(index)

        # Prepare sprite names list.
        self.SpriteNames.ClearAll()
        client_width = self.SpriteNames.GetClientSize()[0] - 20
        self.SpriteNames.InsertColumn(0, 'Name', width=client_width)

        # Add the filtered sprite names to the names list.
        for index in self.filter_list:
            self.SpriteNames.InsertItem(index, self.patch.sprite_names[index])

        # Select the first item by default.
        if len(self.filter_list) > 0:
            self.SpriteNames.Select(0, True)

        self.update_preview()

    def frameindex_set(self, modifier):
        """
        Modifies the frame index value by a specified amount.
        """

        if self.FrameIndex.GetValue() == '':
            self.FrameIndex.SetValue('0')

        index = int(self.FrameIndex.GetValue())
        self.FrameIndex.SetValue(str(index + modifier))

    def frameindex_spin_up(self, event):
        self.frameindex_set(1)

    def frameindex_spin_down(self, event):
        self.frameindex_set(-1)

    def focus_text(self, event):
        utils.focus_text(event, self)
        event.Skip()

    def cancel(self, event):
        self.EndModal(0)

    def filter_update(self, event):
        window = self.FindWindowById(event.GetId())
        self.filter_build(window.GetValue().upper())
