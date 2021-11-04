# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

from whacked4.ui.state_list import StateList
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
THING_VAL_NAME = 1686
THING_VAL_OBIT_NAME = 1687
THING_VAL_OBIT_NAME_PLURAL = 1688
THING_VAL_GAME = 1689
THING_VAL_ID = 1690
THING_VAL_SPAWNID = 1691
THING_VAL_DROPPED_ITEM_ID = 1692
THING_VAL_BLOOD_ID = 1693
THING_VAL_HEALTH = 1694
THING_VAL_GIBHEALTH = 1695
THING_VAL_SPEED = 1696
THING_VAL_RADIUS = 1697
THING_VAL_PICKUP_RADIUS = 1698
THING_VAL_HEIGHT = 1699
THING_VAL_PROJECTILE_PASS_HEIGHT = 1700
THING_VAL_DAMAGE = 1701
THING_VAL_DAMAGEFACTOR = 1702
THING_VAL_REACTIONTIME = 1703
THING_VAL_PAINCHANCE = 1704
THING_VAL_MASS = 1705
THING_VAL_GRAVITY = 1706
THING_VAL_RESPAWNTIME = 1707
THING_VAL_FULLBRIGHT = 1708
THING_VAL_RENDERSTYLE = 1709
THING_VAL_ALPHA = 1710
THING_VAL_SCALE = 1711
THING_VAL_DECAL = 1712
THING_VAL_SHADOW_OFFSET = 1713
THING_STATE_SPAWN = 1714
THING_STATENAME_SPAWN = 1715
THING_STATESET_SPAWN = 1716
THING_STATE_WALK = 1717
THING_STATENAME_WALK = 1718
THING_STATESET_WALK = 1719
THING_STATE_PAIN = 1720
THING_STATENAME_PAIN = 1721
THING_STATESET_PAIN = 1722
THING_STATE_MELEE = 1723
THING_STATENAME_MELEE = 1724
THING_STATESET_MELEE = 1725
THING_STATE_ATTACK = 1726
THING_STATENAME_ATTACK = 1727
THING_STATESET_ATTACK = 1728
THING_STATE_DEATH = 1729
THING_STATENAME_DEATH = 1730
THING_STATESET_DEATH = 1731
THING_STATE_EXPLODE = 1732
THING_STATENAME_EXPLODE = 1733
THING_STATESET_EXPLODE = 1734
THING_STATE_RAISE = 1735
THING_STATENAME_RAISE = 1736
THING_STATESET_RAISE = 1737
THING_STATE_CRASH = 1738
THING_STATENAME_CRASH = 1739
THING_STATESET_CRASH = 1740
THING_STATE_FREEZE = 1741
THING_STATENAME_FREEZE = 1742
THING_STATESET_FREEZE = 1743
THING_STATE_BURN = 1744
THING_STATENAME_BURN = 1745
THING_STATESET_BURN = 1746
THING_SOUND_ALERT = 1747
THING_SOUNDNAME_ALERT = 1748
THING_SOUNDSET_ALERT = 1749
THING_SOUND_ATTACK = 1750
THING_SOUNDNAME_ATTACK = 1751
THING_SOUNDSET_ATTACK = 1752
THING_SOUND_PAIN = 1753
THING_SOUNDNAME_PAIN = 1754
THING_SOUNDSET_PAIN = 1755
THING_SOUND_DEATH = 1756
THING_SOUNDNAME_DEATH = 1757
THING_SOUNDSET_DEATH = 1758
THING_SOUND_ACTIVE = 1759
THING_SOUNDNAME_ACTIVE = 1760
THING_SOUNDSET_ACTIVE = 1761
THING_FLAGS = 1762
THING_RESTORE = 1763
THING_LIST = 1764
FRAME_STATES = 1765
STATES_SPRITE = 1766
STATES_FRAME = 1767
STATES_FRAMESPIN = 1768
STATES_LIT = 1769
STATES_NEXT = 1770
STATES_DURATION = 1771
STATES_ACTION = 1772
STATES_LABEL_UNUSED1 = 1773
STATES_UNUSED1 = 1774
STATES_LABEL_UNUSED2 = 1775
STATES_UNUSED2 = 1776
STATES_LABEL_ARG1 = 1777
STATES_ARG1 = 1778
STATES_LABEL_ARG2 = 1779
STATES_ARG2 = 1780
STATES_LABEL_ARG3 = 1781
STATES_ARG3 = 1782
STATES_LABEL_ARG4 = 1783
STATES_ARG4 = 1784
STATES_LABEL_ARG5 = 1785
STATES_ARG5 = 1786
STATES_LABEL_ARG6 = 1787
STATES_ARG6 = 1788
STATES_LABEL_ARG7 = 1789
STATES_ARG7 = 1790
STATES_LABEL_ARG8 = 1791
STATES_ARG8 = 1792
STATES_LABEL_ARG9 = 1793
STATES_ARG9 = 1794
STATES_FILTER = 1795
STATES_FILTERTOOLS = 1796
STATES_FILTERTOOLS_REFRESH = 1797
FRAME_SOUNDS = 1798
SOUNDS_PRIORITY = 1799
SOUNDS_PRIORITYSPIN = 1800
SOUNDS_SINGULAR = 1801
SOUNDS_RESTORE = 1802
SOUNDS_LIST = 1803
FRAME_STRINGS = 1804
STRINGS_LIST = 1805
STRINGS_RESTORE = 1806
FRAME_WEAPONS = 1807
WEAPON_AMMOTYPE = 1808
WEAPON_VAL_AMMO_USE = 1809
WEAPON_VAL_MIN_AMMO = 1810
WEAPON_VAL_DECAL = 1811
WEAPON_STATE_SELECT = 1812
WEAPON_STATENAME_SELECT = 1813
WEAPON_STATESET_SELECT = 1814
WEAPON_STATE_DESELECT = 1815
WEAPON_STATENAME_DESELECT = 1816
WEAPON_STATESET_DESELECT = 1817
WEAPON_STATE_BOB = 1818
WEAPON_STATENAME_BOB = 1819
WEAPON_STATESET_BOB = 1820
WEAPON_STATE_FIRE = 1821
WEAPON_STATENAME_FIRE = 1822
WEAPON_STATESET_FIRE = 1823
WEAPON_STATE_MUZZLE = 1824
WEAPON_STATENAME_MUZZLE = 1825
WEAPON_STATESET_MUZZLE = 1826
WEAPON_RENAME = 1827
WEAPON_RESTORE = 1828
FRAME_AMMO = 1829
AMMO_VAL_MAXIMUM = 1830
AMMO_VAL_PICKUP = 1831
AMMO_RENAME = 1832
AMMO_RESTORE = 1833
AMMO_LIST = 1834
FRAME_CHEATS = 1835
CHEATS_LIST = 1836
CHEATS_RESTORE = 1837
FRAME_MISC = 1838
MISC_VALUE = 1839
MISC_VALUE_ENABLED = 1840
MISC_RESTORE = 1841
MISC_LIST = 1842
FRAME_PAR = 1843
PAR_EPISODE = 1844
PAR_MAP = 1845
PAR_SECONDS = 1846
PAR_TOOLS = 1847
PAR_TOOL_ADD = 1848
PAR_TOOL_REMOVE = 1849
PAR_LIST = 1850
DIALOG_SPRITES = 1851
SPRITES_FILTER = 1852
SPRITES_FRAME = 1853
SPRITES_FRAMESPIN = 1854
SPRITES_OK = 1855
SPRITES_CANCEL = 1856
STRING_OLD = 1857
STRING_NEW = 1858
STRING_OK = 1859
STRING_CANCEL = 1860
DIALOG_PATCHINFO = 1861
PATCHINFO_TOOLBAR = 1862
PATCHINFO_TOOLBAR_ADD = 1863
PATCHINFO_TOOLBAR_REMOVE = 1864
PATCHINFO_CANCEL = 1865
DIALOG_START = 1866
START_NEW = 1867
START_OPEN = 1868
START_RECENT = 1869
START_CANCEL = 1870
DIALOG_ABOUT = 1871
ABOUT_OK = 1872
DIALOG_ERROR = 1873
ERROR_REPORT = 1874
ERROR_COPY = 1875
ERROR_CLOSE = 1876
PREVIEW_CLOSE = 1877

###########################################################################
## Class MainFrameBase
###########################################################################

