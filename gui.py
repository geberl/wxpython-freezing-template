# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"wxPython Freezing Template"), pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.RESIZE_BORDER|wx.STAY_ON_TOP|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 200,55 ), wx.DefaultSize )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.MainPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.MainPanel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.MainPanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.MainPanel.SetMinSize( wx.Size( 250,100 ) )
		
		PanelSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.VersionText = wx.StaticText( self.MainPanel, wx.ID_ANY, _(u"Version"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.VersionText.Wrap( -1 )
		PanelSizer.Add( self.VersionText, 0, wx.ALIGN_CENTER_HORIZONTAL, 50 )
		
		
		self.MainPanel.SetSizer( PanelSizer )
		self.MainPanel.Layout()
		PanelSizer.Fit( self.MainPanel )
		MainSizer.Add( self.MainPanel, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 0 )
		
		
		self.SetSizer( MainSizer )
		self.Layout()
		MainSizer.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

