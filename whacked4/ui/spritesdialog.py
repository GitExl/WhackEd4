from ui import windows, utils
import wx

class SpritesDialog(windows.SpritesDialogBase):

    def __init__(self, parent):
        windows.SpritesDialogBase.__init__(self, parent)
        
        self.missing = wx.Bitmap('res/icon-missing.bmp', wx.BITMAP_TYPE_BMP)
        
        self.patch = self.GetParent().patch
        self.pwads = self.GetParent().pwads
        self.sprite = None
        
        self.build_filter('')
        
        self.selected_sprite = -1
        self.selected_frame = -1
        
        
    def cancel(self, event):
        self.Hide()
        
        
    def ok(self, event):
        window = self.FindWindowById(windows.SPRITES_NAMES)
        
        selections = window.GetSelections() 
        if len(selections) > 0:
            self.selected_sprite = self.filter_list[selections[0]]
            
            # Store the frame index if one was selected.
            frame_index = self.FrameIndex.GetValue()
            if frame_index == '':
                self.selected_frame = -1
            else:
                self.selected_frame = int(frame_index)
        else:
            self.selected_sprite = -1
            self.selected_frame = -1
                 
        self.Hide()
        
        
    def select(self, event):
        self.FrameIndex.SetValue('0')
        self.update_preview()
        
        
    def update_preview(self):
        selected = self.SpriteNames.GetSelection()
        if selected != wx.NOT_FOUND:
            sprite_name = self.SpriteNames.GetString(selected)
            sprite_frame = self.FrameIndex.GetValue()
            if sprite_frame != '':
                sprite_frame = int(sprite_frame)
            
                # Refresh sprite preview with new sprite.
                self.sprite = None
                if len(self.pwads) > 0:
                    sprite_lump = self.pwads.get_sprite(sprite_name, sprite_frame, 0)
                    if sprite_lump is None:
                        sprite_lump = self.pwads.get_sprite(sprite_name, sprite_frame, 1)
                    else:
                        self.sprite = self.pwads.get_sprite_bitmap(sprite_lump)
        
        self.SpritePreview.Refresh()
            
    
    def paint_preview(self, event):
        dc = wx.PaintDC(self.SpritePreview)
        dc.Clear()
        
        size = self.SpritePreview.GetSizeTuple()
        if self.sprite is not None:
            x = size[0] / 2 - self.sprite.width / 2
            y = size[1] * 0.7 - self.sprite.height
            x + self.sprite.left
            y + self.sprite.top
            dc.DrawBitmap(self.sprite.bitmap, x, y, True)
            
        else:
            x = size[0] / 2 - self.missing.GetWidth() / 2
            y = size[1] / 2 - self.missing.GetHeight() / 2
            dc.DrawBitmap(self.missing, x, y, True)
        
        
    def set_state(self, sprite_index, frame_index=None):
        self.Filter.SetValue('')
        
        self.selected_sprite = sprite_index
        self.SpriteNames.Select(sprite_index)
        
        if frame_index is not None:
            self.selected_frame = frame_index
            self.FrameIndex.ChangeValue(str(frame_index))
        else:
            self.selected_frame = -1
            self.FrameIndex.ChangeValue('')
        
        self.Filter.SetFocus()
        self.update_preview()
        
    
    def update_frame(self, event):
        window_id = event.GetId() 
        window = self.FindWindowById(window_id)
        value = utils.validate_numeric(window)

        if value < 0:
            value = 0
        elif value > 29:
            value = 29
            
        if str(value) != window.GetValue():
            window.ChangeValue(str(value))
            
        self.update_preview()
            
            
    def spin_up(self, event):
        if self.FrameIndex.GetValue() == '':
            self.FrameIndex.SetValue('0')
        else:    
            index = int(self.FrameIndex.GetValue())
            self.FrameIndex.SetValue(str(index + 1))
    
    
    def spin_down(self, event):
        if self.FrameIndex.GetValue() == '':
            self.FrameIndex.SetValue('0')
        else:    
            index = int(self.FrameIndex.GetValue())
            self.FrameIndex.SetValue(str(index - 1))
        
        
    def filter_key(self, event):
        key = event.GetKeyCode()
        list_index = self.SpriteNames.GetSelection()
        
        if key == 315:
            list_index -= 1
            if list_index < 0:
                list_index = 0
            self.SpriteNames.Select(list_index)
            self.update_preview()
            
        elif key == 317:
            list_index += 1
            if list_index >= self.SpriteNames.GetCount():
                list_index = self.SpriteNames.GetCount() - 1
            self.SpriteNames.Select(list_index)
            self.update_preview()
            
        event.Skip()
        
        
    def update_filter(self, event):
        window = self.FindWindowById(event.GetId())
        self.build_filter(window.GetValue().upper())
        
    
    def build_filter(self, filter_string):
        index = 0
        self.filter_list = []
        for name in self.patch.sprite_names:
            if name.startswith(filter_string):
                self.filter_list.append(index)
            index += 1
        
        list_index = 0
        self.SpriteNames.Clear()
        for index in self.filter_list:
            self.SpriteNames.Insert(self.patch.sprite_names[index], list_index)
            list_index += 1
            
        if len(self.filter_list) > 0:
            self.SpriteNames.Select(0)
        
        self.update_preview()
    
    
    def focus_text(self, event):
        utils.focus_text(event, self)
        event.Skip()