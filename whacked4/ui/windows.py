# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from ui import spritepreview

WINDOW_MAIN = 1666
MAIN_TOOL_THINGS = 1667
MAIN_TOOL_STATES = 1668
MAIN_TOOL_SOUNDS = 1669
MAIN_TOOL_STRINGS = 1670
MAIN_TOOL_WEAPONS = 1671
MAIN_TOOL_AMMO = 1672
MAIN_TOOL_CHEATS = 1673
MAIN_TOOL_MISC = 1674
MAIN_TOOL_PAR = 1675
MAIN_MENU_THINGS = 1676
MAIN_MENU_STATES = 1677
MAIN_MENU_SOUNDS = 1678
MAIN_MENU_STRINGS = 1679
MAIN_MENU_WEAPONS = 1680
MAIN_MENU_AMMO = 1681
MAIN_MENU_CHEATS = 1682
MAIN_MENU_MISC = 1683
MAIN_MENU_PAR = 1684
FRAME_THINGS = 1685
THING_LIST = 1686
THING_VAL_ID = 1687
THING_VAL_HEALTH = 1688
THING_VAL_SPEED = 1689
THING_VAL_RADIUS = 1690
THING_VAL_HEIGHT = 1691
THING_VAL_DAMAGE = 1692
THING_VAL_REACTIONTIME = 1693
THING_VAL_PAINCHANCE = 1694
THING_VAL_MASS = 1695
THING_FLAGS = 1696
THING_STATE_SPAWN = 1697
THING_STATENAME_SPAWN = 1698
THING_STATESET_SPAWN = 1699
THING_STATE_WALK = 1700
THING_STATENAME_WALK = 1701
THING_STATESET_WALK = 1702
THING_STATE_PAIN = 1703
THING_STATENAME_PAIN = 1704
THING_STATESET_PAIN = 1705
THING_STATE_MELEE = 1706
THING_STATENAME_MELEE = 1707
THING_STATESET_MELEE = 1708
THING_STATE_ATTACK = 1709
THING_STATENAME_ATTACK = 1710
THING_STATESET_ATTACK = 1711
THING_STATE_DEATH = 1712
THING_STATENAME_DEATH = 1713
THING_STATESET_DEATH = 1714
THING_STATE_EXPLODE = 1715
THING_STATENAME_EXPLODE = 1716
THING_STATESET_EXPLODE = 1717
THING_STATE_RAISE = 1718
THING_STATENAME_RAISE = 1719
THING_STATESET_RAISE = 1720
THING_SOUND_ALERT = 1721
THING_SOUNDSET_ALERT = 1722
THING_SOUND_ATTACK = 1723
THING_SOUNDSET_ATTACK = 1724
THING_SOUND_PAIN = 1725
THING_SOUNDSET_PAIN = 1726
THING_SOUND_DEATH = 1727
THING_SOUNDSET_DEATH = 1728
THING_SOUND_ACTIVE = 1729
THING_SOUNDSET_ACTIVE = 1730
THING_RENAME = 1731
THING_RESTORE = 1732
FRAME_STATES = 1733
STATES_SPRITE = 1734
STATES_FRAME = 1735
STATES_FRAMESPIN = 1736
STATES_LIT = 1737
STATES_NEXT = 1738
STATES_DURATION = 1739
STATES_ACTION = 1740
STATES_PARM1 = 1741
STATES_PARM2 = 1742
STATES_FILTER = 1743
STATES_FILTERTOOLS = 1744
STATES_FILTERTOOLS_REFRESH = 1745
FRAME_SOUNDS = 1746
SOUNDS_PRIORITY = 1747
SOUNDS_PRIORITYSPIN = 1748
SOUNDS_SINGULAR = 1749
SOUNDS_RESTORE = 1750
SOUNDS_LIST = 1751
FRAME_STRINGS = 1752
STRINGS_LIST = 1753
FRAME_WEAPONS = 1754
WEAPON_LIST = 1755
WEAPON_AMMOTYPE = 1756
WEAPON_STATE_SELECT = 1757
WEAPON_STATENAME_SELECT = 1758
WEAPON_STATESET_SELECT = 1759
WEAPON_STATE_DESELECT = 1760
WEAPON_STATENAME_DESELECT = 1761
WEAPON_STATESET_DESELECT = 1762
WEAPON_STATE_BOB = 1763
WEAPON_STATENAME_BOB = 1764
WEAPON_STATESET_BOB = 1765
WEAPON_STATE_FIRE = 1766
WEAPON_STATENAME_FIRE = 1767
WEAPON_STATESET_FIRE = 1768
WEAPON_STATE_MUZZLE = 1769
WEAPON_STATENAME_MUZZLE = 1770
WEAPON_STATESET_MUZZLE = 1771
WEAPON_RENAME = 1772
WEAPON_RESTORE = 1773
FRAME_AMMO = 1774
AMMO_LIST = 1775
AMMO_MAXIMUM = 1776
AMMO_PICKUP = 1777
AMMO_RENAME = 1778
AMMO_RESTORE = 1779
FRAME_CHEATS = 1780
CHEATS_LIST = 1781
CHEATS_INFIGHT = 1782
CHEATS_RESTORE = 1783
FRAME_MISC = 1784
MISC_LIST = 1785
MISC_RESTORE = 1786
FRAME_PAR = 1787
PAR_LIST = 1788
PAR_EPISODE = 1789
PAR_MAP = 1790
PAR_TIME = 1791
PAR_RENAME = 1792
PAR_RESTORE = 1793
DIALOG_SPRITES = 1794
SPRITES_NAMES = 1795
SPRITES_FILTER = 1796
SPRITES_FRAME = 1797
SPRITES_FRAMESPIN = 1798
SPRITES_OK = 1799
SPRITES_CANCEL = 1800
DIALOG_PATCHINFO = 1801
PATCHINFO_TOOLBAR = 1802
PATCHINFO_TOOLBAR_ADD = 1803
PATCHINFO_TOOLBAR_REMOVE = 1804
DIALOG_START = 1805
START_NEW = 1806
START_OPEN = 1807
START_RECENT = 1808
START_CANCEL = 1809
DIALOG_ABOUT = 1810
ABOUT_OK = 1811

###########################################################################
## Class MainFrameBase
###########################################################################

