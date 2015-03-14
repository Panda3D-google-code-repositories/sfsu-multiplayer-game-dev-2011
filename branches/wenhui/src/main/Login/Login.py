from common.Constants import Constants
from common.DatabaseHelper import DatabaseHelper
from common.DirectBasicButton import DirectBasicButton
from common.DirectTextField import DirectTextField
from common.DirectWindow import DirectWindow
from direct.actor.Actor import Actor
from direct.gui.DirectGui import DGG, DirectFrame, DirectLabel
from direct.gui.OnscreenText import OnscreenText
from direct.interval.FunctionInterval import Func, Wait
from direct.interval.IntervalGlobal import Sequence
from main.Chatcontrol.Chat import Chat
from main.Login.LoginControls import LoginControls
from panda3d.core import Point3, TextNode
from pandac.PandaModules import *


class Login:
    
    def __init__(self):

        if Constants.DEBUG:
            print 'Loading Login...'

        self.eFocus = -1
        self.loginEntry = []

        base.disableMouse()

        self.createMainFrame()
        self.createBackground()
        self.createText()
        self.createTextEntry()
        self.createButtons()
        self.createVersion()
#        self.chat = Chat()
        # add background music to login screen
#        main.audioManager.setMusic('01.ogg')
        self.mainFrame.setControls(LoginControls(self))

    def createMainFrame(self):
        """Create the main base frame."""
        # frameColor is defined as (R,G,B,A)
        self.mainFrame = DirectWindow(frameSize=(-0.5, 0.5, -0.3, 0.5),
                                       frameColor=(0, 0.2, 0, 0.8),
                                       state=DGG.NORMAL)

        self.titleBar = DirectFrame(frameSize=(-0.5, 0.5, -0.08, 0.08),
                                     frameColor=(0, 0, 0, 0.5),
                                     pos=(0, 0, 0.42),
                                     state=DGG.NORMAL)
        self.titleBar.reparentTo(self.mainFrame)

        self.titleName = DirectLabel(text='Welcome to Beast Reality',
                                      text_align=TextNode.ALeft,
                                      text_fg=Constants.TEXT_COLOR,
                                      text_font=Constants.FONT_TYPE_01,
                                      text_scale=0.065,
                                      frameColor=(0, 0, 0, 0),
                                      pos=(-0.48, 0, -0.025))
        self.titleName.reparentTo(self.titleBar)

    def createBackground(self):
        """Create a background for the login screen."""
        self.envModel = 'loginScene/environment'

        self.environ = loader.loadModel('models/maps/' + self.envModel)
        self.environ.reparentTo(render)

        self.environ.setPos(0, 42, -7)
        self.environ.setScale(0.16)
        
        self.actorModelFile = 'sparrow/sparrow'
        self.actorObject = Actor('models/' + self.actorModelFile, {
                                'walk': 'models/sparrow/sparrow-walk',
                                'peck': 'models/sparrow/sparrow-peck',
                                'flap': 'models/sparrow/sparrow-flap',
                                'die': 'models/sparrow/sparrow-die'})
        self.actorObject.reparentTo(render)
        
#        self.actorObject.enableBlend()
        
        self.actorObject.setH(30)
        self.actorObject.setPos(-7, 35, -7)
        self.actorObject.setScale(0.7)
        
#        dlight = DirectionalLight('dlight')
#        dlight.setColor(Vec4(0.8, 0.8, 0.5, 1))
#        dlnp = render.attachNewNode(dlight)
#        dlnp.setHpr(0, -60, 0)
#        render.setLight(dlnp)
        
