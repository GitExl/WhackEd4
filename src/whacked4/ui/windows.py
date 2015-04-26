# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from whacked4.ui import spritepreview

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
THING_VAL_ID = 1686
THING_VAL_HEALTH = 1687
THING_VAL_SPEED = 1688
THING_VAL_RADIUS = 1689
THING_VAL_HEIGHT = 1690
THING_VAL_DAMAGE = 1691
THING_VAL_REACTIONTIME = 1692
THING_VAL_PAINCHANCE = 1693
THING_VAL_MASS = 1694
THING_VAL_GAME = 1695
THING_VAL_SPAWNID = 1696
THING_VAL_RESPAWNTIME = 1697
THING_VAL_RENDERSTYLE = 1698
THING_VAL_ALPHA = 1699
THING_VAL_SCALE = 1700
THING_VAL_DECAL = 1701
THING_RENAME = 1702
THING_RESTORE = 1703
THING_STATE_SPAWN = 1704
THING_STATENAME_SPAWN = 1705
THING_STATESET_SPAWN = 1706
THING_STATE_WALK = 1707
THING_STATENAME_WALK = 1708
THING_STATESET_WALK = 1709
THING_STATE_PAIN = 1710
THING_STATENAME_PAIN = 1711
THING_STATESET_PAIN = 1712
THING_STATE_MELEE = 1713
THING_STATENAME_MELEE = 1714
THING_STATESET_MELEE = 1715
THING_STATE_ATTACK = 1716
THING_STATENAME_ATTACK = 1717
THING_STATESET_ATTACK = 1718
THING_STATE_DEATH = 1719
THING_STATENAME_DEATH = 1720
THING_STATESET_DEATH = 1721
THING_STATE_EXPLODE = 1722
THING_STATENAME_EXPLODE = 1723
THING_STATESET_EXPLODE = 1724
THING_STATE_RAISE = 1725
THING_STATENAME_RAISE = 1726
THING_STATESET_RAISE = 1727
THING_STATE_CRASH = 1728
THING_STATENAME_CRASH = 1729
THING_STATESET_CRASH = 1730
THING_STATE_FREEZE = 1731
THING_STATENAME_FREEZE = 1732
THING_STATESET_FREEZE = 1733
THING_STATE_BURN = 1734
THING_STATENAME_BURN = 1735
THING_STATESET_BURN = 1736
THING_SOUND_ALERT = 1737
THING_SOUNDNAME_ALERT = 1738
THING_SOUNDSET_ALERT = 1739
THING_SOUND_ATTACK = 1740
THING_SOUNDNAME_ATTACK = 1741
THING_SOUNDSET_ATTACK = 1742
THING_SOUND_PAIN = 1743
THING_SOUNDNAME_PAIN = 1744
THING_SOUNDSET_PAIN = 1745
THING_SOUND_DEATH = 1746
THING_SOUNDNAME_DEATH = 1747
THING_SOUNDSET_DEATH = 1748
THING_SOUND_ACTIVE = 1749
THING_SOUNDNAME_ACTIVE = 1750
THING_SOUNDSET_ACTIVE = 1751
THING_FLAGS = 1752
THING_LIST = 1753
FRAME_STATES = 1754
STATES_SPRITE = 1755
STATES_FRAME = 1756
STATES_FRAMESPIN = 1757
STATES_LIT = 1758
STATES_NEXT = 1759
STATES_DURATION = 1760
STATES_ACTION = 1761
STATES_LABEL_UNUSED1 = 1762
STATES_UNUSED1 = 1763
STATES_LABEL_UNUSED2 = 1764
STATES_UNUSED2 = 1765
STATES_LABEL_ARG1 = 1766
STATES_ARG1 = 1767
STATES_LABEL_ARG2 = 1768
STATES_ARG2 = 1769
STATES_LABEL_ARG3 = 1770
STATES_ARG3 = 1771
STATES_LABEL_ARG4 = 1772
STATES_ARG4 = 1773
STATES_LABEL_ARG5 = 1774
STATES_ARG5 = 1775
STATES_LABEL_ARG6 = 1776
STATES_ARG6 = 1777
STATES_LABEL_ARG7 = 1778
STATES_ARG7 = 1779
STATES_LABEL_ARG8 = 1780
STATES_ARG8 = 1781
STATES_LABEL_ARG9 = 1782
STATES_ARG9 = 1783
STATES_FILTER = 1784
STATES_FILTERTOOLS = 1785
STATES_FILTERTOOLS_REFRESH = 1786
FRAME_SOUNDS = 1787
SOUNDS_PRIORITY = 1788
SOUNDS_PRIORITYSPIN = 1789
SOUNDS_SINGULAR = 1790
SOUNDS_RESTORE = 1791
SOUNDS_LIST = 1792
FRAME_STRINGS = 1793
STRINGS_LIST = 1794
STRINGS_RESTORE = 1795
FRAME_WEAPONS = 1796
WEAPON_AMMOTYPE = 1797
WEAPON_STATE_SELECT = 1798
WEAPON_STATENAME_SELECT = 1799
WEAPON_STATESET_SELECT = 1800
WEAPON_STATE_DESELECT = 1801
WEAPON_STATENAME_DESELECT = 1802
WEAPON_STATESET_DESELECT = 1803
WEAPON_STATE_BOB = 1804
WEAPON_STATENAME_BOB = 1805
WEAPON_STATESET_BOB = 1806
WEAPON_STATE_FIRE = 1807
WEAPON_STATENAME_FIRE = 1808
WEAPON_STATESET_FIRE = 1809
WEAPON_STATE_MUZZLE = 1810
WEAPON_STATENAME_MUZZLE = 1811
WEAPON_STATESET_MUZZLE = 1812
WEAPON_RENAME = 1813
WEAPON_RESTORE = 1814
FRAME_AMMO = 1815
AMMO_VAL_MAXIMUM = 1816
AMMO_VAL_PICKUP = 1817
AMMO_RENAME = 1818
AMMO_RESTORE = 1819
AMMO_LIST = 1820
FRAME_CHEATS = 1821
CHEATS_LIST = 1822
CHEATS_RESTORE = 1823
FRAME_MISC = 1824
MISC_VALUE = 1825
MISC_VALUE_ENABLED = 1826
MISC_RESTORE = 1827
MISC_LIST = 1828
FRAME_PAR = 1829
PAR_EPISODE = 1830
PAR_MAP = 1831
PAR_SECONDS = 1832
PAR_TOOLS = 1833
PAR_TOOL_ADD = 1834
PAR_TOOL_REMOVE = 1835
PAR_LIST = 1836
DIALOG_SPRITES = 1837
SPRITES_FILTER = 1838
SPRITES_FRAME = 1839
SPRITES_FRAMESPIN = 1840
SPRITES_OK = 1841
SPRITES_CANCEL = 1842
STRING_OLD = 1843
STRING_NEW = 1844
STRING_OK = 1845
STRING_CANCEL = 1846
DIALOG_PATCHINFO = 1847
PATCHINFO_TOOLBAR = 1848
PATCHINFO_TOOLBAR_ADD = 1849
PATCHINFO_TOOLBAR_REMOVE = 1850
PATCHINFO_CANCEL = 1851
DIALOG_START = 1852
START_NEW = 1853
START_OPEN = 1854
START_RECENT = 1855
START_CANCEL = 1856
DIALOG_ABOUT = 1857
ABOUT_OK = 1858
DIALOG_ERROR = 1859
ERROR_REPORT = 1860
ERROR_COPY = 1861
ERROR_CLOSE = 1862

###########################################################################
## Class MainFrameBase
###########################################################################

