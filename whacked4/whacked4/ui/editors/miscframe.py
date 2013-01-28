#!/usr/bin/env python
#coding=utf8

from whacked4 import utils
from whacked4.ui import editormixin, windows
import copy
import wx


class MiscFrame(editormixin.EditorMixin, windows.MiscFrameBase):
    """
    Misc editor window.
    """
    
    # Window Id to property key dict.
    PROPS_VALUES = {
        windows.MISC_START_HEALTH: 'startHealth',
        windows.MISC_START_BULLETS: 'startAmmo',
        windows.MISC_MAX_HEALTH: 'maxHealth',
        windows.MISC_MAX_ARMOR: 'maxArmor',
        windows.MISC_ARMOR_CLASS_GREEN: 'armorClassGreen',
        windows.MISC_ARMOR_CLASS_BLUE: 'armorClassBlue',
        windows.MISC_MAX_SOULSPHERE_HEALTH: 'maxSoulSphereHealth',
        windows.MISC_SOULSPHERE_HEALTH: 'soulSphereHealth',
        windows.MISC_MEGASPHERE_HEALTH: 'megaSphereHealth',
        windows.MISC_GODMODE_HEALTH: 'godModeHealth',
        windows.MISC_IDFA_ARMOR: 'idfaArmor',
        windows.MISC_IDFA_ARMOR_CLASS: 'idfaArmorClass',
        windows.MISC_IDKFA_ARMOR: 'idkfaArmor',
        windows.MISC_IDKFA_ARMOR_CLASS: 'idkfaArmorClass',
        windows.MISC_BFG_AMMO: 'bfgAmmoUsage'
    }
    
    def __init__(self, params):
        windows.MiscFrameBase.__init__(self, params)
        editormixin.EditorMixin.__init__(self)
        
        self.SetIcon(wx.Icon('res/editor-misc.ico'))


    def build(self, patch):
        """
        @see: EditorMixin.build
        """
        
        self.patch = patch
        self.update_properties()
        
        
    def update_properties(self):
        """
        Update all property control values.
        """
        
        for window_id, key in self.PROPS_VALUES.iteritems():
            window = self.FindWindowById(window_id)
            window.ChangeValue(str(self.patch.misc[key]))
        
        data = self.patch.engine.misc_data['monstersInfight']
        value = self.patch.misc['monstersInfight']
        if value == data['on']:
            value = True
        else:
            value = False
        self.MonstersInfight.SetValue(value)
        
        
    def set_value(self, event):
        """
        Validates and sets a misc. property.
        """
                
        self.undo_add()
        
        window_id = event.GetId() 
        window = self.FindWindowById(window_id)
        
        value = utils.validate_numeric(window)
        key = self.PROPS_VALUES[window_id]
        data = self.patch.engine.misc_data[key]
        
        # Clamp values to their data type range.
        if data['type'] == 'int':
            if value < -0x80000000:
                value = -0x80000000
            elif value > 0x80000000:
                value = 0x80000000
        elif data['type'] == 'byte':
            if value < 0:
                value = 0
            elif value > 255:
                value = 255
        window.ChangeValue(str(value))
        
        self.patch.misc[key] = value 
        self.is_modified(True)
        
        
    def set_infight(self, event):
        """
        Sets the monsters infight misc. data.
        """
        
        self.undo_add()
        
        data = self.patch.engine.misc_data['monstersInfight']
        value = self.MonstersInfight.GetValue()
        if value == True:
            value = data['on']
        else:
            value = data['off']
        
        self.patch.misc['monstersInfight'] = value
        
    
    def restore(self, event):
        """
        Restore all misc. values to their engine state.
        """
        
        self.undo_add()
        
        for key in self.PROPS_VALUES.itervalues():
            self.patch.misc[key] = self.patch.engine.misc[key]
        self.patch.misc['monstersInfight'] = self.patch.engine.misc['monstersInfight']
        
        self.update_properties()

        
    def undo_restore_item(self, item):
        """
        @see: EditorMixin.undo_restore_item
        """
        
        self.patch.misc = item
        self.update_properties()
        
        
    def undo_store_item(self):
        """
        @see: EditorMixin.undo_store_item
        """
        
        return copy.deepcopy(self.patch.misc)