#        self.actorObject.loop('walk')

        delay = Wait(1.5)
        interval01 = self.actorObject.posInterval(2,
                                                  Point3(-3.25, 33, -7),
                                                  startPos = Point3(-7, 33, -7))
        interval02 = self.actorObject.posInterval(1.5,
                                                  Point3(-1, 33, -7),
                                                  startPos = Point3(-3.25, 33, -7))
        
        interval17 = self.actorObject.hprInterval(0.5, Point3(-10, 0, 0), startHpr = Point3(35, 0,0))
        interval18 = self.actorObject.hprInterval(0.5, Point3(35, 0, 0), startHpr = Point3(-10, 0,0))

        interval03 = self.actorObject.posInterval(1.5,
                                                  Point3(5, 33, -7),
                                                  startPos = Point3(-1, 33, -7))
        interval04 = self.actorObject.hprInterval(0.6,
                                                  Point3(-105, 0, 0),
                                                  startHpr = Point3(35, 0, 0))
        interval05 = self.actorObject.posInterval(1.5,
                                                  Point3(-0.5, 40, -7),
                                                  startPos = Point3(5, 33, -7))
        interval06 = self.actorObject.hprInterval(0.6,
                                                  Point3(25, 0, 0),
                                                  startHpr = Point3(-105, 0, 0))
        interval07 = self.actorObject.actorInterval("peck",
                                                    loop = 0,
                                                    duration = 2.0, 
                                                    startFrame = 0,
                                                    endFrame = 2.0)
        intervalStill = self.actorObject.actorInterval("peck", loop = 0,
                                                       duration = 3.0,
                                                       startTime = 2.0, 
                                                       endTime = 3.0)
        intervalDie = self.actorObject.actorInterval("die", loop=0, duration = 2.0)
        intervalStartWalking = Func(self.controlAnimation, 1, self.actorObject, "walk")
        intervalStartFlaping = Func(self.controlAnimation, 1, self.actorObject, "flap")
        interval10 = Func(self.controlAnimation, 0, self.actorObject)
        interval11 = self.actorObject.posInterval(0.8,
                                                  Point3(7, 33, -3.9),
                                                  startPos = Point3(-0.5, 40, -7))
        interval12 = self.actorObject.hprInterval(0.5, Point3(-25, 0, 0), startHpr = Point3(25, 0,0))
        
        interval13 = self.actorObject.posInterval(0.6, Point3(2, 27, -7), startPos = Point3(7, 33, -3.9))
        interval14 = self.actorObject.posInterval(2, Point3(-7, 33, -7), startPos = Point3(2, 27, -7))
        interval15 = self.actorObject.hprInterval(0.5, Point3(-100, 0,0), startHpr = Point3(-25,0,0))
        interval16 = self.actorObject.hprInterval(0.5, Point3(35, 0,0), startHpr = Point3(-100, 0,0))
        
        self.actorPace = Sequence(intervalStartWalking,
                                  interval01, # walk
                                  interval02,
                                  interval10, # disable animation
                                  delay,
                                  interval07, # pecking
                                  intervalStartWalking,
                                  interval17,
                                  interval10,
                                  interval07, # pecking
                                  intervalStartWalking, # walking
                                  interval18,
                                  interval03,
                                  interval10, 
                                  delay,
                                  intervalStartWalking, # walking
                                  interval04,
                                  interval05,
                                  interval06,
                                  interval10,
                                  delay, 
                                  interval07,
                                  intervalStartFlaping, # fly
                                  interval11,
                                  interval12,
                                  intervalStill,
                                  intervalStartFlaping,
                                  interval13,
                                  intervalStill,
                                  interval07,
                                  interval07,
                                  intervalStartWalking,
                                  interval15,
                                  interval14,
                                  interval10,
                                  delay,
                                  interval10,
                                  intervalDie,
                                  name='actorPace' )
        
        self.actorPace.start()

        
    def controlAnimation(self, toStopAnim, actor, anim=None):
        if toStopAnim == 0:
            actor.stop()
        else:
            actor.loop(anim)
            
    def createText(self):
        """Create some label for login text entry field"""
        self.headerText = DirectLabel(text='Login',
                                       text_align=TextNode.ACenter,
                                       frameSize=(-0.2, 0.2, 0.2, 0.2),
                                       text_fg=Constants.TEXT_COLOR,
                                       text_font=Constants.FONT_TYPE_01,
                                       text_scale=0.07,
                                       frameColor=(0, 0, 0, 0),
                                       pos=(0, 0, 0.23))
        self.headerText.reparentTo(self.mainFrame)

        self.usernameText = DirectLabel(text='Username',
                                         text_fg=Constants.TEXT_COLOR,
                                         text_font=Constants.FONT_TYPE_01,
                                         text_scale=0.06,
                                         frameColor=(0, 0, 0, 0),
                                         pos=(-0.32, 0, 0.097))
        self.usernameText.reparentTo(self.mainFrame)

        self.passwordText = DirectLabel(text='Password',
                                         text_fg=Constants.TEXT_COLOR,
                                         text_font=Constants.FONT_TYPE_01,
                                         text_scale=0.06,
                                         frameColor=(0, 0, 0, 0),
                                         pos=(-0.32, 0, -0.045))
        self.passwordText.reparentTo(self.mainFrame)


    def createTextEntry(self):
        """Create entry boxes for credentials."""
        self.usernameEntry = DirectTextField(self.mainFrame,
                                              text_font=Constants.FONT_TYPE_01,
                                              scale=0.055,
                                              pos=(-0.14, 0, 0.085),
                                              command=self.submit,
                                              focus=1,
                                              focusInCommand=self.setFocus,
                                              focusInExtraArgs=[0])
        self.usernameEntry.reparentTo(self.mainFrame)
        self.loginEntry.append(self.usernameEntry)
        
        self.passwordEntry = DirectTextField(self.mainFrame,
                                              text_font=Constants.FONT_TYPE_01,
                                              scale=0.055,
                                              pos=(-0.14, 0, -0.05),
                                              command=self.submit,
                                              obscured=1,
                                              focusInCommand=self.setFocus,
                                              focusInExtraArgs=[1])
        self.passwordEntry.reparentTo(self.mainFrame)
        self.loginEntry.append(self.passwordEntry)

    def createButtons(self):
        """Create some buttons."""
        self.validateLogin = DirectBasicButton (text='Log In',
                                                 text_fg=Constants.TEXT_COLOR,
                                                 text_font=Constants.FONT_TYPE_01,
                                                 text_pos=(0, -0.015),
                                                 text_scale=0.06,
                                                 frameSize=(-0.15, 0.15, -0.06, 0.06),
                                                 frameColor=(0, 0, 0, 0.3),
                                                 relief=DGG.FLAT,
                                                 pos=(-0.2, 0, -0.19),
                                                 command=self.submit)
        self.validateLogin.reparentTo(self.mainFrame)

        self.registerButton = DirectBasicButton(text='Register',
                                                 text_fg=Constants.TEXT_COLOR,
                                                 text_font=Constants.FONT_TYPE_01,
                                                 text_pos=(0, -0.015),
                                                 text_scale=0.06,
                                                 frameSize=(-0.15, 0.15, -0.06, 0.06),
                                                 frameColor=(0, 0, 0, 0.3),
                                                 relief=DGG.FLAT,
                                                 pos=(0.2, 0, -0.19),
                                                 command=self.register)
        self.registerButton.reparentTo(self.mainFrame)

    def createVersion(self):

        self.versionLabel = OnscreenText(text='v' + Constants.CLIENT_VERSION,
                                          pos=(1.55, -0.95),
                                          scale=0.05,
                                          fg=Constants.TEXT_COLOR,
                                          shadow=Constants.TEXT_SHADOW_COLOR,
                                          align=TextNode.ARight,
                                          font=Constants.FONT_TYPE_01)

    def submit(self, text=None):
        """Submit credentials to the server."""