class MainFrameBase ( wx.MDIParentFrame ):

	def __init__( self, parent ):
		wx.MDIParentFrame.__init__ ( self, parent, id = WINDOW_MAIN, title = u"WhackEd4", pos = wx.DefaultPosition, size = wx.Size( 1024,560 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU|wx.HSCROLL|wx.VSCROLL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

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
		self.MenuFile.Append( self.MenuFileNew )

		self.MenuFileOpen = wx.MenuItem( self.MenuFile, wx.ID_ANY, u"Open..."+ u"\t" + u"Ctrl+O", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuFile.Append( self.MenuFileOpen )

		self.MenuFileOpenAs = wx.MenuItem( self.MenuFile, wx.ID_ANY, u"Open as...", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuFile.Append( self.MenuFileOpenAs )

		self.MenuFileMergeWith = wx.MenuItem( self.MenuFile, wx.ID_ANY, u"Merge with..."+ u"\t" + u"Ctrl+M", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuFile.Append( self.MenuFileMergeWith )

		self.MenuFileSave = wx.MenuItem( self.MenuFile, wx.ID_ANY, u"Save"+ u"\t" + u"Ctrl+S", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuFile.Append( self.MenuFileSave )

		self.MenuFileSaveAs = wx.MenuItem( self.MenuFile, wx.ID_ANY, u"Save as..."+ u"\t" + u"Ctrl+Shift+S", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuFile.Append( self.MenuFileSaveAs )

		self.MenuFile.AppendSeparator()

		self.MenuFileReloadWADs = wx.MenuItem( self.MenuFile, wx.ID_ANY, u"Reload WADs"+ u"\t" + u"CTRL+R", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuFile.Append( self.MenuFileReloadWADs )

		self.MenuFile.AppendSeparator()

		self.MenuFileRecent = wx.Menu()
		self.MenuFile.AppendSubMenu( self.MenuFileRecent, u"Recent files" )

		self.MenuFile.AppendSeparator()

		self.MenuFileExit = wx.MenuItem( self.MenuFile, wx.ID_ANY, u"Exit"+ u"\t" + u"Ctrl+Q", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuFile.Append( self.MenuFileExit )

		self.MainMenu.Append( self.MenuFile, u"File" )

		self.MenuEdit = wx.Menu()
		self.MenuEditUndo = wx.MenuItem( self.MenuEdit, wx.ID_ANY, u"Undo"+ u"\t" + u"Ctrl+Z", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuEdit.Append( self.MenuEditUndo )

		self.MenuEdit.AppendSeparator()

		self.MenuEditCopy = wx.MenuItem( self.MenuEdit, wx.ID_ANY, u"Copy"+ u"\t" + u"Ctrl+C", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuEdit.Append( self.MenuEditCopy )

		self.MenuEditPaste = wx.MenuItem( self.MenuEdit, wx.ID_ANY, u"Paste"+ u"\t" + u"Ctrl+V", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuEdit.Append( self.MenuEditPaste )

		self.MainMenu.Append( self.MenuEdit, u"Edit" )

		self.MenuView = wx.Menu()
		self.MenuViewThings = wx.MenuItem( self.MenuView, MAIN_MENU_THINGS, u"Things"+ u"\t" + u"F2", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuView.Append( self.MenuViewThings )

		self.MenuViewStates = wx.MenuItem( self.MenuView, MAIN_MENU_STATES, u"States"+ u"\t" + u"F3", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuView.Append( self.MenuViewStates )

		self.MenuViewSounds = wx.MenuItem( self.MenuView, MAIN_MENU_SOUNDS, u"Sounds"+ u"\t" + u"F4", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuView.Append( self.MenuViewSounds )
		self.MenuViewSounds.Enable( False )

		self.MenuViewStrings = wx.MenuItem( self.MenuView, MAIN_MENU_STRINGS, u"Strings"+ u"\t" + u"F6", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuView.Append( self.MenuViewStrings )
		self.MenuViewStrings.Enable( False )

		self.MenuViewWeapons = wx.MenuItem( self.MenuView, MAIN_MENU_WEAPONS, u"Weapons"+ u"\t" + u"F7", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuView.Append( self.MenuViewWeapons )
		self.MenuViewWeapons.Enable( False )

		self.MenuViewAmmo = wx.MenuItem( self.MenuView, MAIN_MENU_AMMO, u"Ammo"+ u"\t" + u"F8", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuView.Append( self.MenuViewAmmo )
		self.MenuViewAmmo.Enable( False )

		self.MenuViewCheats = wx.MenuItem( self.MenuView, MAIN_MENU_CHEATS, u"Cheats"+ u"\t" + u"F9", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuView.Append( self.MenuViewCheats )
		self.MenuViewCheats.Enable( False )

		self.MenuViewMiscellaneous = wx.MenuItem( self.MenuView, MAIN_MENU_MISC, u"Miscellaneous"+ u"\t" + u"F11", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuView.Append( self.MenuViewMiscellaneous )
		self.MenuViewMiscellaneous.Enable( False )

		self.MenuViewPar = wx.MenuItem( self.MenuView, MAIN_MENU_PAR, u"Par times"+ u"\t" + u"F12", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuView.Append( self.MenuViewPar )
		self.MenuViewPar.Enable( False )

		self.MenuView.AppendSeparator()

		self.MenuViewPatchSettings = wx.MenuItem( self.MenuView, wx.ID_ANY, u"Patch settings...", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuView.Append( self.MenuViewPatchSettings )

		self.MainMenu.Append( self.MenuView, u"View" )

		self.MenuHelp = wx.Menu()
		self.MenuHelpHelp = wx.MenuItem( self.MenuHelp, wx.ID_ANY, u"Help"+ u"\t" + u"F1", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuHelp.Append( self.MenuHelpHelp )
		self.MenuHelpHelp.Enable( False )

		self.MenuHelpAbout = wx.MenuItem( self.MenuHelp, wx.ID_ANY, u"About...", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuHelp.Append( self.MenuHelpAbout )

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
		self.Bind( wx.EVT_MENU, self.file_merge_with, id = self.MenuFileMergeWith.GetId() )
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
		self.Bind( wx.EVT_MENU, self.help_help, id = self.MenuHelpHelp.GetId() )
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

	def file_merge_with( self, event ):
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

	def help_help( self, event ):
		pass

	def help_about( self, event ):
		pass


###########################################################################
## Class ThingsFrameBase
###########################################################################

class ThingsFrameBase ( wx.MDIChildFrame ):

	def __init__( self, parent ):
		wx.MDIChildFrame.__init__ ( self, parent, id = FRAME_THINGS, title = u"Things", pos = wx.DefaultPosition, size = wx.Size( 640,640 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 640,640 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		SizerMain = wx.BoxSizer( wx.HORIZONTAL )

		TabsSizer = wx.BoxSizer( wx.VERTICAL )

		self.Tabs = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.PanelProperties = wx.ScrolledWindow( self.Tabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL )
		self.PanelProperties.SetScrollRate( 0, 6 )
		SizerProperties = wx.BoxSizer( wx.VERTICAL )

		self.PanelName = wx.Panel( self.PanelProperties, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerName = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingNameLabel = wx.StaticText( self.PanelName, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.ThingNameLabel.Wrap( -1 )

		SizerName.Add( self.ThingNameLabel, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

		self.ThingName = wx.TextCtrl( self.PanelName, THING_VAL_NAME, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.ThingName.SetMaxLength( 64 )
		SizerName.Add( self.ThingName, 1, wx.ALIGN_CENTER_VERTICAL, 0 )


		self.PanelName.SetSizer( SizerName )
		self.PanelName.Layout()
		SizerName.Fit( self.PanelName )
		SizerProperties.Add( self.PanelName, 0, wx.EXPAND |wx.ALL, 6 )

		self.PanelObituaryName = wx.Panel( self.PanelProperties, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerObituaryName = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingObituaryNameLabel = wx.StaticText( self.PanelObituaryName, wx.ID_ANY, u"Obituary name", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.ThingObituaryNameLabel.Wrap( -1 )

		SizerObituaryName.Add( self.ThingObituaryNameLabel, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

		self.ThingObituaryName = wx.TextCtrl( self.PanelObituaryName, THING_VAL_OBIT_NAME, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.ThingObituaryName.SetMaxLength( 64 )
		SizerObituaryName.Add( self.ThingObituaryName, 1, wx.ALIGN_CENTER_VERTICAL, 0 )


		self.PanelObituaryName.SetSizer( SizerObituaryName )
		self.PanelObituaryName.Layout()
		SizerObituaryName.Fit( self.PanelObituaryName )
		SizerProperties.Add( self.PanelObituaryName, 0, wx.EXPAND |wx.ALL, 6 )

		self.PanelObituaryNamePlural = wx.Panel( self.PanelProperties, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerObituaryNamePlural = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingObituaryNamePluralLabel = wx.StaticText( self.PanelObituaryNamePlural, wx.ID_ANY, u"Obituary plural name", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.ThingObituaryNamePluralLabel.Wrap( -1 )

		SizerObituaryNamePlural.Add( self.ThingObituaryNamePluralLabel, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

		self.ThingObituaryNamePlural = wx.TextCtrl( self.PanelObituaryNamePlural, THING_VAL_OBIT_NAME_PLURAL, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.ThingObituaryNamePlural.SetMaxLength( 64 )
		SizerObituaryNamePlural.Add( self.ThingObituaryNamePlural, 1, wx.ALIGN_CENTER_VERTICAL, 0 )


		self.PanelObituaryNamePlural.SetSizer( SizerObituaryNamePlural )
		self.PanelObituaryNamePlural.Layout()
		SizerObituaryNamePlural.Fit( self.PanelObituaryNamePlural )
		SizerProperties.Add( self.PanelObituaryNamePlural, 0, wx.EXPAND |wx.ALL, 6 )

		self.PanelGame = wx.Panel( self.PanelProperties, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerGame = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingGameLabel = wx.StaticText( self.PanelGame, wx.ID_ANY, u"Game", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.ThingGameLabel.Wrap( -1 )

		SizerGame.Add( self.ThingGameLabel, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

		ThingGameChoices = []
		self.ThingGame = wx.Choice( self.PanelGame, THING_VAL_GAME, wx.DefaultPosition, wx.Size( -1,-1 ), ThingGameChoices, 0 )
		self.ThingGame.SetSelection( 0 )
		SizerGame.Add( self.ThingGame, 1, 0, 0 )


		self.PanelGame.SetSizer( SizerGame )
		self.PanelGame.Layout()
		SizerGame.Fit( self.PanelGame )
		SizerProperties.Add( self.PanelGame, 0, wx.ALL|wx.EXPAND, 6 )

		self.PanelID = wx.Panel( self.PanelProperties, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerID = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingIdLabel = wx.StaticText( self.PanelID, wx.ID_ANY, u"ID", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.ThingIdLabel.Wrap( -1 )

		SizerID.Add( self.ThingIdLabel, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

		self.ThingId = wx.TextCtrl( self.PanelID, THING_VAL_ID, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.ThingId.SetMaxLength( 6 )
		SizerID.Add( self.ThingId, 1, wx.ALIGN_CENTER_VERTICAL, 0 )


		self.PanelID.SetSizer( SizerID )
		self.PanelID.Layout()
		SizerID.Fit( self.PanelID )
		SizerProperties.Add( self.PanelID, 0, wx.ALL|wx.EXPAND, 6 )

		self.PanelSpawnID = wx.Panel( self.PanelProperties, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerSpawnID = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingSpawnIdLabel = wx.StaticText( self.PanelSpawnID, wx.ID_ANY, u"Spawn ID", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.ThingSpawnIdLabel.Wrap( -1 )

		SizerSpawnID.Add( self.ThingSpawnIdLabel, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

		self.ThingSpawnId = wx.TextCtrl( self.PanelSpawnID, THING_VAL_SPAWNID, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.ThingSpawnId.SetMaxLength( 6 )
		SizerSpawnID.Add( self.ThingSpawnId, 1, wx.ALIGN_CENTER_VERTICAL, 0 )


		self.PanelSpawnID.SetSizer( SizerSpawnID )
		self.PanelSpawnID.Layout()
		SizerSpawnID.Fit( self.PanelSpawnID )
		SizerProperties.Add( self.PanelSpawnID, 0, wx.ALL|wx.EXPAND, 6 )

		self.PanelDroppedItemID = wx.Panel( self.PanelProperties, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerScale1 = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingDroppedItemIDLabel = wx.StaticText( self.PanelDroppedItemID, wx.ID_ANY, u"Dropped item ID", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.ThingDroppedItemIDLabel.Wrap( -1 )

		SizerScale1.Add( self.ThingDroppedItemIDLabel, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

		self.ThingDroppedItemID = wx.TextCtrl( self.PanelDroppedItemID, THING_VAL_DROPPED_ITEM_ID, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.ThingDroppedItemID.SetMaxLength( 6 )
		SizerScale1.Add( self.ThingDroppedItemID, 1, wx.ALIGN_CENTER_VERTICAL, 0 )


		self.PanelDroppedItemID.SetSizer( SizerScale1 )
		self.PanelDroppedItemID.Layout()
		SizerScale1.Fit( self.PanelDroppedItemID )
		SizerProperties.Add( self.PanelDroppedItemID, 0, wx.ALL|wx.EXPAND, 6 )

		self.PanelBloodID = wx.Panel( self.PanelProperties, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerScale11 = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingBloodIDLabel = wx.StaticText( self.PanelBloodID, wx.ID_ANY, u"Blood item ID", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.ThingBloodIDLabel.Wrap( -1 )

		SizerScale11.Add( self.ThingBloodIDLabel, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

		self.ThingBloodID = wx.TextCtrl( self.PanelBloodID, THING_VAL_BLOOD_ID, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.ThingBloodID.SetMaxLength( 6 )
		SizerScale11.Add( self.ThingBloodID, 1, wx.ALIGN_CENTER_VERTICAL, 0 )


		self.PanelBloodID.SetSizer( SizerScale11 )
		self.PanelBloodID.Layout()
		SizerScale11.Fit( self.PanelBloodID )
		SizerProperties.Add( self.PanelBloodID, 0, wx.EXPAND |wx.ALL, 5 )

		self.PanelHealth = wx.Panel( self.PanelProperties, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerHealth = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingHealthLabel = wx.StaticText( self.PanelHealth, wx.ID_ANY, u"Health", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.ThingHealthLabel.Wrap( -1 )

		SizerHealth.Add( self.ThingHealthLabel, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

		self.ThingHealth = wx.TextCtrl( self.PanelHealth, THING_VAL_HEALTH, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.ThingHealth.SetMaxLength( 6 )
		SizerHealth.Add( self.ThingHealth, 1, wx.ALIGN_CENTER_VERTICAL, 0 )


		self.PanelHealth.SetSizer( SizerHealth )
		self.PanelHealth.Layout()
		SizerHealth.Fit( self.PanelHealth )
		SizerProperties.Add( self.PanelHealth, 0, wx.ALL|wx.EXPAND, 6 )

		self.PanelGibHealth = wx.Panel( self.PanelProperties, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerHealth1 = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingGibHealthLabel = wx.StaticText( self.PanelGibHealth, wx.ID_ANY, u"Gib health", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.ThingGibHealthLabel.Wrap( -1 )

		SizerHealth1.Add( self.ThingGibHealthLabel, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

		self.ThingGibHealth = wx.TextCtrl( self.PanelGibHealth, THING_VAL_GIBHEALTH, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.ThingGibHealth.SetMaxLength( 6 )
		SizerHealth1.Add( self.ThingGibHealth, 1, wx.ALIGN_CENTER_VERTICAL, 0 )


		self.PanelGibHealth.SetSizer( SizerHealth1 )
		self.PanelGibHealth.Layout()
		SizerHealth1.Fit( self.PanelGibHealth )
		SizerProperties.Add( self.PanelGibHealth, 0, wx.ALL|wx.EXPAND, 6 )

		self.PanelSpeed = wx.Panel( self.PanelProperties, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerSpeed = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingSpeeLabel = wx.StaticText( self.PanelSpeed, wx.ID_ANY, u"Speed", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.ThingSpeeLabel.Wrap( -1 )

		SizerSpeed.Add( self.ThingSpeeLabel, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

		self.ThingSpeed = wx.TextCtrl( self.PanelSpeed, THING_VAL_SPEED, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.ThingSpeed.SetMaxLength( 6 )
		SizerSpeed.Add( self.ThingSpeed, 1, wx.ALIGN_CENTER_VERTICAL, 0 )


		self.PanelSpeed.SetSizer( SizerSpeed )
		self.PanelSpeed.Layout()
		SizerSpeed.Fit( self.PanelSpeed )
		SizerProperties.Add( self.PanelSpeed, 0, wx.ALL|wx.EXPAND, 6 )

		self.PanelRadius = wx.Panel( self.PanelProperties, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerRadius = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingRadiusLabel = wx.StaticText( self.PanelRadius, wx.ID_ANY, u"Radius", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.ThingRadiusLabel.Wrap( -1 )

		SizerRadius.Add( self.ThingRadiusLabel, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

		self.ThingRadius = wx.TextCtrl( self.PanelRadius, THING_VAL_RADIUS, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.ThingRadius.SetMaxLength( 6 )
		SizerRadius.Add( self.ThingRadius, 1, wx.ALIGN_CENTER_VERTICAL, 0 )


		self.PanelRadius.SetSizer( SizerRadius )
		self.PanelRadius.Layout()
		SizerRadius.Fit( self.PanelRadius )
		SizerProperties.Add( self.PanelRadius, 0, wx.ALL|wx.EXPAND, 6 )

		self.PanelPickupRadius = wx.Panel( self.PanelProperties, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerRadius1 = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingPickupRadiusLabel = wx.StaticText( self.PanelPickupRadius, wx.ID_ANY, u"Pickup radius", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.ThingPickupRadiusLabel.Wrap( -1 )

		SizerRadius1.Add( self.ThingPickupRadiusLabel, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

		self.ThingPickupRadius = wx.TextCtrl( self.PanelPickupRadius, THING_VAL_PICKUP_RADIUS, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.ThingPickupRadius.SetMaxLength( 6 )
		SizerRadius1.Add( self.ThingPickupRadius, 1, wx.ALIGN_CENTER_VERTICAL, 0 )


		self.PanelPickupRadius.SetSizer( SizerRadius1 )
		self.PanelPickupRadius.Layout()
		SizerRadius1.Fit( self.PanelPickupRadius )
		SizerProperties.Add( self.PanelPickupRadius, 0, wx.ALL|wx.EXPAND, 6 )

		self.PanelHeight = wx.Panel( self.PanelProperties, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerHeight = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingHeightLabel = wx.StaticText( self.PanelHeight, wx.ID_ANY, u"Height", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.ThingHeightLabel.Wrap( -1 )

		SizerHeight.Add( self.ThingHeightLabel, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

		self.ThingHeight = wx.TextCtrl( self.PanelHeight, THING_VAL_HEIGHT, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.ThingHeight.SetMaxLength( 6 )
		SizerHeight.Add( self.ThingHeight, 1, wx.ALIGN_CENTER_VERTICAL, 0 )


		self.PanelHeight.SetSizer( SizerHeight )
		self.PanelHeight.Layout()
		SizerHeight.Fit( self.PanelHeight )
		SizerProperties.Add( self.PanelHeight, 0, wx.ALL|wx.EXPAND, 6 )

		self.PanelProjectilePassHeight = wx.Panel( self.PanelProperties, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerHeight1 = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingProjectilePassHeightLabel = wx.StaticText( self.PanelProjectilePassHeight, wx.ID_ANY, u"Projectile pass height", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.ThingProjectilePassHeightLabel.Wrap( -1 )

		SizerHeight1.Add( self.ThingProjectilePassHeightLabel, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

		self.ThingProjectilePassHeight = wx.TextCtrl( self.PanelProjectilePassHeight, THING_VAL_PROJECTILE_PASS_HEIGHT, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.ThingProjectilePassHeight.SetMaxLength( 6 )
		SizerHeight1.Add( self.ThingProjectilePassHeight, 1, wx.ALIGN_CENTER_VERTICAL, 0 )


		self.PanelProjectilePassHeight.SetSizer( SizerHeight1 )
		self.PanelProjectilePassHeight.Layout()
		SizerHeight1.Fit( self.PanelProjectilePassHeight )
		SizerProperties.Add( self.PanelProjectilePassHeight, 0, wx.ALL|wx.EXPAND, 6 )

		self.PanelDamage = wx.Panel( self.PanelProperties, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerDamage = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingDamageLabel = wx.StaticText( self.PanelDamage, wx.ID_ANY, u"Damage", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.ThingDamageLabel.Wrap( -1 )

		SizerDamage.Add( self.ThingDamageLabel, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

		self.ThingDamage = wx.TextCtrl( self.PanelDamage, THING_VAL_DAMAGE, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.ThingDamage.SetMaxLength( 6 )
		SizerDamage.Add( self.ThingDamage, 1, wx.ALIGN_CENTER_VERTICAL, 0 )


		self.PanelDamage.SetSizer( SizerDamage )
		self.PanelDamage.Layout()
		SizerDamage.Fit( self.PanelDamage )
		SizerProperties.Add( self.PanelDamage, 0, wx.ALL|wx.EXPAND, 6 )

		self.PanelDamageFactor = wx.Panel( self.PanelProperties, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerDamageFactor = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingDamageFactorLabel = wx.StaticText( self.PanelDamageFactor, wx.ID_ANY, u"Damage factor", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.ThingDamageFactorLabel.Wrap( -1 )

		SizerDamageFactor.Add( self.ThingDamageFactorLabel, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

		self.ThingDamageFactor = wx.TextCtrl( self.PanelDamageFactor, THING_VAL_DAMAGEFACTOR, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.ThingDamageFactor.SetMaxLength( 6 )
		SizerDamageFactor.Add( self.ThingDamageFactor, 1, wx.ALIGN_CENTER_VERTICAL, 0 )


		self.PanelDamageFactor.SetSizer( SizerDamageFactor )
		self.PanelDamageFactor.Layout()
		SizerDamageFactor.Fit( self.PanelDamageFactor )
		SizerProperties.Add( self.PanelDamageFactor, 0, wx.ALL|wx.EXPAND, 6 )

		self.PanelReactionTime = wx.Panel( self.PanelProperties, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerReactionTime = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingReactionTimeLabel = wx.StaticText( self.PanelReactionTime, wx.ID_ANY, u"Reaction time", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.ThingReactionTimeLabel.Wrap( -1 )

		SizerReactionTime.Add( self.ThingReactionTimeLabel, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

		self.ThingReactionTime = wx.TextCtrl( self.PanelReactionTime, THING_VAL_REACTIONTIME, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.ThingReactionTime.SetMaxLength( 6 )
		SizerReactionTime.Add( self.ThingReactionTime, 1, wx.ALIGN_CENTER_VERTICAL, 0 )


		self.PanelReactionTime.SetSizer( SizerReactionTime )
		self.PanelReactionTime.Layout()
		SizerReactionTime.Fit( self.PanelReactionTime )
		SizerProperties.Add( self.PanelReactionTime, 0, wx.ALL|wx.EXPAND, 6 )

		self.PanelPainChance = wx.Panel( self.PanelProperties, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerPainChance = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingPainChanceLabel = wx.StaticText( self.PanelPainChance, wx.ID_ANY, u"Pain chance", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.ThingPainChanceLabel.Wrap( -1 )

		SizerPainChance.Add( self.ThingPainChanceLabel, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

		self.ThingPainChance = wx.TextCtrl( self.PanelPainChance, THING_VAL_PAINCHANCE, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.ThingPainChance.SetMaxLength( 6 )
		SizerPainChance.Add( self.ThingPainChance, 1, wx.ALIGN_CENTER_VERTICAL, 0 )


		self.PanelPainChance.SetSizer( SizerPainChance )
		self.PanelPainChance.Layout()
		SizerPainChance.Fit( self.PanelPainChance )
		SizerProperties.Add( self.PanelPainChance, 0, wx.ALL|wx.EXPAND, 6 )

		self.PanelMass = wx.Panel( self.PanelProperties, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerMass = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingMassLabel = wx.StaticText( self.PanelMass, wx.ID_ANY, u"Mass", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.ThingMassLabel.Wrap( -1 )

		SizerMass.Add( self.ThingMassLabel, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

		self.ThingMass = wx.TextCtrl( self.PanelMass, THING_VAL_MASS, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.ThingMass.SetMaxLength( 6 )
		SizerMass.Add( self.ThingMass, 1, wx.ALIGN_CENTER_VERTICAL, 0 )


		self.PanelMass.SetSizer( SizerMass )
		self.PanelMass.Layout()
		SizerMass.Fit( self.PanelMass )
		SizerProperties.Add( self.PanelMass, 0, wx.ALL|wx.EXPAND, 6 )

		self.PanelGravity = wx.Panel( self.PanelProperties, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerGravity = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingGravityLabel = wx.StaticText( self.PanelGravity, wx.ID_ANY, u"Gravity", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.ThingGravityLabel.Wrap( -1 )

		SizerGravity.Add( self.ThingGravityLabel, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

		self.ThingGravity = wx.TextCtrl( self.PanelGravity, THING_VAL_GRAVITY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.ThingGravity.SetMaxLength( 6 )
		SizerGravity.Add( self.ThingGravity, 1, wx.ALIGN_CENTER_VERTICAL, 0 )


		self.PanelGravity.SetSizer( SizerGravity )
		self.PanelGravity.Layout()
		SizerGravity.Fit( self.PanelGravity )
		SizerProperties.Add( self.PanelGravity, 0, wx.ALL|wx.EXPAND, 6 )

		self.PanelRespawnTime = wx.Panel( self.PanelProperties, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerRespawnTime = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingRespawnTimeLabel = wx.StaticText( self.PanelRespawnTime, wx.ID_ANY, u"Respawn time", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.ThingRespawnTimeLabel.Wrap( -1 )

		SizerRespawnTime.Add( self.ThingRespawnTimeLabel, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

		self.ThingRespawnTime = wx.TextCtrl( self.PanelRespawnTime, THING_VAL_RESPAWNTIME, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.ThingRespawnTime.SetMaxLength( 6 )
		SizerRespawnTime.Add( self.ThingRespawnTime, 1, wx.ALIGN_CENTER_VERTICAL, 0 )


		self.PanelRespawnTime.SetSizer( SizerRespawnTime )
		self.PanelRespawnTime.Layout()
		SizerRespawnTime.Fit( self.PanelRespawnTime )
		SizerProperties.Add( self.PanelRespawnTime, 0, wx.ALL|wx.EXPAND, 6 )

		self.PanelFullbright = wx.Panel( self.PanelProperties, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerRespawnTime1 = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingFullbrightLabel = wx.StaticText( self.PanelFullbright, wx.ID_ANY, u"Full brightness", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.ThingFullbrightLabel.Wrap( -1 )

		SizerRespawnTime1.Add( self.ThingFullbrightLabel, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

		self.ThingFullbright = wx.CheckBox( self.PanelFullbright, THING_VAL_FULLBRIGHT, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		SizerRespawnTime1.Add( self.ThingFullbright, 0, wx.ALIGN_CENTER_VERTICAL, 0 )


		self.PanelFullbright.SetSizer( SizerRespawnTime1 )
		self.PanelFullbright.Layout()
		SizerRespawnTime1.Fit( self.PanelFullbright )
		SizerProperties.Add( self.PanelFullbright, 0, wx.ALL|wx.EXPAND, 6 )

		self.PanelRenderStyle = wx.Panel( self.PanelProperties, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerRenderStyle = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingRenderStyleLabel = wx.StaticText( self.PanelRenderStyle, wx.ID_ANY, u"Render style", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.ThingRenderStyleLabel.Wrap( -1 )

		SizerRenderStyle.Add( self.ThingRenderStyleLabel, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

		ThingRenderStyleChoices = []
		self.ThingRenderStyle = wx.Choice( self.PanelRenderStyle, THING_VAL_RENDERSTYLE, wx.DefaultPosition, wx.Size( -1,-1 ), ThingRenderStyleChoices, 0 )
		self.ThingRenderStyle.SetSelection( 0 )
		SizerRenderStyle.Add( self.ThingRenderStyle, 1, 0, 0 )


		self.PanelRenderStyle.SetSizer( SizerRenderStyle )
		self.PanelRenderStyle.Layout()
		SizerRenderStyle.Fit( self.PanelRenderStyle )
		SizerProperties.Add( self.PanelRenderStyle, 0, wx.ALL|wx.EXPAND, 6 )

		self.PanelAlpha = wx.Panel( self.PanelProperties, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerAlpha = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingAlphaLabel = wx.StaticText( self.PanelAlpha, wx.ID_ANY, u"Alpha", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.ThingAlphaLabel.Wrap( -1 )

		SizerAlpha.Add( self.ThingAlphaLabel, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

		self.ThingAlpha = wx.TextCtrl( self.PanelAlpha, THING_VAL_ALPHA, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.ThingAlpha.SetMaxLength( 6 )
		SizerAlpha.Add( self.ThingAlpha, 1, wx.ALIGN_CENTER_VERTICAL, 0 )


		self.PanelAlpha.SetSizer( SizerAlpha )
		self.PanelAlpha.Layout()
		SizerAlpha.Fit( self.PanelAlpha )
		SizerProperties.Add( self.PanelAlpha, 0, wx.ALL|wx.EXPAND, 6 )

		self.PanelScale = wx.Panel( self.PanelProperties, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerScale = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingScaleLabel = wx.StaticText( self.PanelScale, wx.ID_ANY, u"Scale", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.ThingScaleLabel.Wrap( -1 )

		SizerScale.Add( self.ThingScaleLabel, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

		self.ThingScale = wx.TextCtrl( self.PanelScale, THING_VAL_SCALE, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.ThingScale.SetMaxLength( 6 )
		SizerScale.Add( self.ThingScale, 1, wx.ALIGN_CENTER_VERTICAL, 0 )


		self.PanelScale.SetSizer( SizerScale )
		self.PanelScale.Layout()
		SizerScale.Fit( self.PanelScale )
		SizerProperties.Add( self.PanelScale, 0, wx.ALL|wx.EXPAND, 6 )

		self.PanelDecal = wx.Panel( self.PanelProperties, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerDecal = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingDecalLabel = wx.StaticText( self.PanelDecal, wx.ID_ANY, u"Decal", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.ThingDecalLabel.Wrap( -1 )

		SizerDecal.Add( self.ThingDecalLabel, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

		self.ThingDecal = wx.TextCtrl( self.PanelDecal, THING_VAL_DECAL, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.ThingDecal.SetMaxLength( 6 )
		SizerDecal.Add( self.ThingDecal, 1, wx.ALIGN_CENTER_VERTICAL, 0 )


		self.PanelDecal.SetSizer( SizerDecal )
		self.PanelDecal.Layout()
		SizerDecal.Fit( self.PanelDecal )
		SizerProperties.Add( self.PanelDecal, 0, wx.ALL|wx.EXPAND, 6 )

		self.PanelShadowOffset = wx.Panel( self.PanelProperties, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerScale111 = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingShadowOffsetLabel = wx.StaticText( self.PanelShadowOffset, wx.ID_ANY, u"Shadow offset", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.ThingShadowOffsetLabel.Wrap( -1 )

		SizerScale111.Add( self.ThingShadowOffsetLabel, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

		self.ThingShadowOffset = wx.TextCtrl( self.PanelShadowOffset, THING_VAL_SHADOW_OFFSET, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.ThingShadowOffset.SetMaxLength( 6 )
		SizerScale111.Add( self.ThingShadowOffset, 1, wx.ALIGN_CENTER_VERTICAL, 0 )


		self.PanelShadowOffset.SetSizer( SizerScale111 )
		self.PanelShadowOffset.Layout()
		SizerScale111.Fit( self.PanelShadowOffset )
		SizerProperties.Add( self.PanelShadowOffset, 0, wx.EXPAND |wx.ALL, 5 )


		self.PanelProperties.SetSizer( SizerProperties )
		self.PanelProperties.Layout()
		SizerProperties.Fit( self.PanelProperties )
		self.Tabs.AddPage( self.PanelProperties, u"Properties", True )
		self.PanelStates = wx.Panel( self.Tabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerStates = wx.BoxSizer( wx.VERTICAL )

		self.PanelStateSpawn = wx.Panel( self.PanelStates, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerStateSpawn = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingStateSpawnLabel = wx.StaticText( self.PanelStateSpawn, wx.ID_ANY, u"Spawn", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingStateSpawnLabel.Wrap( -1 )

		SizerStateSpawn.Add( self.ThingStateSpawnLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingStateSpawn = wx.TextCtrl( self.PanelStateSpawn, THING_STATE_SPAWN, u"318", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.ThingStateSpawn.SetMaxLength( 4 )
		SizerStateSpawn.Add( self.ThingStateSpawn, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingStateSpawnName = wx.StaticText( self.PanelStateSpawn, THING_STATENAME_SPAWN, u"TROOA", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingStateSpawnName.Wrap( -1 )

		self.ThingStateSpawnName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.ThingStateSpawnName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		SizerStateSpawn.Add( self.ThingStateSpawnName, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingStateSpawnSet = wx.Button( self.PanelStateSpawn, THING_STATESET_SPAWN, u"<", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.ThingStateSpawnSet.SetMinSize( wx.Size( 30,30 ) )

		SizerStateSpawn.Add( self.ThingStateSpawnSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )


		self.PanelStateSpawn.SetSizer( SizerStateSpawn )
		self.PanelStateSpawn.Layout()
		SizerStateSpawn.Fit( self.PanelStateSpawn )
		SizerStates.Add( self.PanelStateSpawn, 0, wx.ALL|wx.EXPAND, 3 )

		self.PanelStateWalk = wx.Panel( self.PanelStates, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerStateWalk = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingStateWalkLabel = wx.StaticText( self.PanelStateWalk, wx.ID_ANY, u"Walk", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingStateWalkLabel.Wrap( -1 )

		SizerStateWalk.Add( self.ThingStateWalkLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingStateWalk = wx.TextCtrl( self.PanelStateWalk, THING_STATE_WALK, u"318", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.ThingStateWalk.SetMaxLength( 4 )
		SizerStateWalk.Add( self.ThingStateWalk, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingStateWalkName = wx.StaticText( self.PanelStateWalk, THING_STATENAME_WALK, u"TROOA", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingStateWalkName.Wrap( -1 )

		self.ThingStateWalkName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.ThingStateWalkName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		SizerStateWalk.Add( self.ThingStateWalkName, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingStateWalkSet = wx.Button( self.PanelStateWalk, THING_STATESET_WALK, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingStateWalkSet.SetMinSize( wx.Size( 30,30 ) )

		SizerStateWalk.Add( self.ThingStateWalkSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )


		self.PanelStateWalk.SetSizer( SizerStateWalk )
		self.PanelStateWalk.Layout()
		SizerStateWalk.Fit( self.PanelStateWalk )
		SizerStates.Add( self.PanelStateWalk, 0, wx.ALL|wx.EXPAND, 3 )

		self.PanelStatePain = wx.Panel( self.PanelStates, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerStatePain = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingStatePainLabel = wx.StaticText( self.PanelStatePain, wx.ID_ANY, u"Pain", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingStatePainLabel.Wrap( -1 )

		SizerStatePain.Add( self.ThingStatePainLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingStatePain = wx.TextCtrl( self.PanelStatePain, THING_STATE_PAIN, u"318", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.ThingStatePain.SetMaxLength( 4 )
		SizerStatePain.Add( self.ThingStatePain, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingStatePainName = wx.StaticText( self.PanelStatePain, THING_STATENAME_PAIN, u"TROOA", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingStatePainName.Wrap( -1 )

		self.ThingStatePainName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.ThingStatePainName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		SizerStatePain.Add( self.ThingStatePainName, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingStatePainSet = wx.Button( self.PanelStatePain, THING_STATESET_PAIN, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingStatePainSet.SetMinSize( wx.Size( 30,30 ) )

		SizerStatePain.Add( self.ThingStatePainSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )


		self.PanelStatePain.SetSizer( SizerStatePain )
		self.PanelStatePain.Layout()
		SizerStatePain.Fit( self.PanelStatePain )
		SizerStates.Add( self.PanelStatePain, 0, wx.ALL|wx.EXPAND, 3 )

		self.PanelStateMelee = wx.Panel( self.PanelStates, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerStateMelee = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingStateMeleeLabel = wx.StaticText( self.PanelStateMelee, wx.ID_ANY, u"Melee", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingStateMeleeLabel.Wrap( -1 )

		SizerStateMelee.Add( self.ThingStateMeleeLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingStateMelee = wx.TextCtrl( self.PanelStateMelee, THING_STATE_MELEE, u"318", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.ThingStateMelee.SetMaxLength( 4 )
		SizerStateMelee.Add( self.ThingStateMelee, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingStateMeleeName = wx.StaticText( self.PanelStateMelee, THING_STATENAME_MELEE, u"TROOA", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingStateMeleeName.Wrap( -1 )

		self.ThingStateMeleeName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.ThingStateMeleeName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		SizerStateMelee.Add( self.ThingStateMeleeName, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingStateMeleeSet = wx.Button( self.PanelStateMelee, THING_STATESET_MELEE, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingStateMeleeSet.SetMinSize( wx.Size( 30,30 ) )

		SizerStateMelee.Add( self.ThingStateMeleeSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )


		self.PanelStateMelee.SetSizer( SizerStateMelee )
		self.PanelStateMelee.Layout()
		SizerStateMelee.Fit( self.PanelStateMelee )
		SizerStates.Add( self.PanelStateMelee, 0, wx.ALL|wx.EXPAND, 3 )

		self.PanelStateAttack = wx.Panel( self.PanelStates, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerStateAttack = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingStateAttackLabel = wx.StaticText( self.PanelStateAttack, wx.ID_ANY, u"Attack", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingStateAttackLabel.Wrap( -1 )

		SizerStateAttack.Add( self.ThingStateAttackLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingStateAttack = wx.TextCtrl( self.PanelStateAttack, THING_STATE_ATTACK, u"318", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.ThingStateAttack.SetMaxLength( 4 )
		SizerStateAttack.Add( self.ThingStateAttack, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingStateAttackName = wx.StaticText( self.PanelStateAttack, THING_STATENAME_ATTACK, u"TROOA", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingStateAttackName.Wrap( -1 )

		self.ThingStateAttackName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.ThingStateAttackName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		SizerStateAttack.Add( self.ThingStateAttackName, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingStateAttackSet = wx.Button( self.PanelStateAttack, THING_STATESET_ATTACK, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingStateAttackSet.SetMinSize( wx.Size( 30,30 ) )

		SizerStateAttack.Add( self.ThingStateAttackSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )


		self.PanelStateAttack.SetSizer( SizerStateAttack )
		self.PanelStateAttack.Layout()
		SizerStateAttack.Fit( self.PanelStateAttack )
		SizerStates.Add( self.PanelStateAttack, 0, wx.ALL|wx.EXPAND, 3 )

		self.PanelStateDeath = wx.Panel( self.PanelStates, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerStateDeath = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingStateDeathLabel = wx.StaticText( self.PanelStateDeath, wx.ID_ANY, u"Death", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingStateDeathLabel.Wrap( -1 )

		SizerStateDeath.Add( self.ThingStateDeathLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingStateDeath = wx.TextCtrl( self.PanelStateDeath, THING_STATE_DEATH, u"318", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.ThingStateDeath.SetMaxLength( 4 )
		SizerStateDeath.Add( self.ThingStateDeath, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingStateDeathName = wx.StaticText( self.PanelStateDeath, THING_STATENAME_DEATH, u"TROOA", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingStateDeathName.Wrap( -1 )

		self.ThingStateDeathName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.ThingStateDeathName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		SizerStateDeath.Add( self.ThingStateDeathName, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingStateDeathSet = wx.Button( self.PanelStateDeath, THING_STATESET_DEATH, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingStateDeathSet.SetMinSize( wx.Size( 30,30 ) )

		SizerStateDeath.Add( self.ThingStateDeathSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )


		self.PanelStateDeath.SetSizer( SizerStateDeath )
		self.PanelStateDeath.Layout()
		SizerStateDeath.Fit( self.PanelStateDeath )
		SizerStates.Add( self.PanelStateDeath, 0, wx.ALL|wx.EXPAND, 3 )

		self.PanelStateExplode = wx.Panel( self.PanelStates, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerStateExplode = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingStateExplodeLabel = wx.StaticText( self.PanelStateExplode, wx.ID_ANY, u"Explode", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingStateExplodeLabel.Wrap( -1 )

		SizerStateExplode.Add( self.ThingStateExplodeLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingStateExplode = wx.TextCtrl( self.PanelStateExplode, THING_STATE_EXPLODE, u"318", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.ThingStateExplode.SetMaxLength( 4 )
		SizerStateExplode.Add( self.ThingStateExplode, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingStateExplodeName = wx.StaticText( self.PanelStateExplode, THING_STATENAME_EXPLODE, u"TROOA", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingStateExplodeName.Wrap( -1 )

		self.ThingStateExplodeName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.ThingStateExplodeName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		SizerStateExplode.Add( self.ThingStateExplodeName, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingStateExplodeSet = wx.Button( self.PanelStateExplode, THING_STATESET_EXPLODE, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingStateExplodeSet.SetMinSize( wx.Size( 30,30 ) )

		SizerStateExplode.Add( self.ThingStateExplodeSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )


		self.PanelStateExplode.SetSizer( SizerStateExplode )
		self.PanelStateExplode.Layout()
		SizerStateExplode.Fit( self.PanelStateExplode )
		SizerStates.Add( self.PanelStateExplode, 0, wx.ALL|wx.EXPAND, 3 )

		self.PanelStateRaise = wx.Panel( self.PanelStates, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerStateRaise = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingStateRaiseLabel = wx.StaticText( self.PanelStateRaise, wx.ID_ANY, u"Raise", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingStateRaiseLabel.Wrap( -1 )

		SizerStateRaise.Add( self.ThingStateRaiseLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingStateRaise = wx.TextCtrl( self.PanelStateRaise, THING_STATE_RAISE, u"318", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.ThingStateRaise.SetMaxLength( 4 )
		SizerStateRaise.Add( self.ThingStateRaise, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingStateRaiseName = wx.StaticText( self.PanelStateRaise, THING_STATENAME_RAISE, u"TROOA", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingStateRaiseName.Wrap( -1 )

		self.ThingStateRaiseName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.ThingStateRaiseName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		SizerStateRaise.Add( self.ThingStateRaiseName, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingStateRaiseSet = wx.Button( self.PanelStateRaise, THING_STATESET_RAISE, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingStateRaiseSet.SetMinSize( wx.Size( 30,30 ) )

		SizerStateRaise.Add( self.ThingStateRaiseSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )


		self.PanelStateRaise.SetSizer( SizerStateRaise )
		self.PanelStateRaise.Layout()
		SizerStateRaise.Fit( self.PanelStateRaise )
		SizerStates.Add( self.PanelStateRaise, 0, wx.ALL|wx.EXPAND, 3 )

		self.PanelStateCrash = wx.Panel( self.PanelStates, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerStateCrash = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingStateCrashLabel = wx.StaticText( self.PanelStateCrash, wx.ID_ANY, u"Crash", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingStateCrashLabel.Wrap( -1 )

		SizerStateCrash.Add( self.ThingStateCrashLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingStateCrash = wx.TextCtrl( self.PanelStateCrash, THING_STATE_CRASH, u"318", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.ThingStateCrash.SetMaxLength( 4 )
		SizerStateCrash.Add( self.ThingStateCrash, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingStateCrashName = wx.StaticText( self.PanelStateCrash, THING_STATENAME_CRASH, u"TROOA", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingStateCrashName.Wrap( -1 )

		self.ThingStateCrashName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.ThingStateCrashName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		SizerStateCrash.Add( self.ThingStateCrashName, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingStateCrashSet = wx.Button( self.PanelStateCrash, THING_STATESET_CRASH, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingStateCrashSet.SetMinSize( wx.Size( 30,30 ) )

		SizerStateCrash.Add( self.ThingStateCrashSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )


		self.PanelStateCrash.SetSizer( SizerStateCrash )
		self.PanelStateCrash.Layout()
		SizerStateCrash.Fit( self.PanelStateCrash )
		SizerStates.Add( self.PanelStateCrash, 0, wx.ALL|wx.EXPAND, 3 )

		self.PanelStateFreeze = wx.Panel( self.PanelStates, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerStateFreeze = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingStateFreezeLabel = wx.StaticText( self.PanelStateFreeze, wx.ID_ANY, u"Freeze", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingStateFreezeLabel.Wrap( -1 )

		SizerStateFreeze.Add( self.ThingStateFreezeLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingStateFreeze = wx.TextCtrl( self.PanelStateFreeze, THING_STATE_FREEZE, u"318", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.ThingStateFreeze.SetMaxLength( 4 )
		SizerStateFreeze.Add( self.ThingStateFreeze, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingStateFreezeName = wx.StaticText( self.PanelStateFreeze, THING_STATENAME_FREEZE, u"TROOA", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingStateFreezeName.Wrap( -1 )

		self.ThingStateFreezeName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.ThingStateFreezeName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		SizerStateFreeze.Add( self.ThingStateFreezeName, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingStateFreezeSet = wx.Button( self.PanelStateFreeze, THING_STATESET_FREEZE, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingStateFreezeSet.SetMinSize( wx.Size( 30,30 ) )

		SizerStateFreeze.Add( self.ThingStateFreezeSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )


		self.PanelStateFreeze.SetSizer( SizerStateFreeze )
		self.PanelStateFreeze.Layout()
		SizerStateFreeze.Fit( self.PanelStateFreeze )
		SizerStates.Add( self.PanelStateFreeze, 0, wx.ALL|wx.EXPAND, 3 )

		self.PanelStateBurn = wx.Panel( self.PanelStates, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerStateBurn = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingStateBurnLabel = wx.StaticText( self.PanelStateBurn, wx.ID_ANY, u"Burn", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingStateBurnLabel.Wrap( -1 )

		SizerStateBurn.Add( self.ThingStateBurnLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingStateBurn = wx.TextCtrl( self.PanelStateBurn, THING_STATE_BURN, u"318", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.ThingStateBurn.SetMaxLength( 4 )
		SizerStateBurn.Add( self.ThingStateBurn, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingStateBurnName = wx.StaticText( self.PanelStateBurn, THING_STATENAME_BURN, u"TROOA", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingStateBurnName.Wrap( -1 )

		self.ThingStateBurnName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.ThingStateBurnName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		SizerStateBurn.Add( self.ThingStateBurnName, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingStateBurnSet = wx.Button( self.PanelStateBurn, THING_STATESET_BURN, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingStateBurnSet.SetMinSize( wx.Size( 30,30 ) )

		SizerStateBurn.Add( self.ThingStateBurnSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )


		self.PanelStateBurn.SetSizer( SizerStateBurn )
		self.PanelStateBurn.Layout()
		SizerStateBurn.Fit( self.PanelStateBurn )
		SizerStates.Add( self.PanelStateBurn, 0, wx.ALL|wx.EXPAND, 3 )


		self.PanelStates.SetSizer( SizerStates )
		self.PanelStates.Layout()
		SizerStates.Fit( self.PanelStates )
		self.Tabs.AddPage( self.PanelStates, u"States", False )
		self.PanelSounds = wx.Panel( self.Tabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerSounds = wx.BoxSizer( wx.VERTICAL )

		self.PanelSoundAlert = wx.Panel( self.PanelSounds, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerSoundAlert = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingSoundAlertLabel = wx.StaticText( self.PanelSoundAlert, wx.ID_ANY, u"Alert", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingSoundAlertLabel.Wrap( -1 )

		SizerSoundAlert.Add( self.ThingSoundAlertLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingSoundAlert = wx.TextCtrl( self.PanelSoundAlert, THING_SOUND_ALERT, u"46", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.ThingSoundAlert.SetMaxLength( 4 )
		SizerSoundAlert.Add( self.ThingSoundAlert, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingSoundAlertName = wx.StaticText( self.PanelSoundAlert, THING_SOUNDNAME_ALERT, u"PLPAIN", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingSoundAlertName.Wrap( -1 )

		self.ThingSoundAlertName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.ThingSoundAlertName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		SizerSoundAlert.Add( self.ThingSoundAlertName, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingSoundAlertSet = wx.Button( self.PanelSoundAlert, THING_SOUNDSET_ALERT, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingSoundAlertSet.SetMinSize( wx.Size( 30,30 ) )

		SizerSoundAlert.Add( self.ThingSoundAlertSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )


		self.PanelSoundAlert.SetSizer( SizerSoundAlert )
		self.PanelSoundAlert.Layout()
		SizerSoundAlert.Fit( self.PanelSoundAlert )
		SizerSounds.Add( self.PanelSoundAlert, 0, wx.ALL|wx.EXPAND, 3 )

		self.PanelSoundAttack = wx.Panel( self.PanelSounds, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerSoundAttack = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingSoundAttackLabel = wx.StaticText( self.PanelSoundAttack, wx.ID_ANY, u"Attack", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingSoundAttackLabel.Wrap( -1 )

		SizerSoundAttack.Add( self.ThingSoundAttackLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingSoundAttack = wx.TextCtrl( self.PanelSoundAttack, THING_SOUND_ATTACK, u"46", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.ThingSoundAttack.SetMaxLength( 4 )
		SizerSoundAttack.Add( self.ThingSoundAttack, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingSoundAttackName = wx.StaticText( self.PanelSoundAttack, THING_SOUNDNAME_ATTACK, u"PLPAIN", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingSoundAttackName.Wrap( -1 )

		self.ThingSoundAttackName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.ThingSoundAttackName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		SizerSoundAttack.Add( self.ThingSoundAttackName, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingSoundAttackSet = wx.Button( self.PanelSoundAttack, THING_SOUNDSET_ATTACK, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingSoundAttackSet.SetMinSize( wx.Size( 30,30 ) )

		SizerSoundAttack.Add( self.ThingSoundAttackSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )


		self.PanelSoundAttack.SetSizer( SizerSoundAttack )
		self.PanelSoundAttack.Layout()
		SizerSoundAttack.Fit( self.PanelSoundAttack )
		SizerSounds.Add( self.PanelSoundAttack, 0, wx.ALL|wx.EXPAND, 3 )

		self.PanelSoundPain = wx.Panel( self.PanelSounds, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerSoundPain = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingSoundPainLabel = wx.StaticText( self.PanelSoundPain, wx.ID_ANY, u"Pain", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingSoundPainLabel.Wrap( -1 )

		SizerSoundPain.Add( self.ThingSoundPainLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingSoundPain = wx.TextCtrl( self.PanelSoundPain, THING_SOUND_PAIN, u"46", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.ThingSoundPain.SetMaxLength( 4 )
		SizerSoundPain.Add( self.ThingSoundPain, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingSoundPainName = wx.StaticText( self.PanelSoundPain, THING_SOUNDNAME_PAIN, u"PLPAIN", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingSoundPainName.Wrap( -1 )

		self.ThingSoundPainName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.ThingSoundPainName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		SizerSoundPain.Add( self.ThingSoundPainName, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingSoundPainSet = wx.Button( self.PanelSoundPain, THING_SOUNDSET_PAIN, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingSoundPainSet.SetMinSize( wx.Size( 30,30 ) )

		SizerSoundPain.Add( self.ThingSoundPainSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )


		self.PanelSoundPain.SetSizer( SizerSoundPain )
		self.PanelSoundPain.Layout()
		SizerSoundPain.Fit( self.PanelSoundPain )
		SizerSounds.Add( self.PanelSoundPain, 0, wx.ALL|wx.EXPAND, 3 )

		self.PanelSoundDeath = wx.Panel( self.PanelSounds, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerSoundDeath = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingSoundDeathLabel = wx.StaticText( self.PanelSoundDeath, wx.ID_ANY, u"Death", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingSoundDeathLabel.Wrap( -1 )

		SizerSoundDeath.Add( self.ThingSoundDeathLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingSoundDeath = wx.TextCtrl( self.PanelSoundDeath, THING_SOUND_DEATH, u"46", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.ThingSoundDeath.SetMaxLength( 4 )
		SizerSoundDeath.Add( self.ThingSoundDeath, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingSoundDeathName = wx.StaticText( self.PanelSoundDeath, THING_SOUNDNAME_DEATH, u"PLPAIN", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingSoundDeathName.Wrap( -1 )

		self.ThingSoundDeathName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.ThingSoundDeathName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		SizerSoundDeath.Add( self.ThingSoundDeathName, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingSoundDeathSet = wx.Button( self.PanelSoundDeath, THING_SOUNDSET_DEATH, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingSoundDeathSet.SetMinSize( wx.Size( 30,30 ) )

		SizerSoundDeath.Add( self.ThingSoundDeathSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )


		self.PanelSoundDeath.SetSizer( SizerSoundDeath )
		self.PanelSoundDeath.Layout()
		SizerSoundDeath.Fit( self.PanelSoundDeath )
		SizerSounds.Add( self.PanelSoundDeath, 0, wx.ALL|wx.EXPAND, 3 )

		self.PanelSoundActive = wx.Panel( self.PanelSounds, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerSoundActive = wx.BoxSizer( wx.HORIZONTAL )

		self.ThingSoundActiveLabel = wx.StaticText( self.PanelSoundActive, wx.ID_ANY, u"Active", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.ThingSoundActiveLabel.Wrap( -1 )

		SizerSoundActive.Add( self.ThingSoundActiveLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingSoundActive = wx.TextCtrl( self.PanelSoundActive, THING_SOUND_ACTIVE, u"46", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.ThingSoundActive.SetMaxLength( 4 )
		SizerSoundActive.Add( self.ThingSoundActive, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingSoundActiveName = wx.StaticText( self.PanelSoundActive, THING_SOUNDNAME_ACTIVE, u"PLPAIN", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.ThingSoundActiveName.Wrap( -1 )

		self.ThingSoundActiveName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.ThingSoundActiveName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		SizerSoundActive.Add( self.ThingSoundActiveName, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ThingSoundActiveSet = wx.Button( self.PanelSoundActive, THING_SOUNDSET_ACTIVE, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThingSoundActiveSet.SetMinSize( wx.Size( 30,30 ) )

		SizerSoundActive.Add( self.ThingSoundActiveSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )


		self.PanelSoundActive.SetSizer( SizerSoundActive )
		self.PanelSoundActive.Layout()
		SizerSoundActive.Fit( self.PanelSoundActive )
		SizerSounds.Add( self.PanelSoundActive, 0, wx.ALL|wx.EXPAND, 3 )


		self.PanelSounds.SetSizer( SizerSounds )
		self.PanelSounds.Layout()
		SizerSounds.Fit( self.PanelSounds )
		self.Tabs.AddPage( self.PanelSounds, u"Sounds", False )
		self.PanelFlags = wx.Panel( self.Tabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerFlags = wx.BoxSizer( wx.VERTICAL )

		ThingFlagsChoices = []
		self.ThingFlags = wx.CheckListBox( self.PanelFlags, THING_FLAGS, wx.DefaultPosition, wx.Size( -1,-1 ), ThingFlagsChoices, 0|wx.BORDER_NONE )
		self.ThingFlags.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.ThingFlags.SetMinSize( wx.Size( 210,-1 ) )

		SizerFlags.Add( self.ThingFlags, 1, wx.EXPAND, 3 )


		self.PanelFlags.SetSizer( SizerFlags )
		self.PanelFlags.Layout()
		SizerFlags.Fit( self.PanelFlags )
		self.Tabs.AddPage( self.PanelFlags, u"Flags", False )

		TabsSizer.Add( self.Tabs, 1, wx.ALL|wx.EXPAND, 6 )

		ButtonSizer = wx.BoxSizer( wx.VERTICAL )

		self.ButtonRestore = wx.Button( self, THING_RESTORE, u"Restore", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.ButtonRestore.SetMinSize( wx.Size( -1,36 ) )

		ButtonSizer.Add( self.ButtonRestore, 0, wx.EXPAND|wx.TOP, 6 )


		TabsSizer.Add( ButtonSizer, 0, wx.ALL|wx.EXPAND, 6 )


		SizerMain.Add( TabsSizer, 0, wx.EXPAND, 0 )

		self.ThingList = wx.ListCtrl( self, THING_LIST, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.BORDER_NONE )
		SizerMain.Add( self.ThingList, 1, wx.EXPAND, 0 )


		self.SetSizer( SizerMain )
		self.Layout()
		self.ThingContext = wx.Menu()
		self.ThingContextCopy = wx.MenuItem( self.ThingContext, wx.ID_ANY, u"Copy"+ u"\t" + u"Ctrl+C", wx.EmptyString, wx.ITEM_NORMAL )
		self.ThingContext.Append( self.ThingContextCopy )

		self.ThingContextPaste = wx.MenuItem( self.ThingContext, wx.ID_ANY, u"Paste"+ u"\t" + u"Ctrl+V", wx.EmptyString, wx.ITEM_NORMAL )
		self.ThingContext.Append( self.ThingContextPaste )

		self.ThingContextClear = wx.MenuItem( self.ThingContext, wx.ID_ANY, u"Clear", wx.EmptyString, wx.ITEM_NORMAL )
		self.ThingContext.Append( self.ThingContextClear )



		# Connect Events
		self.ThingNameLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingName.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingName.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingObituaryNameLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingObituaryName.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingObituaryName.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingObituaryNamePluralLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingObituaryNamePlural.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingObituaryNamePlural.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingGameLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingGame.Bind( wx.EVT_CHOICE, self.set_renderstyle )
		self.ThingIdLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingId.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingId.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingSpawnIdLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingSpawnId.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingSpawnId.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingDroppedItemIDLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingDroppedItemID.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingDroppedItemID.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingBloodIDLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingBloodID.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingBloodID.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingHealthLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingHealth.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingHealth.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingGibHealthLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingGibHealth.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingGibHealth.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingSpeeLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingSpeed.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingSpeed.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingRadiusLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingRadius.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingRadius.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingPickupRadiusLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingPickupRadius.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingPickupRadius.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingHeightLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingHeight.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingHeight.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingProjectilePassHeightLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingProjectilePassHeight.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingProjectilePassHeight.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingDamageLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingDamage.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingDamage.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingDamageFactorLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingDamageFactor.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingDamageFactor.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingReactionTimeLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingReactionTime.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingReactionTime.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingPainChanceLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingPainChance.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingPainChance.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingMassLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingMass.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingMass.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingGravityLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingGravity.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingGravity.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingRespawnTimeLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingRespawnTime.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingRespawnTime.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingFullbrightLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingFullbright.Bind( wx.EVT_CHECKBOX, self.set_value )
		self.ThingRenderStyleLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingRenderStyle.Bind( wx.EVT_CHOICE, self.set_renderstyle )
		self.ThingAlphaLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingAlpha.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingAlpha.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingScaleLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingScale.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingScale.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingDecalLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingDecal.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingDecal.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingShadowOffsetLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingShadowOffset.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingShadowOffset.Bind( wx.EVT_TEXT, self.set_value )
		self.ThingStateSpawnLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingStateSpawn.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingStateSpawn.Bind( wx.EVT_TEXT, self.set_state )
		self.ThingStateSpawnName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingStateSpawnName.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingStateSpawnName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingStateSpawnName.Bind( wx.EVT_LEFT_UP, self.goto_state_event )
		self.ThingStateSpawnName.Bind( wx.EVT_RIGHT_UP, self.preview_state )
		self.ThingStateSpawnSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.ThingStateWalkLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingStateWalk.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingStateWalk.Bind( wx.EVT_TEXT, self.set_state )
		self.ThingStateWalkName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingStateWalkName.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingStateWalkName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingStateWalkName.Bind( wx.EVT_LEFT_UP, self.goto_state_event )
		self.ThingStateWalkName.Bind( wx.EVT_RIGHT_UP, self.preview_state )
		self.ThingStateWalkSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.ThingStatePainLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingStatePain.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingStatePain.Bind( wx.EVT_TEXT, self.set_state )
		self.ThingStatePainName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingStatePainName.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingStatePainName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingStatePainName.Bind( wx.EVT_LEFT_UP, self.goto_state_event )
		self.ThingStatePainName.Bind( wx.EVT_RIGHT_UP, self.preview_state )
		self.ThingStatePainSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.ThingStateMeleeLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingStateMelee.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingStateMelee.Bind( wx.EVT_TEXT, self.set_state )
		self.ThingStateMeleeName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingStateMeleeName.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingStateMeleeName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingStateMeleeName.Bind( wx.EVT_LEFT_UP, self.goto_state_event )
		self.ThingStateMeleeName.Bind( wx.EVT_RIGHT_UP, self.preview_state )
		self.ThingStateMeleeSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.ThingStateAttackLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingStateAttack.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingStateAttack.Bind( wx.EVT_TEXT, self.set_state )
		self.ThingStateAttackName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingStateAttackName.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingStateAttackName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingStateAttackName.Bind( wx.EVT_LEFT_UP, self.goto_state_event )
		self.ThingStateAttackName.Bind( wx.EVT_RIGHT_UP, self.preview_state )
		self.ThingStateAttackSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.ThingStateDeathLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingStateDeath.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingStateDeath.Bind( wx.EVT_TEXT, self.set_state )
		self.ThingStateDeathName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingStateDeathName.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingStateDeathName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingStateDeathName.Bind( wx.EVT_LEFT_UP, self.goto_state_event )
		self.ThingStateDeathName.Bind( wx.EVT_RIGHT_UP, self.preview_state )
		self.ThingStateDeathSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.ThingStateExplodeLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingStateExplode.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingStateExplode.Bind( wx.EVT_TEXT, self.set_state )
		self.ThingStateExplodeName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingStateExplodeName.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingStateExplodeName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingStateExplodeName.Bind( wx.EVT_LEFT_UP, self.goto_state_event )
		self.ThingStateExplodeName.Bind( wx.EVT_RIGHT_UP, self.preview_state )
		self.ThingStateExplodeSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.ThingStateRaiseLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingStateRaise.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingStateRaise.Bind( wx.EVT_TEXT, self.set_state )
		self.ThingStateRaiseName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingStateRaiseName.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingStateRaiseName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingStateRaiseName.Bind( wx.EVT_LEFT_UP, self.goto_state_event )
		self.ThingStateRaiseName.Bind( wx.EVT_RIGHT_UP, self.preview_state )
		self.ThingStateRaiseSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.ThingStateCrashLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingStateCrash.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingStateCrash.Bind( wx.EVT_TEXT, self.set_state )
		self.ThingStateCrashName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingStateCrashName.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingStateCrashName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingStateCrashName.Bind( wx.EVT_LEFT_UP, self.goto_state_event )
		self.ThingStateCrashName.Bind( wx.EVT_RIGHT_UP, self.preview_state )
		self.ThingStateCrashSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.ThingStateFreezeLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingStateFreeze.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingStateFreeze.Bind( wx.EVT_TEXT, self.set_state )
		self.ThingStateFreezeName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingStateFreezeName.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingStateFreezeName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingStateFreezeName.Bind( wx.EVT_LEFT_UP, self.goto_state_event )
		self.ThingStateFreezeName.Bind( wx.EVT_RIGHT_UP, self.preview_state )
		self.ThingStateFreezeSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.ThingStateBurnLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingStateBurn.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingStateBurn.Bind( wx.EVT_TEXT, self.set_state )
		self.ThingStateBurnName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingStateBurnName.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingStateBurnName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingStateBurnName.Bind( wx.EVT_LEFT_UP, self.goto_state_event )
		self.ThingStateBurnName.Bind( wx.EVT_RIGHT_UP, self.preview_state )
		self.ThingStateBurnSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.ThingSoundAlertLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingSoundAlert.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingSoundAlert.Bind( wx.EVT_TEXT, self.set_sound )
		self.ThingSoundAlertName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingSoundAlertName.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingSoundAlertName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingSoundAlertName.Bind( wx.EVT_LEFT_UP, self.goto_sound_event )
		self.ThingSoundAlertName.Bind( wx.EVT_RIGHT_UP, self.sound_play )
		self.ThingSoundAlertSet.Bind( wx.EVT_BUTTON, self.set_sound_external )
		self.ThingSoundAttackLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingSoundAttack.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingSoundAttack.Bind( wx.EVT_TEXT, self.set_sound )
		self.ThingSoundAttackName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingSoundAttackName.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingSoundAttackName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingSoundAttackName.Bind( wx.EVT_LEFT_UP, self.goto_sound_event )
		self.ThingSoundAttackName.Bind( wx.EVT_RIGHT_UP, self.sound_play )
		self.ThingSoundAttackSet.Bind( wx.EVT_BUTTON, self.set_sound_external )
		self.ThingSoundPainLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingSoundPain.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingSoundPain.Bind( wx.EVT_TEXT, self.set_sound )
		self.ThingSoundPainName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingSoundPainName.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingSoundPainName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingSoundPainName.Bind( wx.EVT_LEFT_UP, self.goto_sound_event )
		self.ThingSoundPainName.Bind( wx.EVT_RIGHT_UP, self.sound_play )
		self.ThingSoundPainSet.Bind( wx.EVT_BUTTON, self.set_sound_external )
		self.ThingSoundDeathLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingSoundDeath.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingSoundDeath.Bind( wx.EVT_TEXT, self.set_sound )
		self.ThingSoundDeathName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingSoundDeathName.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingSoundDeathName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingSoundDeathName.Bind( wx.EVT_LEFT_UP, self.goto_sound_event )
		self.ThingSoundDeathName.Bind( wx.EVT_RIGHT_UP, self.sound_play )
		self.ThingSoundDeathSet.Bind( wx.EVT_BUTTON, self.set_sound_external )
		self.ThingSoundActiveLabel.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingSoundActive.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.ThingSoundActive.Bind( wx.EVT_TEXT, self.set_sound )
		self.ThingSoundActiveName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.ThingSoundActiveName.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ThingSoundActiveName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.ThingSoundActiveName.Bind( wx.EVT_LEFT_UP, self.goto_sound_event )
		self.ThingSoundActiveName.Bind( wx.EVT_RIGHT_UP, self.sound_play )
		self.ThingSoundActiveSet.Bind( wx.EVT_BUTTON, self.set_sound_external )
		self.ThingFlags.Bind( wx.EVT_CHECKLISTBOX, self.set_flags )
		self.ThingFlags.Bind( wx.EVT_MOTION, self.set_flag_tooltip )
		self.ButtonRestore.Bind( wx.EVT_BUTTON, self.thing_restore )
		self.ThingList.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.thing_rename )
		self.ThingList.Bind( wx.EVT_LIST_ITEM_RIGHT_CLICK, self.thing_context )
		self.ThingList.Bind( wx.EVT_LIST_ITEM_SELECTED, self.thing_select )
		self.ThingList.Bind( wx.EVT_SIZE, self.thinglist_resize )
		self.Bind( wx.EVT_MENU, self.thing_context_copy, id = self.ThingContextCopy.GetId() )
		self.Bind( wx.EVT_MENU, self.thing_context_paste, id = self.ThingContextPaste.GetId() )
		self.Bind( wx.EVT_MENU, self.thing_context_clear, id = self.ThingContextClear.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def dummy( self, event ):
		pass

	def focus_text( self, event ):
		pass

	def set_value( self, event ):
		pass








	def set_renderstyle( self, event ):
		pass









































































	def set_state( self, event ):
		pass

	def enter_state( self, event ):
		pass


	def leave_state( self, event ):
		pass

	def goto_state_event( self, event ):
		pass

	def preview_state( self, event ):
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

	def thing_restore( self, event ):
		pass

	def thing_rename( self, event ):
		pass

	def thing_context( self, event ):
		pass

	def thing_select( self, event ):
		pass

	def thinglist_resize( self, event ):
		pass

	def thing_context_copy( self, event ):
		pass

	def thing_context_paste( self, event ):
		pass

	def thing_context_clear( self, event ):
		pass


###########################################################################
## Class StatesFrameBase
###########################################################################

class StatesFrameBase ( wx.MDIChildFrame ):

	def __init__( self, parent ):
		wx.MDIChildFrame.__init__ ( self, parent, id = FRAME_STATES, title = u"States", pos = wx.DefaultPosition, size = wx.Size( 1024,768 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU|wx.WANTS_CHARS )

		self.SetSizeHints( wx.Size( 1024,768 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		SizerMain = wx.BoxSizer( wx.HORIZONTAL )

		SizerSidebar = wx.BoxSizer( wx.VERTICAL )

		self.SpritePreview = spritepreview.SpritePreview(self)
		self.SpritePreview.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )
		self.SpritePreview.SetMinSize( wx.Size( 400,360 ) )

		SizerSidebar.Add( self.SpritePreview, 0, wx.EXPAND, 5 )

		SizerProps = wx.BoxSizer( wx.VERTICAL )

		SizerPropSprite = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText39 = wx.StaticText( self, wx.ID_ANY, u"Sprite", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText39.Wrap( -1 )

		SizerPropSprite.Add( self.m_staticText39, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.SpriteIndex = wx.TextCtrl( self, STATES_SPRITE, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.SpriteIndex.SetMaxLength( 3 )
		SizerPropSprite.Add( self.SpriteIndex, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.SpriteName = wx.StaticText( self, wx.ID_ANY, u"TROO", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.SpriteName.Wrap( -1 )

		self.SpriteName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.SpriteName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		SizerPropSprite.Add( self.SpriteName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.SpriteSelect = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.SpriteSelect.SetMinSize( wx.Size( 40,28 ) )

		SizerPropSprite.Add( self.SpriteSelect, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )


		SizerProps.Add( SizerPropSprite, 0, wx.EXPAND, 5 )

		SizerPropFrame = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText391 = wx.StaticText( self, wx.ID_ANY, u"Frame", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText391.Wrap( -1 )

		SizerPropFrame.Add( self.m_staticText391, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.FrameIndex = wx.TextCtrl( self, STATES_FRAME, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		SizerPropFrame.Add( self.FrameIndex, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.LEFT|wx.TOP, 3 )

		self.FrameIndexSpinner = wx.SpinButton( self, STATES_FRAMESPIN, wx.DefaultPosition, wx.Size( 17,25 ), 0 )
		SizerPropFrame.Add( self.FrameIndexSpinner, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 3 )

		self.AlwaysLit = wx.CheckBox( self, STATES_LIT, u" Always lit", wx.DefaultPosition, wx.DefaultSize, 0 )
		SizerPropFrame.Add( self.AlwaysLit, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 6 )


		SizerProps.Add( SizerPropFrame, 0, wx.EXPAND, 5 )


		SizerProps.Add( ( 0, 9), 0, wx.EXPAND, 5 )

		SizerPropNext = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3911 = wx.StaticText( self, wx.ID_ANY, u"Next state", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText3911.Wrap( -1 )

		SizerPropNext.Add( self.m_staticText3911, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.NextStateIndex = wx.TextCtrl( self, STATES_NEXT, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.NextStateIndex.SetMaxLength( 4 )
		SizerPropNext.Add( self.NextStateIndex, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.NextStateName = wx.StaticText( self, wx.ID_ANY, u"PLAYD", wx.DefaultPosition, wx.Size( 70,-1 ), wx.ST_NO_AUTORESIZE )
		self.NextStateName.Wrap( -1 )

		self.NextStateName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.NextStateName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		SizerPropNext.Add( self.NextStateName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )


		SizerProps.Add( SizerPropNext, 0, wx.EXPAND, 5 )


		SizerProps.Add( ( 0, 9), 0, wx.EXPAND, 5 )

		SizerPropDuration = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3912 = wx.StaticText( self, wx.ID_ANY, u"Duration", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText3912.Wrap( -1 )

		SizerPropDuration.Add( self.m_staticText3912, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.Duration = wx.TextCtrl( self, STATES_DURATION, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.Duration.SetMaxLength( 4 )
		SizerPropDuration.Add( self.Duration, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.ticks = wx.StaticText( self, wx.ID_ANY, u"ticks", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ticks.Wrap( -1 )

		SizerPropDuration.Add( self.ticks, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )


		SizerProps.Add( SizerPropDuration, 0, wx.EXPAND, 5 )


		SizerProps.Add( ( 0, 9), 0, wx.EXPAND, 6 )

		SizerPropAction = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText54 = wx.StaticText( self, wx.ID_ANY, u"Action", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText54.Wrap( -1 )

		SizerPropAction.Add( self.m_staticText54, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		ActionChoices = []
		self.Action = wx.Choice( self, STATES_ACTION, wx.DefaultPosition, wx.Size( -1,-1 ), ActionChoices, wx.CB_SORT )
		self.Action.SetSelection( 0 )
		self.Action.SetMinSize( wx.Size( 180,-1 ) )

		SizerPropAction.Add( self.Action, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )


		SizerProps.Add( SizerPropAction, 0, wx.EXPAND, 5 )

		SizerPropUnused1 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText541 = wx.StaticText( self, STATES_LABEL_UNUSED1, u"Param 1", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText541.Wrap( -1 )

		SizerPropUnused1.Add( self.m_staticText541, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.Unused1 = wx.TextCtrl( self, STATES_UNUSED1, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.Unused1.SetMaxLength( 9 )
		SizerPropUnused1.Add( self.Unused1, 0, wx.ALL, 3 )


		SizerProps.Add( SizerPropUnused1, 0, wx.EXPAND, 5 )

		SizerPropUnused2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText5411 = wx.StaticText( self, STATES_LABEL_UNUSED2, u"Param 2", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText5411.Wrap( -1 )

		SizerPropUnused2.Add( self.m_staticText5411, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.Unused2 = wx.TextCtrl( self, STATES_UNUSED2, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.Unused2.SetMaxLength( 9 )
		SizerPropUnused2.Add( self.Unused2, 0, wx.ALL, 3 )


		SizerProps.Add( SizerPropUnused2, 0, wx.EXPAND, 5 )

		bSizer5212121 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText54111 = wx.StaticText( self, STATES_LABEL_ARG1, u"Arg 1", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText54111.Wrap( -1 )

		bSizer5212121.Add( self.m_staticText54111, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.Arg1 = wx.TextCtrl( self, STATES_ARG1, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.Arg1.SetMaxLength( 9 )
		bSizer5212121.Add( self.Arg1, 0, wx.ALL, 3 )


		SizerProps.Add( bSizer5212121, 0, wx.EXPAND, 5 )

		bSizer5212122 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText54112 = wx.StaticText( self, STATES_LABEL_ARG2, u"Arg 2", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText54112.Wrap( -1 )

		bSizer5212122.Add( self.m_staticText54112, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.Arg2 = wx.TextCtrl( self, STATES_ARG2, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.Arg2.SetMaxLength( 9 )
		bSizer5212122.Add( self.Arg2, 0, wx.ALL, 3 )


		SizerProps.Add( bSizer5212122, 0, wx.EXPAND, 5 )

		bSizer5212123 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText54113 = wx.StaticText( self, STATES_LABEL_ARG3, u"Arg 3", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText54113.Wrap( -1 )

		bSizer5212123.Add( self.m_staticText54113, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.Arg3 = wx.TextCtrl( self, STATES_ARG3, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.Arg3.SetMaxLength( 9 )
		bSizer5212123.Add( self.Arg3, 0, wx.ALL, 3 )


		SizerProps.Add( bSizer5212123, 0, wx.EXPAND, 5 )

		bSizer5212124 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText54114 = wx.StaticText( self, STATES_LABEL_ARG4, u"Arg 4", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText54114.Wrap( -1 )

		bSizer5212124.Add( self.m_staticText54114, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.Arg4 = wx.TextCtrl( self, STATES_ARG4, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.Arg4.SetMaxLength( 9 )
		bSizer5212124.Add( self.Arg4, 0, wx.ALL, 3 )


		SizerProps.Add( bSizer5212124, 0, wx.EXPAND, 5 )

		bSizer5212125 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText54115 = wx.StaticText( self, STATES_LABEL_ARG5, u"Arg 5", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText54115.Wrap( -1 )

		bSizer5212125.Add( self.m_staticText54115, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.Arg5 = wx.TextCtrl( self, STATES_ARG5, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.Arg5.SetMaxLength( 9 )
		bSizer5212125.Add( self.Arg5, 0, wx.ALL, 3 )


		SizerProps.Add( bSizer5212125, 0, wx.EXPAND, 5 )

		bSizer5212126 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText54116 = wx.StaticText( self, STATES_LABEL_ARG6, u"Arg 6", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText54116.Wrap( -1 )

		bSizer5212126.Add( self.m_staticText54116, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.Arg6 = wx.TextCtrl( self, STATES_ARG6, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.Arg6.SetMaxLength( 9 )
		bSizer5212126.Add( self.Arg6, 0, wx.ALL, 3 )


		SizerProps.Add( bSizer5212126, 0, wx.EXPAND, 5 )

		bSizer5212127 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText54117 = wx.StaticText( self, STATES_LABEL_ARG7, u"Arg 7", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText54117.Wrap( -1 )

		bSizer5212127.Add( self.m_staticText54117, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.Arg7 = wx.TextCtrl( self, STATES_ARG7, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.Arg7.SetMaxLength( 9 )
		bSizer5212127.Add( self.Arg7, 0, wx.ALL, 3 )


		SizerProps.Add( bSizer5212127, 0, wx.EXPAND, 5 )

		bSizer5212128 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText54118 = wx.StaticText( self, STATES_LABEL_ARG8, u"Arg 8", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText54118.Wrap( -1 )

		bSizer5212128.Add( self.m_staticText54118, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.Arg8 = wx.TextCtrl( self, STATES_ARG8, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.Arg8.SetMaxLength( 9 )
		bSizer5212128.Add( self.Arg8, 0, wx.ALL, 3 )


		SizerProps.Add( bSizer5212128, 0, wx.EXPAND, 5 )

		bSizer5212129 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText54119 = wx.StaticText( self, STATES_LABEL_ARG9, u"Arg 9", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText54119.Wrap( -1 )

		bSizer5212129.Add( self.m_staticText54119, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.Arg9 = wx.TextCtrl( self, STATES_ARG9, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.Arg9.SetMaxLength( 9 )
		bSizer5212129.Add( self.Arg9, 0, wx.ALL, 3 )


		SizerProps.Add( bSizer5212129, 0, wx.EXPAND, 5 )


		SizerProps.Add( ( 0, 9), 0, wx.EXPAND, 5 )

		self.Restore = wx.Button( self, wx.ID_ANY, u"Restore", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.Restore.SetMinSize( wx.Size( -1,36 ) )

		SizerProps.Add( self.Restore, 0, wx.EXPAND|wx.TOP, 3 )


		SizerSidebar.Add( SizerProps, 1, wx.ALL|wx.EXPAND, 6 )


		SizerMain.Add( SizerSidebar, 0, wx.EXPAND, 5 )

		SizerStates = wx.BoxSizer( wx.VERTICAL )

		self.m_panel61 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer140 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText45 = wx.StaticText( self.m_panel61, wx.ID_ANY, u"Filter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )

		self.m_staticText45.SetMinSize( wx.Size( 50,-1 ) )

		bSizer140.Add( self.m_staticText45, 0, wx.ALIGN_CENTER_VERTICAL, 0 )

		FilterChoices = []
		self.Filter = wx.Choice( self.m_panel61, STATES_FILTER, wx.DefaultPosition, wx.DefaultSize, FilterChoices, 0 )
		self.Filter.SetSelection( 0 )
		self.Filter.SetMinSize( wx.Size( 300,-1 ) )

		bSizer140.Add( self.Filter, 0, wx.RIGHT, 6 )

		self.FilterTools = wx.ToolBar( self.m_panel61, STATES_FILTERTOOLS, wx.DefaultPosition, wx.DefaultSize, wx.TB_FLAT|wx.TB_HORIZONTAL|wx.TB_NODIVIDER )
		self.FilterTools.SetToolBitmapSize( wx.Size( 18,18 ) )
		self.FilterTools.SetToolSeparation( 0 )
		self.FilterTools.SetMargins( wx.Size( 0,0 ) )
		self.FilterTools.SetToolPacking( 0 )
		self.FilterToolRefresh = self.FilterTools.AddLabelTool( STATES_FILTERTOOLS_REFRESH, u"tool", wx.Bitmap( u"res/icon-refresh.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Refreshes the state list.", wx.EmptyString, None )

		self.FilterTools.Realize()

		bSizer140.Add( self.FilterTools, 0, wx.ALIGN_CENTER_VERTICAL, 0 )


		self.m_panel61.SetSizer( bSizer140 )
		self.m_panel61.Layout()
		bSizer140.Fit( self.m_panel61 )
		SizerStates.Add( self.m_panel61, 0, wx.ALL, 6 )

		self.StateList = StateList( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_REPORT|wx.BORDER_NONE )
		self.StateList.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		SizerStates.Add( self.StateList, 1, wx.EXPAND, 5 )


		SizerMain.Add( SizerStates, 1, wx.EXPAND, 5 )


		self.SetSizer( SizerMain )
		self.Layout()
		self.StateContext = wx.Menu()
		self.StateContextCopy = wx.MenuItem( self.StateContext, wx.ID_ANY, u"Copy"+ u"\t" + u"Ctrl+C", wx.EmptyString, wx.ITEM_NORMAL )
		self.StateContext.Append( self.StateContextCopy )

		self.StateContextPaste = wx.MenuItem( self.StateContext, wx.ID_ANY, u"Paste"+ u"\t" + u"Ctrl+V", wx.EmptyString, wx.ITEM_NORMAL )
		self.StateContext.Append( self.StateContextPaste )

		self.StateContextClear = wx.MenuItem( self.StateContext, wx.ID_ANY, u"Clear", wx.EmptyString, wx.ITEM_NORMAL )
		self.StateContext.Append( self.StateContextClear )

		self.StateContext.AppendSeparator()

		self.StateContextLink = wx.MenuItem( self.StateContext, wx.ID_ANY, u"Link"+ u"\t" + u"L", wx.EmptyString, wx.ITEM_NORMAL )
		self.StateContext.Append( self.StateContextLink )

		self.StateContextLinkLoop = wx.MenuItem( self.StateContext, wx.ID_ANY, u"Link (loop)"+ u"\t" + u"Shift+L", wx.EmptyString, wx.ITEM_NORMAL )
		self.StateContext.Append( self.StateContextLinkLoop )

		self.StateContext.AppendSeparator()

		self.StateContextPreview = wx.MenuItem( self.StateContext, wx.ID_ANY, u"Preview"+ u"\t" + u"~", wx.EmptyString, wx.ITEM_NORMAL )
		self.StateContext.Append( self.StateContextPreview )



		# Connect Events
		self.m_staticText39.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.SpriteIndex.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.SpriteIndex.Bind( wx.EVT_TEXT, self.set_value )
		self.SpriteName.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.SpriteSelect.Bind( wx.EVT_BUTTON, self.select_sprite )
		self.m_staticText391.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.FrameIndex.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.FrameIndex.Bind( wx.EVT_TEXT, self.set_frame )
		self.FrameIndexSpinner.Bind( wx.EVT_SPIN_DOWN, self.frame_spin_down )
		self.FrameIndexSpinner.Bind( wx.EVT_SPIN_UP, self.frame_spin_up )
		self.AlwaysLit.Bind( wx.EVT_CHECKBOX, self.set_lit )
		self.m_staticText3911.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.NextStateIndex.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.NextStateIndex.Bind( wx.EVT_TEXT, self.set_value )
		self.NextStateName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.NextStateName.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.NextStateName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.NextStateName.Bind( wx.EVT_LEFT_UP, self.goto_next_state )
		self.m_staticText3912.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.Duration.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Duration.Bind( wx.EVT_TEXT, self.set_value )
		self.ticks.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.m_staticText54.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.Action.Bind( wx.EVT_CHOICE, self.set_action )
		self.m_staticText541.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.Unused1.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Unused1.Bind( wx.EVT_TEXT, self.set_value )
		self.m_staticText5411.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.Unused2.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Unused2.Bind( wx.EVT_TEXT, self.set_value )
		self.m_staticText54111.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.Arg1.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Arg1.Bind( wx.EVT_TEXT, self.set_value )
		self.m_staticText54112.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.Arg2.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Arg2.Bind( wx.EVT_TEXT, self.set_value )
		self.m_staticText54113.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.Arg3.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Arg3.Bind( wx.EVT_TEXT, self.set_value )
		self.m_staticText54114.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.Arg4.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Arg4.Bind( wx.EVT_TEXT, self.set_value )
		self.m_staticText54115.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.Arg5.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Arg5.Bind( wx.EVT_TEXT, self.set_value )
		self.m_staticText54116.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.Arg6.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Arg6.Bind( wx.EVT_TEXT, self.set_value )
		self.m_staticText54117.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.Arg7.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Arg7.Bind( wx.EVT_TEXT, self.set_value )
		self.m_staticText54118.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.Arg8.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Arg8.Bind( wx.EVT_TEXT, self.set_value )
		self.m_staticText54119.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.Arg9.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Arg9.Bind( wx.EVT_TEXT, self.set_value )
		self.Restore.Bind( wx.EVT_BUTTON, self.state_restore )
		self.m_staticText45.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.Filter.Bind( wx.EVT_CHOICE, self.filter_select )
		self.Filter.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.Bind( wx.EVT_TOOL, self.filter_select, id = self.FilterToolRefresh.GetId() )
		self.StateList.Bind( wx.EVT_KEY_DOWN, self.statelist_key_down )
		self.StateList.Bind( wx.EVT_LEFT_DOWN, self.state_link )
		self.StateList.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.select_sprite )
		self.StateList.Bind( wx.EVT_LIST_ITEM_RIGHT_CLICK, self.state_context )
		self.Bind( wx.EVT_MENU, self.state_context_copy, id = self.StateContextCopy.GetId() )
		self.Bind( wx.EVT_MENU, self.state_context_paste, id = self.StateContextPaste.GetId() )
		self.Bind( wx.EVT_MENU, self.state_context_clear, id = self.StateContextClear.GetId() )
		self.Bind( wx.EVT_MENU, self.state_context_link, id = self.StateContextLink.GetId() )
		self.Bind( wx.EVT_MENU, self.state_context_link_loop, id = self.StateContextLinkLoop.GetId() )
		self.Bind( wx.EVT_MENU, self.state_context_preview, id = self.StateContextPreview.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def dummy( self, event ):
		pass

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



	def statelist_key_down( self, event ):
		pass

	def state_link( self, event ):
		pass


	def state_context( self, event ):
		pass

	def state_context_copy( self, event ):
		pass

	def state_context_paste( self, event ):
		pass

	def state_context_clear( self, event ):
		pass

	def state_context_link( self, event ):
		pass

	def state_context_link_loop( self, event ):
		pass

	def state_context_preview( self, event ):
		pass


###########################################################################
## Class SoundsFrameBase
###########################################################################

class SoundsFrameBase ( wx.MDIChildFrame ):

	def __init__( self, parent ):
		wx.MDIChildFrame.__init__ ( self, parent, id = FRAME_SOUNDS, title = u"Sounds", pos = wx.DefaultPosition, size = wx.Size( 430,480 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU )

		self.SetSizeHints( wx.Size( 430,480 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel43 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer42 = wx.BoxSizer( wx.VERTICAL )

		bSizer52 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText39 = wx.StaticText( self.m_panel43, wx.ID_ANY, u"Priority", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.m_staticText39.Wrap( -1 )

		bSizer52.Add( self.m_staticText39, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.Priority = wx.TextCtrl( self.m_panel43, SOUNDS_PRIORITY, wx.EmptyString, wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.Priority.SetMaxLength( 10 )
		bSizer52.Add( self.Priority, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.LEFT|wx.TOP, 3 )

		self.PrioritySpinner = wx.SpinButton( self.m_panel43, SOUNDS_PRIORITYSPIN, wx.DefaultPosition, wx.Size( 17,21 ), 0 )
		bSizer52.Add( self.PrioritySpinner, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.RIGHT|wx.TOP, 3 )


		bSizer42.Add( bSizer52, 0, wx.EXPAND, 5 )

		bSizer521 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText391 = wx.StaticText( self.m_panel43, wx.ID_ANY, u"Singular", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.m_staticText391.Wrap( -1 )

		bSizer521.Add( self.m_staticText391, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.Singular = wx.CheckBox( self.m_panel43, SOUNDS_SINGULAR, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer521.Add( self.Singular, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 6 )


		bSizer42.Add( bSizer521, 0, wx.EXPAND, 5 )


		bSizer42.Add( ( 0, 12), 0, wx.EXPAND, 0 )

		self.Restore = wx.Button( self.m_panel43, SOUNDS_RESTORE, u"Restore", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.Restore.SetMinSize( wx.Size( -1,36 ) )

		bSizer42.Add( self.Restore, 0, wx.EXPAND|wx.TOP, 3 )


		self.m_panel43.SetSizer( bSizer42 )
		self.m_panel43.Layout()
		bSizer42.Fit( self.m_panel43 )
		bSizer41.Add( self.m_panel43, 0, wx.ALL, 6 )

		self.SoundList = wx.ListCtrl( self, SOUNDS_LIST, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_NO_SORT_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.BORDER_NONE )
		self.SoundList.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer41.Add( self.SoundList, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer41 )
		self.Layout()

		# Connect Events
		self.m_staticText39.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.Priority.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Priority.Bind( wx.EVT_TEXT, self.set_priority )
		self.PrioritySpinner.Bind( wx.EVT_SPIN_DOWN, self.priority_spin_down )
		self.PrioritySpinner.Bind( wx.EVT_SPIN_UP, self.priority_spin_up )
		self.m_staticText391.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.Singular.Bind( wx.EVT_CHECKBOX, self.set_singular )
		self.Restore.Bind( wx.EVT_BUTTON, self.sound_restore )
		self.SoundList.Bind( wx.EVT_LIST_ITEM_DESELECTED, self.sound_deselect )
		self.SoundList.Bind( wx.EVT_LIST_ITEM_RIGHT_CLICK, self.sound_play )
		self.SoundList.Bind( wx.EVT_LIST_ITEM_SELECTED, self.sound_select )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def dummy( self, event ):
		pass

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

		self.SetSizeHints( wx.Size( 640,480 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )

		self.StringList = wx.ListCtrl( self, STRINGS_LIST, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_NO_SORT_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.BORDER_NONE )
		self.StringList.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer41.Add( self.StringList, 1, wx.EXPAND, 5 )

		bSizer158 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer158.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.Restore = wx.Button( self, STRINGS_RESTORE, u"Restore", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Restore.SetMinSize( wx.Size( 120,36 ) )

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
		wx.MDIChildFrame.__init__ ( self, parent, id = FRAME_WEAPONS, title = u"Weapons", pos = wx.DefaultPosition, size = wx.Size( 560,472 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 560,472 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel44 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer93 = wx.BoxSizer( wx.VERTICAL )

		bSizer139 = wx.BoxSizer( wx.VERTICAL )

		self.PanelAmmoType = wx.Panel( self.m_panel44, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerAmmoType = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText88 = wx.StaticText( self.PanelAmmoType, wx.ID_ANY, u"Ammo type", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText88.Wrap( -1 )

		SizerAmmoType.Add( self.m_staticText88, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		AmmoTypeChoices = []
		self.AmmoType = wx.Choice( self.PanelAmmoType, WEAPON_AMMOTYPE, wx.DefaultPosition, wx.DefaultSize, AmmoTypeChoices, 0 )
		self.AmmoType.SetSelection( 0 )
		SizerAmmoType.Add( self.AmmoType, 1, wx.ALL, 3 )


		self.PanelAmmoType.SetSizer( SizerAmmoType )
		self.PanelAmmoType.Layout()
		SizerAmmoType.Fit( self.PanelAmmoType )
		bSizer139.Add( self.PanelAmmoType, 0, wx.EXPAND, 0 )

		self.PanelAmmoPerUse = wx.Panel( self.m_panel44, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerAmmoPerUse = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText88141 = wx.StaticText( self.PanelAmmoPerUse, wx.ID_ANY, u"Ammo per use", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText88141.Wrap( -1 )

		SizerAmmoPerUse.Add( self.m_staticText88141, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		bSizer12441 = wx.BoxSizer( wx.HORIZONTAL )

		self.AmmoUse = wx.TextCtrl( self.PanelAmmoPerUse, WEAPON_VAL_AMMO_USE, u"2", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.AmmoUse.SetMaxLength( 4 )
		bSizer12441.Add( self.AmmoUse, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )


		SizerAmmoPerUse.Add( bSizer12441, 1, wx.EXPAND, 5 )


		self.PanelAmmoPerUse.SetSizer( SizerAmmoPerUse )
		self.PanelAmmoPerUse.Layout()
		SizerAmmoPerUse.Fit( self.PanelAmmoPerUse )
		bSizer139.Add( self.PanelAmmoPerUse, 0, wx.EXPAND, 0 )

		self.PanelAmmoNeeded = wx.Panel( self.m_panel44, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerAmmoNeeded = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText88142 = wx.StaticText( self.PanelAmmoNeeded, wx.ID_ANY, u"Ammo needed", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText88142.Wrap( -1 )

		SizerAmmoNeeded.Add( self.m_staticText88142, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		bSizer12442 = wx.BoxSizer( wx.HORIZONTAL )

		self.MinAmmo = wx.TextCtrl( self.PanelAmmoNeeded, WEAPON_VAL_MIN_AMMO, u"2", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.MinAmmo.SetMaxLength( 4 )
		bSizer12442.Add( self.MinAmmo, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )


		SizerAmmoNeeded.Add( bSizer12442, 1, wx.EXPAND, 5 )


		self.PanelAmmoNeeded.SetSizer( SizerAmmoNeeded )
		self.PanelAmmoNeeded.Layout()
		SizerAmmoNeeded.Fit( self.PanelAmmoNeeded )
		bSizer139.Add( self.PanelAmmoNeeded, 0, wx.EXPAND, 0 )

		self.PanelDecal = wx.Panel( self.m_panel44, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerDecal = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText88143 = wx.StaticText( self.PanelDecal, wx.ID_ANY, u"Decal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText88143.Wrap( -1 )

		SizerDecal.Add( self.m_staticText88143, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		bSizer12443 = wx.BoxSizer( wx.HORIZONTAL )

		self.Decal = wx.TextCtrl( self.PanelDecal, WEAPON_VAL_DECAL, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer12443.Add( self.Decal, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )


		SizerDecal.Add( bSizer12443, 1, wx.EXPAND, 5 )


		self.PanelDecal.SetSizer( SizerDecal )
		self.PanelDecal.Layout()
		SizerDecal.Fit( self.PanelDecal )
		bSizer139.Add( self.PanelDecal, 0, wx.EXPAND, 0 )


		bSizer139.Add( ( 0, 16), 0, wx.EXPAND, 0 )

		self.PanelStateLower = wx.Panel( self.m_panel44, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerStateLower = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText881 = wx.StaticText( self.PanelStateLower, wx.ID_ANY, u"Lower state", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText881.Wrap( -1 )

		SizerStateLower.Add( self.m_staticText881, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		bSizer124 = wx.BoxSizer( wx.HORIZONTAL )

		self.WeaponStateSelect = wx.TextCtrl( self.PanelStateLower, WEAPON_STATE_SELECT, u"318", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.WeaponStateSelect.SetMaxLength( 4 )
		bSizer124.Add( self.WeaponStateSelect, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.WeaponStateSelectName = wx.StaticText( self.PanelStateLower, WEAPON_STATENAME_SELECT, u"TROOA", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.WeaponStateSelectName.Wrap( -1 )

		self.WeaponStateSelectName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.WeaponStateSelectName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer124.Add( self.WeaponStateSelectName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.WeaponStateSelectSet = wx.Button( self.PanelStateLower, WEAPON_STATESET_SELECT, u"<", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.WeaponStateSelectSet.SetMinSize( wx.Size( 30,30 ) )

		bSizer124.Add( self.WeaponStateSelectSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )


		SizerStateLower.Add( bSizer124, 1, wx.EXPAND, 5 )


		self.PanelStateLower.SetSizer( SizerStateLower )
		self.PanelStateLower.Layout()
		SizerStateLower.Fit( self.PanelStateLower )
		bSizer139.Add( self.PanelStateLower, 0, wx.EXPAND, 0 )

		self.PanelStateRaise = wx.Panel( self.m_panel44, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerStateRaise = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText8811 = wx.StaticText( self.PanelStateRaise, wx.ID_ANY, u"Raise state", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8811.Wrap( -1 )

		SizerStateRaise.Add( self.m_staticText8811, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		bSizer1241 = wx.BoxSizer( wx.HORIZONTAL )

		self.WeaponStateDeselect = wx.TextCtrl( self.PanelStateRaise, WEAPON_STATE_DESELECT, u"318", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.WeaponStateDeselect.SetMaxLength( 4 )
		bSizer1241.Add( self.WeaponStateDeselect, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.WeaponStateDeselectName = wx.StaticText( self.PanelStateRaise, WEAPON_STATENAME_DESELECT, u"TROOA", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.WeaponStateDeselectName.Wrap( -1 )

		self.WeaponStateDeselectName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.WeaponStateDeselectName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer1241.Add( self.WeaponStateDeselectName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.WeaponStateDeselectSet = wx.Button( self.PanelStateRaise, WEAPON_STATESET_DESELECT, u"<", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.WeaponStateDeselectSet.SetMinSize( wx.Size( 30,30 ) )

		bSizer1241.Add( self.WeaponStateDeselectSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )


		SizerStateRaise.Add( bSizer1241, 1, wx.EXPAND, 5 )


		self.PanelStateRaise.SetSizer( SizerStateRaise )
		self.PanelStateRaise.Layout()
		SizerStateRaise.Fit( self.PanelStateRaise )
		bSizer139.Add( self.PanelStateRaise, 0, wx.EXPAND, 0 )

		self.PanelStateBob = wx.Panel( self.m_panel44, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerStateBob = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText8812 = wx.StaticText( self.PanelStateBob, wx.ID_ANY, u"Bob state", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8812.Wrap( -1 )

		SizerStateBob.Add( self.m_staticText8812, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		bSizer1242 = wx.BoxSizer( wx.HORIZONTAL )

		self.WeaponStateBob = wx.TextCtrl( self.PanelStateBob, WEAPON_STATE_BOB, u"318", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.WeaponStateBob.SetMaxLength( 4 )
		bSizer1242.Add( self.WeaponStateBob, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.WeaponStateBobName = wx.StaticText( self.PanelStateBob, WEAPON_STATENAME_BOB, u"TROOA", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.WeaponStateBobName.Wrap( -1 )

		self.WeaponStateBobName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.WeaponStateBobName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer1242.Add( self.WeaponStateBobName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.WeaponStateBobSet = wx.Button( self.PanelStateBob, WEAPON_STATESET_BOB, u"<", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.WeaponStateBobSet.SetMinSize( wx.Size( 30,30 ) )

		bSizer1242.Add( self.WeaponStateBobSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )


		SizerStateBob.Add( bSizer1242, 1, wx.EXPAND, 5 )


		self.PanelStateBob.SetSizer( SizerStateBob )
		self.PanelStateBob.Layout()
		SizerStateBob.Fit( self.PanelStateBob )
		bSizer139.Add( self.PanelStateBob, 0, wx.EXPAND, 0 )

		self.PanelStateFire = wx.Panel( self.m_panel44, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerStateFire = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText8813 = wx.StaticText( self.PanelStateFire, wx.ID_ANY, u"Fire state", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8813.Wrap( -1 )

		SizerStateFire.Add( self.m_staticText8813, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		bSizer1243 = wx.BoxSizer( wx.HORIZONTAL )

		self.WeaponStateFire = wx.TextCtrl( self.PanelStateFire, WEAPON_STATE_FIRE, u"318", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.WeaponStateFire.SetMaxLength( 4 )
		bSizer1243.Add( self.WeaponStateFire, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.WeaponStateFireName = wx.StaticText( self.PanelStateFire, WEAPON_STATENAME_FIRE, u"TROOA", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.WeaponStateFireName.Wrap( -1 )

		self.WeaponStateFireName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.WeaponStateFireName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer1243.Add( self.WeaponStateFireName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.WeaponStateFireSet = wx.Button( self.PanelStateFire, WEAPON_STATESET_FIRE, u"<", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.WeaponStateFireSet.SetMinSize( wx.Size( 30,30 ) )

		bSizer1243.Add( self.WeaponStateFireSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )


		SizerStateFire.Add( bSizer1243, 1, wx.EXPAND, 5 )


		self.PanelStateFire.SetSizer( SizerStateFire )
		self.PanelStateFire.Layout()
		SizerStateFire.Fit( self.PanelStateFire )
		bSizer139.Add( self.PanelStateFire, 0, wx.EXPAND, 0 )

		self.PanelStateMuzzle = wx.Panel( self.m_panel44, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerStateMuzzle = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText8814 = wx.StaticText( self.PanelStateMuzzle, wx.ID_ANY, u"Muzzle flash state", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8814.Wrap( -1 )

		SizerStateMuzzle.Add( self.m_staticText8814, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		bSizer1244 = wx.BoxSizer( wx.HORIZONTAL )

		self.WeaponStateMuzzle = wx.TextCtrl( self.PanelStateMuzzle, WEAPON_STATE_MUZZLE, u"318", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.WeaponStateMuzzle.SetMaxLength( 4 )
		bSizer1244.Add( self.WeaponStateMuzzle, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.WeaponStateMuzzleName = wx.StaticText( self.PanelStateMuzzle, WEAPON_STATENAME_MUZZLE, u"TROOA", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ST_NO_AUTORESIZE )
		self.WeaponStateMuzzleName.Wrap( -1 )

		self.WeaponStateMuzzleName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.WeaponStateMuzzleName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer1244.Add( self.WeaponStateMuzzleName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.WeaponStateMuzzleSet = wx.Button( self.PanelStateMuzzle, WEAPON_STATESET_MUZZLE, u"<", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.WeaponStateMuzzleSet.SetMinSize( wx.Size( 30,30 ) )

		bSizer1244.Add( self.WeaponStateMuzzleSet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )


		SizerStateMuzzle.Add( bSizer1244, 1, wx.EXPAND, 5 )


		self.PanelStateMuzzle.SetSizer( SizerStateMuzzle )
		self.PanelStateMuzzle.Layout()
		SizerStateMuzzle.Fit( self.PanelStateMuzzle )
		bSizer139.Add( self.PanelStateMuzzle, 0, wx.EXPAND, 0 )


		bSizer93.Add( bSizer139, 0, wx.ALL, 6 )


		bSizer93.Add( ( 0, 16), 1, wx.EXPAND, 0 )

		bSizer92 = wx.BoxSizer( wx.VERTICAL )

		self.Rename = wx.Button( self.m_panel44, WEAPON_RENAME, u"Rename", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Rename.SetMinSize( wx.Size( -1,36 ) )

		bSizer92.Add( self.Rename, 0, wx.ALL|wx.EXPAND, 3 )

		self.Restore = wx.Button( self.m_panel44, WEAPON_RESTORE, u"Restore", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Restore.SetMinSize( wx.Size( -1,36 ) )

		bSizer92.Add( self.Restore, 0, wx.ALL|wx.EXPAND, 3 )


		bSizer93.Add( bSizer92, 0, wx.ALL|wx.EXPAND, 3 )


		self.m_panel44.SetSizer( bSizer93 )
		self.m_panel44.Layout()
		bSizer93.Fit( self.m_panel44 )
		bSizer41.Add( self.m_panel44, 0, wx.EXPAND, 0 )

		self.WeaponList = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.BORDER_NONE )
		bSizer41.Add( self.WeaponList, 1, wx.ALL|wx.EXPAND, 0 )


		self.SetSizer( bSizer41 )
		self.Layout()

		# Connect Events
		self.m_staticText88.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.AmmoType.Bind( wx.EVT_CHOICE, self.set_ammo )
		self.m_staticText88141.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.AmmoUse.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.AmmoUse.Bind( wx.EVT_TEXT, self.set_value )
		self.m_staticText88142.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.MinAmmo.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.MinAmmo.Bind( wx.EVT_TEXT, self.set_value )
		self.m_staticText88143.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.Decal.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Decal.Bind( wx.EVT_TEXT, self.set_value )
		self.m_staticText881.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.WeaponStateSelect.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.WeaponStateSelect.Bind( wx.EVT_TEXT, self.set_state_index )
		self.WeaponStateSelectName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.WeaponStateSelectName.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.WeaponStateSelectName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.WeaponStateSelectName.Bind( wx.EVT_LEFT_UP, self.goto_state_event )
		self.WeaponStateSelectName.Bind( wx.EVT_RIGHT_UP, self.preview_state )
		self.WeaponStateSelectSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.m_staticText8811.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.WeaponStateDeselect.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.WeaponStateDeselect.Bind( wx.EVT_TEXT, self.set_state_index )
		self.WeaponStateDeselectName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.WeaponStateDeselectName.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.WeaponStateDeselectName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.WeaponStateDeselectName.Bind( wx.EVT_LEFT_UP, self.goto_state_event )
		self.WeaponStateDeselectName.Bind( wx.EVT_RIGHT_UP, self.preview_state )
		self.WeaponStateDeselectSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.m_staticText8812.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.WeaponStateBob.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.WeaponStateBob.Bind( wx.EVT_TEXT, self.set_state_index )
		self.WeaponStateBobName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.WeaponStateBobName.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.WeaponStateBobName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.WeaponStateBobName.Bind( wx.EVT_LEFT_UP, self.goto_state_event )
		self.WeaponStateBobName.Bind( wx.EVT_RIGHT_UP, self.preview_state )
		self.WeaponStateBobSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.m_staticText8813.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.WeaponStateFire.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.WeaponStateFire.Bind( wx.EVT_TEXT, self.set_state_index )
		self.WeaponStateFireName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.WeaponStateFireName.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.WeaponStateFireName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.WeaponStateFireName.Bind( wx.EVT_LEFT_UP, self.goto_state_event )
		self.WeaponStateFireName.Bind( wx.EVT_RIGHT_UP, self.preview_state )
		self.WeaponStateFireSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.m_staticText8814.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.WeaponStateMuzzle.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.WeaponStateMuzzle.Bind( wx.EVT_TEXT, self.set_state_index )
		self.WeaponStateMuzzleName.Bind( wx.EVT_ENTER_WINDOW, self.enter_state )
		self.WeaponStateMuzzleName.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.WeaponStateMuzzleName.Bind( wx.EVT_LEAVE_WINDOW, self.leave_state )
		self.WeaponStateMuzzleName.Bind( wx.EVT_LEFT_UP, self.goto_state_event )
		self.WeaponStateMuzzleName.Bind( wx.EVT_RIGHT_UP, self.preview_state )
		self.WeaponStateMuzzleSet.Bind( wx.EVT_BUTTON, self.set_state_external )
		self.Rename.Bind( wx.EVT_BUTTON, self.weapon_rename )
		self.Restore.Bind( wx.EVT_BUTTON, self.weapon_restore )
		self.WeaponList.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.weapon_rename )
		self.WeaponList.Bind( wx.EVT_LIST_ITEM_SELECTED, self.weapon_select )
		self.WeaponList.Bind( wx.EVT_SIZE, self.weaponlist_resize )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def dummy( self, event ):
		pass

	def set_ammo( self, event ):
		pass


	def focus_text( self, event ):
		pass

	def set_value( self, event ):
		pass









	def set_state_index( self, event ):
		pass

	def enter_state( self, event ):
		pass


	def leave_state( self, event ):
		pass

	def goto_state_event( self, event ):
		pass

	def preview_state( self, event ):
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

		self.SetSizeHints( wx.Size( 520,250 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel45 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer139 = wx.BoxSizer( wx.VERTICAL )

		gSizer1 = wx.GridSizer( 2, 2, 3, 12 )

		self.m_staticText88 = wx.StaticText( self.m_panel45, wx.ID_ANY, u"Maximum ammo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText88.Wrap( -1 )

		gSizer1.Add( self.m_staticText88, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.Maximum = wx.TextCtrl( self.m_panel45, AMMO_VAL_MAXIMUM, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.Maximum.SetMaxLength( 6 )
		gSizer1.Add( self.Maximum, 0, wx.ALL|wx.EXPAND, 3 )

		self.m_staticText881 = wx.StaticText( self.m_panel45, wx.ID_ANY, u"Pickup ammo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText881.Wrap( -1 )

		gSizer1.Add( self.m_staticText881, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.Pickup = wx.TextCtrl( self.m_panel45, AMMO_VAL_PICKUP, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.Pickup.SetMaxLength( 6 )
		gSizer1.Add( self.Pickup, 0, wx.ALL|wx.EXPAND, 3 )


		bSizer139.Add( gSizer1, 0, wx.ALL, 6 )


		bSizer139.Add( ( 0, 16), 1, wx.EXPAND, 0 )

		bSizer143 = wx.BoxSizer( wx.VERTICAL )

		self.Rename = wx.Button( self.m_panel45, AMMO_RENAME, u"Rename", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Rename.SetMinSize( wx.Size( -1,36 ) )

		bSizer143.Add( self.Rename, 0, wx.ALL|wx.EXPAND, 3 )

		self.Restore = wx.Button( self.m_panel45, AMMO_RESTORE, u"Restore", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Restore.SetMinSize( wx.Size( -1,36 ) )

		bSizer143.Add( self.Restore, 0, wx.ALL|wx.EXPAND, 3 )


		bSizer139.Add( bSizer143, 0, wx.ALL|wx.EXPAND, 3 )


		self.m_panel45.SetSizer( bSizer139 )
		self.m_panel45.Layout()
		bSizer139.Fit( self.m_panel45 )
		bSizer41.Add( self.m_panel45, 0, wx.EXPAND, 0 )

		self.AmmoList = wx.ListCtrl( self, AMMO_LIST, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.BORDER_NONE )
		bSizer41.Add( self.AmmoList, 1, wx.ALL|wx.EXPAND, 0 )


		self.SetSizer( bSizer41 )
		self.Layout()

		# Connect Events
		self.m_staticText88.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.Maximum.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Maximum.Bind( wx.EVT_TEXT, self.set_value )
		self.m_staticText881.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
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
	def dummy( self, event ):
		pass

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

		self.SetSizeHints( wx.Size( 340,401 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )

		self.CheatList = wx.ListCtrl( self, CHEATS_LIST, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.BORDER_NONE )
		bSizer41.Add( self.CheatList, 1, wx.EXPAND, 5 )

		bSizer158 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer158.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.Restore = wx.Button( self, CHEATS_RESTORE, u"Restore", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Restore.SetMinSize( wx.Size( 120,36 ) )

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
		wx.MDIChildFrame.__init__ ( self, parent, id = FRAME_MISC, title = u"Miscellaneous", pos = wx.DefaultPosition, size = wx.Size( 420,450 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU )

		self.SetSizeHints( wx.Size( 420,350 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		bSizer152 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel46 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer153 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel2 = wx.Panel( self.m_panel46, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer154 = wx.BoxSizer( wx.VERTICAL )

		bSizer154.SetMinSize( wx.Size( 100,-1 ) )
		self.Value = wx.TextCtrl( self.m_panel2, MISC_VALUE, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		bSizer154.Add( self.Value, 0, wx.ALL|wx.EXPAND, 3 )

		self.ValueEnabled = wx.CheckBox( self.m_panel2, MISC_VALUE_ENABLED, u"Enabled", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer154.Add( self.ValueEnabled, 0, wx.ALL|wx.EXPAND, 9 )

		self.Restore = wx.Button( self.m_panel2, MISC_RESTORE, u"Restore", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Restore.SetMinSize( wx.Size( -1,36 ) )

		bSizer154.Add( self.Restore, 0, wx.ALL|wx.EXPAND, 3 )


		self.m_panel2.SetSizer( bSizer154 )
		self.m_panel2.Layout()
		bSizer154.Fit( self.m_panel2 )
		bSizer153.Add( self.m_panel2, 1, wx.ALL, 6 )


		self.m_panel46.SetSizer( bSizer153 )
		self.m_panel46.Layout()
		bSizer153.Fit( self.m_panel46 )
		bSizer152.Add( self.m_panel46, 0, 0, 0 )

		self.m_panel50 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer185 = wx.BoxSizer( wx.VERTICAL )

		self.MiscList = wx.ListCtrl( self.m_panel50, MISC_LIST, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_NO_SORT_HEADER|wx.LC_REPORT|wx.BORDER_NONE )
		bSizer185.Add( self.MiscList, 1, wx.ALL|wx.EXPAND, 0 )


		self.m_panel50.SetSizer( bSizer185 )
		self.m_panel50.Layout()
		bSizer185.Fit( self.m_panel50 )
		bSizer152.Add( self.m_panel50, 1, wx.EXPAND, 0 )


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

		self.SetSizeHints( wx.Size( 400,380 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel47 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer98 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer139 = wx.BoxSizer( wx.VERTICAL )

		bSizer139.SetMinSize( wx.Size( 150,-1 ) )
		bSizer94 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText88 = wx.StaticText( self.m_panel47, wx.ID_ANY, u"Episode", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText88.Wrap( -1 )

		bSizer94.Add( self.m_staticText88, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.Episode = wx.TextCtrl( self.m_panel47, PAR_EPISODE, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.Episode.SetMaxLength( 1 )
		bSizer94.Add( self.Episode, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )


		bSizer139.Add( bSizer94, 0, wx.EXPAND, 5 )

		bSizer95 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText881 = wx.StaticText( self.m_panel47, wx.ID_ANY, u"Map", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText881.Wrap( -1 )

		bSizer95.Add( self.m_staticText881, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.Map = wx.TextCtrl( self.m_panel47, PAR_MAP, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.Map.SetMaxLength( 2 )
		bSizer95.Add( self.Map, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )


		bSizer139.Add( bSizer95, 0, wx.EXPAND, 5 )

		bSizer96 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText8811 = wx.StaticText( self.m_panel47, wx.ID_ANY, u"Seconds", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8811.Wrap( -1 )

		bSizer96.Add( self.m_staticText8811, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.Seconds = wx.TextCtrl( self.m_panel47, PAR_SECONDS, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.Seconds.SetMaxLength( 6 )
		bSizer96.Add( self.Seconds, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )


		bSizer139.Add( bSizer96, 0, wx.EXPAND, 5 )


		bSizer98.Add( bSizer139, 0, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.TOP, 6 )

		bSizer97 = wx.BoxSizer( wx.VERTICAL )

		self.Tools = wx.ToolBar( self.m_panel47, PAR_TOOLS, wx.DefaultPosition, wx.DefaultSize, wx.TB_FLAT|wx.TB_NODIVIDER|wx.TB_VERTICAL )
		self.Add = self.Tools.AddLabelTool( PAR_TOOL_ADD, u"tool", wx.Bitmap( u"res/icon-plus.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.Remove = self.Tools.AddLabelTool( PAR_TOOL_REMOVE, u"tool", wx.Bitmap( u"res/icon-minus.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.Tools.Realize()

		bSizer97.Add( self.Tools, 0, wx.EXPAND, 5 )


		bSizer98.Add( bSizer97, 0, wx.ALL|wx.EXPAND, 6 )


		self.m_panel47.SetSizer( bSizer98 )
		self.m_panel47.Layout()
		bSizer98.Fit( self.m_panel47 )
		bSizer41.Add( self.m_panel47, 0, 0, 0 )

		self.ParList = wx.ListCtrl( self, PAR_LIST, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.BORDER_NONE )
		bSizer41.Add( self.ParList, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer41 )
		self.Layout()

		# Connect Events
		self.m_staticText88.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.Episode.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Episode.Bind( wx.EVT_TEXT, self.set_value )
		self.m_staticText881.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.Map.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Map.Bind( wx.EVT_TEXT, self.set_value )
		self.m_staticText8811.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.Seconds.Bind( wx.EVT_LEFT_UP, self.focus_text )
		self.Seconds.Bind( wx.EVT_TEXT, self.set_value )
		self.Bind( wx.EVT_TOOL, self.par_add, id = self.Add.GetId() )
		self.Bind( wx.EVT_TOOL, self.par_remove, id = self.Remove.GetId() )
		self.ParList.Bind( wx.EVT_LIST_ITEM_SELECTED, self.par_select )
		self.ParList.Bind( wx.EVT_SIZE, self.parlist_resize )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def dummy( self, event ):
		pass

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
		wx.Dialog.__init__ ( self, parent, id = DIALOG_SPRITES, title = u"Sprites", pos = wx.DefaultPosition, size = wx.Size( 640,490 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.WANTS_CHARS )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer39 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel49 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer42 = wx.BoxSizer( wx.HORIZONTAL )

		self.SpriteNames = wx.ListCtrl( self.m_panel49, wx.ID_ANY, wx.DefaultPosition, wx.Size( 74,-1 ), wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.SpriteNames.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer42.Add( self.SpriteNames, 0, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 6 )

		bSizer40 = wx.BoxSizer( wx.VERTICAL )

		self.SpritePreview = spritepreview.SpritePreview(self)
		self.SpritePreview.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )

		bSizer40.Add( self.SpritePreview, 1, wx.EXPAND|wx.RIGHT|wx.TOP, 6 )


		bSizer42.Add( bSizer40, 1, wx.EXPAND, 5 )


		self.m_panel49.SetSizer( bSizer42 )
		self.m_panel49.Layout()
		bSizer42.Fit( self.m_panel49 )
		bSizer39.Add( self.m_panel49, 1, wx.EXPAND, 0 )

		self.m_panel48 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer431 = wx.BoxSizer( wx.HORIZONTAL )

		self.Filter = wx.TextCtrl( self.m_panel48, SPRITES_FILTER, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_PROCESS_ENTER )
		self.Filter.SetMaxLength( 4 )
		self.Filter.SetMinSize( wx.Size( 74,-1 ) )

		bSizer431.Add( self.Filter, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 6 )

		self.FrameLabel = wx.StaticText( self.m_panel48, wx.ID_ANY, u"Frame", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FrameLabel.Wrap( -1 )

		self.FrameLabel.SetMinSize( wx.Size( 40,-1 ) )

		bSizer431.Add( self.FrameLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 6 )

		self.FrameIndex = wx.TextCtrl( self.m_panel48, SPRITES_FRAME, wx.EmptyString, wx.DefaultPosition, wx.Size( 28,-1 ), 0 )
		bSizer431.Add( self.FrameIndex, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.LEFT|wx.TOP, 6 )

		self.FrameIndexSpinner = wx.SpinButton( self.m_panel48, SPRITES_FRAMESPIN, wx.DefaultPosition, wx.Size( 17,25 ), 0 )
		bSizer431.Add( self.FrameIndexSpinner, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.RIGHT|wx.TOP, 5 )


		self.m_panel48.SetSizer( bSizer431 )
		self.m_panel48.Layout()
		bSizer431.Fit( self.m_panel48 )
		bSizer39.Add( self.m_panel48, 0, 0, 0 )

		bSizer43 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer43.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.ButtonOk = wx.Button( self, SPRITES_OK, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.ButtonOk.SetDefault()
		self.ButtonOk.SetMinSize( wx.Size( 120,36 ) )

		bSizer43.Add( self.ButtonOk, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 6 )

		self.ButtonCancel = wx.Button( self, SPRITES_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ButtonCancel.SetMinSize( wx.Size( 120,36 ) )

		bSizer43.Add( self.ButtonCancel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 6 )


		bSizer39.Add( bSizer43, 0, wx.EXPAND, 6 )


		self.SetSizer( bSizer39 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.activate )
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
	def activate( self, event ):
		pass

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

		self.SetSizeHints( wx.Size( 640,480 ), wx.DefaultSize )

		bSizer39 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel51 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer186 = wx.BoxSizer( wx.VERTICAL )

		bSizer113 = wx.BoxSizer( wx.VERTICAL )

		bSizer42 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText81 = wx.StaticText( self.m_panel51, wx.ID_ANY, u"Original", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText81.Wrap( -1 )

		bSizer42.Add( self.m_staticText81, 0, wx.LEFT|wx.RIGHT|wx.TOP, 6 )

		self.Original = wx.TextCtrl( self.m_panel51, STRING_OLD, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_DONTWRAP|wx.TE_MULTILINE|wx.TE_READONLY )
		self.Original.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.Original.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		bSizer42.Add( self.Original, 2, wx.ALL|wx.EXPAND, 6 )


		bSizer113.Add( bSizer42, 2, wx.EXPAND, 5 )

		bSizer421 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText811 = wx.StaticText( self.m_panel51, wx.ID_ANY, u"New", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText811.Wrap( -1 )

		bSizer421.Add( self.m_staticText811, 0, wx.LEFT|wx.RIGHT|wx.TOP, 6 )

		self.New = wx.TextCtrl( self.m_panel51, STRING_NEW, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_DONTWRAP|wx.TE_MULTILINE|wx.TE_PROCESS_ENTER|wx.TE_PROCESS_TAB )
		self.New.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer421.Add( self.New, 2, wx.ALL|wx.EXPAND, 6 )


		bSizer113.Add( bSizer421, 2, wx.EXPAND, 5 )


		bSizer186.Add( bSizer113, 1, wx.ALL|wx.EXPAND, 6 )

		bSizer43 = wx.BoxSizer( wx.HORIZONTAL )

		self.CharsLeft = wx.StaticText( self.m_panel51, wx.ID_ANY, u"12 characters left", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CharsLeft.Wrap( -1 )

		bSizer43.Add( self.CharsLeft, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 6 )


		bSizer43.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.ButtonOk = wx.Button( self.m_panel51, STRING_OK, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.ButtonOk.SetDefault()
		self.ButtonOk.SetMinSize( wx.Size( 120,36 ) )

		bSizer43.Add( self.ButtonOk, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 6 )

		self.ButtonCancel = wx.Button( self.m_panel51, STRING_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ButtonCancel.SetMinSize( wx.Size( 120,36 ) )

		bSizer43.Add( self.ButtonCancel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 6 )


		bSizer186.Add( bSizer43, 0, wx.ALL|wx.EXPAND, 6 )


		self.m_panel51.SetSizer( bSizer186 )
		self.m_panel51.Layout()
		bSizer186.Fit( self.m_panel51 )
		bSizer39.Add( self.m_panel51, 1, wx.EXPAND, 0 )


		self.SetSizer( bSizer39 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.activate )
		self.m_staticText81.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.m_staticText811.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.New.Bind( wx.EVT_TEXT, self.text_enter )
		self.CharsLeft.Bind( wx.EVT_ERASE_BACKGROUND, self.dummy )
		self.ButtonOk.Bind( wx.EVT_BUTTON, self.ok )
		self.ButtonCancel.Bind( wx.EVT_BUTTON, self.cancel )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def activate( self, event ):
		pass

	def dummy( self, event ):
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

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer44 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel52 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer187 = wx.BoxSizer( wx.VERTICAL )

		bSizer45 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText46 = wx.StaticText( self.m_panel52, wx.ID_ANY, u"Engine", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )

		self.m_staticText46.SetMinSize( wx.Size( 75,-1 ) )

		bSizer45.Add( self.m_staticText46, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 6 )

		EngineListChoices = []
		self.EngineList = wx.Choice( self.m_panel52, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, EngineListChoices, 0 )
		self.EngineList.SetSelection( 0 )
		bSizer45.Add( self.EngineList, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 6 )


		bSizer45.Add( ( 26, 0), 0, wx.BOTTOM|wx.EXPAND|wx.RIGHT|wx.TOP, 6 )


		bSizer187.Add( bSizer45, 0, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 6 )

		bSizer451 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText461 = wx.StaticText( self.m_panel52, wx.ID_ANY, u"IWAD", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText461.Wrap( -1 )

		self.m_staticText461.SetMinSize( wx.Size( 75,-1 ) )

		bSizer451.Add( self.m_staticText461, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 6 )

		self.IWAD = wx.TextCtrl( self.m_panel52, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.IWAD.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		bSizer451.Add( self.IWAD, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 6 )

		self.IWADBrowse = wx.Button( self.m_panel52, wx.ID_ANY, u"...", wx.DefaultPosition, wx.Size( 36,28 ), 0 )
		bSizer451.Add( self.IWADBrowse, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.RIGHT|wx.TOP, 6 )

		self.IWADDelete = wx.Button( self.m_panel52, wx.ID_ANY, u"X", wx.DefaultPosition, wx.Size( 36,28 ), 0 )
		bSizer451.Add( self.IWADDelete, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.RIGHT|wx.TOP, 6 )


		bSizer187.Add( bSizer451, 0, wx.EXPAND|wx.LEFT|wx.RIGHT, 6 )

		bSizer452 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText462 = wx.StaticText( self.m_panel52, wx.ID_ANY, u"PWADs", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText462.Wrap( -1 )

		self.m_staticText462.SetMinSize( wx.Size( 75,-1 ) )

		bSizer452.Add( self.m_staticText462, 0, wx.ALL, 6 )

		self.PWADList = wx.ListCtrl( self.m_panel52, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		bSizer452.Add( self.PWADList, 1, wx.ALL|wx.EXPAND, 6 )

		bSizer63 = wx.BoxSizer( wx.VERTICAL )

		self.m_toolBar3 = wx.ToolBar( self.m_panel52, PATCHINFO_TOOLBAR, wx.DefaultPosition, wx.DefaultSize, wx.TB_FLAT|wx.TB_NODIVIDER|wx.TB_VERTICAL )
		self.AddPWAD = self.m_toolBar3.AddLabelTool( PATCHINFO_TOOLBAR_ADD, u"tool", wx.Bitmap( u"res/icon-plus.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.RemovePWAD = self.m_toolBar3.AddLabelTool( PATCHINFO_TOOLBAR_REMOVE, u"tool", wx.Bitmap( u"res/icon-minus.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_toolBar3.Realize()

		bSizer63.Add( self.m_toolBar3, 0, wx.EXPAND, 6 )


		bSizer452.Add( bSizer63, 0, wx.BOTTOM|wx.RIGHT|wx.TOP, 6 )


		bSizer187.Add( bSizer452, 1, wx.EXPAND|wx.LEFT|wx.RIGHT, 6 )

		bSizer4521 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer4521.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.ButtonOk = wx.Button( self.m_panel52, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.ButtonOk.SetDefault()
		self.ButtonOk.SetMinSize( wx.Size( 120,36 ) )

		bSizer4521.Add( self.ButtonOk, 0, wx.ALL, 5 )

		self.ButtonCancel = wx.Button( self.m_panel52, PATCHINFO_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ButtonCancel.SetMinSize( wx.Size( 120,36 ) )

		bSizer4521.Add( self.ButtonCancel, 0, wx.ALL, 5 )


		bSizer187.Add( bSizer4521, 0, wx.ALL|wx.EXPAND, 6 )


		self.m_panel52.SetSizer( bSizer187 )
		self.m_panel52.Layout()
		bSizer187.Fit( self.m_panel52 )
		bSizer44.Add( self.m_panel52, 1, wx.EXPAND, 0 )


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

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer50 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel53 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer188 = wx.BoxSizer( wx.VERTICAL )

		bSizer56 = wx.BoxSizer( wx.VERTICAL )

		bSizer52 = wx.BoxSizer( wx.HORIZONTAL )

		self.NewFile = wx.Button( self.m_panel53, START_NEW, u"New file", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.NewFile.SetMinSize( wx.Size( 160,36 ) )

		bSizer52.Add( self.NewFile, 1, wx.ALL, 6 )

		self.OpenFile = wx.Button( self.m_panel53, START_OPEN, u"Open file", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.OpenFile.SetMinSize( wx.Size( 160,36 ) )

		bSizer52.Add( self.OpenFile, 1, wx.ALL, 6 )


		bSizer56.Add( bSizer52, 0, wx.ALL|wx.EXPAND, 6 )

		bSizer54 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText50 = wx.StaticText( self.m_panel53, wx.ID_ANY, u"Recent files", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )

		bSizer54.Add( self.m_staticText50, 0, wx.LEFT|wx.RIGHT|wx.TOP, 5 )

		self.FileList = wx.ListCtrl( self.m_panel53, START_RECENT, wx.DefaultPosition, wx.DefaultSize, wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		bSizer54.Add( self.FileList, 1, wx.ALL|wx.EXPAND, 6 )


		bSizer56.Add( bSizer54, 1, wx.EXPAND|wx.LEFT|wx.RIGHT, 6 )


		bSizer56.Add( ( 0, 0), 0, wx.ALL|wx.EXPAND, 3 )


		bSizer188.Add( bSizer56, 1, wx.ALL|wx.EXPAND, 3 )

		bSizer55 = wx.BoxSizer( wx.HORIZONTAL )

		self.Help = wx.Button( self.m_panel53, wx.ID_ANY, u"Help", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Help.Enable( False )
		self.Help.SetMinSize( wx.Size( 120,36 ) )

		bSizer55.Add( self.Help, 0, wx.BOTTOM|wx.LEFT|wx.RIGHT, 12 )


		bSizer55.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.Cancel = wx.Button( self.m_panel53, START_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.Cancel.SetDefault()
		self.Cancel.SetMinSize( wx.Size( 120,36 ) )

		bSizer55.Add( self.Cancel, 0, wx.BOTTOM|wx.LEFT|wx.RIGHT, 12 )


		bSizer188.Add( bSizer55, 0, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 3 )


		self.m_panel53.SetSizer( bSizer188 )
		self.m_panel53.Layout()
		bSizer188.Fit( self.m_panel53 )
		bSizer50.Add( self.m_panel53, 1, wx.EXPAND, 0 )


		self.SetSizer( bSizer50 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.NewFile.Bind( wx.EVT_BUTTON, self.new_file )
		self.OpenFile.Bind( wx.EVT_BUTTON, self.open_file )
		self.FileList.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.open_file_list )
		self.Help.Bind( wx.EVT_BUTTON, self.help )
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

	def help( self, event ):
		pass

	def cancel( self, event ):
		pass


###########################################################################
## Class AboutDialogBase
###########################################################################

class AboutDialogBase ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = DIALOG_ABOUT, title = u"About WhackEd4", pos = wx.DefaultPosition, size = wx.Size( 640,480 ), style = wx.CAPTION|wx.CLOSE_BOX )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

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

		bSizer56.Add( self.Version, 0, wx.ALL, 3 )


		bSizer56.Add( ( 0, 9), 0, wx.EXPAND, 5 )

		self.m_staticText115 = wx.StaticText( self, wx.ID_ANY, u"http://www.teamhellspawn.com/exl/whacked4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText115.Wrap( -1 )

		bSizer56.Add( self.m_staticText115, 0, wx.ALL, 3 )


		bSizer56.Add( ( 0, 9), 0, wx.EXPAND, 5 )

		bSizer84 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1391 = wx.StaticText( self, wx.ID_ANY, u"Application icon by Paul Davey, from the ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1391.Wrap( -1 )

		bSizer84.Add( self.m_staticText1391, 0, wx.BOTTOM|wx.LEFT|wx.TOP, 3 )

		self.m_staticText116 = wx.StaticText( self, wx.ID_ANY, u"Buuf Icon set http://www.iconarchive.com/show/buuf-icons-by-mattahan.html", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText116.Wrap( -1 )

		bSizer84.Add( self.m_staticText116, 0, wx.ALL, 5 )


		bSizer56.Add( bSizer84, 0, wx.EXPAND, 5 )


		bSizer56.Add( ( 0, 9), 0, wx.EXPAND, 5 )

		self.m_staticText139 = wx.StaticText( self, wx.ID_ANY, u"Thanks to...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText139.Wrap( -1 )

		bSizer56.Add( self.m_staticText139, 0, wx.LEFT|wx.RIGHT|wx.TOP, 3 )

		self.m_staticText138 = wx.StaticText( self, wx.ID_ANY, u"Aeyesx, Aliotroph?, Altazimuth, Andy Fox, Andy Shawaluk, antares031, Big_Al, CodeImp, CSabo, Da Werecat, Dani J666, Daniel Carroll, Doom Dude, DooMAD, Doomer, EarthQuake, Endy McGufin, Enjay, esselfortium, Frades, Francesco Orsenigo, Greg Lewis, hawkwind3, iori, j0e, Kurisutaru, Leonard Pitre, Looney, MaiklRussia, Marc. A. Pullen, Palladium, plums, Rellik, REZ, scifista42, Skullers, SlayeR, The Doommer, TheStupidestBeing, tempun, un4seen, VGA, WildWeasel, XDelusion, Xyzzy01, Zodomaniac", wx.DefaultPosition, wx.Size( -1,-1 ), wx.ST_NO_AUTORESIZE )
		self.m_staticText138.Wrap( 450 )

		bSizer56.Add( self.m_staticText138, 1, wx.ALL, 3 )


		bSizer56.Add( ( 0, 12), 0, wx.EXPAND, 5 )

		bSizer58 = wx.BoxSizer( wx.HORIZONTAL )

		self.License = wx.Button( self, wx.ID_ANY, u"License", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.License.SetMinSize( wx.Size( 150,36 ) )

		bSizer58.Add( self.License, 0, wx.ALL, 0 )


		bSizer58.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.ButtonOk = wx.Button( self, ABOUT_OK, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.ButtonOk.SetDefault()
		self.ButtonOk.SetMinSize( wx.Size( 150,36 ) )

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
		wx.Dialog.__init__ ( self, parent, id = DIALOG_ERROR, title = u"WhackEd4 fatal error", pos = wx.DefaultPosition, size = wx.Size( 640,560 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer118 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel54 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer189 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText91 = wx.StaticText( self.m_panel54, wx.ID_ANY, u"Oops! Something terrible has happened.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText91.Wrap( -1 )

		self.m_staticText91.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer189.Add( self.m_staticText91, 0, wx.ALL, 12 )

		self.m_staticText92 = wx.StaticText( self.m_panel54, wx.ID_ANY, u"Below you can find more details about the error. You can copy it to the clipboard and send it to a developer who can fix this bug.", wx.DefaultPosition, wx.DefaultSize, wx.ST_NO_AUTORESIZE )
		self.m_staticText92.Wrap( 592 )

		self.m_staticText92.SetMinSize( wx.Size( -1,40 ) )

		bSizer189.Add( self.m_staticText92, 0, wx.BOTTOM|wx.LEFT|wx.RIGHT, 12 )

		self.Report = wx.TextCtrl( self.m_panel54, ERROR_REPORT, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		self.Report.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.Report.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		bSizer189.Add( self.Report, 1, wx.ALL|wx.EXPAND, 12 )

		bSizer119 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button43 = wx.Button( self.m_panel54, ERROR_COPY, u"Copy to clipboard", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button43.SetMinSize( wx.Size( 144,36 ) )

		bSizer119.Add( self.m_button43, 0, wx.ALL, 6 )


		bSizer119.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button44 = wx.Button( self.m_panel54, ERROR_CLOSE, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button44.SetMinSize( wx.Size( 144,36 ) )

		bSizer119.Add( self.m_button44, 0, wx.ALL, 6 )


		bSizer189.Add( bSizer119, 0, wx.ALL|wx.EXPAND, 6 )


		self.m_panel54.SetSizer( bSizer189 )
		self.m_panel54.Layout()
		bSizer189.Fit( self.m_panel54 )
		bSizer118.Add( self.m_panel54, 1, wx.EXPAND, 0 )


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


###########################################################################
## Class StatePreviewDialogBase
###########################################################################

class StatePreviewDialogBase ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Preview", pos = wx.DefaultPosition, size = wx.Size( 658,495 ), style = wx.CAPTION|wx.WANTS_CHARS|wx.BORDER_RAISED )

		self.SetSizeHints( wx.Size( 658,495 ), wx.DefaultSize )

		bSizer140 = wx.BoxSizer( wx.VERTICAL )

		self.Sprite = spritepreview.SpritePreview(self, size=(-1, 160))
		self.Sprite.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )

		bSizer140.Add( self.Sprite, 1, wx.ALL|wx.EXPAND, 0 )

		bSizer141 = wx.BoxSizer( wx.HORIZONTAL )

		self.StateIndex = wx.StaticText( self, wx.ID_ANY, u"0000", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.StateIndex.Wrap( -1 )

		bSizer141.Add( self.StateIndex, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 6 )

		self.StateInfo = wx.StaticText( self, wx.ID_ANY, u"TROOA0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.StateInfo.Wrap( -1 )

		self.StateInfo.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer141.Add( self.StateInfo, 2, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 6 )

		self.StateAction = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.StateAction.Wrap( -1 )

		bSizer141.Add( self.StateAction, 3, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 6 )

		self.StateSound = wx.StaticText( self, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.StateSound.Wrap( -1 )

		bSizer141.Add( self.StateSound, 3, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 6 )

		self.SpawnSound = wx.StaticText( self, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SpawnSound.Wrap( -1 )

		self.SpawnSound.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.SpawnSound.Enable( False )

		bSizer141.Add( self.SpawnSound, 2, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 6 )

		self.Close = wx.Button( self, PREVIEW_CLOSE, u"Close", wx.DefaultPosition, wx.Size( 120,36 ), 0 )
		bSizer141.Add( self.Close, 0, wx.ALL, 6 )


		bSizer140.Add( bSizer141, 0, wx.EXPAND, 0 )


		self.SetSizer( bSizer140 )
		self.Layout()
		self.Timer = wx.Timer()
		self.Timer.SetOwner( self, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.activate )
		self.Close.Bind( wx.EVT_BUTTON, self.close )
		self.Bind( wx.EVT_TIMER, self.timer, id=wx.ID_ANY )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def activate( self, event ):
		pass

	def close( self, event ):
		pass

	def timer( self, event ):
		pass