class MainFrameBase ( wx.MDIParentFrame ):
	
	def __init__( self, parent ):
		wx.MDIParentFrame.__init__ ( self, parent, id = WINDOW_MAIN, title = u"WhackEd4", pos = wx.DefaultPosition, size = wx.Size( 1024,560 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU|wx.HSCROLL|wx.VSCROLL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.MainToolbar = self.CreateToolBar( wx.TB_FLAT|wx.TB_HORZ_TEXT|wx.TB_NODIVIDER|wx.TB_TEXT|wx.TB_VERTICAL, wx.ID_ANY )
		self.MainToolbar.SetToolBitmapSize( wx.Size( 40,40 ) )
		self.MainToolbar.SetToolSeparation( 1 )
		self.ToolThings = self.MainToolbar.AddLabelTool( MAIN_TOOL_THINGS, u" Things", wx.Bitmap( u"res/editor-things.ico", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, wx.EmptyString, wx.EmptyString, None ) 
		
		self.ToolStates = self.MainToolbar.AddLabelTool( MAIN_TOOL_STATES, u" States", wx.Bitmap( u"res/editor-states.ico", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, wx.EmptyString, wx.EmptyString, None ) 
		
		self.ToolSounds = self.MainToolbar.AddLabelTool( MAIN_TOOL_SOUNDS, u" Sounds", wx.Bitmap( u"res/editor-sounds.ico", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, wx.EmptyString, wx.EmptyString, None ) 
		
		self.ToolStrings = self.MainToolbar.AddLabelTool( MAIN_TOOL_STRINGS, u" Strings", wx.Bitmap( u"res/editor-strings.ico", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, wx.EmptyString, wx.EmptyString, None ) 
		
		self.ToolsWeapons = self.MainToolbar.AddLabelTool( MAIN_TOOL_WEAPONS, u" Weapons", wx.Bitmap( u"res/editor-weapons.ico", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, wx.EmptyString, wx.EmptyString, None ) 
		
		self.ToolAmmo = self.MainToolbar.AddLabelTool( MAIN_TOOL_AMMO, u" Ammo", wx.Bitmap( u"res/editor-ammo.ico", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, wx.EmptyString, wx.EmptyString, None ) 
		
		self.ToolCheats = self.MainToolbar.AddLabelTool( MAIN_TOOL_CHEATS, u" Cheats", wx.Bitmap( u"res/editor-cheats.ico", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, wx.EmptyString, wx.EmptyString, None ) 
		
		self.ToolMiscellaneous = self.MainToolbar.AddLabelTool( MAIN_TOOL_MISC, u" Miscellaneous  ", wx.Bitmap( u"res/editor-misc.ico", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, wx.EmptyString, wx.EmptyString, None ) 
		
		self.ToolPar = self.MainToolbar.AddLabelTool( MAIN_TOOL_PAR, u" Par times", wx.Bitmap( u"res/editor-par.ico", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, wx.EmptyString, wx.EmptyString, None ) 
		
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
		self.Bind( wx.EVT_TOOL, self.editor_window_tooltoggle, id = self.ToolThings.GetId() )
		self.Bind( wx.EVT_TOOL, self.editor_window_tooltoggle, id = self.ToolStates.GetId() )
		self.Bind( wx.EVT_TOOL, self.editor_window_tooltoggle, id = self.ToolSounds.GetId() )
		self.Bind( wx.EVT_TOOL, self.editor_window_tooltoggle, id = self.ToolStrings.GetId() )
		self.Bind( wx.EVT_TOOL, self.editor_window_tooltoggle, id = self.ToolsWeapons.GetId() )
		self.Bind( wx.EVT_TOOL, self.editor_window_tooltoggle, id = self.ToolAmmo.GetId() )
		self.Bind( wx.EVT_TOOL, self.editor_window_tooltoggle, id = self.ToolCheats.GetId() )
		self.Bind( wx.EVT_TOOL, self.editor_window_tooltoggle, id = self.ToolMiscellaneous.GetId() )
		self.Bind( wx.EVT_TOOL, self.editor_window_tooltoggle, id = self.ToolPar.GetId() )
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
## Class ThingsFrameBase
###########################################################################

class ThingsFrameBase ( wx.MDIChildFrame ):
	
	def __init__( self, parent ):
		wx.MDIChildFrame.__init__ ( self, parent, id = FRAME_THINGS, title = u"Things", pos = wx.DefaultPosition, size = wx.Size( 980,650 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU )
		
		self.SetSizeHintsSz( wx.Size( 980,650 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		Sizer26 = wx.BoxSizer( wx.HORIZONTAL )
		
		Sizer27 = wx.BoxSizer( wx.VERTICAL )
		
		self.PropertiesLabel = wx.StaticText( self, wx.ID_ANY, u"Properties", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PropertiesLabel.Wrap( -1 )
		self.PropertiesLabel.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		Sizer27.Add( self.PropertiesLabel, 0, wx.ALL, 3 )
		
		Sizer28 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingIdLabel = wx.StaticText( self, wx.ID_ANY, u"Id", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingIdLabel.Wrap( -1 )
		Sizer28.Add( self.ThingIdLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingId = wx.TextCtrl( self, THING_VAL_ID, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.ThingId.SetMaxLength( 6 ) 
		Sizer28.Add( self.ThingId, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 3 )
		
		
		Sizer27.Add( Sizer28, 0, wx.ALL|wx.EXPAND, 0 )
		
		Sizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingHealthLabel = wx.StaticText( self, wx.ID_ANY, u"Health", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingHealthLabel.Wrap( -1 )
		Sizer1.Add( self.ThingHealthLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingHealth = wx.TextCtrl( self, THING_VAL_HEALTH, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.ThingHealth.SetMaxLength( 6 ) 
		Sizer1.Add( self.ThingHealth, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		Sizer27.Add( Sizer1, 0, wx.EXPAND, 0 )
		
		Sizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingSpeeLabel = wx.StaticText( self, wx.ID_ANY, u"Speed", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingSpeeLabel.Wrap( -1 )
		Sizer2.Add( self.ThingSpeeLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingSpeed = wx.TextCtrl( self, THING_VAL_SPEED, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.ThingSpeed.SetMaxLength( 6 ) 
		Sizer2.Add( self.ThingSpeed, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		Sizer27.Add( Sizer2, 0, wx.EXPAND, 0 )
		
		Sizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingRadiusLabel = wx.StaticText( self, wx.ID_ANY, u"Radius", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingRadiusLabel.Wrap( -1 )
		Sizer3.Add( self.ThingRadiusLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingRadius = wx.TextCtrl( self, THING_VAL_RADIUS, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.ThingRadius.SetMaxLength( 6 ) 
		Sizer3.Add( self.ThingRadius, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		Sizer27.Add( Sizer3, 0, wx.EXPAND, 0 )
		
		Sizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingHeightLabel = wx.StaticText( self, wx.ID_ANY, u"Height", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingHeightLabel.Wrap( -1 )
		Sizer4.Add( self.ThingHeightLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingHeight = wx.TextCtrl( self, THING_VAL_HEIGHT, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.ThingHeight.SetMaxLength( 6 ) 
		Sizer4.Add( self.ThingHeight, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		Sizer27.Add( Sizer4, 0, wx.EXPAND, 0 )
		
		Sizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingDamageLabel = wx.StaticText( self, wx.ID_ANY, u"Damage", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingDamageLabel.Wrap( -1 )
		Sizer5.Add( self.ThingDamageLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingDamage = wx.TextCtrl( self, THING_VAL_DAMAGE, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.ThingDamage.SetMaxLength( 6 ) 
		Sizer5.Add( self.ThingDamage, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		Sizer27.Add( Sizer5, 0, wx.EXPAND, 0 )
		
		Sizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingReactionTimeLabel = wx.StaticText( self, wx.ID_ANY, u"Reaction time", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingReactionTimeLabel.Wrap( -1 )
		Sizer6.Add( self.ThingReactionTimeLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingReactionTime = wx.TextCtrl( self, THING_VAL_REACTIONTIME, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.ThingReactionTime.SetMaxLength( 6 ) 
		Sizer6.Add( self.ThingReactionTime, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		Sizer27.Add( Sizer6, 0, wx.EXPAND, 0 )
		
		Sizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingPainChanceLabel = wx.StaticText( self, wx.ID_ANY, u"Pain chance", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingPainChanceLabel.Wrap( -1 )
		Sizer7.Add( self.ThingPainChanceLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingPainChance = wx.TextCtrl( self, THING_VAL_PAINCHANCE, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.ThingPainChance.SetMaxLength( 6 ) 
		Sizer7.Add( self.ThingPainChance, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		Sizer27.Add( Sizer7, 0, wx.EXPAND, 0 )
		
		Sizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingMassLabel = wx.StaticText( self, wx.ID_ANY, u"Mass", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingMassLabel.Wrap( -1 )
		Sizer8.Add( self.ThingMassLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingMass = wx.TextCtrl( self, THING_VAL_MASS, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.ThingMass.SetMaxLength( 6 ) 
		Sizer8.Add( self.ThingMass, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		Sizer27.Add( Sizer8, 0, wx.EXPAND, 0 )
		
		
		Sizer27.AddSpacer( ( 0, 16), 0, wx.EXPAND, 5 )
		
		Sizer82 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingGameLabel = wx.StaticText( self, wx.ID_ANY, u"Game", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingGameLabel.Wrap( -1 )
		Sizer82.Add( self.ThingGameLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		ThingGameChoices = []
		self.ThingGame = wx.Choice( self, THING_VAL_GAME, wx.DefaultPosition, wx.Size( 100,-1 ), ThingGameChoices, 0 )
		self.ThingGame.SetSelection( 0 )
		Sizer82.Add( self.ThingGame, 0, wx.ALL, 3 )
		
		
		Sizer27.Add( Sizer82, 0, wx.EXPAND, 0 )
		
		Sizer81 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingSpawnIdLabel = wx.StaticText( self, wx.ID_ANY, u"Spawn Id", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingSpawnIdLabel.Wrap( -1 )
		Sizer81.Add( self.ThingSpawnIdLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingSpawnId = wx.TextCtrl( self, THING_VAL_SPAWNID, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.ThingSpawnId.SetMaxLength( 6 ) 
		Sizer81.Add( self.ThingSpawnId, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		Sizer27.Add( Sizer81, 0, wx.EXPAND, 0 )
		
		Sizer83 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingRespawnTimeLabel = wx.StaticText( self, wx.ID_ANY, u"Respawn time", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingRespawnTimeLabel.Wrap( -1 )
		Sizer83.Add( self.ThingRespawnTimeLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingRespawnTime = wx.TextCtrl( self, THING_VAL_RESPAWNTIME, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.ThingRespawnTime.SetMaxLength( 6 ) 
		Sizer83.Add( self.ThingRespawnTime, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		Sizer27.Add( Sizer83, 0, wx.EXPAND, 0 )
		
		Sizer84 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingRenderStyleLabel = wx.StaticText( self, wx.ID_ANY, u"Render style", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingRenderStyleLabel.Wrap( -1 )
		Sizer84.Add( self.ThingRenderStyleLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		ThingRenderStyleChoices = []
		self.ThingRenderStyle = wx.Choice( self, THING_VAL_RENDERSTYLE, wx.DefaultPosition, wx.Size( 100,-1 ), ThingRenderStyleChoices, 0 )
		self.ThingRenderStyle.SetSelection( 0 )
		Sizer84.Add( self.ThingRenderStyle, 0, wx.ALL, 3 )
		
		
		Sizer27.Add( Sizer84, 0, wx.EXPAND, 0 )
		
		Sizer85 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingAlphaLabel = wx.StaticText( self, wx.ID_ANY, u"Alpha", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingAlphaLabel.Wrap( -1 )
		Sizer85.Add( self.ThingAlphaLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingAlpha = wx.TextCtrl( self, THING_VAL_ALPHA, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.ThingAlpha.SetMaxLength( 6 ) 
		Sizer85.Add( self.ThingAlpha, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		Sizer27.Add( Sizer85, 0, wx.EXPAND, 0 )
		
		Sizer86 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingScaleLabel = wx.StaticText( self, wx.ID_ANY, u"Scale", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingScaleLabel.Wrap( -1 )
		Sizer86.Add( self.ThingScaleLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingScale = wx.TextCtrl( self, THING_VAL_SCALE, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.ThingScale.SetMaxLength( 6 ) 
		Sizer86.Add( self.ThingScale, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		Sizer27.Add( Sizer86, 0, wx.EXPAND, 0 )
		
		Sizer87 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingDecalLabel = wx.StaticText( self, wx.ID_ANY, u"Decal", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ThingDecalLabel.Wrap( -1 )
		Sizer87.Add( self.ThingDecalLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingDecal = wx.TextCtrl( self, THING_VAL_DECAL, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.ThingDecal.SetMaxLength( 6 ) 
		Sizer87.Add( self.ThingDecal, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		Sizer27.Add( Sizer87, 0, wx.EXPAND, 0 )
		
		
		Sizer27.AddSpacer( ( 0, 16), 0, wx.EXPAND, 5 )
		
		bSizer42 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer42.AddSpacer( ( 0, 0), 1, wx.EXPAND, 0 )
		
		self.ButtonRename = wx.Button( self, THING_RENAME, u"Rename", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ButtonRename.SetMinSize( wx.Size( -1,28 ) )
		
		bSizer42.Add( self.ButtonRename, 0, wx.ALL|wx.EXPAND, 0 )
		
		self.ButtonRestore = wx.Button( self, THING_RESTORE, u"Restore", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.ButtonRestore.SetMinSize( wx.Size( -1,28 ) )
		
		bSizer42.Add( self.ButtonRestore, 0, wx.EXPAND|wx.TOP, 3 )
		
		
		Sizer27.Add( bSizer42, 1, wx.EXPAND, 3 )
		
		
		Sizer26.Add( Sizer27, 0, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.TOP, 9 )
		
		
		Sizer26.AddSpacer( ( 12, 0), 0, 0, 0 )
		
		bSizer43 = wx.BoxSizer( wx.VERTICAL )
		
		self.StatesLabel = wx.StaticText( self, wx.ID_ANY, u"States", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.StatesLabel.Wrap( -1 )
		self.StatesLabel.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer43.Add( self.StatesLabel, 0, wx.ALL, 3 )
		
		Sizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingStateSpawnLabel = wx.StaticText( self, wx.ID_ANY, u"Spawn", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingStateSpawnLabel.Wrap( -1 )
		Sizer9.Add( self.ThingStateSpawnLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateSpawn = wx.TextCtrl( self, THING_STATE_SPAWN, u"318", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.ThingStateSpawn.SetMaxLength( 4 ) 
		Sizer9.Add( self.ThingStateSpawn, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateSpawnName = wx.StaticText( self, THING_STATENAME_SPAWN, u"TROOA", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingStateSpawnName.Wrap( -1 )
		self.ThingStateSpawnName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.ThingStateSpawnName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		Sizer9.Add( self.ThingStateSpawnName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateSpawnSet = wx.Button( self, THING_STATESET_SPAWN, u"<", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.ThingStateSpawnSet.SetMinSize( wx.Size( 25,25 ) )
		
		Sizer9.Add( self.ThingStateSpawnSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )
		
		
		bSizer43.Add( Sizer9, 0, wx.EXPAND, 0 )
		
		Sizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingStateWalkLabel = wx.StaticText( self, wx.ID_ANY, u"Walk", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingStateWalkLabel.Wrap( -1 )
		Sizer10.Add( self.ThingStateWalkLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateWalk = wx.TextCtrl( self, THING_STATE_WALK, u"318", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.ThingStateWalk.SetMaxLength( 4 ) 
		Sizer10.Add( self.ThingStateWalk, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateWalkName = wx.StaticText( self, THING_STATENAME_WALK, u"TROOA", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingStateWalkName.Wrap( -1 )
		self.ThingStateWalkName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.ThingStateWalkName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		Sizer10.Add( self.ThingStateWalkName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateWalkSet = wx.Button( self, THING_STATESET_WALK, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingStateWalkSet.SetMinSize( wx.Size( 25,25 ) )
		
		Sizer10.Add( self.ThingStateWalkSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )
		
		
		bSizer43.Add( Sizer10, 0, wx.EXPAND, 0 )
		
		Sizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingStatePainLabel = wx.StaticText( self, wx.ID_ANY, u"Pain", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingStatePainLabel.Wrap( -1 )
		Sizer11.Add( self.ThingStatePainLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStatePain = wx.TextCtrl( self, THING_STATE_PAIN, u"318", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.ThingStatePain.SetMaxLength( 4 ) 
		Sizer11.Add( self.ThingStatePain, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStatePainName = wx.StaticText( self, THING_STATENAME_PAIN, u"TROOA", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingStatePainName.Wrap( -1 )
		self.ThingStatePainName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.ThingStatePainName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		Sizer11.Add( self.ThingStatePainName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStatePainSet = wx.Button( self, THING_STATESET_PAIN, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingStatePainSet.SetMinSize( wx.Size( 25,25 ) )
		
		Sizer11.Add( self.ThingStatePainSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )
		
		
		bSizer43.Add( Sizer11, 0, wx.EXPAND, 0 )
		
		Sizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingStateMeleeLabel = wx.StaticText( self, wx.ID_ANY, u"Melee", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingStateMeleeLabel.Wrap( -1 )
		Sizer12.Add( self.ThingStateMeleeLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateMelee = wx.TextCtrl( self, THING_STATE_MELEE, u"318", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.ThingStateMelee.SetMaxLength( 4 ) 
		Sizer12.Add( self.ThingStateMelee, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateMeleeName = wx.StaticText( self, THING_STATENAME_MELEE, u"TROOA", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingStateMeleeName.Wrap( -1 )
		self.ThingStateMeleeName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.ThingStateMeleeName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		Sizer12.Add( self.ThingStateMeleeName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateMeleeSet = wx.Button( self, THING_STATESET_MELEE, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingStateMeleeSet.SetMinSize( wx.Size( 25,25 ) )
		
		Sizer12.Add( self.ThingStateMeleeSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )
		
		
		bSizer43.Add( Sizer12, 0, wx.EXPAND, 0 )
		
		Sizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingStateAttackLabel = wx.StaticText( self, wx.ID_ANY, u"Attack", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingStateAttackLabel.Wrap( -1 )
		Sizer13.Add( self.ThingStateAttackLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateAttack = wx.TextCtrl( self, THING_STATE_ATTACK, u"318", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.ThingStateAttack.SetMaxLength( 4 ) 
		Sizer13.Add( self.ThingStateAttack, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateAttackName = wx.StaticText( self, THING_STATENAME_ATTACK, u"TROOA", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingStateAttackName.Wrap( -1 )
		self.ThingStateAttackName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.ThingStateAttackName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		Sizer13.Add( self.ThingStateAttackName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateAttackSet = wx.Button( self, THING_STATESET_ATTACK, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingStateAttackSet.SetMinSize( wx.Size( 25,25 ) )
		
		Sizer13.Add( self.ThingStateAttackSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )
		
		
		bSizer43.Add( Sizer13, 0, wx.EXPAND, 0 )
		
		Sizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingStateDeathLabel = wx.StaticText( self, wx.ID_ANY, u"Death", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingStateDeathLabel.Wrap( -1 )
		Sizer14.Add( self.ThingStateDeathLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateDeath = wx.TextCtrl( self, THING_STATE_DEATH, u"318", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.ThingStateDeath.SetMaxLength( 4 ) 
		Sizer14.Add( self.ThingStateDeath, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateDeathName = wx.StaticText( self, THING_STATENAME_DEATH, u"TROOA", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingStateDeathName.Wrap( -1 )
		self.ThingStateDeathName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.ThingStateDeathName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		Sizer14.Add( self.ThingStateDeathName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateDeathSet = wx.Button( self, THING_STATESET_DEATH, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingStateDeathSet.SetMinSize( wx.Size( 25,25 ) )
		
		Sizer14.Add( self.ThingStateDeathSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )
		
		
		bSizer43.Add( Sizer14, 0, wx.EXPAND, 0 )
		
		Sizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingStateExplodeLabel = wx.StaticText( self, wx.ID_ANY, u"Explode", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingStateExplodeLabel.Wrap( -1 )
		Sizer15.Add( self.ThingStateExplodeLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateExplode = wx.TextCtrl( self, THING_STATE_EXPLODE, u"318", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.ThingStateExplode.SetMaxLength( 4 ) 
		Sizer15.Add( self.ThingStateExplode, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateExplodeName = wx.StaticText( self, THING_STATENAME_EXPLODE, u"TROOA", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingStateExplodeName.Wrap( -1 )
		self.ThingStateExplodeName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.ThingStateExplodeName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		Sizer15.Add( self.ThingStateExplodeName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateExplodeSet = wx.Button( self, THING_STATESET_EXPLODE, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingStateExplodeSet.SetMinSize( wx.Size( 25,25 ) )
		
		Sizer15.Add( self.ThingStateExplodeSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )
		
		
		bSizer43.Add( Sizer15, 0, wx.EXPAND, 0 )
		
		Sizer152 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingStateRaiseLabel = wx.StaticText( self, wx.ID_ANY, u"Raise", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingStateRaiseLabel.Wrap( -1 )
		Sizer152.Add( self.ThingStateRaiseLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateRaise = wx.TextCtrl( self, THING_STATE_RAISE, u"318", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.ThingStateRaise.SetMaxLength( 4 ) 
		Sizer152.Add( self.ThingStateRaise, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateRaiseName = wx.StaticText( self, THING_STATENAME_RAISE, u"TROOA", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingStateRaiseName.Wrap( -1 )
		self.ThingStateRaiseName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.ThingStateRaiseName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		Sizer152.Add( self.ThingStateRaiseName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateRaiseSet = wx.Button( self, THING_STATESET_RAISE, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingStateRaiseSet.SetMinSize( wx.Size( 25,25 ) )
		
		Sizer152.Add( self.ThingStateRaiseSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )
		
		
		bSizer43.Add( Sizer152, 0, wx.EXPAND, 0 )
		
		Sizer1521 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingStateCrashLabel = wx.StaticText( self, wx.ID_ANY, u"Crash", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingStateCrashLabel.Wrap( -1 )
		Sizer1521.Add( self.ThingStateCrashLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateCrash = wx.TextCtrl( self, THING_STATE_CRASH, u"318", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.ThingStateCrash.SetMaxLength( 4 ) 
		Sizer1521.Add( self.ThingStateCrash, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateCrashName = wx.StaticText( self, THING_STATENAME_CRASH, u"TROOA", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingStateCrashName.Wrap( -1 )
		self.ThingStateCrashName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.ThingStateCrashName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		Sizer1521.Add( self.ThingStateCrashName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateCrashSet = wx.Button( self, THING_STATESET_CRASH, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingStateCrashSet.SetMinSize( wx.Size( 25,25 ) )
		
		Sizer1521.Add( self.ThingStateCrashSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )
		
		
		bSizer43.Add( Sizer1521, 0, wx.EXPAND, 0 )
		
		Sizer1522 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingStateFreezeLabel = wx.StaticText( self, wx.ID_ANY, u"Freeze", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingStateFreezeLabel.Wrap( -1 )
		Sizer1522.Add( self.ThingStateFreezeLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateFreeze = wx.TextCtrl( self, THING_STATE_FREEZE, u"318", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.ThingStateFreeze.SetMaxLength( 4 ) 
		Sizer1522.Add( self.ThingStateFreeze, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateFreezeName = wx.StaticText( self, THING_STATENAME_FREEZE, u"TROOA", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingStateFreezeName.Wrap( -1 )
		self.ThingStateFreezeName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.ThingStateFreezeName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		Sizer1522.Add( self.ThingStateFreezeName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateFreezeSet = wx.Button( self, THING_STATESET_FREEZE, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingStateFreezeSet.SetMinSize( wx.Size( 25,25 ) )
		
		Sizer1522.Add( self.ThingStateFreezeSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )
		
		
		bSizer43.Add( Sizer1522, 0, wx.EXPAND, 0 )
		
		Sizer1523 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingStateBurnLabel = wx.StaticText( self, wx.ID_ANY, u"Burn", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingStateBurnLabel.Wrap( -1 )
		Sizer1523.Add( self.ThingStateBurnLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateBurn = wx.TextCtrl( self, THING_STATE_BURN, u"318", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.ThingStateBurn.SetMaxLength( 4 ) 
		Sizer1523.Add( self.ThingStateBurn, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateBurnName = wx.StaticText( self, THING_STATENAME_BURN, u"TROOA", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingStateBurnName.Wrap( -1 )
		self.ThingStateBurnName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.ThingStateBurnName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		Sizer1523.Add( self.ThingStateBurnName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingStateBurnSet = wx.Button( self, THING_STATESET_BURN, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingStateBurnSet.SetMinSize( wx.Size( 25,25 ) )
		
		Sizer1523.Add( self.ThingStateBurnSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )
		
		
		bSizer43.Add( Sizer1523, 0, wx.EXPAND, 0 )
		
		
		bSizer43.AddSpacer( ( 0, 16), 0, wx.EXPAND, 3 )
		
		self.SoundsLabel = wx.StaticText( self, wx.ID_ANY, u"Sounds", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SoundsLabel.Wrap( -1 )
		self.SoundsLabel.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer43.Add( self.SoundsLabel, 0, wx.ALL, 3 )
		
		Sizer151 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingSoundAlertLabel = wx.StaticText( self, wx.ID_ANY, u"Alert", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingSoundAlertLabel.Wrap( -1 )
		Sizer151.Add( self.ThingSoundAlertLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingSoundAlert = wx.TextCtrl( self, THING_SOUND_ALERT, u"46", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.ThingSoundAlert.SetMaxLength( 4 ) 
		Sizer151.Add( self.ThingSoundAlert, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingSoundAlertName = wx.StaticText( self, THING_SOUNDNAME_ALERT, u"PLPAIN", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingSoundAlertName.Wrap( -1 )
		self.ThingSoundAlertName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.ThingSoundAlertName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		Sizer151.Add( self.ThingSoundAlertName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingSoundAlertSet = wx.Button( self, THING_SOUNDSET_ALERT, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingSoundAlertSet.SetMinSize( wx.Size( 25,25 ) )
		
		Sizer151.Add( self.ThingSoundAlertSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )
		
		
		bSizer43.Add( Sizer151, 0, wx.EXPAND, 5 )
		
		Sizer1511 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingSoundAttackLabel = wx.StaticText( self, wx.ID_ANY, u"Attack", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingSoundAttackLabel.Wrap( -1 )
		Sizer1511.Add( self.ThingSoundAttackLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingSoundAttack = wx.TextCtrl( self, THING_SOUND_ATTACK, u"46", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.ThingSoundAttack.SetMaxLength( 4 ) 
		Sizer1511.Add( self.ThingSoundAttack, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingSoundAttackName = wx.StaticText( self, THING_SOUNDNAME_ATTACK, u"PLPAIN", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingSoundAttackName.Wrap( -1 )
		self.ThingSoundAttackName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.ThingSoundAttackName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		Sizer1511.Add( self.ThingSoundAttackName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingSoundAttackSet = wx.Button( self, THING_SOUNDSET_ATTACK, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingSoundAttackSet.SetMinSize( wx.Size( 25,25 ) )
		
		Sizer1511.Add( self.ThingSoundAttackSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )
		
		
		bSizer43.Add( Sizer1511, 0, wx.EXPAND, 5 )
		
		Sizer1512 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingSoundPainLabel = wx.StaticText( self, wx.ID_ANY, u"Pain", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingSoundPainLabel.Wrap( -1 )
		Sizer1512.Add( self.ThingSoundPainLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingSoundPain = wx.TextCtrl( self, THING_SOUND_PAIN, u"46", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.ThingSoundPain.SetMaxLength( 4 ) 
		Sizer1512.Add( self.ThingSoundPain, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingSoundPainName = wx.StaticText( self, THING_SOUNDNAME_PAIN, u"PLPAIN", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingSoundPainName.Wrap( -1 )
		self.ThingSoundPainName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.ThingSoundPainName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		Sizer1512.Add( self.ThingSoundPainName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingSoundPainSet = wx.Button( self, THING_SOUNDSET_PAIN, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingSoundPainSet.SetMinSize( wx.Size( 25,25 ) )
		
		Sizer1512.Add( self.ThingSoundPainSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )
		
		
		bSizer43.Add( Sizer1512, 0, wx.EXPAND, 5 )
		
		Sizer1513 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingSoundDeathLabel = wx.StaticText( self, wx.ID_ANY, u"Death", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingSoundDeathLabel.Wrap( -1 )
		Sizer1513.Add( self.ThingSoundDeathLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingSoundDeath = wx.TextCtrl( self, THING_SOUND_DEATH, u"46", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.ThingSoundDeath.SetMaxLength( 4 ) 
		Sizer1513.Add( self.ThingSoundDeath, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingSoundDeathName = wx.StaticText( self, THING_SOUNDNAME_DEATH, u"PLPAIN", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingSoundDeathName.Wrap( -1 )
		self.ThingSoundDeathName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.ThingSoundDeathName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		Sizer1513.Add( self.ThingSoundDeathName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingSoundDeathSet = wx.Button( self, THING_SOUNDSET_DEATH, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingSoundDeathSet.SetMinSize( wx.Size( 25,25 ) )
		
		Sizer1513.Add( self.ThingSoundDeathSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )
		
		
		bSizer43.Add( Sizer1513, 0, wx.EXPAND, 5 )
		
		Sizer1514 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ThingSoundActiveLabel = wx.StaticText( self, wx.ID_ANY, u"Active", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingSoundActiveLabel.Wrap( -1 )
		Sizer1514.Add( self.ThingSoundActiveLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingSoundActive = wx.TextCtrl( self, THING_SOUND_ACTIVE, u"46", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.ThingSoundActive.SetMaxLength( 4 ) 
		Sizer1514.Add( self.ThingSoundActive, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingSoundActiveName = wx.StaticText( self, THING_SOUNDNAME_ACTIVE, u"PLPAIN", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingSoundActiveName.Wrap( -1 )
		self.ThingSoundActiveName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.ThingSoundActiveName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		Sizer1514.Add( self.ThingSoundActiveName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.ThingSoundActiveSet = wx.Button( self, THING_SOUNDSET_ACTIVE, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingSoundActiveSet.SetMinSize( wx.Size( 25,25 ) )
		
		Sizer1514.Add( self.ThingSoundActiveSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )
		
		
		bSizer43.Add( Sizer1514, 0, wx.EXPAND, 5 )
		
		
		Sizer26.Add( bSizer43, 0, wx.BOTTOM|wx.EXPAND|wx.TOP, 9 )
		
		
		Sizer26.AddSpacer( ( 12, 0), 0, 0, 0 )
		
		bSizer122 = wx.BoxSizer( wx.VERTICAL )
		
		self.FlagsLabel = wx.StaticText( self, wx.ID_ANY, u"Flags", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FlagsLabel.Wrap( -1 )
		self.FlagsLabel.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer122.Add( self.FlagsLabel, 0, wx.ALL, 3 )
		
		ThingFlagsChoices = []
		self.ThingFlags = wx.CheckListBox( self, THING_FLAGS, wx.DefaultPosition, wx.Size( -1,-1 ), ThingFlagsChoices, 0|wx.SIMPLE_BORDER )
		self.ThingFlags.SetMinSize( wx.Size( 190,-1 ) )
		
		bSizer122.Add( self.ThingFlags, 1, wx.EXPAND, 3 )
		
		
		Sizer26.Add( bSizer122, 0, wx.BOTTOM|wx.EXPAND|wx.TOP, 9 )
		
		
		Sizer26.AddSpacer( ( 12, 0), 0, 0, 0 )
		
		self.ThingList = wx.ListCtrl( self, THING_LIST, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.NO_BORDER )
		Sizer26.Add( self.ThingList, 1, wx.EXPAND, 0 )
		
		
		self.SetSizer( Sizer26 )
		self.Layout()
		
		# Connect Events
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
		self.ThingGame.Bind( wx.EVT_CHOICE, self.set_game )
		self.ThingSpawnId.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingSpawnId.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingRespawnTime.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingRespawnTime.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingRenderStyle.Bind( wx.EVT_CHOICE, self.set_renderstyle )
		self.ThingAlpha.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingAlpha.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingScale.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingScale.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingDecal.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingDecal.Bind( wx.EVT_TEXT, self.set_value )
		self.ButtonRename.Bind( wx.EVT_BUTTON, self.thing_rename )
		self.ButtonRestore.Bind( wx.EVT_BUTTON, self.thing_restore )
		self.ThingStateSpawn.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingStateSpawn.Bind( wx.EVT_TEXT, self.set_state )
		self.ThingStateSpawnName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingStateSpawnName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingStateSpawnName.Bind( wx.EVT_LEFT_UP, self.goto_state_event )
		self.ThingStateSpawnSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.ThingStateWalk.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingStateWalk.Bind( wx.EVT_TEXT, self.set_state )
		self.ThingStateWalkName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingStateWalkName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingStateWalkName.Bind( wx.EVT_LEFT_UP, self.goto_state_event )
		self.ThingStateWalkSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.ThingStatePain.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingStatePain.Bind( wx.EVT_TEXT, self.set_state )
		self.ThingStatePainName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingStatePainName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingStatePainName.Bind( wx.EVT_LEFT_UP, self.goto_state_event )
		self.ThingStatePainSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.ThingStateMelee.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingStateMelee.Bind( wx.EVT_TEXT, self.set_state )
		self.ThingStateMeleeName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingStateMeleeName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingStateMeleeName.Bind( wx.EVT_LEFT_UP, self.goto_state_event )
		self.ThingStateMeleeSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.ThingStateAttack.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingStateAttack.Bind( wx.EVT_TEXT, self.set_state )
		self.ThingStateAttackName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingStateAttackName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingStateAttackName.Bind( wx.EVT_LEFT_UP, self.goto_state_event )
		self.ThingStateAttackSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.ThingStateDeath.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingStateDeath.Bind( wx.EVT_TEXT, self.set_state )
		self.ThingStateDeathName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingStateDeathName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingStateDeathName.Bind( wx.EVT_LEFT_UP, self.goto_state_event )
		self.ThingStateDeathSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.ThingStateExplode.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingStateExplode.Bind( wx.EVT_TEXT, self.set_state )
		self.ThingStateExplodeName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingStateExplodeName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingStateExplodeName.Bind( wx.EVT_LEFT_UP, self.goto_state_event )
		self.ThingStateExplodeSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.ThingStateRaise.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingStateRaise.Bind( wx.EVT_TEXT, self.set_state )
		self.ThingStateRaiseName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingStateRaiseName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingStateRaiseName.Bind( wx.EVT_LEFT_UP, self.goto_state_event )
		self.ThingStateRaiseSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.ThingStateCrash.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingStateCrash.Bind( wx.EVT_TEXT, self.set_state )
		self.ThingStateCrashName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingStateCrashName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingStateCrashName.Bind( wx.EVT_LEFT_UP, self.goto_state_event )
		self.ThingStateCrashSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.ThingStateFreeze.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingStateFreeze.Bind( wx.EVT_TEXT, self.set_state )
		self.ThingStateFreezeName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingStateFreezeName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingStateFreezeName.Bind( wx.EVT_LEFT_UP, self.goto_state_event )
		self.ThingStateFreezeSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.ThingStateBurn.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingStateBurn.Bind( wx.EVT_TEXT, self.set_state )
		self.ThingStateBurnName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingStateBurnName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingStateBurnName.Bind( wx.EVT_LEFT_UP, self.goto_state_event )
		self.ThingStateBurnSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.ThingSoundAlert.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingSoundAlert.Bind( wx.EVT_TEXT, self.set_sound )
		self.ThingSoundAlertName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingSoundAlertName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingSoundAlertName.Bind( wx.EVT_LEFT_UP, self.goto_sound_event )
		self.ThingSoundAlertName.Bind( wx.EVT_RIGHT_UP, self.sound_play )
		self.ThingSoundAlertSet.Bind( wx.EVT_BUTTON, self.set_sound_external )
		self.ThingSoundAttack.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingSoundAttack.Bind( wx.EVT_TEXT, self.set_sound )
		self.ThingSoundAttackName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingSoundAttackName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingSoundAttackName.Bind( wx.EVT_LEFT_UP, self.goto_sound_event )
		self.ThingSoundAttackName.Bind( wx.EVT_RIGHT_UP, self.sound_play )
		self.ThingSoundAttackSet.Bind( wx.EVT_BUTTON, self.set_sound_external )
		self.ThingSoundPain.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingSoundPain.Bind( wx.EVT_TEXT, self.set_sound )
		self.ThingSoundPainName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingSoundPainName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingSoundPainName.Bind( wx.EVT_LEFT_UP, self.goto_sound_event )
		self.ThingSoundPainName.Bind( wx.EVT_RIGHT_UP, self.sound_play )
		self.ThingSoundPainSet.Bind( wx.EVT_BUTTON, self.set_sound_external )
		self.ThingSoundDeath.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingSoundDeath.Bind( wx.EVT_TEXT, self.set_sound )
		self.ThingSoundDeathName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingSoundDeathName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingSoundDeathName.Bind( wx.EVT_LEFT_UP, self.goto_sound_event )
		self.ThingSoundDeathName.Bind( wx.EVT_RIGHT_UP, self.sound_play )
		self.ThingSoundDeathSet.Bind( wx.EVT_BUTTON, self.set_sound_external )
		self.ThingSoundActive.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingSoundActive.Bind( wx.EVT_TEXT, self.set_sound )
		self.ThingSoundActiveName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingSoundActiveName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingSoundActiveName.Bind( wx.EVT_LEFT_UP, self.goto_sound_event )
		self.ThingSoundActiveName.Bind( wx.EVT_RIGHT_UP, self.sound_play )
		self.ThingSoundActiveSet.Bind( wx.EVT_BUTTON, self.set_sound_external )
		self.ThingFlags.Bind( wx.EVT_CHECKLISTBOX, self.set_flags )
		self.ThingFlags.Bind( wx.EVT_MOTION, self.set_flag_tooltip )
		self.ThingList.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.thing_rename )
		self.ThingList.Bind( wx.EVT_LIST_ITEM_SELECTED, self.thing_select )
		self.ThingList.Bind( wx.EVT_SIZE, self.thinglist_resize )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def focus_text( self, event ):
		pass
	
	def set_value( self, event ):
		pass
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	def set_game( self, event ):
		pass
	
	
	
	
	
	def set_renderstyle( self, event ):
		pass
	
	
	
	
	
	
	
	def thing_rename( self, event ):
		pass
	
	def thing_restore( self, event ):
		pass
	
	
	def set_state( self, event ):
		pass
	
	def enter_state( self, event ):
		pass
	
	def leave_state( self, event ):
		pass
	
	def goto_state_event( self, event ):
		pass
	
	def set_state_external( self, event ):
		pass
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	def set_sound( self, event ):
		pass
	
	
	
	def goto_sound_event( self, event ):
		pass
	
	def sound_play( self, event ):
		pass
	
	def set_sound_external( self, event ):
		pass
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	def set_flags( self, event ):
		pass
	
	def set_flag_tooltip( self, event ):
		pass
	
	
	def thing_select( self, event ):
		pass
	
	def thinglist_resize( self, event ):
		pass
	

###########################################################################
## Class StatesFrameBase
###########################################################################

class StatesFrameBase ( wx.MDIChildFrame ):
	
	def __init__( self, parent ):
		wx.MDIChildFrame.__init__ ( self, parent, id = FRAME_STATES, title = u"States", pos = wx.DefaultPosition, size = wx.Size( 860,700 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU )
		
		self.SetSizeHintsSz( wx.Size( 860,700 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer41 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer40 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer132 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer130 = wx.BoxSizer( wx.VERTICAL )
		
		self.SpritePreview = spritepreview.SpritePreview(self, size=(-1, 160))
		self.SpritePreview.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )
		
		bSizer130.Add( self.SpritePreview, 0, wx.EXPAND, 5 )
		
		
		bSizer132.Add( bSizer130, 0, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 6 )
		
		bSizer131 = wx.BoxSizer( wx.VERTICAL )
		
		self.PropertyPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		PropertySizer = wx.BoxSizer( wx.VERTICAL )
		
		
		PropertySizer.AddSpacer( ( 0, 6), 0, wx.EXPAND, 5 )
		
		bSizer52 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText39 = wx.StaticText( self.PropertyPanel, wx.ID_ANY, u"Sprite", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText39.Wrap( -1 )
		bSizer52.Add( self.m_staticText39, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.SpriteIndex = wx.TextCtrl( self.PropertyPanel, STATES_SPRITE, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.SpriteIndex.SetMaxLength( 3 ) 
		bSizer52.Add( self.SpriteIndex, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.SpriteName = wx.StaticText( self.PropertyPanel, wx.ID_ANY, u"TROO", wx.DefaultPosition, wx.Size( 63,-1 ), wx.ST_NO_AUTORESIZE )
		self.SpriteName.Wrap( -1 )
		self.SpriteName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.SpriteName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer52.Add( self.SpriteName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.SpriteSelect = wx.Button( self.PropertyPanel, wx.ID_ANY, u"...", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.SpriteSelect.SetMinSize( wx.Size( 30,22 ) )
		
		bSizer52.Add( self.SpriteSelect, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		PropertySizer.Add( bSizer52, 0, wx.EXPAND, 5 )
		
		bSizer521 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText391 = wx.StaticText( self.PropertyPanel, wx.ID_ANY, u"Frame", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText391.Wrap( -1 )
		bSizer521.Add( self.m_staticText391, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.FrameIndex = wx.TextCtrl( self.PropertyPanel, STATES_FRAME, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		bSizer521.Add( self.FrameIndex, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.LEFT|wx.TOP, 3 )
		
		self.FrameIndexSpinner = wx.SpinButton( self.PropertyPanel, STATES_FRAMESPIN, wx.DefaultPosition, wx.Size( 17,24 ), 0 )
		bSizer521.Add( self.FrameIndexSpinner, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 3 )
		
		self.AlwaysLit = wx.CheckBox( self.PropertyPanel, STATES_LIT, u" Always lit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer521.Add( self.AlwaysLit, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 6 )
		
		
		PropertySizer.Add( bSizer521, 0, wx.EXPAND, 5 )
		
		
		PropertySizer.AddSpacer( ( 0, 9), 0, wx.EXPAND, 5 )
		
		bSizer5211 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3911 = wx.StaticText( self.PropertyPanel, wx.ID_ANY, u"Next state", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText3911.Wrap( -1 )
		bSizer5211.Add( self.m_staticText3911, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.NextStateIndex = wx.TextCtrl( self.PropertyPanel, STATES_NEXT, wx.EmptyString, wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.NextStateIndex.SetMaxLength( 4 ) 
		bSizer5211.Add( self.NextStateIndex, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.NextStateName = wx.StaticText( self.PropertyPanel, wx.ID_ANY, u"PLAYD", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ST_NO_AUTORESIZE )
		self.NextStateName.Wrap( -1 )
		self.NextStateName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.NextStateName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer5211.Add( self.NextStateName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		PropertySizer.Add( bSizer5211, 0, wx.EXPAND, 5 )
		
		
		PropertySizer.AddSpacer( ( 0, 9), 0, wx.EXPAND, 5 )
		
		bSizer5212 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3912 = wx.StaticText( self.PropertyPanel, wx.ID_ANY, u"Duration", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText3912.Wrap( -1 )
		bSizer5212.Add( self.m_staticText3912, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.Duration = wx.TextCtrl( self.PropertyPanel, STATES_DURATION, wx.EmptyString, wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.Duration.SetMaxLength( 4 ) 
		bSizer5212.Add( self.Duration, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		PropertySizer.Add( bSizer5212, 0, wx.EXPAND, 5 )
		
		
		PropertySizer.AddSpacer( ( 0, 9), 0, wx.EXPAND, 6 )
		
		bSizer521211 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText54 = wx.StaticText( self.PropertyPanel, wx.ID_ANY, u"Action", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText54.Wrap( -1 )
		bSizer521211.Add( self.m_staticText54, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		ActionChoices = []
		self.Action = wx.Choice( self.PropertyPanel, STATES_ACTION, wx.DefaultPosition, wx.Size( -1,-1 ), ActionChoices, wx.CB_SORT )
		self.Action.SetSelection( 0 )
		self.Action.SetMinSize( wx.Size( 160,-1 ) )
		
		bSizer521211.Add( self.Action, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		PropertySizer.Add( bSizer521211, 0, wx.EXPAND, 5 )
		
		bSizer52121 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText541 = wx.StaticText( self.PropertyPanel, STATES_LABEL_UNUSED1, u"Unused 1", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText541.Wrap( -1 )
		bSizer52121.Add( self.m_staticText541, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.Unused1 = wx.TextCtrl( self.PropertyPanel, STATES_UNUSED1, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.Unused1.SetMaxLength( 9 ) 
		bSizer52121.Add( self.Unused1, 0, wx.ALL, 3 )
		
		
		PropertySizer.Add( bSizer52121, 0, wx.EXPAND, 5 )
		
		bSizer521212 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText5411 = wx.StaticText( self.PropertyPanel, STATES_LABEL_UNUSED2, u"Unused 2", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText5411.Wrap( -1 )
		bSizer521212.Add( self.m_staticText5411, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.Unused2 = wx.TextCtrl( self.PropertyPanel, STATES_UNUSED2, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.Unused2.SetMaxLength( 9 ) 
		bSizer521212.Add( self.Unused2, 0, wx.ALL, 3 )
		
		
		PropertySizer.Add( bSizer521212, 0, wx.EXPAND, 5 )
		
		bSizer5212121 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText54111 = wx.StaticText( self.PropertyPanel, STATES_LABEL_ARG1, u"Arg 1", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText54111.Wrap( -1 )
		bSizer5212121.Add( self.m_staticText54111, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.Arg1 = wx.TextCtrl( self.PropertyPanel, STATES_ARG1, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.Arg1.SetMaxLength( 9 ) 
		bSizer5212121.Add( self.Arg1, 0, wx.ALL, 3 )
		
		
		PropertySizer.Add( bSizer5212121, 0, wx.EXPAND, 5 )
		
		bSizer5212122 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText54112 = wx.StaticText( self.PropertyPanel, STATES_LABEL_ARG2, u"Arg 2", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText54112.Wrap( -1 )
		bSizer5212122.Add( self.m_staticText54112, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.Arg2 = wx.TextCtrl( self.PropertyPanel, STATES_ARG2, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.Arg2.SetMaxLength( 9 ) 
		bSizer5212122.Add( self.Arg2, 0, wx.ALL, 3 )
		
		
		PropertySizer.Add( bSizer5212122, 0, wx.EXPAND, 5 )
		
		bSizer5212123 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText54113 = wx.StaticText( self.PropertyPanel, STATES_LABEL_ARG3, u"Arg 3", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText54113.Wrap( -1 )
		bSizer5212123.Add( self.m_staticText54113, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.Arg3 = wx.TextCtrl( self.PropertyPanel, STATES_ARG3, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.Arg3.SetMaxLength( 9 ) 
		bSizer5212123.Add( self.Arg3, 0, wx.ALL, 3 )
		
		
		PropertySizer.Add( bSizer5212123, 0, wx.EXPAND, 5 )
		
		bSizer5212124 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText54114 = wx.StaticText( self.PropertyPanel, STATES_LABEL_ARG4, u"Arg 4", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText54114.Wrap( -1 )
		bSizer5212124.Add( self.m_staticText54114, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.Arg4 = wx.TextCtrl( self.PropertyPanel, STATES_ARG4, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.Arg4.SetMaxLength( 9 ) 
		bSizer5212124.Add( self.Arg4, 0, wx.ALL, 3 )
		
		
		PropertySizer.Add( bSizer5212124, 0, wx.EXPAND, 5 )
		
		bSizer5212125 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText54115 = wx.StaticText( self.PropertyPanel, STATES_LABEL_ARG5, u"Arg 5", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText54115.Wrap( -1 )
		bSizer5212125.Add( self.m_staticText54115, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.Arg5 = wx.TextCtrl( self.PropertyPanel, STATES_ARG5, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.Arg5.SetMaxLength( 9 ) 
		bSizer5212125.Add( self.Arg5, 0, wx.ALL, 3 )
		
		
		PropertySizer.Add( bSizer5212125, 0, wx.EXPAND, 5 )
		
		bSizer5212126 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText54116 = wx.StaticText( self.PropertyPanel, STATES_LABEL_ARG6, u"Arg 6", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText54116.Wrap( -1 )
		bSizer5212126.Add( self.m_staticText54116, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.Arg6 = wx.TextCtrl( self.PropertyPanel, STATES_ARG6, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.Arg6.SetMaxLength( 9 ) 
		bSizer5212126.Add( self.Arg6, 0, wx.ALL, 3 )
		
		
		PropertySizer.Add( bSizer5212126, 0, wx.EXPAND, 5 )
		
		bSizer5212127 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText54117 = wx.StaticText( self.PropertyPanel, STATES_LABEL_ARG7, u"Arg 7", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText54117.Wrap( -1 )
		bSizer5212127.Add( self.m_staticText54117, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.Arg7 = wx.TextCtrl( self.PropertyPanel, STATES_ARG7, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.Arg7.SetMaxLength( 9 ) 
		bSizer5212127.Add( self.Arg7, 0, wx.ALL, 3 )
		
		
		PropertySizer.Add( bSizer5212127, 0, wx.EXPAND, 5 )
		
		bSizer5212128 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText54118 = wx.StaticText( self.PropertyPanel, STATES_LABEL_ARG8, u"Arg 8", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText54118.Wrap( -1 )
		bSizer5212128.Add( self.m_staticText54118, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.Arg8 = wx.TextCtrl( self.PropertyPanel, STATES_ARG8, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.Arg8.SetMaxLength( 9 ) 
		bSizer5212128.Add( self.Arg8, 0, wx.ALL, 3 )
		
		
		PropertySizer.Add( bSizer5212128, 0, wx.EXPAND, 5 )
		
		bSizer5212129 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText54119 = wx.StaticText( self.PropertyPanel, STATES_LABEL_ARG9, u"Arg 9", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText54119.Wrap( -1 )
		bSizer5212129.Add( self.m_staticText54119, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.Arg9 = wx.TextCtrl( self.PropertyPanel, STATES_ARG9, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.Arg9.SetMaxLength( 9 ) 
		bSizer5212129.Add( self.Arg9, 0, wx.ALL, 3 )
		
		
		PropertySizer.Add( bSizer5212129, 0, wx.EXPAND, 5 )
		
		
		PropertySizer.AddSpacer( ( 0, 9), 0, wx.EXPAND, 5 )
		
		self.Restore = wx.Button( self.PropertyPanel, wx.ID_ANY, u"Restore", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.Restore.SetMinSize( wx.Size( -1,28 ) )
		
		PropertySizer.Add( self.Restore, 0, wx.EXPAND|wx.TOP, 3 )
		
		
		self.PropertyPanel.SetSizer( PropertySizer )
		self.PropertyPanel.Layout()
		PropertySizer.Fit( self.PropertyPanel )
		bSizer131.Add( self.PropertyPanel, 0, wx.ALL|wx.EXPAND, 0 )
		
		
		bSizer132.Add( bSizer131, 0, wx.ALL, 6 )
		
		
		bSizer40.Add( bSizer132, 0, 0, 5 )
		
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
		self.FilterToolRefresh = self.FilterTools.AddLabelTool( STATES_FILTERTOOLS_REFRESH, u"tool", wx.Bitmap( u"res/icon-refresh.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Refreshes the state list.", wx.EmptyString, None ) 
		
		self.FilterTools.Realize() 
		
		bSizer441.Add( self.FilterTools, 0, wx.EXPAND, 0 )
		
		
		bSizer421.Add( bSizer441, 0, wx.ALL|wx.EXPAND, 6 )
		
		self.StateList = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_NO_SORT_HEADER|wx.LC_REPORT|wx.NO_BORDER )
		self.StateList.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer421.Add( self.StateList, 1, wx.EXPAND, 5 )
		
		
		bSizer40.Add( bSizer421, 1, wx.EXPAND, 5 )
		
		
		bSizer41.Add( bSizer40, 1, wx.EXPAND, 6 )
		
		
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
		self.Unused1.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Unused1.Bind( wx.EVT_TEXT, self.set_value )
		self.Unused2.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Unused2.Bind( wx.EVT_TEXT, self.set_value )
		self.Arg1.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Arg1.Bind( wx.EVT_TEXT, self.set_value )
		self.Arg2.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Arg2.Bind( wx.EVT_TEXT, self.set_value )
		self.Arg3.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Arg3.Bind( wx.EVT_TEXT, self.set_value )
		self.Arg4.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Arg4.Bind( wx.EVT_TEXT, self.set_value )
		self.Arg5.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Arg5.Bind( wx.EVT_TEXT, self.set_value )
		self.Arg6.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Arg6.Bind( wx.EVT_TEXT, self.set_value )
		self.Arg7.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Arg7.Bind( wx.EVT_TEXT, self.set_value )
		self.Arg8.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Arg8.Bind( wx.EVT_TEXT, self.set_value )
		self.Arg9.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Arg9.Bind( wx.EVT_TEXT, self.set_value )
		self.Restore.Bind( wx.EVT_BUTTON, self.state_restore )
		self.Filter.Bind( wx.EVT_CHOICE, self.filter_select )
		self.Bind( wx.EVT_TOOL, self.filter_select, id = self.FilterToolRefresh.GetId() )
		self.StateList.Bind( wx.EVT_LEFT_DOWN, self.state_link )
		self.StateList.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.select_sprite )
		self.StateList.Bind( wx.EVT_LIST_ITEM_DESELECTED, self.state_deselect )
		self.StateList.Bind( wx.EVT_LIST_ITEM_SELECTED, self.state_select )
		self.StateList.Bind( wx.EVT_SIZE, self.statelist_resize )
	
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
	
	def statelist_resize( self, event ):
		pass
	

###########################################################################
## Class SoundsFrameBase
###########################################################################

class SoundsFrameBase ( wx.MDIChildFrame ):
	
	def __init__( self, parent ):
		wx.MDIChildFrame.__init__ ( self, parent, id = FRAME_SOUNDS, title = u"Sounds", pos = wx.DefaultPosition, size = wx.Size( 430,480 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU )
		
		self.SetSizeHintsSz( wx.Size( 430,480 ), wx.DefaultSize )
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
		wx.MDIChildFrame.__init__ ( self, parent, id = FRAME_STRINGS, title = u"Strings", pos = wx.DefaultPosition, size = wx.Size( 640,480 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU )
		
		self.SetSizeHintsSz( wx.Size( 640,480 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer41 = wx.BoxSizer( wx.VERTICAL )
		
		self.StringList = wx.ListCtrl( self, STRINGS_LIST, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_NO_SORT_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.NO_BORDER )
		self.StringList.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer41.Add( self.StringList, 1, wx.EXPAND, 5 )
		
		bSizer158 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer158.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.Restore = wx.Button( self, STRINGS_RESTORE, u"Restore", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Restore.SetMinSize( wx.Size( 120,28 ) )
		
		bSizer158.Add( self.Restore, 0, wx.ALL, 6 )
		
		
		bSizer41.Add( bSizer158, 0, wx.EXPAND, 6 )
		
		
		self.SetSizer( bSizer41 )
		self.Layout()
		
		# Connect Events
		self.StringList.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.string_edit )
		self.StringList.Bind( wx.EVT_LIST_ITEM_SELECTED, self.string_select )
		self.StringList.Bind( wx.EVT_SIZE, self.stringlist_resize )
		self.Restore.Bind( wx.EVT_BUTTON, self.string_restore )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def string_edit( self, event ):
		pass
	
	def string_select( self, event ):
		pass
	
	def stringlist_resize( self, event ):
		pass
	
	def string_restore( self, event ):
		pass
	

###########################################################################
## Class WeaponsFrameBase
###########################################################################

class WeaponsFrameBase ( wx.MDIChildFrame ):
	
	def __init__( self, parent ):
		wx.MDIChildFrame.__init__ ( self, parent, id = FRAME_WEAPONS, title = u"Weapons", pos = wx.DefaultPosition, size = wx.Size( 560,360 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU )
		
		self.SetSizeHintsSz( wx.Size( 560,360 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer93 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer139 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer86 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText88 = wx.StaticText( self, wx.ID_ANY, u"Ammo type", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText88.Wrap( -1 )
		bSizer86.Add( self.m_staticText88, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		AmmoTypeChoices = []
		self.AmmoType = wx.Choice( self, WEAPON_AMMOTYPE, wx.DefaultPosition, wx.DefaultSize, AmmoTypeChoices, 0 )
		self.AmmoType.SetSelection( 0 )
		bSizer86.Add( self.AmmoType, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND|wx.FIXED_MINSIZE, 3 )
		
		
		bSizer139.Add( bSizer86, 1, wx.EXPAND, 5 )
		
		bSizer87 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText881 = wx.StaticText( self, wx.ID_ANY, u"Lower state", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText881.Wrap( -1 )
		bSizer87.Add( self.m_staticText881, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		bSizer124 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.WeaponStateSelect = wx.TextCtrl( self, WEAPON_STATE_SELECT, u"318", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.WeaponStateSelect.SetMaxLength( 4 ) 
		bSizer124.Add( self.WeaponStateSelect, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.WeaponStateSelectName = wx.StaticText( self, WEAPON_STATENAME_SELECT, u"TROOA", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.WeaponStateSelectName.Wrap( -1 )
		self.WeaponStateSelectName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.WeaponStateSelectName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer124.Add( self.WeaponStateSelectName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.WeaponStateSelectSet = wx.Button( self, WEAPON_STATESET_SELECT, u"<", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.WeaponStateSelectSet.SetMinSize( wx.Size( 25,25 ) )
		
		bSizer124.Add( self.WeaponStateSelectSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		bSizer87.Add( bSizer124, 1, wx.EXPAND, 5 )
		
		
		bSizer139.Add( bSizer87, 1, wx.EXPAND, 5 )
		
		bSizer88 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText8811 = wx.StaticText( self, wx.ID_ANY, u"Raise state", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8811.Wrap( -1 )
		bSizer88.Add( self.m_staticText8811, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bSizer1241 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.WeaponStateDeselect = wx.TextCtrl( self, WEAPON_STATE_DESELECT, u"318", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.WeaponStateDeselect.SetMaxLength( 4 ) 
		bSizer1241.Add( self.WeaponStateDeselect, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.WeaponStateDeselectName = wx.StaticText( self, WEAPON_STATENAME_DESELECT, u"TROOA", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.WeaponStateDeselectName.Wrap( -1 )
		self.WeaponStateDeselectName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.WeaponStateDeselectName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer1241.Add( self.WeaponStateDeselectName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.WeaponStateDeselectSet = wx.Button( self, WEAPON_STATESET_DESELECT, u"<", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.WeaponStateDeselectSet.SetMinSize( wx.Size( 25,25 ) )
		
		bSizer1241.Add( self.WeaponStateDeselectSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		bSizer88.Add( bSizer1241, 1, wx.EXPAND, 5 )
		
		
		bSizer139.Add( bSizer88, 1, wx.EXPAND, 5 )
		
		bSizer89 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText8812 = wx.StaticText( self, wx.ID_ANY, u"Bob state", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8812.Wrap( -1 )
		bSizer89.Add( self.m_staticText8812, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bSizer1242 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.WeaponStateBob = wx.TextCtrl( self, WEAPON_STATE_BOB, u"318", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.WeaponStateBob.SetMaxLength( 4 ) 
		bSizer1242.Add( self.WeaponStateBob, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.WeaponStateBobName = wx.StaticText( self, WEAPON_STATENAME_BOB, u"TROOA", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.WeaponStateBobName.Wrap( -1 )
		self.WeaponStateBobName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.WeaponStateBobName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer1242.Add( self.WeaponStateBobName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.WeaponStateBobSet = wx.Button( self, WEAPON_STATESET_BOB, u"<", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.WeaponStateBobSet.SetMinSize( wx.Size( 25,25 ) )
		
		bSizer1242.Add( self.WeaponStateBobSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		bSizer89.Add( bSizer1242, 1, wx.EXPAND, 5 )
		
		
		bSizer139.Add( bSizer89, 1, wx.EXPAND, 5 )
		
		bSizer90 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText8813 = wx.StaticText( self, wx.ID_ANY, u"Fire state", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8813.Wrap( -1 )
		bSizer90.Add( self.m_staticText8813, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bSizer1243 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.WeaponStateFire = wx.TextCtrl( self, WEAPON_STATE_FIRE, u"318", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.WeaponStateFire.SetMaxLength( 4 ) 
		bSizer1243.Add( self.WeaponStateFire, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.WeaponStateFireName = wx.StaticText( self, WEAPON_STATENAME_FIRE, u"TROOA", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.WeaponStateFireName.Wrap( -1 )
		self.WeaponStateFireName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.WeaponStateFireName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer1243.Add( self.WeaponStateFireName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.WeaponStateFireSet = wx.Button( self, WEAPON_STATESET_FIRE, u"<", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.WeaponStateFireSet.SetMinSize( wx.Size( 25,25 ) )
		
		bSizer1243.Add( self.WeaponStateFireSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		bSizer90.Add( bSizer1243, 1, wx.EXPAND, 5 )
		
		
		bSizer139.Add( bSizer90, 1, wx.EXPAND, 5 )
		
		bSizer91 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText8814 = wx.StaticText( self, wx.ID_ANY, u"Muzzle flash state", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8814.Wrap( -1 )
		bSizer91.Add( self.m_staticText8814, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bSizer1244 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.WeaponStateMuzzle = wx.TextCtrl( self, WEAPON_STATE_MUZZLE, u"318", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.WeaponStateMuzzle.SetMaxLength( 4 ) 
		bSizer1244.Add( self.WeaponStateMuzzle, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.WeaponStateMuzzleName = wx.StaticText( self, WEAPON_STATENAME_MUZZLE, u"TROOA", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.WeaponStateMuzzleName.Wrap( -1 )
		self.WeaponStateMuzzleName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Bitstream Vera Sans Mono" ) )
		self.WeaponStateMuzzleName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer1244.Add( self.WeaponStateMuzzleName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.WeaponStateMuzzleSet = wx.Button( self, WEAPON_STATESET_MUZZLE, u"<", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.WeaponStateMuzzleSet.SetMinSize( wx.Size( 25,25 ) )
		
		bSizer1244.Add( self.WeaponStateMuzzleSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		bSizer91.Add( bSizer1244, 1, wx.EXPAND, 5 )
		
		
		bSizer139.Add( bSizer91, 1, wx.EXPAND, 5 )
		
		
		bSizer93.Add( bSizer139, 0, wx.ALL, 6 )
		
		
		bSizer93.AddSpacer( ( 0, 0), 1, wx.EXPAND, 0 )
		
		bSizer92 = wx.BoxSizer( wx.VERTICAL )
		
		self.Rename = wx.Button( self, WEAPON_RENAME, u"Rename", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Rename.SetMinSize( wx.Size( -1,28 ) )
		
		bSizer92.Add( self.Rename, 0, wx.ALL|wx.EXPAND, 3 )
		
		self.Restore = wx.Button( self, WEAPON_RESTORE, u"Restore", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Restore.SetMinSize( wx.Size( -1,28 ) )
		
		bSizer92.Add( self.Restore, 0, wx.ALL|wx.EXPAND, 3 )
		
		
		bSizer93.Add( bSizer92, 0, wx.ALL|wx.EXPAND, 3 )
		
		
		bSizer41.Add( bSizer93, 0, wx.EXPAND, 5 )
		
		self.WeaponList = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.NO_BORDER )
		bSizer41.Add( self.WeaponList, 1, wx.ALL|wx.EXPAND, 0 )
		
		
		self.SetSizer( bSizer41 )
		self.Layout()
		
		# Connect Events
		self.AmmoType.Bind( wx.EVT_CHOICE, self.set_ammo )
		self.WeaponStateSelect.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.WeaponStateSelect.Bind( wx.EVT_TEXT, self.set_state_index )
		self.WeaponStateSelectName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.WeaponStateSelectName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.WeaponStateSelectName.Bind( wx.EVT_LEFT_UP, self.goto_state_event )
		self.WeaponStateSelectSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.WeaponStateDeselect.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.WeaponStateDeselect.Bind( wx.EVT_TEXT, self.set_state_index )
		self.WeaponStateDeselectName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.WeaponStateDeselectName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.WeaponStateDeselectName.Bind( wx.EVT_LEFT_UP, self.goto_state_event )
		self.WeaponStateDeselectSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.WeaponStateBob.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.WeaponStateBob.Bind( wx.EVT_TEXT, self.set_state_index )
		self.WeaponStateBobName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.WeaponStateBobName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.WeaponStateBobName.Bind( wx.EVT_LEFT_UP, self.goto_state_event )
		self.WeaponStateBobSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.WeaponStateFire.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.WeaponStateFire.Bind( wx.EVT_TEXT, self.set_state_index )
		self.WeaponStateFireName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.WeaponStateFireName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.WeaponStateFireName.Bind( wx.EVT_LEFT_UP, self.goto_state_event )
		self.WeaponStateFireSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.WeaponStateMuzzle.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.WeaponStateMuzzle.Bind( wx.EVT_TEXT, self.set_state_index )
		self.WeaponStateMuzzleName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.WeaponStateMuzzleName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.WeaponStateMuzzleName.Bind( wx.EVT_LEFT_UP, self.goto_state_event )
		self.WeaponStateMuzzleSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.Rename.Bind( wx.EVT_BUTTON, self.weapon_rename )
		self.Restore.Bind( wx.EVT_BUTTON, self.weapon_restore )
		self.WeaponList.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.weapon_rename )
		self.WeaponList.Bind( wx.EVT_LIST_ITEM_SELECTED, self.weapon_select )
		self.WeaponList.Bind( wx.EVT_SIZE, self.weaponlist_resize )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def set_ammo( self, event ):
		pass
	
	def focus_text( self, event ):
		pass
	
	def set_state_index( self, event ):
		pass
	
	def enter_state( self, event ):
		pass
	
	def leave_state( self, event ):
		pass
	
	def goto_state_event( self, event ):
		pass
	
	def set_state_external( self, event ):
		pass
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	def weapon_rename( self, event ):
		pass
	
	def weapon_restore( self, event ):
		pass
	
	
	def weapon_select( self, event ):
		pass
	
	def weaponlist_resize( self, event ):
		pass
	

###########################################################################
## Class AmmoFrameBase
###########################################################################

class AmmoFrameBase ( wx.MDIChildFrame ):
	
	def __init__( self, parent ):
		wx.MDIChildFrame.__init__ ( self, parent, id = FRAME_AMMO, title = u"Ammo", pos = wx.DefaultPosition, size = wx.Size( 520,250 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU )
		
		self.SetSizeHintsSz( wx.Size( 520,250 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer139 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer1 = wx.GridSizer( 2, 2, 3, 12 )
		
		self.m_staticText88 = wx.StaticText( self, wx.ID_ANY, u"Maximum ammo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText88.Wrap( -1 )
		gSizer1.Add( self.m_staticText88, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.Maximum = wx.TextCtrl( self, AMMO_VAL_MAXIMUM, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.Maximum.SetMaxLength( 6 ) 
		gSizer1.Add( self.Maximum, 0, wx.ALL|wx.EXPAND, 3 )
		
		self.m_staticText881 = wx.StaticText( self, wx.ID_ANY, u"Pickup ammo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText881.Wrap( -1 )
		gSizer1.Add( self.m_staticText881, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.Pickup = wx.TextCtrl( self, AMMO_VAL_PICKUP, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.Pickup.SetMaxLength( 6 ) 
		gSizer1.Add( self.Pickup, 0, wx.ALL|wx.EXPAND, 3 )
		
		
		bSizer139.Add( gSizer1, 0, wx.ALL, 6 )
		
		
		bSizer139.AddSpacer( ( 0, 0), 1, wx.EXPAND, 0 )
		
		self.Rename = wx.Button( self, AMMO_RENAME, u"Rename", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Rename.SetMinSize( wx.Size( -1,28 ) )
		
		bSizer139.Add( self.Rename, 0, wx.ALL|wx.EXPAND, 3 )
		
		self.Restore = wx.Button( self, AMMO_RESTORE, u"Restore", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Restore.SetMinSize( wx.Size( -1,28 ) )
		
		bSizer139.Add( self.Restore, 0, wx.ALL|wx.EXPAND, 3 )
		
		
		bSizer41.Add( bSizer139, 0, wx.ALL|wx.EXPAND, 6 )
		
		self.AmmoList = wx.ListCtrl( self, AMMO_LIST, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.NO_BORDER )
		bSizer41.Add( self.AmmoList, 1, wx.ALL|wx.EXPAND, 0 )
		
		
		self.SetSizer( bSizer41 )
		self.Layout()
		
		# Connect Events
		self.Maximum.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Maximum.Bind( wx.EVT_TEXT, self.set_value )
		self.Pickup.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Pickup.Bind( wx.EVT_TEXT, self.set_value )
		self.Rename.Bind( wx.EVT_BUTTON, self.ammo_rename )
		self.Restore.Bind( wx.EVT_BUTTON, self.ammo_restore )
		self.AmmoList.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.ammo_rename )
		self.AmmoList.Bind( wx.EVT_LIST_ITEM_SELECTED, self.ammo_select )
		self.AmmoList.Bind( wx.EVT_SIZE, self.ammolist_resize )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def focus_text( self, event ):
		pass
	
	def set_value( self, event ):
		pass
	
	
	
	def ammo_rename( self, event ):
		pass
	
	def ammo_restore( self, event ):
		pass
	
	
	def ammo_select( self, event ):
		pass
	
	def ammolist_resize( self, event ):
		pass
	

###########################################################################
## Class CheatsFrameBase
###########################################################################

class CheatsFrameBase ( wx.MDIChildFrame ):
	
	def __init__( self, parent ):
		wx.MDIChildFrame.__init__ ( self, parent, id = FRAME_CHEATS, title = u"Cheats", pos = wx.DefaultPosition, size = wx.Size( 340,401 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU )
		
		self.SetSizeHintsSz( wx.Size( 340,401 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer41 = wx.BoxSizer( wx.VERTICAL )
		
		self.CheatList = wx.ListCtrl( self, CHEATS_LIST, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.NO_BORDER )
		bSizer41.Add( self.CheatList, 1, wx.EXPAND, 5 )
		
		bSizer158 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer158.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.Restore = wx.Button( self, CHEATS_RESTORE, u"Restore", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Restore.SetMinSize( wx.Size( 120,28 ) )
		
		bSizer158.Add( self.Restore, 0, wx.ALL, 6 )
		
		
		bSizer41.Add( bSizer158, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer41 )
		self.Layout()
		
		# Connect Events
		self.CheatList.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.cheat_edit )
		self.CheatList.Bind( wx.EVT_LIST_ITEM_SELECTED, self.cheat_select )
		self.CheatList.Bind( wx.EVT_SIZE, self.cheatlist_resize )
		self.Restore.Bind( wx.EVT_BUTTON, self.cheat_restore )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def cheat_edit( self, event ):
		pass
	
	def cheat_select( self, event ):
		pass
	
	def cheatlist_resize( self, event ):
		pass
	
	def cheat_restore( self, event ):
		pass
	

###########################################################################
## Class MiscFrameBase
###########################################################################

class MiscFrameBase ( wx.MDIChildFrame ):
	
	def __init__( self, parent ):
		wx.MDIChildFrame.__init__ ( self, parent, id = FRAME_MISC, title = u"Miscellaneous", pos = wx.DefaultPosition, size = wx.Size( 420,350 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU )
		
		self.SetSizeHintsSz( wx.Size( 420,350 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer152 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer153 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer154 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer154.SetMinSize( wx.Size( 100,-1 ) ) 
		self.Value = wx.TextCtrl( self.m_panel2, MISC_VALUE, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		bSizer154.Add( self.Value, 0, wx.ALL|wx.EXPAND, 3 )
		
		self.ValueEnabled = wx.CheckBox( self.m_panel2, MISC_VALUE_ENABLED, u"Enabled", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer154.Add( self.ValueEnabled, 0, wx.ALL|wx.EXPAND, 9 )
		
		self.Restore = wx.Button( self.m_panel2, MISC_RESTORE, u"Restore", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Restore.SetMinSize( wx.Size( -1,28 ) )
		
		bSizer154.Add( self.Restore, 0, wx.ALL|wx.EXPAND, 3 )
		
		
		self.m_panel2.SetSizer( bSizer154 )
		self.m_panel2.Layout()
		bSizer154.Fit( self.m_panel2 )
		bSizer153.Add( self.m_panel2, 1, wx.ALL, 6 )
		
		
		bSizer152.Add( bSizer153, 0, wx.EXPAND, 0 )
		
		self.MiscList = wx.ListCtrl( self, MISC_LIST, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_NO_SORT_HEADER|wx.LC_REPORT|wx.NO_BORDER )
		bSizer152.Add( self.MiscList, 1, wx.ALL|wx.EXPAND, 0 )
		
		
		self.SetSizer( bSizer152 )
		self.Layout()
		
		# Connect Events
		self.Value.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Value.Bind( wx.EVT_TEXT, self.set_value )
		self.ValueEnabled.Bind( wx.EVT_CHECKBOX, self.set_bool_value )
		self.Restore.Bind( wx.EVT_BUTTON, self.restore )
		self.MiscList.Bind( wx.EVT_LEFT_DCLICK, self.misc_action )
		self.MiscList.Bind( wx.EVT_LIST_ITEM_SELECTED, self.misc_select )
		self.MiscList.Bind( wx.EVT_SIZE, self.misclist_resize )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def focus_text( self, event ):
		pass
	
	def set_value( self, event ):
		pass
	
	def set_bool_value( self, event ):
		pass
	
	def restore( self, event ):
		pass
	
	def misc_action( self, event ):
		pass
	
	def misc_select( self, event ):
		pass
	
	def misclist_resize( self, event ):
		pass
	

###########################################################################
## Class ParFrameBase
###########################################################################

class ParFrameBase ( wx.MDIChildFrame ):
	
	def __init__( self, parent ):
		wx.MDIChildFrame.__init__ ( self, parent, id = FRAME_PAR, title = u"Par times", pos = wx.DefaultPosition, size = wx.Size( 400,380 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU )
		
		self.SetSizeHintsSz( wx.Size( 400,380 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer98 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer139 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer139.SetMinSize( wx.Size( 150,-1 ) ) 
		bSizer94 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText88 = wx.StaticText( self, wx.ID_ANY, u"Episode", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText88.Wrap( -1 )
		bSizer94.Add( self.m_staticText88, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.Episode = wx.TextCtrl( self, PAR_EPISODE, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.Episode.SetMaxLength( 1 ) 
		bSizer94.Add( self.Episode, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		bSizer139.Add( bSizer94, 0, wx.EXPAND, 5 )
		
		bSizer95 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText881 = wx.StaticText( self, wx.ID_ANY, u"Map", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText881.Wrap( -1 )
		bSizer95.Add( self.m_staticText881, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.Map = wx.TextCtrl( self, PAR_MAP, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.Map.SetMaxLength( 2 ) 
		bSizer95.Add( self.Map, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		bSizer139.Add( bSizer95, 0, wx.EXPAND, 5 )
		
		bSizer96 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText8811 = wx.StaticText( self, wx.ID_ANY, u"Seconds", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8811.Wrap( -1 )
		bSizer96.Add( self.m_staticText8811, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.Seconds = wx.TextCtrl( self, PAR_SECONDS, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.Seconds.SetMaxLength( 6 ) 
		bSizer96.Add( self.Seconds, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		bSizer139.Add( bSizer96, 0, wx.EXPAND, 5 )
		
		
		bSizer98.Add( bSizer139, 0, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.TOP, 6 )
		
		bSizer97 = wx.BoxSizer( wx.VERTICAL )
		
		self.Tools = wx.ToolBar( self, PAR_TOOLS, wx.DefaultPosition, wx.DefaultSize, wx.TB_FLAT|wx.TB_NODIVIDER|wx.TB_VERTICAL ) 
		self.Add = self.Tools.AddLabelTool( PAR_TOOL_ADD, u"tool", wx.Bitmap( u"res/icon-plus.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.Remove = self.Tools.AddLabelTool( PAR_TOOL_REMOVE, u"tool", wx.Bitmap( u"res/icon-minus.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.Tools.Realize() 
		
		bSizer97.Add( self.Tools, 0, wx.EXPAND, 5 )
		
		
		bSizer98.Add( bSizer97, 0, wx.ALL|wx.EXPAND, 6 )
		
		
		bSizer41.Add( bSizer98, 0, wx.EXPAND, 5 )
		
		self.ParList = wx.ListCtrl( self, PAR_LIST, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.NO_BORDER )
		bSizer41.Add( self.ParList, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer41 )
		self.Layout()
		
		# Connect Events
		self.Episode.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Episode.Bind( wx.EVT_TEXT, self.set_value )
		self.Map.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Map.Bind( wx.EVT_TEXT, self.set_value )
		self.Seconds.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Seconds.Bind( wx.EVT_TEXT, self.set_value )
		self.Bind( wx.EVT_TOOL, self.par_add, id = self.Add.GetId() )
		self.Bind( wx.EVT_TOOL, self.par_remove, id = self.Remove.GetId() )
		self.ParList.Bind( wx.EVT_LIST_ITEM_SELECTED, self.par_select )
		self.ParList.Bind( wx.EVT_SIZE, self.parlist_resize )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def focus_text( self, event ):
		pass
	
	def set_value( self, event ):
		pass
	
	
	
	
	
	def par_add( self, event ):
		pass
	
	def par_remove( self, event ):
		pass
	
	def par_select( self, event ):
		pass
	
	def parlist_resize( self, event ):
		pass
	

###########################################################################
## Class SpritesDialogBase
###########################################################################

class SpritesDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = DIALOG_SPRITES, title = u"Sprites", pos = wx.DefaultPosition, size = wx.Size( 500,490 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.WANTS_CHARS )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer39 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer42 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.SpriteNames = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 74,-1 ), wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
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
		self.Filter.SetMinSize( wx.Size( 74,-1 ) )
		
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
		self.SpriteNames.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.ok )
		self.SpriteNames.Bind( wx.EVT_LIST_ITEM_SELECTED, self.sprite_select_list )
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
	def ok( self, event ):
		pass
	
	def sprite_select_list( self, event ):
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
		wx.Dialog.__init__ ( self, parent, id = DIALOG_SPRITES, title = u"String", pos = wx.DefaultPosition, size = wx.Size( 640,480 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU )
		
		self.SetSizeHintsSz( wx.Size( 640,480 ), wx.DefaultSize )
		
		bSizer39 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer113 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer42 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText81 = wx.StaticText( self, wx.ID_ANY, u"Original", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText81.Wrap( -1 )
		bSizer42.Add( self.m_staticText81, 0, wx.LEFT|wx.RIGHT|wx.TOP, 6 )
		
		self.Original = wx.TextCtrl( self, STRING_OLD, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_DONTWRAP|wx.TE_MULTILINE|wx.TE_READONLY )
		self.Original.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, "Bitstream Vera Sans Mono" ) )
		self.Original.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer42.Add( self.Original, 1, wx.ALL|wx.EXPAND, 6 )
		
		
		bSizer113.Add( bSizer42, 1, wx.EXPAND, 5 )
		
		bSizer421 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText811 = wx.StaticText( self, wx.ID_ANY, u"New", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText811.Wrap( -1 )
		bSizer421.Add( self.m_staticText811, 0, wx.LEFT|wx.RIGHT|wx.TOP, 6 )
		
		self.New = wx.TextCtrl( self, STRING_NEW, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_DONTWRAP|wx.TE_MULTILINE|wx.TE_PROCESS_ENTER|wx.TE_PROCESS_TAB )
		self.New.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, "Bitstream Vera Sans Mono" ) )
		
		bSizer421.Add( self.New, 1, wx.ALL|wx.EXPAND, 6 )
		
		
		bSizer113.Add( bSizer421, 1, wx.EXPAND, 5 )
		
		
		bSizer39.Add( bSizer113, 1, wx.ALL|wx.EXPAND, 6 )
		
		bSizer43 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.CharsLeft = wx.StaticText( self, wx.ID_ANY, u"12 characters left", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CharsLeft.Wrap( -1 )
		bSizer43.Add( self.CharsLeft, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 6 )
		
		
		bSizer43.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.ButtonOk = wx.Button( self, STRING_OK, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ButtonOk.SetDefault() 
		self.ButtonOk.SetMinSize( wx.Size( 120,28 ) )
		
		bSizer43.Add( self.ButtonOk, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 6 )
		
		self.ButtonCancel = wx.Button( self, STRING_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ButtonCancel.SetMinSize( wx.Size( 120,28 ) )
		
		bSizer43.Add( self.ButtonCancel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 6 )
		
		
		bSizer39.Add( bSizer43, 0, wx.ALL|wx.EXPAND, 6 )
		
		
		self.SetSizer( bSizer39 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_ACTIVATE, self.activate )
		self.New.Bind( wx.EVT_KEY_DOWN, self.text_keydown )
		self.New.Bind( wx.EVT_TEXT, self.text_enter )
		self.ButtonOk.Bind( wx.EVT_BUTTON, self.ok )
		self.ButtonCancel.Bind( wx.EVT_BUTTON, self.cancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def activate( self, event ):
		pass
	
	def text_keydown( self, event ):
		pass
	
	def text_enter( self, event ):
		pass
	
	def ok( self, event ):
		pass
	
	def cancel( self, event ):
		pass
	

###########################################################################
## Class PatchInfoDialogBase
###########################################################################

class PatchInfoDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = DIALOG_PATCHINFO, title = u"Patch", pos = wx.DefaultPosition, size = wx.Size( 600,325 ), style = wx.CAPTION|wx.CLOSE_BOX )
		
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
		
		self.IWADBrowse = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.Size( 32,25 ), 0 )
		bSizer451.Add( self.IWADBrowse, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.RIGHT|wx.TOP, 6 )
		
		self.IWADDelete = wx.Button( self, wx.ID_ANY, u"X", wx.DefaultPosition, wx.Size( 32,25 ), 0 )
		bSizer451.Add( self.IWADDelete, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.RIGHT|wx.TOP, 6 )
		
		
		bSizer44.Add( bSizer451, 0, wx.EXPAND|wx.LEFT|wx.RIGHT, 6 )
		
		bSizer452 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText462 = wx.StaticText( self, wx.ID_ANY, u"PWADs", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText462.Wrap( -1 )
		self.m_staticText462.SetMinSize( wx.Size( 75,-1 ) )
		
		bSizer452.Add( self.m_staticText462, 0, wx.ALL, 6 )
		
		self.PWADList = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		bSizer452.Add( self.PWADList, 1, wx.ALL|wx.EXPAND, 6 )
		
		bSizer63 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_toolBar3 = wx.ToolBar( self, PATCHINFO_TOOLBAR, wx.DefaultPosition, wx.DefaultSize, wx.TB_FLAT|wx.TB_NODIVIDER|wx.TB_VERTICAL ) 
		self.AddPWAD = self.m_toolBar3.AddLabelTool( PATCHINFO_TOOLBAR_ADD, u"tool", wx.Bitmap( u"res/icon-plus.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.RemovePWAD = self.m_toolBar3.AddLabelTool( PATCHINFO_TOOLBAR_REMOVE, u"tool", wx.Bitmap( u"res/icon-minus.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
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
		
		self.ButtonCancel = wx.Button( self, PATCHINFO_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ButtonCancel.SetMinSize( wx.Size( 120,28 ) )
		
		bSizer4521.Add( self.ButtonCancel, 0, wx.ALL, 5 )
		
		
		bSizer44.Add( bSizer4521, 0, wx.ALL|wx.EXPAND, 6 )
		
		
		self.SetSizer( bSizer44 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.EngineList.Bind( wx.EVT_CHOICE, self.engine_select )
		self.IWADBrowse.Bind( wx.EVT_BUTTON, self.browse_iwad )
		self.IWADDelete.Bind( wx.EVT_BUTTON, self.delete_iwad )
		self.Bind( wx.EVT_TOOL, self.pwad_add, id = self.AddPWAD.GetId() )
		self.Bind( wx.EVT_TOOL, self.pwad_remove, id = self.RemovePWAD.GetId() )
		self.ButtonOk.Bind( wx.EVT_BUTTON, self.ok )
		self.ButtonCancel.Bind( wx.EVT_BUTTON, self.cancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def engine_select( self, event ):
		pass
	
	def browse_iwad( self, event ):
		pass
	
	def delete_iwad( self, event ):
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
		wx.Dialog.__init__ ( self, parent, id = DIALOG_START, title = u"WhackEd4", pos = wx.DefaultPosition, size = wx.Size( 600,340 ), style = wx.CAPTION|wx.CLOSE_BOX )
		
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
		
		self.FileList = wx.ListCtrl( self, START_RECENT, wx.DefaultPosition, wx.DefaultSize, wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
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
		self.FileList.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.open_file_list )
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
		wx.Dialog.__init__ ( self, parent, id = DIALOG_ABOUT, title = u"About WhackEd4", pos = wx.DefaultPosition, size = wx.Size( 640,420 ), style = wx.CAPTION|wx.CLOSE_BOX )
		
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
		
		self.m_staticText138 = wx.StaticText( self, wx.ID_ANY, u"Aeyesx, Aliotroph?, Andy Fox, Andy Shawaluk, Big_Al, CodeImp, CSabo, Dani J666, Daniel Carroll, Doom Dude, DooMAD, Doomer, EarthQuake, Enjay, esselfortium, Frades, Francesco Orsenigo, Greg Lewis, iori, Kurisutaru, Leonard Pitre, Looney, Marc. A. Pullen, Palladium, Rellik, REZ, scifista42, Skullers, SlayeR, tempun, un4seen, VGA, WildWeasel, XDelusion", wx.DefaultPosition, wx.Size( -1,-1 ), wx.ST_NO_AUTORESIZE )
		self.m_staticText138.Wrap( 450 )
		bSizer56.Add( self.m_staticText138, 1, wx.ALL, 6 )
		
		
		bSizer56.AddSpacer( ( 0, 12), 0, wx.EXPAND, 5 )
		
		bSizer58 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.License = wx.Button( self, wx.ID_ANY, u"License", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.License.SetMinSize( wx.Size( 150,28 ) )
		
		bSizer58.Add( self.License, 0, wx.ALL, 0 )
		
		
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
		self.License.Bind( wx.EVT_BUTTON, self.license )
		self.ButtonOk.Bind( wx.EVT_BUTTON, self.ok )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def license( self, event ):
		pass
	
	def ok( self, event ):
		pass
	

###########################################################################
## Class ErrorDialogBase
###########################################################################

class ErrorDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = DIALOG_ERROR, title = u"WhackEd4 fatal error", pos = wx.DefaultPosition, size = wx.Size( 640,480 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer118 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText91 = wx.StaticText( self, wx.ID_ANY, u"Oops! Something terrible has happened.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText91.Wrap( -1 )
		self.m_staticText91.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer118.Add( self.m_staticText91, 0, wx.ALL, 12 )
		
		self.m_staticText92 = wx.StaticText( self, wx.ID_ANY, u"Below you can find more details about the error. You can copy it to the clipboard and send it to a developer who can fix this bug.", wx.DefaultPosition, wx.DefaultSize, wx.ST_NO_AUTORESIZE )
		self.m_staticText92.Wrap( 592 )
		self.m_staticText92.SetMinSize( wx.Size( -1,40 ) )
		
		bSizer118.Add( self.m_staticText92, 0, wx.BOTTOM|wx.LEFT|wx.RIGHT, 12 )
		
		self.Report = wx.TextCtrl( self, ERROR_REPORT, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		self.Report.SetFont( wx.Font( 7, 70, 90, 90, False, "Bitstream Vera Sans Mono" ) )
		self.Report.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer118.Add( self.Report, 1, wx.ALL|wx.EXPAND, 12 )
		
		bSizer119 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button43 = wx.Button( self, ERROR_COPY, u"Copy to clipboard", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button43.SetMinSize( wx.Size( 144,28 ) )
		
		bSizer119.Add( self.m_button43, 0, wx.ALL, 6 )
		
		
		bSizer119.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button44 = wx.Button( self, ERROR_CLOSE, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button44.SetMinSize( wx.Size( 144,28 ) )
		
		bSizer119.Add( self.m_button44, 0, wx.ALL, 6 )
		
		
		bSizer118.Add( bSizer119, 0, wx.ALL|wx.EXPAND, 6 )
		
		
		self.SetSizer( bSizer118 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button43.Bind( wx.EVT_BUTTON, self.copy )
		self.m_button44.Bind( wx.EVT_BUTTON, self.close )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def copy( self, event ):
		pass
	
	def close( self, event ):
		pass
	

