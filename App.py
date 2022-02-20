# -*- coding: utf-8 -*-
import traceback
import os
import tempfile
import sys

import dabo
from dabo.dApp import dApp
from dabo.dLocalize import _
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping


class App(dApp):
    def initProperties(self):
        # Manages how preferences are saved
        self.BasePrefKey = "dabo.app.WBSTools"
        self.setAppInfo("appShortName", "WBSTools")
        self.setAppInfo("appName", "WBSTools")
        self.setAppInfo("copyright", "(c) 2013-2022")
        self.setAppInfo("companyName", "Monrovia Church of Christ")
        self.setAppInfo("companyAddress1", "595 Nance Road")
        self.setAppInfo("companyAddress2", "Madison, AL 35757")
        self.setAppInfo("companyPhone", "256.837.5255")
        self.setAppInfo("companyEmail", "wbs@monrovia.org")
        self.setAppInfo("companyUrl", "https://monrovia.org")

        self.setAppInfo("appDescription", _("Tools for grading World Bible School lessons and recording \
                                           student information in a MySQL database"))

        # Information about the developer of the software:
        self.setAppInfo("authorName", "Arnie Elkins")
        self.setAppInfo("authorEmail", "wbstools@pm.me")
        self.setAppInfo("authorURL", "https://monrovia.org/wbs")

        # Set app version information:
        # This is the central place to keep your application's version updated.
        __version__ = "1.1.1.5"
        self.setAppInfo("appVersion", __version__)
        # self.CryptoKey = ""
        # Crypto connection not working -- will check AWE 2022.02.08
        # clarification -- connections are not encrypted, it is the saved passwords that are. At this time the passwords in
        # the .cnxml files are using SimpleCrypt 'obfuscation' rather than encryption. I believe all that needs to be done
        # is regenerate those files using the CryptoKey that is in the code.
        # pycrypto is not supported, changed to use the 'near drop-in replacement' pycryptodome
        self.registerFonts(os.getcwd())
        self.Icon = "icons/wbs.ico"

    def setup(self):
        if dabo.MDI:
            # self.MainFormClass = dabo.ui.createForm("ui/StudentsForm.cdxml")
            self.MainFormClass = dabo.ui.dFormMain
        else:
            # no need for main form in SDI mode
            self.MainFormClass = None
        super(App, self).setup()

    def getTempDir(self):
        self.TempDir = tempfile.mkdtemp()
        print 'self.TempDir = ', self.TempDir, type(self.TempDir)
        if not self.testTempDir:
            self.getTempDir()
        self.PreferenceManager.setValue("TempDir", self.TempDir)

    def testTempDir(self):
        if self.TempDir:
            if os.path.exists(self.TempDir):
                try:
                    handle = open('testfile', 'wb')
                    handle.write('fileData')
                    handle.close()
                    os.remove('testfile')
                    self.PreferenceManager.setValue("TempDir", self.TempDir)
                    return True
                except Exception, e:
                    dabo.ui.exclaim(
                        "Oh No!  An exception while writing the file!  This is a Really, Really Bad Thing!\n" + str(
                            traceback.format_exc(e)))
            else:
                response = dabo.ui.areYouSure(message="TempDir is defined as " + str(
                    self.TempDir) + " but it does not exist.  Attempt to create it?",
                                              defaultNo=True,
                                              cancelButton=False,
                                              requestUserAttention=True)
                if response:
                    try:
                        os.mkdir(self.TempDir)
                        self.PreferenceManager.setValue("TempDir", self.TempDir)
                        return True
                    except Exception, e:
                        dabo.ui.exclaim('Unable to create a temp directory!!'+str(traceback.format_exc(e)))
                        dabo.ui.exclaim("Well alrighty then, since I can't work without one, I quit!")
                        sys.exit(1)

    def registerFonts(self, homedir):
        font_mappings = []
        for fname in os.listdir(os.path.join(homedir, "resources")):
            psname, ext = os.path.splitext(fname)
            if ext == ".ttf":
                name = psname
                name_lower = name.lower()
                pdfmetrics.registerFont(TTFont(psname, os.path.join(homedir, "resources", fname)))
                try:
                    idx = name_lower.index("oblique")
                    italic = True
                    name = name[:idx] + name[idx + len("oblique"):]
                    name_lower = name.lower()
                except ValueError:
                    italic = False

                if not italic:
                    try:
                        idx = name_lower.index("italic")
                        italic = True
                        name = name[:idx] + name[idx + len("italic"):]
                        name_lower = name.lower()
                    except ValueError:
                        italic = False

                try:
                    idx = name_lower.index("bold")
                    bold = True
                    name = name[:idx] + name[idx + len("bold"):]
                except ValueError:
                    bold = False

                name = name.replace("-", "").lower()
                font_mappings.append((name, bold, italic, psname))

        for font_mapping in sorted(font_mappings):
            addMapping(*font_mapping)
            print font_mapping
