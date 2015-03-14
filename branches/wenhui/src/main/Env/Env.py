#@PydevCodeAnalysisIgnore
from direct.gui.DirectGui import DGG
from direct.gui.DirectGui import DirectFrame
from direct.gui.DirectGui import DirectLabel
from direct.gui.OnscreenText import OnscreenText

from panda3d.core import Point3
from panda3d.core import TextNode

from common.Constants import Constants
from common.DatabaseHelper import DatabaseHelper
from common.DirectBasicButton import DirectBasicButton
from common.DirectTextField import DirectTextField
from common.DirectWindow import DirectWindow

from main.Env.EnvControls import EnvControls

class Env:
    
    def __init__(self):

        if Constants.DEBUG:
            print 'Loading GameEnv...'

        self.eFocus = -1
        self.loginEntry = []

        base.disableMouse()

        self.createMainFrame()
        self.createBackground()
        self.createText()
        self.createTextEntry()
        self.createButtons()
        self.createVersion()
        
        # add background music to login screen
        main.audioManager.setMusic('01.ogg')

        self.mainFrame.setControls(EnvControls(self))

    def createMainFrame(self):
        """Create the main base frame."""
        # frameColor is defined as (R,G,B,A)
        self.mainFrame = DirectWindow( frameSize = (-0.5, 0.5, -0.3, 0.5),
                                       frameColor = (0, 0.2, 0, 0.8),
                                       state = DGG.NORMAL )

        self.titleBar = DirectFrame( frameSize = (-0.5, 0.5, -0.1, 0.1),
                                     frameColor = (0, 0, 0, 0.5),
                                     pos = (0, 0, 0.4),
                                     state = DGG.NORMAL )
        self.titleBar.reparentTo(self.mainFrame)

        self.titleName = DirectLabel( text = 'Welcome to Beast Reality Screen',
                                      text_align = TextNode.ALeft,
                                      text_fg = Constants.TEXT_COLOR,
                                      text_font = Constants.FONT_TYPE_01,
                                      text_scale = 0.065,
                                      frameColor = (0, 0, 0, 0),
                                      pos = (-0.48, 0, -0.025) )
        self.titleName.reparentTo(self.titleBar)

    def createBackground(self):
        """Create a background for the login screen."""
        self.envModel = 'loginScene/environment'

        self.environ = loader.loadModel('models/maps/' + self.envModel)
        self.environ.reparentTo(render)

        self.environ.setPos(0, 42, -7)
        self.environ.setScale(0.16)

    def createText(self):
        """Create some label for login text entry field"""
        self.headerText = DirectLabel( text = 'Login2',
                                       text_align = TextNode.ACenter,
                                       frameSize = (-0.2, 0.2, 0.2, 0.2),
                                       text_fg = Constants.TEXT_COLOR,
                                       text_font = Constants.FONT_TYPE_01,
                                       text_scale = 0.07,
                                       frameColor = (0, 0, 0, 0),
                                       pos = (0, 0, 0.2) )
        self.headerText.reparentTo(self.mainFrame)

        self.usernameText = DirectLabel( text = 'Username2',
                                         text_fg = Constants.TEXT_COLOR,
                                         text_font = Constants.FONT_TYPE_01,
                                         text_scale = 0.06,
                                         frameColor = (0, 0, 0, 0),
                                         pos = (-0.32, 0, 0.05) )
        self.usernameText.reparentTo(self.mainFrame)

        self.passwordText = DirectLabel( text = 'Password2',
                                         text_fg = Constants.TEXT_COLOR,
                                         text_font = Constants.FONT_TYPE_01,
                                         text_scale = 0.06,
                                         frameColor = (0, 0, 0, 0),
                                         pos = (-0.32, 0, -0.05) )
        self.passwordText.reparentTo(self.mainFrame)

    def createTextEntry(self):
        """Create entry boxes for credentials."""
        self.usernameEntry = DirectTextField( self.mainFrame,
                                              text_font = Constants.FONT_TYPE_01,
                                              scale = 0.057,
                                              pos = (-0.14, 0, 0.05),
                                              command = self.submit,
                                              focus = 1,
                                              focusInCommand = self.setFocus,
                                              focusInExtraArgs = [0] )
        self.usernameEntry.reparentTo(self.mainFrame)
        self.loginEntry.append(self.usernameEntry)

        self.passwordEntry = DirectTextField( self.mainFrame,
                                              text_font = Constants.FONT_TYPE_01,
                                              scale = 0.057,
                                              pos = (-0.14, 0, -0.05),
                                              command = self.submit,
                                              obscured = 1,
                                              focusInCommand = self.setFocus,
                                              focusInExtraArgs = [1] )
        self.passwordEntry.reparentTo(self.mainFrame)
        self.loginEntry.append(self.passwordEntry)

    def createButtons(self):
        """Create some buttons."""
        self.validateLogin = DirectBasicButton ( text = 'Log In2',
                                                 text_fg = Constants.TEXT_COLOR,
                                                 text_font = Constants.FONT_TYPE_01,
                                                 text_pos = (0, -0.015),
                                                 text_scale = 0.06,
                                                 frameSize = (-0.15, 0.15, -0.06, 0.06),
                                                 frameColor = (0, 0, 0, 0.3),
                                                 relief = DGG.FLAT,
                                                 pos = (-0.2, 0, -0.19),
                                                 command = self.submit )
        self.validateLogin.reparentTo(self.mainFrame)

        self.registerButton = DirectBasicButton( text = 'Register2',
                                                 text_fg = Constants.TEXT_COLOR,
                                                 text_font = Constants.FONT_TYPE_01,
                                                 text_pos = (0, -0.015),
                                                 text_scale = 0.06,
                                                 frameSize = (-0.15, 0.15, -0.06, 0.06),
                                                 frameColor = (0, 0, 0, 0.3),
                                                 relief = DGG.FLAT,
                                                 pos = (0.2, 0, -0.19),
                                                 command = self.register )
        self.registerButton.reparentTo(self.mainFrame)

    def createVersion(self):

        self.versionLabel = OnscreenText( text = 'v' + Constants.CLIENT_VERSION,
                                          pos = (1.55, -0.95),
                                          scale = 0.05,
                                          fg = Constants.TEXT_COLOR,
                                          shadow = Constants.TEXT_SHADOW_COLOR,
                                          align = TextNode.ARight,
                                          font = Constants.FONT_TYPE_01 )

    def submit(self, text = None):
        """Submit credentials to the server."""
        main.createMessageBox(0, 'This is the other Login', self.selectEntry, [self.eFocus])
        """
        if self.usernameEntry.get().strip() == '':
            result = DatabaseHelper.dbSelectRowByID('msg', 'msg_id', 55)
            main.createMessageBox(0, result['msg_text'], self.selectEntry, [self.eFocus])
            self.setFocus(0)
        elif self.passwordEntry.get().strip() == '':
            result = DatabaseHelper.dbSelectRowByID('msg', 'msg_id', 57)
            main.createMessageBox(0, result['msg_text'], self.selectEntry, [self.eFocus])
            self.setFocus(1)
        elif main.startConnection():
            main.login(self.usernameEntry.get().strip(), self.passwordEntry.get().strip())
        else:
            result = DatabaseHelper.dbSelectRowByID('msg', 'msg_id', 45)
            main.createMessageBox(0, result['msg_text'], self.selectEntry, [self.eFocus])
        """

    def register(self):
        """Switch to the registration screen."""
        main.switchEnvironment('Register')

    def toggleEntry(self, direction):
        """Toggle through the entry boxes."""
        self.eFocus = (self.eFocus + direction + len(self.loginEntry)) % len(self.loginEntry)
        self.selectEntry(self.eFocus)

    def setFocus(self, eNum):
        """Store current entry box number."""
        self.eFocus = eNum

    def selectEntry(self, eNum):
        """Focus on a specific entry box."""
        for eObject in self.loginEntry:
            eObject['focus'] = 0

        self.loginEntry[eNum]['focus'] = 1

    def showAlert(self, status):
        """Create failed login box."""
        if status == 1:
            result = DatabaseHelper.dbSelectRowByID('msg', 'msg_id', 68)
            main.createMessageBox(0, result['msg_text'], self.selectEntry, [self.eFocus])
        elif status == 2:
            result = DatabaseHelper.dbSelectRowByID('msg', 'msg_id', 69)
            main.createMessageBox(0, result['msg_text'], self.selectEntry, [self.eFocus])
        elif status == 3:
            result = DatabaseHelper.dbSelectRowByID('msg', 'msg_id', 81)
            main.createMessageBox(0, result['msg_text'], self.selectEntry, [self.eFocus])

    def unload(self):
        """Unload this instance."""
        if Constants.DEBUG:
            print 'Unloading Login2...'

        main.audioManager.removeMusic()

        loader.unloadModel('models/maps/' + self.envModel)
        self.environ.removeNode()

        self.versionLabel.destroy()
        self.mainFrame.destroy()

        base.enableMouse()