#        if self.usernameEntry.get().strip() == '':
#            result = DatabaseHelper.dbSelectRowByID('msg', 'msg_id', 55)
#            main.createMessageBox(0, result['msg_text'], self.selectEntry, [self.eFocus])
#            self.setFocus(0)
#        elif self.passwordEntry.get().strip() == '':
#            result = DatabaseHelper.dbSelectRowByID('msg', 'msg_id', 57)
#            main.createMessageBox(0, result['msg_text'], self.selectEntry, [self.eFocus])
#            self.setFocus(1)
#        elif main.startConnection():
#            main.login(self.usernameEntry.get().strip(), self.passwordEntry.get().strip())
#        else:
#            result = DatabaseHelper.dbSelectRowByID('msg', 'msg_id', 45)
#            main.createMessageBox(0, result['msg_text'], self.selectEntry, [self.eFocus])
        main.switchEnvironment('LobbyHeader')

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
            print 'Unloading Login...'
        main.audioManager.removeMusic()

        self.actorPace.clearToInitial()

        self.actorObject.unloadAnims()
        loader.unloadModel('models/bugs/' + self.actorModelFile)

        self.actorObject.cleanup()
        self.actorObject.removeNode()
        
        loader.unloadModel('models/maps/' + self.envModel)
        self.environ.removeNode()

        self.versionLabel.destroy()
        self.mainFrame.destroy()

        base.enableMouse()

        