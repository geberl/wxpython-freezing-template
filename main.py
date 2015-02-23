# -*- coding: utf-8 -*-
__author__ = 'guenther@eberl.se'

# Import program components / modules from python standard library / non-standard modules.
import mainframe
import wx

import logging
import logging.config
import os
import sys


class WxPythonFreezingTemplate(wx.App):
    def __init__(self):
        super(WxPythonFreezingTemplate, self).__init__()

        # Logging config on base-module level.
        logger = logging.getLogger(__name__)
        logging.config.fileConfig(r'logging_to_terminal.ini', disable_existing_loggers=False)
        # logging.config.fileConfig(r'logging_to_file.ini', disable_existing_loggers=False)
        # logging.config.fileConfig(r'logging_to_terminal_and_file.ini', disable_existing_loggers=False)

        # Show GUI.
        logger.debug('Loading GUI ...')
        self.frame = mainframe.MainFrame(None)
        self.SetTopWindow(self.frame)
        self.frame.Show()


if __name__ == '__main__':
    # Create object.
    app = WxPythonFreezingTemplate()

    # Handle internationalisation.
    base_path = os.path.abspath(os.path.dirname(sys.argv[0]))
    locale_dir = os.path.join(base_path, 'locale')
    my_locale = wx.Locale(wx.LANGUAGE_DEFAULT)

    # Loop.
    app.MainLoop()

    # Exit with default exit code 0.
    sys.exit()