class MainFrameBase ( wx.MDIParentFrame ):
	
	def __init__( self, parent ):
		wx.MDIParentFrame.__init__ ( self, parent, id = WINDOW_MAIN, title = u"WhackEd4", pos = wx.DefaultPosition, size = wx.Size( 1024,560 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU|wx.HSCROLL|wx.VSCROLL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.MainToolbar = self.CreateToolBar( wx.TB_FLAT|wx.TB_HORZ_TEXT|wx.TB_NODIVIDER|wx.TB_TEXT|wx.TB_VERTICAL, wx.ID_ANY ) 
		self.MainToolbar.AddLabelTool( MAIN_TOOL_THINGS, u"Things", wx.Bitmap( u"res/icon-weapons.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, wx.EmptyString, wx.EmptyString, None ) 
		
		self.MainToolbar.AddLabelTool( MAIN_TOOL_STATES, u"States", wx.Bitmap( u"res/icon-weapons.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, wx.EmptyString, wx.EmptyString, None ) 
		
		self.MainToolbar.AddLabelTool( MAIN_TOOL_SOUNDS, u"Sounds", wx.Bitmap( u"res/icon-weapons.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, wx.EmptyString, wx.EmptyString, None ) 
		
		self.MainToolbar.AddLabelTool( MAIN_TOOL_STRINGS, u"Strings", wx.Bitmap( u"res/icon-weapons.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, wx.EmptyString, wx.EmptyString, None ) 
		
		self.MainToolbar.AddLabelTool( MAIN_TOOL_WEAPONS, u"Weapons", wx.Bitmap( u"res/icon-weapons.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, wx.EmptyString, wx.EmptyString, None ) 
		
		self.MainToolbar.AddLabelTool( MAIN_TOOL_AMMO, u"Ammo", wx.Bitmap( u"res/icon-weapons.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, wx.EmptyString, wx.EmptyString, None ) 
		
		self.MainToolbar.AddLabelTool( MAIN_TOOL_CHEATS, u"Cheats", wx.Bitmap( u"res/icon-weapons.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, wx.EmptyString, wx.EmptyString, None ) 
		
		self.MainToolbar.AddLabelTool( MAIN_TOOL_MISC, u"Miscellaneous  ", wx.Bitmap( u"res/icon-weapons.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, wx.EmptyString, wx.EmptyString, None ) 
		
		self.MainToolbar.AddLabelTool( MAIN_TOOL_PAR, u"Par times", wx.Bitmap( u"res/icon-weapons.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, wx.EmptyString, wx.EmptyString, None ) 
		
		self.MainToolbar.Realize() 
		
		self.MainMenu = wx.MenuBar( 0 )
		self.MenuFile = wx.Menu()
		self.MenuFileNew = wx.MenuItem( self.MenuFile, wx.ID_ANY, u"New..."+ u"\t" + u"Ctrl+N", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuFile.AppendItem( self.MenuFileNew )
		
		self.MenuFileOpen = wx.MenuItem( self.MenuFile, wx.ID_ANY, u"Open..."+ u"\t" + u"Ctrl+O", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuFile.AppendItem( self.MenuFileOpen )
		
		self.MenuFileOpenAs = wx.MenuItem( self.MenuFile, wx.ID_ANY, u"Open as...", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuFile.AppendItem( self.MenuFileOpenAs )
		
		self.MenuFileSave = wx.MenuItem( self.MenuFile, wx.ID_ANY, u"Save"+ u"\t" + u"Ctrl+S", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuFile.AppendItem( self.MenuFileSave )
		
		self.MenuFileSaveAs = wx.MenuItem( self.MenuFile, wx.ID_ANY, u"Save as..."+ u"\t" + u"Ctrl+Shift+S", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuFile.AppendItem( self.MenuFileSaveAs )
		
		self.MenuFile.AppendSeparator()
		
		self.MenuFileReloadWADs = wx.MenuItem( self.MenuFile, wx.ID_ANY, u"Reload WADs"+ u"\t" + u"CTRL+R", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuFile.AppendItem( self.MenuFileReloadWADs )
		
		self.MenuFile.AppendSeparator()
		
		self.MenuFileRecent = wx.Menu()
		self.MenuFile.AppendSubMenu( self.MenuFileRecent, u"Recent files" )
		
		self.MenuFile.AppendSeparator()
		
		self.MenuFileExit = wx.MenuItem( self.MenuFile, wx.ID_ANY, u"Exit"+ u"\t" + u"Ctrl+Q", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuFile.AppendItem( self.MenuFileExit )
		
		self.MainMenu.Append( self.MenuFile, u"File" ) 
		
		self.MenuEdit = wx.Menu()
		self.MenuEditUndo = wx.MenuItem( self.MenuEdit, wx.ID_ANY, u"Undo"+ u"\t" + u"Ctrl+Z", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuEdit.AppendItem( self.MenuEditUndo )
		
		self.MenuEdit.AppendSeparator()
		
		self.MenuEditCopy = wx.MenuItem( self.MenuEdit, wx.ID_ANY, u"Copy"+ u"\t" + u"Ctrl+C", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuEdit.AppendItem( self.MenuEditCopy )
		
		self.MenuEditPaste = wx.MenuItem( self.MenuEdit, wx.ID_ANY, u"Paste"+ u"\t" + u"Ctrl+V", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuEdit.AppendItem( self.MenuEditPaste )
		
		self.MainMenu.Append( self.MenuEdit, u"Edit" ) 
		
		self.MenuView = wx.Menu()
		self.MenuViewThings = wx.MenuItem( self.MenuView, MAIN_MENU_THINGS, u"Things"+ u"\t" + u"F2", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuView.AppendItem( self.MenuViewThings )
		
		self.MenuViewStates = wx.MenuItem( self.MenuView, MAIN_MENU_STATES, u"States"+ u"\t" + u"F3", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuView.AppendItem( self.MenuViewStates )
		
		self.MenuViewSounds = wx.MenuItem( self.MenuView, MAIN_MENU_SOUNDS, u"Sounds"+ u"\t" + u"F4", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuView.AppendItem( self.MenuViewSounds )
		self.MenuViewSounds.Enable( False )
		
		self.MenuViewStrings = wx.MenuItem( self.MenuView, MAIN_MENU_STRINGS, u"Strings"+ u"\t" + u"F6", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuView.AppendItem( self.MenuViewStrings )
		self.MenuViewStrings.Enable( False )
		
		self.MenuViewWeapons = wx.MenuItem( self.MenuView, MAIN_MENU_WEAPONS, u"Weapons"+ u"\t" + u"F7", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuView.AppendItem( self.MenuViewWeapons )
		self.MenuViewWeapons.Enable( False )
		
		self.MenuViewAmmo = wx.MenuItem( self.MenuView, MAIN_MENU_AMMO, u"Ammo"+ u"\t" + u"F8", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuView.AppendItem( self.MenuViewAmmo )
		self.MenuViewAmmo.Enable( False )
		
		self.MenuViewCheats = wx.MenuItem( self.MenuView, MAIN_MENU_CHEATS, u"Cheats"+ u"\t" + u"F9", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuView.AppendItem( self.MenuViewCheats )
		self.MenuViewCheats.Enable( False )
		
		self.MenuViewMiscellaneous = wx.MenuItem( self.MenuView, MAIN_MENU_MISC, u"Miscellaneous"+ u"\t" + u"F11", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuView.AppendItem( self.MenuViewMiscellaneous )
		self.MenuViewMiscellaneous.Enable( False )
		
		self.MenuViewPar = wx.MenuItem( self.MenuView, MAIN_MENU_PAR, u"Par times"+ u"\t" + u"F12", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuView.AppendItem( self.MenuViewPar )
		self.MenuViewPar.Enable( False )
		
		self.MenuView.AppendSeparator()
		
		self.MenuViewPatchSettings = wx.MenuItem( self.MenuView, wx.ID_ANY, u"Patch settings...", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuView.AppendItem( self.MenuViewPatchSettings )
		
		self.MainMenu.Append( self.MenuView, u"View" ) 
		
		self.MenuHelp = wx.Menu()
		self.MenuHelpAbout = wx.MenuItem( self.MenuHelp, wx.ID_ANY, u"About..."+ u"\t" + u"F1", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuHelp.AppendItem( self.MenuHelpAbout )
		
		self.MainMenu.Append( self.MenuHelp, u"Help" ) 
		
		self.SetMenuBar( self.MainMenu )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.close )
		self.Bind( wx.EVT_TOOL, self.editor_window_tooltoggle, id = MAIN_TOOL_THINGS )
		self.Bind( wx.EVT_TOOL, self.editor_window_tooltoggle, id = MAIN_TOOL_STATES )
		self.Bind( wx.EVT_TOOL, self.editor_window_tooltoggle, id = MAIN_TOOL_SOUNDS )
		self.Bind( wx.EVT_TOOL, self.editor_window_tooltoggle, id = MAIN_TOOL_STRINGS )
		self.Bind( wx.EVT_TOOL, self.editor_window_tooltoggle, id = MAIN_TOOL_WEAPONS )
		self.Bind( wx.EVT_TOOL, self.editor_window_tooltoggle, id = MAIN_TOOL_AMMO )
		self.Bind( wx.EVT_TOOL, self.editor_window_tooltoggle, id = MAIN_TOOL_CHEATS )
		self.Bind( wx.EVT_TOOL, self.editor_window_tooltoggle, id = MAIN_TOOL_MISC )
		self.Bind( wx.EVT_TOOL, self.editor_window_tooltoggle, id = MAIN_TOOL_PAR )
		self.Bind( wx.EVT_MENU, self.file_new, id = self.MenuFileNew.GetId() )
		self.Bind( wx.EVT_MENU, self.file_open, id = self.MenuFileOpen.GetId() )
		self.Bind( wx.EVT_MENU, self.file_open_as, id = self.MenuFileOpenAs.GetId() )
		self.Bind( wx.EVT_MENU, self.file_save, id = self.MenuFileSave.GetId() )
		self.Bind( wx.EVT_MENU, self.file_save_as, id = self.MenuFileSaveAs.GetId() )
		self.Bind( wx.EVT_MENU, self.wads_reload, id = self.MenuFileReloadWADs.GetId() )
		self.Bind( wx.EVT_MENU, self.close, id = self.MenuFileExit.GetId() )
		self.Bind( wx.EVT_MENU, self.edit_undo, id = self.MenuEditUndo.GetId() )
		self.Bind( wx.EVT_MENU, self.edit_copy, id = self.MenuEditCopy.GetId() )
		self.Bind( wx.EVT_MENU, self.edit_paste, id = self.MenuEditPaste.GetId() )
		self.Bind( wx.EVT_MENU, self.editor_window_menutoggle, id = self.MenuViewThings.GetId() )
		self.Bind( wx.EVT_MENU, self.editor_window_menutoggle, id = self.MenuViewStates.GetId() )
		self.Bind( wx.EVT_MENU, self.editor_window_menutoggle, id = self.MenuViewSounds.GetId() )
		self.Bind( wx.EVT_MENU, self.editor_window_menutoggle, id = self.MenuViewStrings.GetId() )
		self.Bind( wx.EVT_MENU, self.editor_window_menutoggle, id = self.MenuViewWeapons.GetId() )
		self.Bind( wx.EVT_MENU, self.editor_window_menutoggle, id = self.MenuViewAmmo.GetId() )
		self.Bind( wx.EVT_MENU, self.editor_window_menutoggle, id = self.MenuViewCheats.GetId() )
		self.Bind( wx.EVT_MENU, self.editor_window_menutoggle, id = self.MenuViewMiscellaneous.GetId() )
		self.Bind( wx.EVT_MENU, self.editor_window_menutoggle, id = self.MenuViewPar.GetId() )
		self.Bind( wx.EVT_MENU, self.view_patch_settings, id = self.MenuViewPatchSettings.GetId() )
		self.Bind( wx.EVT_MENU, self.help_about, id = self.MenuHelpAbout.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def close( self, event ):
		pass
	
	def editor_window_tooltoggle( self, event ):
		pass
	
	
	
	
	
	
	
	
	
	def file_new( self, event ):
		pass
	
	def file_open( self, event ):
		pass
	
	def file_open_as( self, event ):
		pass
	
	def file_save( self, event ):
		pass
	
	def file_save_as( self, event ):
		pass
	
	def wads_reload( self, event ):
		pass
	
	
	def edit_undo( self, event ):
		pass
	
	def edit_copy( self, event ):
		pass
	
	def edit_paste( self, event ):
		pass
	
	def editor_window_menutoggle( self, event ):
		pass
	
	
	
	
	
	
	
	
	
	def view_patch_settings( self, event ):
		pass
	
	def help_about( self, event ):
		pass
	

###########################################################################
## Class ThingFrameBase
###########################################################################

class ThingFrameBase ( wx.MDIChildFrame ):
	
	def __init__( self, parent ):
		wx.MDIChildFrame.__init__ ( self, parent, id = FRAME_THINGS, title = u"Things", pos = wx.DefaultPosition, size = wx.Size( 640,540 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU )
		
		self.SetSizeHintsSz( wx.Size( 640,540 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		Sizer26 = wx.BoxSizer( wx.HORIZONTAL )
		
		ThingNamesChoices = []
		self.ThingNames = wx.ListBox( self, THING_LIST, wx.DefaultPosition, wx.Size( -1,-1 ), ThingNamesChoices, wx.LB_HSCROLL|wx.LB_NEEDED_SB|wx.LB_SINGLE|wx.SUNKEN_BORDER )
		Sizer26.Add( self.ThingNames, 10, wx.EXPAND|wx.FIXED_MINSIZE, 0 )
		
		
		Sizer26.AddSpacer( ( 12, 0), 0, 0, 0 )
		
		Sizer27 = wx.BoxSizer( wx.VERTICAL )
		
		Sizer28 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingIdLabel = wx.StaticText( self, wx.ID_ANY, u"Id", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingIdLabel.Wrap( -1 )
		Sizer28.Add( self.ThingIdLabel, 5, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.ThingId = wx.TextCtrl( self, THING_VAL_ID, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingId.SetMaxLength( 6 ) 
		Sizer28.Add( self.ThingId, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 3 )
		
		
		Sizer27.Add( Sizer28, 0, wx.ALL|wx.EXPAND, 0 )
		
		Sizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingHealthLabel = wx.StaticText( self, wx.ID_ANY, u"Health", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingHealthLabel.Wrap( -1 )
		Sizer1.Add( self.ThingHealthLabel, 5, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.ThingHealth = wx.TextCtrl( self, THING_VAL_HEALTH, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingHealth.SetMaxLength( 6 ) 
		Sizer1.Add( self.ThingHealth, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		Sizer27.Add( Sizer1, 0, wx.EXPAND, 0 )
		
		Sizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingSpeeLabel = wx.StaticText( self, wx.ID_ANY, u"Speed", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingSpeeLabel.Wrap( -1 )
		Sizer2.Add( self.ThingSpeeLabel, 5, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.ThingSpeed = wx.TextCtrl( self, THING_VAL_SPEED, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingSpeed.SetMaxLength( 6 ) 
		Sizer2.Add( self.ThingSpeed, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		Sizer27.Add( Sizer2, 0, wx.EXPAND, 0 )
		
		Sizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingRadiusLabel = wx.StaticText( self, wx.ID_ANY, u"Radius", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingRadiusLabel.Wrap( -1 )
		Sizer3.Add( self.ThingRadiusLabel, 5, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.ThingRadius = wx.TextCtrl( self, THING_VAL_RADIUS, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingRadius.SetMaxLength( 6 ) 
		Sizer3.Add( self.ThingRadius, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		Sizer27.Add( Sizer3, 0, wx.EXPAND, 0 )
		
		Sizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingHeightLabel = wx.StaticText( self, wx.ID_ANY, u"Height", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingHeightLabel.Wrap( -1 )
		Sizer4.Add( self.ThingHeightLabel, 5, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.ThingHeight = wx.TextCtrl( self, THING_VAL_HEIGHT, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingHeight.SetMaxLength( 6 ) 
		Sizer4.Add( self.ThingHeight, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		Sizer27.Add( Sizer4, 0, wx.EXPAND, 0 )
		
		Sizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingDamageLabel = wx.StaticText( self, wx.ID_ANY, u"Damage", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingDamageLabel.Wrap( -1 )
		Sizer5.Add( self.ThingDamageLabel, 5, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.ThingDamage = wx.TextCtrl( self, THING_VAL_DAMAGE, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingDamage.SetMaxLength( 6 ) 
		Sizer5.Add( self.ThingDamage, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		Sizer27.Add( Sizer5, 0, wx.EXPAND, 0 )
		
		Sizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingReactionTimeLabel = wx.StaticText( self, wx.ID_ANY, u"Reaction time", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingReactionTimeLabel.Wrap( -1 )
		Sizer6.Add( self.ThingReactionTimeLabel, 5, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.ThingReactionTime = wx.TextCtrl( self, THING_VAL_REACTIONTIME, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingReactionTime.SetMaxLength( 6 ) 
		Sizer6.Add( self.ThingReactionTime, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		Sizer27.Add( Sizer6, 0, wx.EXPAND, 0 )
		
		Sizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingPainChanceLabel = wx.StaticText( self, wx.ID_ANY, u"Pain chance", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingPainChanceLabel.Wrap( -1 )
		Sizer7.Add( self.ThingPainChanceLabel, 5, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.ThingPainChance = wx.TextCtrl( self, THING_VAL_PAINCHANCE, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingPainChance.SetMaxLength( 6 ) 
		Sizer7.Add( self.ThingPainChance, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		Sizer27.Add( Sizer7, 0, wx.EXPAND, 0 )
		
		Sizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingMassLabel = wx.StaticText( self, wx.ID_ANY, u"Mass", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingMassLabel.Wrap( -1 )
		Sizer8.Add( self.ThingMassLabel, 5, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.ThingMass = wx.TextCtrl( self, THING_VAL_MASS, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingMass.SetMaxLength( 6 ) 
		Sizer8.Add( self.ThingMass, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		Sizer27.Add( Sizer8, 0, wx.EXPAND, 0 )
		
		
		Sizer27.AddSpacer( ( 0, 12), 0, wx.EXPAND, 5 )
		
		ThingFlagsChoices = []
		self.ThingFlags = wx.CheckListBox( self, THING_FLAGS, wx.DefaultPosition, wx.Size( -1,-1 ), ThingFlagsChoices, 0|wx.SUNKEN_BORDER )
		Sizer27.Add( self.ThingFlags, 8, wx.EXPAND|wx.FIXED_MINSIZE, 0 )
		
		
		Sizer26.Add( Sizer27, 10, wx.ALL|wx.EXPAND, 6 )
		
		
		Sizer26.AddSpacer( ( 12, 0), 0, wx.EXPAND, 5 )
		
		bSizer40 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer43 = wx.BoxSizer( wx.VERTICAL )
		
		Sizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingStateSpawnLabel = wx.StaticText( self, wx.ID_ANY, u"Spawn state", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingStateSpawnLabel.Wrap( -1 )
		Sizer9.Add( self.ThingStateSpawnLabel, 12, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateSpawn = wx.TextCtrl( self, THING_STATE_SPAWN, u"318", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.ThingStateSpawn.SetMaxLength( 4 ) 
		Sizer9.Add( self.ThingStateSpawn, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateSpawnName = wx.StaticText( self, THING_STATENAME_SPAWN, u"TROOA", wx.DefaultPosition, wx.Size( 45,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingStateSpawnName.Wrap( -1 )
		self.ThingStateSpawnName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.ThingStateSpawnName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		Sizer9.Add( self.ThingStateSpawnName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateSpawnSet = wx.Button( self, THING_STATESET_SPAWN, u"<", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.ThingStateSpawnSet.SetMinSize( wx.Size( 22,22 ) )
		
		Sizer9.Add( self.ThingStateSpawnSet, 5, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )
		
		
		bSizer43.Add( Sizer9, 1, wx.EXPAND, 5 )
		
		Sizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingStateWalkLabel = wx.StaticText( self, wx.ID_ANY, u"Walk state", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingStateWalkLabel.Wrap( -1 )
		Sizer10.Add( self.ThingStateWalkLabel, 12, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateWalk = wx.TextCtrl( self, THING_STATE_WALK, u"318", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.ThingStateWalk.SetMaxLength( 4 ) 
		Sizer10.Add( self.ThingStateWalk, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateWalkName = wx.StaticText( self, THING_STATENAME_WALK, u"TROOA", wx.DefaultPosition, wx.Size( 45,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingStateWalkName.Wrap( -1 )
		self.ThingStateWalkName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.ThingStateWalkName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		Sizer10.Add( self.ThingStateWalkName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateWalkSet = wx.Button( self, THING_STATESET_WALK, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingStateWalkSet.SetMinSize( wx.Size( 22,22 ) )
		
		Sizer10.Add( self.ThingStateWalkSet, 5, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )
		
		
		bSizer43.Add( Sizer10, 1, wx.EXPAND, 5 )
		
		Sizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingStatePainLabel = wx.StaticText( self, wx.ID_ANY, u"Pain state", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingStatePainLabel.Wrap( -1 )
		Sizer11.Add( self.ThingStatePainLabel, 12, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStatePain = wx.TextCtrl( self, THING_STATE_PAIN, u"318", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.ThingStatePain.SetMaxLength( 4 ) 
		Sizer11.Add( self.ThingStatePain, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStatePainName = wx.StaticText( self, THING_STATENAME_PAIN, u"TROOA", wx.DefaultPosition, wx.Size( 45,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingStatePainName.Wrap( -1 )
		self.ThingStatePainName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.ThingStatePainName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		Sizer11.Add( self.ThingStatePainName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStatePainSet = wx.Button( self, THING_STATESET_PAIN, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingStatePainSet.SetMinSize( wx.Size( 22,22 ) )
		
		Sizer11.Add( self.ThingStatePainSet, 5, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )
		
		
		bSizer43.Add( Sizer11, 1, wx.EXPAND, 5 )
		
		Sizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingStateMeleeLabel = wx.StaticText( self, wx.ID_ANY, u"Melee state", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingStateMeleeLabel.Wrap( -1 )
		Sizer12.Add( self.ThingStateMeleeLabel, 12, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateMelee = wx.TextCtrl( self, THING_STATE_MELEE, u"318", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.ThingStateMelee.SetMaxLength( 4 ) 
		Sizer12.Add( self.ThingStateMelee, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateMeleeName = wx.StaticText( self, THING_STATENAME_MELEE, u"TROOA", wx.DefaultPosition, wx.Size( 45,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingStateMeleeName.Wrap( -1 )
		self.ThingStateMeleeName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.ThingStateMeleeName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		Sizer12.Add( self.ThingStateMeleeName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateMeleeSet = wx.Button( self, THING_STATESET_MELEE, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingStateMeleeSet.SetMinSize( wx.Size( 22,22 ) )
		
		Sizer12.Add( self.ThingStateMeleeSet, 5, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )
		
		
		bSizer43.Add( Sizer12, 1, wx.EXPAND, 5 )
		
		Sizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingStateAttackLabel = wx.StaticText( self, wx.ID_ANY, u"Attack state", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingStateAttackLabel.Wrap( -1 )
		Sizer13.Add( self.ThingStateAttackLabel, 12, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateAttack = wx.TextCtrl( self, THING_STATE_ATTACK, u"318", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.ThingStateAttack.SetMaxLength( 4 ) 
		Sizer13.Add( self.ThingStateAttack, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateAttackName = wx.StaticText( self, THING_STATENAME_ATTACK, u"TROOA", wx.DefaultPosition, wx.Size( 45,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingStateAttackName.Wrap( -1 )
		self.ThingStateAttackName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.ThingStateAttackName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		Sizer13.Add( self.ThingStateAttackName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateAttackSet = wx.Button( self, THING_STATESET_ATTACK, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingStateAttackSet.SetMinSize( wx.Size( 22,22 ) )
		
		Sizer13.Add( self.ThingStateAttackSet, 5, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )
		
		
		bSizer43.Add( Sizer13, 1, wx.EXPAND, 5 )
		
		Sizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingStateDeathLabel = wx.StaticText( self, wx.ID_ANY, u"Death state", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingStateDeathLabel.Wrap( -1 )
		Sizer14.Add( self.ThingStateDeathLabel, 12, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateDeath = wx.TextCtrl( self, THING_STATE_DEATH, u"318", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.ThingStateDeath.SetMaxLength( 4 ) 
		Sizer14.Add( self.ThingStateDeath, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateDeathName = wx.StaticText( self, THING_STATENAME_DEATH, u"TROOA", wx.DefaultPosition, wx.Size( 45,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingStateDeathName.Wrap( -1 )
		self.ThingStateDeathName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.ThingStateDeathName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		Sizer14.Add( self.ThingStateDeathName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateDeathSet = wx.Button( self, THING_STATESET_DEATH, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingStateDeathSet.SetMinSize( wx.Size( 22,22 ) )
		
		Sizer14.Add( self.ThingStateDeathSet, 5, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )
		
		
		bSizer43.Add( Sizer14, 1, wx.EXPAND, 5 )
		
		Sizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingStateExplodeLabel = wx.StaticText( self, wx.ID_ANY, u"Explode state", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingStateExplodeLabel.Wrap( -1 )
		Sizer15.Add( self.ThingStateExplodeLabel, 12, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateExplode = wx.TextCtrl( self, THING_STATE_EXPLODE, u"318", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.ThingStateExplode.SetMaxLength( 4 ) 
		Sizer15.Add( self.ThingStateExplode, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateExplodeName = wx.StaticText( self, THING_STATENAME_EXPLODE, u"TROOA", wx.DefaultPosition, wx.Size( 45,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingStateExplodeName.Wrap( -1 )
		self.ThingStateExplodeName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.ThingStateExplodeName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		Sizer15.Add( self.ThingStateExplodeName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateExplodeSet = wx.Button( self, THING_STATESET_EXPLODE, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingStateExplodeSet.SetMinSize( wx.Size( 22,22 ) )
		
		Sizer15.Add( self.ThingStateExplodeSet, 5, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )
		
		
		bSizer43.Add( Sizer15, 1, wx.EXPAND, 5 )
		
		Sizer152 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingStateRaiseLabel = wx.StaticText( self, wx.ID_ANY, u"Raise", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingStateRaiseLabel.Wrap( -1 )
		Sizer152.Add( self.ThingStateRaiseLabel, 12, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateRaise = wx.TextCtrl( self, THING_STATE_RAISE, u"318", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.ThingStateRaise.SetMaxLength( 4 ) 
		Sizer152.Add( self.ThingStateRaise, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateRaiseName = wx.StaticText( self, THING_STATENAME_RAISE, u"TROOA", wx.DefaultPosition, wx.Size( 45,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingStateRaiseName.Wrap( -1 )
		self.ThingStateRaiseName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.ThingStateRaiseName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		Sizer152.Add( self.ThingStateRaiseName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateRaiseSet = wx.Button( self, THING_STATESET_RAISE, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingStateRaiseSet.SetMinSize( wx.Size( 22,22 ) )
		
		Sizer152.Add( self.ThingStateRaiseSet, 5, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )
		
		
		bSizer43.Add( Sizer152, 1, wx.EXPAND, 5 )
		
		
		bSizer43.AddSpacer( ( 0, 36), 0, wx.EXPAND, 5 )
		
		Sizer151 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingSoundAlertLabel = wx.StaticText( self, wx.ID_ANY, u"Alert sound", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingSoundAlertLabel.Wrap( -1 )
		Sizer151.Add( self.ThingSoundAlertLabel, 12, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingSoundAlert = wx.TextCtrl( self, THING_SOUND_ALERT, u"46", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.ThingSoundAlert.SetMaxLength( 4 ) 
		Sizer151.Add( self.ThingSoundAlert, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingSoundAlertName = wx.StaticText( self, wx.ID_ANY, u"PLPAIN", wx.DefaultPosition, wx.Size( 45,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingSoundAlertName.Wrap( -1 )
		self.ThingSoundAlertName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.ThingSoundAlertName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		Sizer151.Add( self.ThingSoundAlertName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingSoundAlertSet = wx.Button( self, THING_SOUNDSET_ALERT, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingSoundAlertSet.SetMinSize( wx.Size( 22,22 ) )
		
		Sizer151.Add( self.ThingSoundAlertSet, 5, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )
		
		
		bSizer43.Add( Sizer151, 1, wx.EXPAND, 5 )
		
		Sizer1511 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingSoundAttackLabel = wx.StaticText( self, wx.ID_ANY, u"Attack sound", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingSoundAttackLabel.Wrap( -1 )
		Sizer1511.Add( self.ThingSoundAttackLabel, 12, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingSoundAttack = wx.TextCtrl( self, THING_SOUND_ATTACK, u"46", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.ThingSoundAttack.SetMaxLength( 4 ) 
		Sizer1511.Add( self.ThingSoundAttack, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingSoundAttackName = wx.StaticText( self, wx.ID_ANY, u"PLPAIN", wx.DefaultPosition, wx.Size( 45,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingSoundAttackName.Wrap( -1 )
		self.ThingSoundAttackName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.ThingSoundAttackName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		Sizer1511.Add( self.ThingSoundAttackName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingSoundAttackSet = wx.Button( self, THING_SOUNDSET_ATTACK, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingSoundAttackSet.SetMinSize( wx.Size( 22,22 ) )
		
		Sizer1511.Add( self.ThingSoundAttackSet, 5, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )
		
		
		bSizer43.Add( Sizer1511, 1, wx.EXPAND, 5 )
		
		Sizer1512 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingSoundPainLabel = wx.StaticText( self, wx.ID_ANY, u"Pain sound", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingSoundPainLabel.Wrap( -1 )
		Sizer1512.Add( self.ThingSoundPainLabel, 12, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingSoundPain = wx.TextCtrl( self, THING_SOUND_PAIN, u"46", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.ThingSoundPain.SetMaxLength( 4 ) 
		Sizer1512.Add( self.ThingSoundPain, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingSoundPainName = wx.StaticText( self, wx.ID_ANY, u"PLPAIN", wx.DefaultPosition, wx.Size( 45,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingSoundPainName.Wrap( -1 )
		self.ThingSoundPainName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.ThingSoundPainName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		Sizer1512.Add( self.ThingSoundPainName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingSoundPainSet = wx.Button( self, THING_SOUNDSET_PAIN, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingSoundPainSet.SetMinSize( wx.Size( 22,22 ) )
		
		Sizer1512.Add( self.ThingSoundPainSet, 5, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )
		
		
		bSizer43.Add( Sizer1512, 1, wx.EXPAND, 5 )
		
		Sizer1513 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingSoundDeathLabel = wx.StaticText( self, wx.ID_ANY, u"Death sound", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingSoundDeathLabel.Wrap( -1 )
		Sizer1513.Add( self.ThingSoundDeathLabel, 12, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingSoundDeath = wx.TextCtrl( self, THING_SOUND_DEATH, u"46", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.ThingSoundDeath.SetMaxLength( 4 ) 
		Sizer1513.Add( self.ThingSoundDeath, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingSoundDeathName = wx.StaticText( self, wx.ID_ANY, u"PLPAIN", wx.DefaultPosition, wx.Size( 45,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingSoundDeathName.Wrap( -1 )
		self.ThingSoundDeathName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.ThingSoundDeathName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		Sizer1513.Add( self.ThingSoundDeathName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingSoundDeathSet = wx.Button( self, THING_SOUNDSET_DEATH, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingSoundDeathSet.SetMinSize( wx.Size( 22,22 ) )
		
		Sizer1513.Add( self.ThingSoundDeathSet, 5, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )
		
		
		bSizer43.Add( Sizer1513, 1, wx.EXPAND, 5 )
		
		Sizer1514 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingSoundActiveLabel = wx.StaticText( self, wx.ID_ANY, u"Active sound", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingSoundActiveLabel.Wrap( -1 )
		Sizer1514.Add( self.ThingSoundActiveLabel, 12, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingSoundActive = wx.TextCtrl( self, THING_SOUND_ACTIVE, u"46", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.ThingSoundActive.SetMaxLength( 4 ) 
		Sizer1514.Add( self.ThingSoundActive, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingSoundActiveName = wx.StaticText( self, wx.ID_ANY, u"PLPAIN", wx.DefaultPosition, wx.Size( 45,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingSoundActiveName.Wrap( -1 )
		self.ThingSoundActiveName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.ThingSoundActiveName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		Sizer1514.Add( self.ThingSoundActiveName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingSoundActiveSet = wx.Button( self, THING_SOUNDSET_ACTIVE, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingSoundActiveSet.SetMinSize( wx.Size( 22,22 ) )
		
		Sizer1514.Add( self.ThingSoundActiveSet, 5, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )
		
		
		bSizer43.Add( Sizer1514, 1, wx.EXPAND, 5 )
		
		
		bSizer40.Add( bSizer43, 0, wx.ALIGN_TOP|wx.EXPAND, 5 )
		
		
		bSizer40.AddSpacer( ( 0, 9), 0, wx.EXPAND, 5 )
		
		bSizer42 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer42.AddSpacer( ( 0, 0), 1, wx.EXPAND, 0 )
		
		self.ButtonRename = wx.Button( self, THING_RENAME, u"Rename", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ButtonRename.SetMinSize( wx.Size( -1,28 ) )
		
		bSizer42.Add( self.ButtonRename, 0, wx.ALL|wx.EXPAND, 0 )
		
		self.ButtonRestore = wx.Button( self, THING_RESTORE, u"Restore", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.ButtonRestore.SetMinSize( wx.Size( -1,28 ) )
		
		bSizer42.Add( self.ButtonRestore, 0, wx.EXPAND|wx.TOP, 3 )
		
		
		bSizer40.Add( bSizer42, 1, wx.EXPAND, 3 )
		
		
		Sizer26.Add( bSizer40, 10, wx.ALL|wx.EXPAND, 6 )
		
		
		self.SetSizer( Sizer26 )
		self.Layout()
		
		# Connect Events
		self.ThingNames.Bind( wx.EVT_LISTBOX, self.thing_select )
		self.ThingNames.Bind( wx.EVT_LISTBOX_DCLICK, self.thing_rename )
		self.ThingId.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingId.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingHealth.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingHealth.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingSpeed.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingSpeed.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingRadius.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingRadius.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingHeight.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingHeight.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingDamage.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingDamage.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingReactionTime.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingReactionTime.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingPainChance.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingPainChance.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingMass.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingMass.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingFlags.Bind( wx.EVT_CHECKLISTBOX, self.set_flags )
		self.ThingFlags.Bind( wx.EVT_MOTION, self.set_flag_tooltip )
		self.ThingStateSpawn.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingStateSpawn.Bind( wx.EVT_TEXT, self.set_state )
		self.ThingStateSpawnName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingStateSpawnName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingStateSpawnName.Bind( wx.EVT_LEFT_UP, self.goto_state )
		self.ThingStateSpawnSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.ThingStateWalk.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingStateWalk.Bind( wx.EVT_TEXT, self.set_state )
		self.ThingStateWalkName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingStateWalkName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingStateWalkName.Bind( wx.EVT_LEFT_UP, self.goto_state )
		self.ThingStateWalkSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.ThingStatePain.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingStatePain.Bind( wx.EVT_TEXT, self.set_state )
		self.ThingStatePainName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingStatePainName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingStatePainName.Bind( wx.EVT_LEFT_UP, self.goto_state )
		self.ThingStatePainSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.ThingStateMelee.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingStateMelee.Bind( wx.EVT_TEXT, self.set_state )
		self.ThingStateMeleeName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingStateMeleeName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingStateMeleeName.Bind( wx.EVT_LEFT_UP, self.goto_state )
		self.ThingStateMeleeSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.ThingStateAttack.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingStateAttack.Bind( wx.EVT_TEXT, self.set_state )
		self.ThingStateAttackName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingStateAttackName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingStateAttackName.Bind( wx.EVT_LEFT_UP, self.goto_state )
		self.ThingStateAttackSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.ThingStateDeath.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingStateDeath.Bind( wx.EVT_TEXT, self.set_state )
		self.ThingStateDeathName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingStateDeathName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingStateDeathName.Bind( wx.EVT_LEFT_UP, self.goto_state )
		self.ThingStateDeathSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.ThingStateExplode.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingStateExplode.Bind( wx.EVT_TEXT, self.set_state )
		self.ThingStateExplodeName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingStateExplodeName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingStateExplodeName.Bind( wx.EVT_LEFT_UP, self.goto_state )
		self.ThingStateExplodeSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.ThingStateRaise.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingStateRaise.Bind( wx.EVT_TEXT, self.set_state )
		self.ThingStateRaiseName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingStateRaiseName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingStateRaiseName.Bind( wx.EVT_LEFT_UP, self.goto_state )
		self.ThingStateRaiseSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.ThingSoundAlert.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingSoundAlert.Bind( wx.EVT_TEXT, self.set_sound )
		self.ThingSoundAlertName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingSoundAlertName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingSoundAlertName.Bind( wx.EVT_LEFT_UP, self.goto_sound )
		self.ThingSoundAlertSet.Bind( wx.EVT_BUTTON, self.set_sound_external )
		self.ThingSoundAttack.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingSoundAttack.Bind( wx.EVT_TEXT, self.set_sound )
		self.ThingSoundAttackName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingSoundAttackName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingSoundAttackName.Bind( wx.EVT_LEFT_UP, self.goto_sound )
		self.ThingSoundAttackSet.Bind( wx.EVT_BUTTON, self.set_sound_external )
		self.ThingSoundPain.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingSoundPain.Bind( wx.EVT_TEXT, self.set_sound )
		self.ThingSoundPainName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingSoundPainName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingSoundPainName.Bind( wx.EVT_LEFT_UP, self.goto_sound )
		self.ThingSoundPainSet.Bind( wx.EVT_BUTTON, self.set_sound_external )
		self.ThingSoundDeath.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingSoundDeath.Bind( wx.EVT_TEXT, self.set_sound )
		self.ThingSoundDeathName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingSoundDeathName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingSoundDeathName.Bind( wx.EVT_LEFT_UP, self.goto_sound )
		self.ThingSoundDeathSet.Bind( wx.EVT_BUTTON, self.set_sound_external )
		self.ThingSoundActive.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingSoundActive.Bind( wx.EVT_TEXT, self.set_sound )
		self.ThingSoundActiveName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingSoundActiveName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingSoundActiveName.Bind( wx.EVT_LEFT_UP, self.goto_sound )
		self.ThingSoundActiveSet.Bind( wx.EVT_BUTTON, self.set_sound_external )
		self.ButtonRename.Bind( wx.EVT_BUTTON, self.thing_rename )
		self.ButtonRestore.Bind( wx.EVT_BUTTON, self.thing_restore )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def thing_select( self, event ):
		pass
	
	def thing_rename( self, event ):
		pass
	
	def focus_text( self, event ):
		pass
	
	def set_value( self, event ):
		pass
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	def set_flags( self, event ):
		pass
	
	def set_flag_tooltip( self, event ):
		pass
	
	
	def set_state( self, event ):
		pass
	
	def enter_state( self, event ):
		pass
	
	def leave_state( self, event ):
		pass
	
	def goto_state( self, event ):
		pass
	
	def set_state_external( self, event ):
		pass
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	def set_sound( self, event ):
		pass
	
	
	
	def goto_sound( self, event ):
		pass
	
	def set_sound_external( self, event ):
		pass
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	def thing_restore( self, event ):
		pass
	

###########################################################################
## Class StatesFrameBase
###########################################################################

class StatesFrameBase ( wx.MDIChildFrame ):
	
	def __init__( self, parent ):
		wx.MDIChildFrame.__init__ ( self, parent, id = FRAME_STATES, title = u"States", pos = wx.DefaultPosition, size = wx.Size( 679,480 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU )
		
		self.SetSizeHintsSz( wx.Size( 678,480 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer41 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer40 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer42 = wx.BoxSizer( wx.VERTICAL )
		
		self.SpritePreview = spritepreview.SpritePreview(self, size=(-1, 160))
		self.SpritePreview.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )
		
		bSizer42.Add( self.SpritePreview, 0, wx.EXPAND, 5 )
		
		
		bSizer42.AddSpacer( ( 0, 6), 0, wx.EXPAND, 5 )
		
		bSizer52 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText39 = wx.StaticText( self, wx.ID_ANY, u"Sprite", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.m_staticText39.Wrap( -1 )
		bSizer52.Add( self.m_staticText39, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.SpriteIndex = wx.TextCtrl( self, STATES_SPRITE, wx.EmptyString, wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.SpriteIndex.SetMaxLength( 3 ) 
		bSizer52.Add( self.SpriteIndex, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.SpriteName = wx.StaticText( self, wx.ID_ANY, u"TROO", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ST_NO_AUTORESIZE )
		self.SpriteName.Wrap( -1 )
		self.SpriteName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.SpriteName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer52.Add( self.SpriteName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.SpriteSelect = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.SpriteSelect.SetMinSize( wx.Size( 30,22 ) )
		
		bSizer52.Add( self.SpriteSelect, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		bSizer42.Add( bSizer52, 0, wx.EXPAND, 5 )
		
		bSizer521 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText391 = wx.StaticText( self, wx.ID_ANY, u"Frame", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.m_staticText391.Wrap( -1 )
		bSizer521.Add( self.m_staticText391, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.FrameIndex = wx.TextCtrl( self, STATES_FRAME, wx.EmptyString, wx.DefaultPosition, wx.Size( 28,-1 ), 0 )
		bSizer521.Add( self.FrameIndex, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.LEFT|wx.TOP, 3 )
		
		self.FrameIndexSpinner = wx.SpinButton( self, STATES_FRAMESPIN, wx.DefaultPosition, wx.Size( 17,21 ), 0 )
		bSizer521.Add( self.FrameIndexSpinner, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.RIGHT|wx.TOP, 3 )
		
		self.AlwaysLit = wx.CheckBox( self, STATES_LIT, u" Always lit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer521.Add( self.AlwaysLit, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 6 )
		
		
		bSizer42.Add( bSizer521, 0, wx.EXPAND, 5 )
		
		
		bSizer42.AddSpacer( ( 0, 9), 0, wx.EXPAND, 5 )
		
		bSizer5211 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3911 = wx.StaticText( self, wx.ID_ANY, u"Next state", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.m_staticText3911.Wrap( -1 )
		bSizer5211.Add( self.m_staticText3911, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.NextStateIndex = wx.TextCtrl( self, STATES_NEXT, wx.EmptyString, wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.NextStateIndex.SetMaxLength( 4 ) 
		bSizer5211.Add( self.NextStateIndex, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.NextStateName = wx.StaticText( self, wx.ID_ANY, u"PLAYD", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ST_NO_AUTORESIZE )
		self.NextStateName.Wrap( -1 )
		self.NextStateName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.NextStateName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer5211.Add( self.NextStateName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		bSizer42.Add( bSizer5211, 0, wx.EXPAND, 5 )
		
		
		bSizer42.AddSpacer( ( 0, 9), 0, wx.EXPAND, 5 )
		
		bSizer5212 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3912 = wx.StaticText( self, wx.ID_ANY, u"Duration", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.m_staticText3912.Wrap( -1 )
		bSizer5212.Add( self.m_staticText3912, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.Duration = wx.TextCtrl( self, STATES_DURATION, wx.EmptyString, wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.Duration.SetMaxLength( 4 ) 
		bSizer5212.Add( self.Duration, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		bSizer42.Add( bSizer5212, 0, wx.EXPAND, 5 )
		
		
		bSizer42.AddSpacer( ( 0, 9), 0, wx.EXPAND, 6 )
		
		bSizer521211 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText54 = wx.StaticText( self, wx.ID_ANY, u"Action", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.m_staticText54.Wrap( -1 )
		bSizer521211.Add( self.m_staticText54, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		ActionChoices = []
		self.Action = wx.Choice( self, STATES_ACTION, wx.DefaultPosition, wx.DefaultSize, ActionChoices, wx.CB_SORT )
		self.Action.SetSelection( 0 )
		bSizer521211.Add( self.Action, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		bSizer42.Add( bSizer521211, 0, wx.EXPAND, 5 )
		
		bSizer52121 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText541 = wx.StaticText( self, wx.ID_ANY, u"Parameters", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.m_staticText541.Wrap( -1 )
		bSizer52121.Add( self.m_staticText541, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.Parameter1 = wx.TextCtrl( self, STATES_PARM1, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.Parameter1.SetMaxLength( 9 ) 
		bSizer52121.Add( self.Parameter1, 1, wx.ALL, 3 )
		
		self.Parameter2 = wx.TextCtrl( self, STATES_PARM2, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.Parameter2.SetMaxLength( 9 ) 
		bSizer52121.Add( self.Parameter2, 1, wx.ALL, 3 )
		
		
		bSizer42.Add( bSizer52121, 0, wx.EXPAND, 5 )
		
		
		bSizer42.AddSpacer( ( 0, 9), 0, wx.EXPAND, 6 )
		
		self.Restore = wx.Button( self, wx.ID_ANY, u"Restore", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.Restore.SetMinSize( wx.Size( -1,28 ) )
		
		bSizer42.Add( self.Restore, 0, wx.EXPAND|wx.TOP, 3 )
		
		
		bSizer40.Add( bSizer42, 0, wx.ALL|wx.EXPAND, 6 )
		
		bSizer421 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer441 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText45 = wx.StaticText( self, wx.ID_ANY, u"Filter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )
		self.m_staticText45.SetMinSize( wx.Size( 50,-1 ) )
		
		bSizer441.Add( self.m_staticText45, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		FilterChoices = []
		self.Filter = wx.Choice( self, STATES_FILTER, wx.DefaultPosition, wx.DefaultSize, FilterChoices, 0 )
		self.Filter.SetSelection( 0 )
		self.Filter.SetMinSize( wx.Size( 300,-1 ) )
		
		bSizer441.Add( self.Filter, 0, wx.RIGHT, 6 )
		
		self.FilterTools = wx.ToolBar( self, STATES_FILTERTOOLS, wx.DefaultPosition, wx.DefaultSize, wx.TB_FLAT|wx.TB_HORIZONTAL|wx.TB_NODIVIDER )
		self.FilterTools.SetToolBitmapSize( wx.Size( 18,18 ) )
		self.FilterTools.SetToolSeparation( 0 )
		self.FilterTools.SetMargins( wx.Size( 0,0 ) )
		self.FilterTools.SetToolPacking( 0 )
		self.FilterTools.AddLabelTool( STATES_FILTERTOOLS_REFRESH, u"tool", wx.Bitmap( u"res/icon-refresh.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Refreshes the state list.", wx.EmptyString, None ) 
		
		self.FilterTools.Realize() 
		
		bSizer441.Add( self.FilterTools, 0, wx.EXPAND, 0 )
		
		
		bSizer421.Add( bSizer441, 0, wx.ALL|wx.EXPAND, 6 )
		
		self.StateList = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_NO_SORT_HEADER|wx.LC_REPORT )
		self.StateList.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer421.Add( self.StateList, 1, wx.EXPAND, 5 )
		
		
		bSizer40.Add( bSizer421, 1, wx.EXPAND, 5 )
		
		
		bSizer41.Add( bSizer40, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer41 )
		self.Layout()
		
		# Connect Events
		self.SpriteIndex.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.SpriteIndex.Bind( wx.EVT_TEXT, self.set_value )
		self.SpriteSelect.Bind( wx.EVT_BUTTON, self.select_sprite )
		self.FrameIndex.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.FrameIndex.Bind( wx.EVT_TEXT, self.set_frame )
		self.FrameIndexSpinner.Bind( wx.EVT_SPIN_DOWN, self.frame_spin_down )
		self.FrameIndexSpinner.Bind( wx.EVT_SPIN_UP, self.frame_spin_up )
		self.AlwaysLit.Bind( wx.EVT_CHECKBOX, self.set_lit )
		self.NextStateIndex.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.NextStateIndex.Bind( wx.EVT_TEXT, self.set_value )
		self.NextStateName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.NextStateName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.NextStateName.Bind( wx.EVT_LEFT_UP, self.goto_next_state )
		self.Duration.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Duration.Bind( wx.EVT_TEXT, self.set_value )
		self.Action.Bind( wx.EVT_CHOICE, self.set_action )
		self.Parameter1.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Parameter1.Bind( wx.EVT_TEXT, self.set_value )
		self.Parameter2.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Parameter2.Bind( wx.EVT_TEXT, self.set_value )
		self.Restore.Bind( wx.EVT_BUTTON, self.state_restore )
		self.Filter.Bind( wx.EVT_CHOICE, self.filter_select )
		self.Bind( wx.EVT_TOOL, self.filter_select, id = STATES_FILTERTOOLS_REFRESH )
		self.StateList.Bind( wx.EVT_LEFT_DOWN, self.state_link )
		self.StateList.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.select_sprite )
		self.StateList.Bind( wx.EVT_LIST_ITEM_DESELECTED, self.state_deselect )
		self.StateList.Bind( wx.EVT_LIST_ITEM_SELECTED, self.state_select )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def focus_text( self, event ):
		pass
	
	def set_value( self, event ):
		pass
	
	def select_sprite( self, event ):
		pass
	
	
	def set_frame( self, event ):
		pass
	
	def frame_spin_down( self, event ):
		pass
	
	def frame_spin_up( self, event ):
		pass
	
	def set_lit( self, event ):
		pass
	
	
	
	def enter_state( self, event ):
		pass
	
	def leave_state( self, event ):
		pass
	
	def goto_next_state( self, event ):
		pass
	
	
	
	def set_action( self, event ):
		pass
	
	
	
	
	
	def state_restore( self, event ):
		pass
	
	def filter_select( self, event ):
		pass
	
	
	def state_link( self, event ):
		pass
	
	
	def state_deselect( self, event ):
		pass
	
	def state_select( self, event ):
		pass
	

###########################################################################
## Class SoundsFrameBase
###########################################################################

class SoundsFrameBase ( wx.MDIChildFrame ):
	
	def __init__( self, parent ):
		wx.MDIChildFrame.__init__ ( self, parent, id = FRAME_SOUNDS, title = u"Sounds", pos = wx.DefaultPosition, size = wx.Size( 382,480 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU )
		
		self.SetSizeHintsSz( wx.Size( 382,480 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer42 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer52 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText39 = wx.StaticText( self, wx.ID_ANY, u"Priority", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.m_staticText39.Wrap( -1 )
		bSizer52.Add( self.m_staticText39, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.Priority = wx.TextCtrl( self, SOUNDS_PRIORITY, wx.EmptyString, wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.Priority.SetMaxLength( 3 ) 
		bSizer52.Add( self.Priority, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.LEFT|wx.TOP, 3 )
		
		self.PrioritySpinner = wx.SpinButton( self, SOUNDS_PRIORITYSPIN, wx.DefaultPosition, wx.Size( 17,21 ), 0 )
		bSizer52.Add( self.PrioritySpinner, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.RIGHT|wx.TOP, 3 )
		
		
		bSizer42.Add( bSizer52, 0, wx.EXPAND, 5 )
		
		bSizer521 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText391 = wx.StaticText( self, wx.ID_ANY, u"Singular", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.m_staticText391.Wrap( -1 )
		bSizer521.Add( self.m_staticText391, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.Singular = wx.CheckBox( self, SOUNDS_SINGULAR, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer521.Add( self.Singular, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 6 )
		
		
		bSizer42.Add( bSizer521, 0, wx.EXPAND, 5 )
		
		
		bSizer42.AddSpacer( ( 0, 12), 0, wx.EXPAND, 0 )
		
		self.Restore = wx.Button( self, SOUNDS_RESTORE, u"Restore", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.Restore.SetMinSize( wx.Size( -1,28 ) )
		
		bSizer42.Add( self.Restore, 0, wx.EXPAND|wx.TOP, 3 )
		
		
		bSizer41.Add( bSizer42, 0, wx.ALL|wx.EXPAND, 6 )
		
		self.SoundList = wx.ListCtrl( self, SOUNDS_LIST, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_NO_SORT_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.NO_BORDER )
		self.SoundList.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer41.Add( self.SoundList, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer41 )
		self.Layout()
		
		# Connect Events
		self.Priority.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Priority.Bind( wx.EVT_TEXT, self.set_priority )
		self.PrioritySpinner.Bind( wx.EVT_SPIN_DOWN, self.priority_spin_down )
		self.PrioritySpinner.Bind( wx.EVT_SPIN_UP, self.priority_spin_up )
		self.Singular.Bind( wx.EVT_CHECKBOX, self.set_singular )
		self.Restore.Bind( wx.EVT_BUTTON, self.sound_restore )
		self.SoundList.Bind( wx.EVT_LIST_ITEM_DESELECTED, self.sound_deselect )
		self.SoundList.Bind( wx.EVT_LIST_ITEM_RIGHT_CLICK, self.sound_play )
		self.SoundList.Bind( wx.EVT_LIST_ITEM_SELECTED, self.sound_select )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def focus_text( self, event ):
		pass
	
	def set_priority( self, event ):
		pass
	
	def priority_spin_down( self, event ):
		pass
	
	def priority_spin_up( self, event ):
		pass
	
	def set_singular( self, event ):
		pass
	
	def sound_restore( self, event ):
		pass
	
	def sound_deselect( self, event ):
		pass
	
	def sound_play( self, event ):
		pass
	
	def sound_select( self, event ):
		pass
	

###########################################################################
## Class StringsFrameBase
###########################################################################

class StringsFrameBase ( wx.MDIChildFrame ):
	
	def __init__( self, parent ):
		wx.MDIChildFrame.__init__ ( self, parent, id = FRAME_STRINGS, title = u"Strings", pos = wx.DefaultPosition, size = wx.Size( 640,400 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU )
		
		self.SetSizeHintsSz( wx.Size( 640,400 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.StringList = wx.ListCtrl( self, STRINGS_LIST, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_NO_SORT_HEADER|wx.LC_REPORT|wx.NO_BORDER )
		self.StringList.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer41.Add( self.StringList, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer41 )
		self.Layout()
		
		# Connect Events
		self.StringList.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.string_edit )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def string_edit( self, event ):
		pass
	

###########################################################################
## Class WeaponsFrameBase
###########################################################################

class WeaponsFrameBase ( wx.MDIChildFrame ):
	
	def __init__( self, parent ):
		wx.MDIChildFrame.__init__ ( self, parent, id = FRAME_WEAPONS, title = u"Weapons", pos = wx.DefaultPosition, size = wx.Size( 480,360 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU )
		
		self.SetSizeHintsSz( wx.Size( 480,360 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )
		
		WeaponListChoices = []
		self.WeaponList = wx.ListBox( self, WEAPON_LIST, wx.DefaultPosition, wx.DefaultSize, WeaponListChoices, wx.LB_HSCROLL|wx.SUNKEN_BORDER )
		bSizer41.Add( self.WeaponList, 1, wx.EXPAND, 5 )
		
		bSizer139 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer1 = wx.GridSizer( 6, 2, 3, 0 )
		
		self.m_staticText88 = wx.StaticText( self, wx.ID_ANY, u"Ammo type", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText88.Wrap( -1 )
		gSizer1.Add( self.m_staticText88, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		AmmoTypeChoices = []
		self.AmmoType = wx.Choice( self, WEAPON_AMMOTYPE, wx.DefaultPosition, wx.DefaultSize, AmmoTypeChoices, 0 )
		self.AmmoType.SetSelection( 0 )
		gSizer1.Add( self.AmmoType, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.m_staticText881 = wx.StaticText( self, wx.ID_ANY, u"Select state", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText881.Wrap( -1 )
		gSizer1.Add( self.m_staticText881, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		bSizer124 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.WeaponStateSelect = wx.TextCtrl( self, WEAPON_STATE_SELECT, u"318", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.WeaponStateSelect.SetMaxLength( 4 ) 
		bSizer124.Add( self.WeaponStateSelect, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.WeaponStateSelectName = wx.StaticText( self, WEAPON_STATENAME_SELECT, u"TROOA", wx.DefaultPosition, wx.Size( 45,-1 ), wx.ST_NO_AUTORESIZE )
		self.WeaponStateSelectName.Wrap( -1 )
		self.WeaponStateSelectName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.WeaponStateSelectName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer124.Add( self.WeaponStateSelectName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.WeaponStateSelectSet = wx.Button( self, WEAPON_STATESET_SELECT, u"<", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.WeaponStateSelectSet.SetMinSize( wx.Size( 22,22 ) )
		
		bSizer124.Add( self.WeaponStateSelectSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		gSizer1.Add( bSizer124, 1, wx.EXPAND, 5 )
		
		self.m_staticText8811 = wx.StaticText( self, wx.ID_ANY, u"Deselect state", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8811.Wrap( -1 )
		gSizer1.Add( self.m_staticText8811, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bSizer1241 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.WeaponStateDeselect = wx.TextCtrl( self, WEAPON_STATE_DESELECT, u"318", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.WeaponStateDeselect.SetMaxLength( 4 ) 
		bSizer1241.Add( self.WeaponStateDeselect, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.WeaponStateDeselectName = wx.StaticText( self, WEAPON_STATENAME_DESELECT, u"TROOA", wx.DefaultPosition, wx.Size( 45,-1 ), wx.ST_NO_AUTORESIZE )
		self.WeaponStateDeselectName.Wrap( -1 )
		self.WeaponStateDeselectName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.WeaponStateDeselectName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer1241.Add( self.WeaponStateDeselectName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.WeaponStateDeselectSet = wx.Button( self, WEAPON_STATESET_DESELECT, u"<", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.WeaponStateDeselectSet.SetMinSize( wx.Size( 22,22 ) )
		
		bSizer1241.Add( self.WeaponStateDeselectSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		gSizer1.Add( bSizer1241, 1, wx.EXPAND, 5 )
		
		self.m_staticText8812 = wx.StaticText( self, wx.ID_ANY, u"Bob state", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8812.Wrap( -1 )
		gSizer1.Add( self.m_staticText8812, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bSizer1242 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.WeapnStateBob = wx.TextCtrl( self, WEAPON_STATE_BOB, u"318", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.WeapnStateBob.SetMaxLength( 4 ) 
		bSizer1242.Add( self.WeapnStateBob, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.WeaponStateBobName = wx.StaticText( self, WEAPON_STATENAME_BOB, u"TROOA", wx.DefaultPosition, wx.Size( 45,-1 ), wx.ST_NO_AUTORESIZE )
		self.WeaponStateBobName.Wrap( -1 )
		self.WeaponStateBobName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.WeaponStateBobName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer1242.Add( self.WeaponStateBobName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.WeaponStateBobSet = wx.Button( self, WEAPON_STATESET_BOB, u"<", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.WeaponStateBobSet.SetMinSize( wx.Size( 22,22 ) )
		
		bSizer1242.Add( self.WeaponStateBobSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		gSizer1.Add( bSizer1242, 1, wx.EXPAND, 5 )
		
		self.m_staticText8813 = wx.StaticText( self, wx.ID_ANY, u"Fire state", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8813.Wrap( -1 )
		gSizer1.Add( self.m_staticText8813, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bSizer1243 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.WeaponStateFire = wx.TextCtrl( self, WEAPON_STATE_FIRE, u"318", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.WeaponStateFire.SetMaxLength( 4 ) 
		bSizer1243.Add( self.WeaponStateFire, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.WeaponStateFireName = wx.StaticText( self, WEAPON_STATENAME_FIRE, u"TROOA", wx.DefaultPosition, wx.Size( 45,-1 ), wx.ST_NO_AUTORESIZE )
		self.WeaponStateFireName.Wrap( -1 )
		self.WeaponStateFireName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.WeaponStateFireName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer1243.Add( self.WeaponStateFireName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.WeaponStateFireSet = wx.Button( self, WEAPON_STATESET_FIRE, u"<", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.WeaponStateFireSet.SetMinSize( wx.Size( 22,22 ) )
		
		bSizer1243.Add( self.WeaponStateFireSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		gSizer1.Add( bSizer1243, 1, wx.EXPAND, 5 )
		
		self.m_staticText8814 = wx.StaticText( self, wx.ID_ANY, u"Muzzle flash state", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8814.Wrap( -1 )
		gSizer1.Add( self.m_staticText8814, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bSizer1244 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.WeaponStateMuzzle = wx.TextCtrl( self, WEAPON_STATE_MUZZLE, u"318", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.WeaponStateMuzzle.SetMaxLength( 4 ) 
		bSizer1244.Add( self.WeaponStateMuzzle, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.WeaponStateMuzzleName = wx.StaticText( self, WEAPON_STATENAME_MUZZLE, u"TROOA", wx.DefaultPosition, wx.Size( 45,-1 ), wx.ST_NO_AUTORESIZE )
		self.WeaponStateMuzzleName.Wrap( -1 )
		self.WeaponStateMuzzleName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.WeaponStateMuzzleName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer1244.Add( self.WeaponStateMuzzleName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.WeaponStateMuzzleSet = wx.Button( self, WEAPON_STATESET_MUZZLE, u"<", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.WeaponStateMuzzleSet.SetMinSize( wx.Size( 22,22 ) )
		
		bSizer1244.Add( self.WeaponStateMuzzleSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		gSizer1.Add( bSizer1244, 1, wx.EXPAND, 5 )
		
		
		bSizer139.Add( gSizer1, 0, wx.ALL, 6 )
		
		
		bSizer139.AddSpacer( ( 0, 0), 1, wx.EXPAND, 0 )
		
		self.Rename = wx.Button( self, WEAPON_RENAME, u"Rename", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Rename.SetMinSize( wx.Size( -1,28 ) )
		
		bSizer139.Add( self.Rename, 0, wx.ALL|wx.EXPAND, 6 )
		
		self.Restore = wx.Button( self, WEAPON_RESTORE, u"Restore", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Restore.SetMinSize( wx.Size( -1,28 ) )
		
		bSizer139.Add( self.Restore, 0, wx.ALL|wx.EXPAND, 6 )
		
		
		bSizer41.Add( bSizer139, 0, wx.ALL|wx.EXPAND, 6 )
		
		
		self.SetSizer( bSizer41 )
		self.Layout()
		
		# Connect Events
		self.WeaponList.Bind( wx.EVT_LISTBOX, self.weapon_select )
		self.WeaponStateSelect.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.WeaponStateSelect.Bind( wx.EVT_TEXT, self.set_state_index )
		self.WeaponStateSelectName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.WeaponStateSelectName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.WeaponStateSelectName.Bind( wx.EVT_LEFT_UP, self.goto_state )
		self.WeaponStateSelectSet.Bind( wx.EVT_BUTTON, self.set_state )
		self.WeaponStateDeselect.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.WeaponStateDeselect.Bind( wx.EVT_TEXT, self.set_state_index )
		self.WeaponStateDeselectName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.WeaponStateDeselectName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.WeaponStateDeselectName.Bind( wx.EVT_LEFT_UP, self.goto_state )
		self.WeaponStateDeselectSet.Bind( wx.EVT_BUTTON, self.set_state )
		self.WeapnStateBob.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.WeapnStateBob.Bind( wx.EVT_TEXT, self.set_state_index )
		self.WeaponStateBobName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.WeaponStateBobName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.WeaponStateBobName.Bind( wx.EVT_LEFT_UP, self.goto_state )
		self.WeaponStateBobSet.Bind( wx.EVT_BUTTON, self.set_state )
		self.WeaponStateFire.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.WeaponStateFire.Bind( wx.EVT_TEXT, self.set_state_index )
		self.WeaponStateFireName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.WeaponStateFireName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.WeaponStateFireName.Bind( wx.EVT_LEFT_UP, self.goto_state )
		self.WeaponStateFireSet.Bind( wx.EVT_BUTTON, self.set_state )
		self.WeaponStateMuzzle.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.WeaponStateMuzzle.Bind( wx.EVT_TEXT, self.set_state_index )
		self.WeaponStateMuzzleName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.WeaponStateMuzzleName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.WeaponStateMuzzleName.Bind( wx.EVT_LEFT_UP, self.goto_state )
		self.WeaponStateMuzzleSet.Bind( wx.EVT_BUTTON, self.set_state )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def weapon_select( self, event ):
		pass
	
	def focus_text( self, event ):
		pass
	
	def set_state_index( self, event ):
		pass
	
	def enter_state( self, event ):
		pass
	
	def leave_state( self, event ):
		pass
	
	def goto_state( self, event ):
		pass
	
	def set_state( self, event ):
		pass
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

###########################################################################
## Class AmmoFrameBase
###########################################################################

class AmmoFrameBase ( wx.MDIChildFrame ):
	
	def __init__( self, parent ):
		wx.MDIChildFrame.__init__ ( self, parent, id = FRAME_AMMO, title = u"Ammo", pos = wx.DefaultPosition, size = wx.Size( 397,250 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU )
		
		self.SetSizeHintsSz( wx.Size( 350,250 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Ammo = wx.ListCtrl( self, AMMO_LIST, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.NO_BORDER )
		bSizer41.Add( self.Ammo, 1, wx.ALL|wx.EXPAND, 0 )
		
		bSizer139 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer1 = wx.GridSizer( 2, 2, 3, 12 )
		
		self.m_staticText88 = wx.StaticText( self, wx.ID_ANY, u"Maximum ammo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText88.Wrap( -1 )
		gSizer1.Add( self.m_staticText88, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.Maximum = wx.TextCtrl( self, AMMO_MAXIMUM, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.Maximum.SetMaxLength( 6 ) 
		gSizer1.Add( self.Maximum, 0, wx.ALL|wx.EXPAND, 3 )
		
		self.m_staticText881 = wx.StaticText( self, wx.ID_ANY, u"Pickup ammo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText881.Wrap( -1 )
		gSizer1.Add( self.m_staticText881, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.Pickup = wx.TextCtrl( self, AMMO_PICKUP, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.Pickup.SetMaxLength( 6 ) 
		gSizer1.Add( self.Pickup, 0, wx.ALL|wx.EXPAND, 3 )
		
		
		bSizer139.Add( gSizer1, 0, wx.ALL, 6 )
		
		
		bSizer139.AddSpacer( ( 0, 0), 1, wx.EXPAND, 0 )
		
		self.Rename = wx.Button( self, AMMO_RENAME, u"Rename", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Rename.SetMinSize( wx.Size( -1,28 ) )
		
		bSizer139.Add( self.Rename, 0, wx.ALL|wx.EXPAND, 6 )
		
		self.Restore = wx.Button( self, AMMO_RESTORE, u"Restore", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Restore.SetMinSize( wx.Size( -1,28 ) )
		
		bSizer139.Add( self.Restore, 0, wx.ALL|wx.EXPAND, 6 )
		
		
		bSizer41.Add( bSizer139, 0, wx.ALL|wx.EXPAND, 6 )
		
		
		self.SetSizer( bSizer41 )
		self.Layout()
		
		# Connect Events
		self.Maximum.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Maximum.Bind( wx.EVT_TEXT, self.set_value )
		self.Pickup.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Pickup.Bind( wx.EVT_TEXT, self.set_value )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def focus_text( self, event ):
		pass
	
	def set_value( self, event ):
		pass
	
	
	

###########################################################################
## Class CheatsFrameBase
###########################################################################

class CheatsFrameBase ( wx.MDIChildFrame ):
	
	def __init__( self, parent ):
		wx.MDIChildFrame.__init__ ( self, parent, id = FRAME_CHEATS, title = u"Cheats", pos = wx.DefaultPosition, size = wx.Size( 350,380 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU )
		
		self.SetSizeHintsSz( wx.Size( 350,380 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer41 = wx.BoxSizer( wx.VERTICAL )
		
		self.CheatsList = wx.ListCtrl( self, CHEATS_LIST, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.NO_BORDER )
		bSizer41.Add( self.CheatsList, 1, wx.EXPAND, 5 )
		
		bSizer158 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Infight = wx.CheckBox( self, CHEATS_INFIGHT, u" Monsters infight", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer158.Add( self.Infight, 0, wx.ALL|wx.EXPAND, 6 )
		
		
		bSizer158.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.Restore = wx.Button( self, CHEATS_RESTORE, u"Restore", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Restore.SetMinSize( wx.Size( 120,28 ) )
		
		bSizer158.Add( self.Restore, 0, wx.ALL, 6 )
		
		
		bSizer41.Add( bSizer158, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer41 )
		self.Layout()
		
		# Connect Events
		self.CheatsList.Bind( wx.EVT_LIST_BEGIN_LABEL_EDIT, self.cheat_edit_start )
		self.CheatsList.Bind( wx.EVT_LIST_END_LABEL_EDIT, self.cheat_edit_end )
		self.Restore.Bind( wx.EVT_BUTTON, self.cheat_restore )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def cheat_edit_start( self, event ):
		pass
	
	def cheat_edit_end( self, event ):
		pass
	
	def cheat_restore( self, event ):
		pass
	

###########################################################################
## Class MiscFrameBase
###########################################################################

class MiscFrameBase ( wx.MDIChildFrame ):
	
	def __init__( self, parent ):
		wx.MDIChildFrame.__init__ ( self, parent, id = FRAME_MISC, title = u"Miscellaneous", pos = wx.DefaultPosition, size = wx.Size( 406,380 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU )
		
		self.SetSizeHintsSz( wx.Size( 350,380 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer41 = wx.BoxSizer( wx.VERTICAL )
		
		self.MiscList = wx.ListCtrl( self, MISC_LIST, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.NO_BORDER )
		bSizer41.Add( self.MiscList, 1, wx.EXPAND, 0 )
		
		bSizer158 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer158.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.Restore = wx.Button( self, MISC_RESTORE, u"Restore", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Restore.SetMinSize( wx.Size( 120,28 ) )
		
		bSizer158.Add( self.Restore, 0, wx.ALL, 6 )
		
		
		bSizer41.Add( bSizer158, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer41 )
		self.Layout()
		
		# Connect Events
		self.Restore.Bind( wx.EVT_BUTTON, self.cheat_restore )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def cheat_restore( self, event ):
		pass
	

###########################################################################
## Class ParFrameBase
###########################################################################

class ParFrameBase ( wx.MDIChildFrame ):
	
	def __init__( self, parent ):
		wx.MDIChildFrame.__init__ ( self, parent, id = FRAME_PAR, title = u"Par times", pos = wx.DefaultPosition, size = wx.Size( 362,380 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU )
		
		self.SetSizeHintsSz( wx.Size( 350,380 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ParList = wx.ListCtrl( self, PAR_LIST, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.NO_BORDER )
		bSizer41.Add( self.ParList, 1, wx.EXPAND, 5 )
		
		bSizer139 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer1 = wx.GridSizer( 3, 2, 3, 0 )
		
		self.m_staticText88 = wx.StaticText( self, wx.ID_ANY, u"Episode", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText88.Wrap( -1 )
		gSizer1.Add( self.m_staticText88, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.Episode = wx.TextCtrl( self, PAR_EPISODE, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.Episode.SetMaxLength( 6 ) 
		gSizer1.Add( self.Episode, 0, wx.ALL|wx.EXPAND, 3 )
		
		self.m_staticText881 = wx.StaticText( self, wx.ID_ANY, u"Map", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText881.Wrap( -1 )
		gSizer1.Add( self.m_staticText881, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.Map = wx.TextCtrl( self, PAR_MAP, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.Map.SetMaxLength( 6 ) 
		gSizer1.Add( self.Map, 0, wx.ALL, 3 )
		
		self.m_staticText8811 = wx.StaticText( self, wx.ID_ANY, u"Time", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8811.Wrap( -1 )
		gSizer1.Add( self.m_staticText8811, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.Time = wx.TextCtrl( self, PAR_TIME, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.Time.SetMaxLength( 6 ) 
		gSizer1.Add( self.Time, 0, wx.ALL, 3 )
		
		
		bSizer139.Add( gSizer1, 0, wx.ALL, 6 )
		
		
		bSizer139.AddSpacer( ( 0, 0), 1, wx.EXPAND, 0 )
		
		self.Rename = wx.Button( self, PAR_RENAME, u"Rename", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Rename.SetMinSize( wx.Size( -1,28 ) )
		
		bSizer139.Add( self.Rename, 0, wx.ALL|wx.EXPAND, 6 )
		
		self.Restore = wx.Button( self, PAR_RESTORE, u"Restore", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Restore.SetMinSize( wx.Size( -1,28 ) )
		
		bSizer139.Add( self.Restore, 0, wx.ALL|wx.EXPAND, 6 )
		
		
		bSizer41.Add( bSizer139, 0, wx.ALL|wx.EXPAND, 6 )
		
		
		self.SetSizer( bSizer41 )
		self.Layout()
		
		# Connect Events
		self.Episode.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Episode.Bind( wx.EVT_TEXT, self.set_value )
		self.Map.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Map.Bind( wx.EVT_TEXT, self.set_value )
		self.Time.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Time.Bind( wx.EVT_TEXT, self.set_value )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def focus_text( self, event ):
		pass
	
	def set_value( self, event ):
		pass
	
	
	
	
	

###########################################################################
## Class SpritesDialogBase
###########################################################################

class SpritesDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = DIALOG_SPRITES, title = u"Sprites", pos = wx.DefaultPosition, size = wx.Size( 500,490 ), style = wx.CAPTION )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer39 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer42 = wx.BoxSizer( wx.HORIZONTAL )
		
		SpriteNamesChoices = []
		self.SpriteNames = wx.ListBox( self, SPRITES_NAMES, wx.DefaultPosition, wx.DefaultSize, SpriteNamesChoices, wx.LB_SINGLE )
		self.SpriteNames.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, "Bitstream Vera Sans Mono" ) )
		self.SpriteNames.SetMinSize( wx.Size( 60,-1 ) )
		
		bSizer42.Add( self.SpriteNames, 0, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 6 )
		
		bSizer40 = wx.BoxSizer( wx.VERTICAL )
		
		self.SpritePreview = spritepreview.SpritePreview(self)
		self.SpritePreview.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )
		
		bSizer40.Add( self.SpritePreview, 1, wx.EXPAND|wx.RIGHT|wx.TOP, 6 )
		
		
		bSizer42.Add( bSizer40, 1, wx.EXPAND, 5 )
		
		
		bSizer39.Add( bSizer42, 1, wx.EXPAND, 5 )
		
		bSizer431 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Filter = wx.TextCtrl( self, SPRITES_FILTER, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_PROCESS_ENTER )
		self.Filter.SetMaxLength( 4 ) 
		self.Filter.SetMinSize( wx.Size( 60,-1 ) )
		
		bSizer431.Add( self.Filter, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 6 )
		
		self.FrameLabel = wx.StaticText( self, wx.ID_ANY, u"Frame", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FrameLabel.Wrap( -1 )
		self.FrameLabel.SetMinSize( wx.Size( 40,-1 ) )
		
		bSizer431.Add( self.FrameLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 6 )
		
		self.FrameIndex = wx.TextCtrl( self, SPRITES_FRAME, wx.EmptyString, wx.DefaultPosition, wx.Size( 28,-1 ), 0 )
		bSizer431.Add( self.FrameIndex, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.LEFT|wx.TOP, 6 )
		
		self.FrameIndexSpinner = wx.SpinButton( self, SPRITES_FRAMESPIN, wx.DefaultPosition, wx.Size( 17,21 ), 0 )
		bSizer431.Add( self.FrameIndexSpinner, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.RIGHT|wx.TOP, 6 )
		
		
		bSizer39.Add( bSizer431, 0, wx.EXPAND, 0 )
		
		bSizer43 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer43.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.ButtonOk = wx.Button( self, SPRITES_OK, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ButtonOk.SetDefault() 
		self.ButtonOk.SetMinSize( wx.Size( 120,28 ) )
		
		bSizer43.Add( self.ButtonOk, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 6 )
		
		self.ButtonCancel = wx.Button( self, SPRITES_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ButtonCancel.SetMinSize( wx.Size( 120,28 ) )
		
		bSizer43.Add( self.ButtonCancel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 6 )
		
		
		bSizer39.Add( bSizer43, 0, wx.EXPAND, 6 )
		
		
		self.SetSizer( bSizer39 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.SpriteNames.Bind( wx.EVT_LISTBOX, self.sprite_select_list )
		self.SpriteNames.Bind( wx.EVT_LISTBOX_DCLICK, self.ok )
		self.Filter.Bind( wx.EVT_CHAR, self.filter_key )
		self.Filter.Bind( wx.EVT_TEXT, self.filter_update )
		self.Filter.Bind( wx.EVT_TEXT_ENTER, self.ok )
		self.FrameIndex.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.FrameIndex.Bind( wx.EVT_TEXT, self.update_frame )
		self.FrameIndexSpinner.Bind( wx.EVT_SPIN_DOWN, self.frameindex_spin_down )
		self.FrameIndexSpinner.Bind( wx.EVT_SPIN_UP, self.frameindex_spin_up )
		self.ButtonOk.Bind( wx.EVT_BUTTON, self.ok )
		self.ButtonCancel.Bind( wx.EVT_BUTTON, self.cancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def sprite_select_list( self, event ):
		pass
	
	def ok( self, event ):
		pass
	
	def filter_key( self, event ):
		pass
	
	def filter_update( self, event ):
		pass
	
	
	def focus_text( self, event ):
		pass
	
	def update_frame( self, event ):
		pass
	
	def frameindex_spin_down( self, event ):
		pass
	
	def frameindex_spin_up( self, event ):
		pass
	
	
	def cancel( self, event ):
		pass
	

###########################################################################
## Class StringDialogBase
###########################################################################

class StringDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = DIALOG_SPRITES, title = u"String", pos = wx.DefaultPosition, size = wx.Size( 651,483 ), style = wx.CAPTION )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer39 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer113 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer42 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText81 = wx.StaticText( self, wx.ID_ANY, u"Original", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText81.Wrap( -1 )
		bSizer42.Add( self.m_staticText81, 0, wx.LEFT|wx.RIGHT|wx.TOP, 6 )
		
		self.m_textCtrl54 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		self.m_textCtrl54.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, "Bitstream Vera Sans Mono" ) )
		
		bSizer42.Add( self.m_textCtrl54, 1, wx.ALL|wx.EXPAND, 6 )
		
		
		bSizer113.Add( bSizer42, 1, wx.EXPAND, 5 )
		
		bSizer421 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText811 = wx.StaticText( self, wx.ID_ANY, u"New", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText811.Wrap( -1 )
		bSizer421.Add( self.m_staticText811, 0, wx.LEFT|wx.RIGHT|wx.TOP, 6 )
		
		self.m_textCtrl541 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.m_textCtrl541.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, "Bitstream Vera Sans Mono" ) )
		
		bSizer421.Add( self.m_textCtrl541, 1, wx.ALL|wx.EXPAND, 6 )
		
		
		bSizer113.Add( bSizer421, 1, wx.EXPAND, 5 )
		
		
		bSizer39.Add( bSizer113, 1, wx.ALL|wx.EXPAND, 6 )
		
		bSizer43 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer43.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.ButtonOk = wx.Button( self, SPRITES_OK, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ButtonOk.SetDefault() 
		self.ButtonOk.SetMinSize( wx.Size( 120,28 ) )
		
		bSizer43.Add( self.ButtonOk, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 6 )
		
		self.ButtonCancel = wx.Button( self, SPRITES_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ButtonCancel.SetMinSize( wx.Size( 120,28 ) )
		
		bSizer43.Add( self.ButtonCancel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 6 )
		
		
		bSizer39.Add( bSizer43, 0, wx.ALL|wx.EXPAND, 6 )
		
		
		self.SetSizer( bSizer39 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.ButtonOk.Bind( wx.EVT_BUTTON, self.ok )
		self.ButtonCancel.Bind( wx.EVT_BUTTON, self.cancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def ok( self, event ):
		pass
	
	def cancel( self, event ):
		pass
	

###########################################################################
## Class PatchInfoDialogBase
###########################################################################

class PatchInfoDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = DIALOG_PATCHINFO, title = u"Patch", pos = wx.DefaultPosition, size = wx.Size( 600,325 ), style = wx.CAPTION )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer44 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer45 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText46 = wx.StaticText( self, wx.ID_ANY, u"Engine", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )
		self.m_staticText46.SetMinSize( wx.Size( 75,-1 ) )
		
		bSizer45.Add( self.m_staticText46, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 6 )
		
		EngineListChoices = []
		self.EngineList = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, EngineListChoices, 0 )
		self.EngineList.SetSelection( 0 )
		bSizer45.Add( self.EngineList, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 6 )
		
		
		bSizer45.AddSpacer( ( 26, 0), 0, wx.BOTTOM|wx.EXPAND|wx.RIGHT|wx.TOP, 6 )
		
		
		bSizer44.Add( bSizer45, 0, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 6 )
		
		bSizer451 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText461 = wx.StaticText( self, wx.ID_ANY, u"IWAD", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText461.Wrap( -1 )
		self.m_staticText461.SetMinSize( wx.Size( 75,-1 ) )
		
		bSizer451.Add( self.m_staticText461, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 6 )
		
		self.IWAD = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.IWAD.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer451.Add( self.IWAD, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 6 )
		
		self.IWADBrowse = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.Size( 26,23 ), 0 )
		bSizer451.Add( self.IWADBrowse, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.RIGHT|wx.TOP, 6 )
		
		
		bSizer44.Add( bSizer451, 0, wx.EXPAND|wx.LEFT|wx.RIGHT, 6 )
		
		bSizer452 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText462 = wx.StaticText( self, wx.ID_ANY, u"PWADs", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText462.Wrap( -1 )
		self.m_staticText462.SetMinSize( wx.Size( 75,-1 ) )
		
		bSizer452.Add( self.m_staticText462, 0, wx.ALL, 6 )
		
		PWADListChoices = []
		self.PWADList = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, PWADListChoices, 0 )
		bSizer452.Add( self.PWADList, 1, wx.ALL|wx.EXPAND, 6 )
		
		bSizer63 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_toolBar3 = wx.ToolBar( self, PATCHINFO_TOOLBAR, wx.DefaultPosition, wx.DefaultSize, wx.TB_FLAT|wx.TB_NODIVIDER|wx.TB_VERTICAL ) 
		self.m_toolBar3.AddLabelTool( PATCHINFO_TOOLBAR_ADD, u"tool", wx.Bitmap( u"res/icon-plus.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_toolBar3.AddLabelTool( PATCHINFO_TOOLBAR_REMOVE, u"tool", wx.Bitmap( u"res/icon-minus.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_toolBar3.Realize() 
		
		bSizer63.Add( self.m_toolBar3, 0, wx.EXPAND, 6 )
		
		
		bSizer452.Add( bSizer63, 0, wx.BOTTOM|wx.RIGHT|wx.TOP, 6 )
		
		
		bSizer44.Add( bSizer452, 1, wx.EXPAND|wx.LEFT|wx.RIGHT, 6 )
		
		bSizer4521 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer4521.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.ButtonOk = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ButtonOk.SetDefault() 
		self.ButtonOk.SetMinSize( wx.Size( 120,28 ) )
		
		bSizer4521.Add( self.ButtonOk, 0, wx.ALL, 5 )
		
		self.ButtonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ButtonCancel.SetMinSize( wx.Size( 120,28 ) )
		
		bSizer4521.Add( self.ButtonCancel, 0, wx.ALL, 5 )
		
		
		bSizer44.Add( bSizer4521, 0, wx.ALL|wx.EXPAND, 6 )
		
		
		self.SetSizer( bSizer44 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.EngineList.Bind( wx.EVT_CHOICE, self.engine_select )
		self.IWADBrowse.Bind( wx.EVT_BUTTON, self.browse_iwad )
		self.Bind( wx.EVT_TOOL, self.pwad_add, id = PATCHINFO_TOOLBAR_ADD )
		self.Bind( wx.EVT_TOOL, self.pwad_remove, id = PATCHINFO_TOOLBAR_REMOVE )
		self.ButtonOk.Bind( wx.EVT_BUTTON, self.ok )
		self.ButtonCancel.Bind( wx.EVT_BUTTON, self.cancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def engine_select( self, event ):
		pass
	
	def browse_iwad( self, event ):
		pass
	
	def pwad_add( self, event ):
		pass
	
	def pwad_remove( self, event ):
		pass
	
	def ok( self, event ):
		pass
	
	def cancel( self, event ):
		pass
	

###########################################################################
## Class StartDialogBase
###########################################################################

class StartDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = DIALOG_START, title = u"WhackEd4", pos = wx.DefaultPosition, size = wx.Size( 600,340 ), style = wx.CAPTION )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer50 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer56 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer52 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.NewFile = wx.Button( self, START_NEW, u"New file", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.NewFile.SetMinSize( wx.Size( 160,28 ) )
		
		bSizer52.Add( self.NewFile, 1, wx.ALL, 6 )
		
		self.OpenFile = wx.Button( self, START_OPEN, u"Open file", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.OpenFile.SetMinSize( wx.Size( 160,28 ) )
		
		bSizer52.Add( self.OpenFile, 1, wx.ALL, 6 )
		
		
		bSizer56.Add( bSizer52, 0, wx.ALL|wx.EXPAND, 6 )
		
		bSizer54 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText50 = wx.StaticText( self, wx.ID_ANY, u"Recent files", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )
		bSizer54.Add( self.m_staticText50, 0, wx.LEFT|wx.RIGHT|wx.TOP, 5 )
		
		FileListChoices = []
		self.FileList = wx.ListBox( self, START_RECENT, wx.DefaultPosition, wx.DefaultSize, FileListChoices, 0 )
		bSizer54.Add( self.FileList, 1, wx.ALL|wx.EXPAND, 6 )
		
		
		bSizer56.Add( bSizer54, 1, wx.EXPAND|wx.LEFT|wx.RIGHT, 6 )
		
		
		bSizer56.AddSpacer( ( 0, 0), 0, wx.ALL|wx.EXPAND, 3 )
		
		
		bSizer50.Add( bSizer56, 1, wx.ALL|wx.EXPAND, 3 )
		
		bSizer55 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer55.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.Cancel = wx.Button( self, START_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Cancel.SetDefault() 
		self.Cancel.SetMinSize( wx.Size( 120,28 ) )
		
		bSizer55.Add( self.Cancel, 0, wx.BOTTOM|wx.LEFT|wx.RIGHT, 12 )
		
		
		bSizer50.Add( bSizer55, 0, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 3 )
		
		
		self.SetSizer( bSizer50 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.NewFile.Bind( wx.EVT_BUTTON, self.new_file )
		self.OpenFile.Bind( wx.EVT_BUTTON, self.open_file )
		self.FileList.Bind( wx.EVT_LISTBOX_DCLICK, self.open_file_list )
		self.Cancel.Bind( wx.EVT_BUTTON, self.cancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def new_file( self, event ):
		pass
	
	def open_file( self, event ):
		pass
	
	def open_file_list( self, event ):
		pass
	
	def cancel( self, event ):
		pass
	

###########################################################################
## Class AboutDialogBase
###########################################################################

class AboutDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = DIALOG_ABOUT, title = u"About WhackEd4", pos = wx.DefaultPosition, size = wx.Size( 640,478 ), style = wx.CAPTION )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer55 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer57 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap3 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/hatchet.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer57.Add( self.m_bitmap3, 0, wx.BOTTOM|wx.LEFT, 6 )
		
		
		bSizer55.Add( bSizer57, 0, wx.ALL|wx.EXPAND, 12 )
		
		bSizer56 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap4 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/logo.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer56.Add( self.m_bitmap4, 0, wx.LEFT|wx.RIGHT|wx.TOP, 6 )
		
		self.Version = wx.StaticText( self, wx.ID_ANY, u"Version", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Version.Wrap( -1 )
		bSizer56.Add( self.Version, 0, wx.ALL, 6 )
		
		
		bSizer56.AddSpacer( ( 0, 9), 0, wx.EXPAND, 5 )
		
		self.URL = wx.HyperlinkCtrl( self, wx.ID_ANY, u"http://www.teamhellspawn.com/exl/whacked4", u"http://www.teamhellspawn.com/exl/whacked4", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
		bSizer56.Add( self.URL, 0, wx.ALL, 6 )
		
		
		bSizer56.AddSpacer( ( 0, 9), 0, wx.EXPAND, 5 )
		
		bSizer84 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1391 = wx.StaticText( self, wx.ID_ANY, u"Application icon by Paul Davey, from the ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1391.Wrap( -1 )
		bSizer84.Add( self.m_staticText1391, 0, wx.BOTTOM|wx.LEFT|wx.TOP, 6 )
		
		self.URL1 = wx.HyperlinkCtrl( self, wx.ID_ANY, u"Buuf Icon set", u"http://www.iconarchive.com/show/buuf-icons-by-mattahan.html", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
		bSizer84.Add( self.URL1, 0, wx.BOTTOM|wx.RIGHT|wx.TOP, 6 )
		
		
		bSizer56.Add( bSizer84, 0, wx.EXPAND, 5 )
		
		
		bSizer56.AddSpacer( ( 0, 9), 0, wx.EXPAND, 5 )
		
		self.m_staticText139 = wx.StaticText( self, wx.ID_ANY, u"Thanks to...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText139.Wrap( -1 )
		bSizer56.Add( self.m_staticText139, 0, wx.LEFT|wx.RIGHT|wx.TOP, 6 )
		
		self.m_staticText138 = wx.StaticText( self, wx.ID_ANY, u"Aliotroph?, Andy Fox, Andy Shawaluk, Big_Al, CodeImp, CSabo, Dani J666, Daniel Carroll, Doom Dude, DooMAD, EarthQuake, Enjay, esselfortium, Frades, Francesco Orsenigo, Greg Lewis, iori, Kurisutaru, Leonard Pitre, Looney, Marc. A. Pullen, Palladium, Rellik, REZ, Skullers, SlayeR, un4seen, XDelusion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText138.Wrap( 450 )
		bSizer56.Add( self.m_staticText138, 0, wx.ALL, 6 )
		
		
		bSizer56.AddSpacer( ( 0, 9), 0, wx.EXPAND, 5 )
		
		self.License = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		self.License.SetFont( wx.Font( 7, 70, 90, 90, False, "Courier New" ) )
		
		bSizer56.Add( self.License, 1, wx.ALL|wx.EXPAND, 6 )
		
		
		bSizer56.AddSpacer( ( 0, 9), 0, wx.EXPAND, 5 )
		
		bSizer58 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer58.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.ButtonOk = wx.Button( self, ABOUT_OK, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ButtonOk.SetDefault() 
		self.ButtonOk.SetMinSize( wx.Size( 150,28 ) )
		
		bSizer58.Add( self.ButtonOk, 0, 0, 0 )
		
		
		bSizer56.Add( bSizer58, 0, wx.EXPAND, 0 )
		
		
		bSizer55.Add( bSizer56, 1, wx.BOTTOM|wx.EXPAND|wx.RIGHT|wx.TOP, 12 )
		
		
		self.SetSizer( bSizer55 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.ButtonOk.Bind( wx.EVT_BUTTON, self.ok )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def ok( self, event ):
		pass
	

