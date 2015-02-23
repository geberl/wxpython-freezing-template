# -*- coding: utf-8 -*-
__author__ = 'guenther@eberl.se'

# Import program components / modules from python standard library / non-standard modules.
import gui
import wx

import logging
import logging.config
import os
import sys
import platform


# Logging config on sub-module level.
logger = logging.getLogger(__name__)


class MainFrame(gui.MainFrame):
    def __init__(self, parent):
        gui.MainFrame.__init__(self, parent)
        logger.debug('Running __init__ ...')

        # Bind the "on close" event.
        self.Bind(wx.EVT_CLOSE, self.on_close)

        # Determine if program is running compiled to *.exe/*.app or from Python interpreter.
        if hasattr(sys, 'frozen'):
            running_mode_string = ' (frozen)'
            application_path = os.path.dirname(sys.executable)
        else:
            running_mode_string = ' (not frozen)'
            application_path = os.path.dirname(__file__)

        # Set the application icon, unsupported on Mac OS X.
        if platform.system() != 'Darwin':
            ico = wx.Icon(application_path + os.sep + 'icon.ico', wx.BITMAP_TYPE_ICO)
            self.SetIcon(ico)

        # Append current version number to existing static text.
        self.VersionText.SetLabelText(self.VersionText.GetLabelText() + u' 1.2.3.4' + running_mode_string)

    def on_close(self, event):
        logger.debug('Running on_close (event "%s", id "%i") ...' % (event.GetClassName(), event.GetId()))

        # Close GUI.
        self.Destroy()
