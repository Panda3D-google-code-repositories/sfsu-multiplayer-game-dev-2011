from direct.actor.Actor import Actor
from direct.gui.DirectGui import DGG
from direct.gui.DirectGui import DirectFrame
from direct.gui.DirectGui import DirectLabel
from direct.gui.OnscreenText import OnscreenText
from direct.interval.IntervalGlobal import Func
from direct.interval.IntervalGlobal import Sequence
from direct.interval.IntervalGlobal import Wait

from panda3d.core import Point3
from panda3d.core import TextNode

from common.Constants import Constants
from common.DatabaseHelper import DatabaseHelper
from common.DirectBasicButton import DirectBasicButton
from common.DirectTextField import DirectTextField
from common.DirectWindow import DirectWindow

from main.Login.LoginControls import LoginControls
from main.Login.WorldSelection import WorldSelection
from main.MainLobby.WorldLobby.PvPWorldLobby import WorldObj

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

        self.menuBox = WorldSelection(self)
        self.menuBox.setPos(0, 0, 0.1)
        self.menuBox.hide()

        # add background music to login screen
#        main.audioManager.setMusic('01.ogg')
        main.msgQ.addToCommandList(Constants.CMSG_AUTH, self.responseToLogin)
        main.msgQ.addToCommandList(Constants.CMSG_JOIN_PVE_WORLD, self.responseJoinPvEWorld)
        self.mainFrame.setControls(LoginControls(self))

        self.loginMsgBox = None

    def createMainFrame(self):
        """Create the main base frame."""
        # frameColor is defined as (R,G,B,A)
        self.mainFrame = DirectWindow( frameSize = (-0.512, 0.512, -0.362, 0.362),
                                       frameColor = Constants.BG_COLOR,
                                       pos = (0, 0, 0.1) )

        self.mainBox = DirectFrame( frameSize = (-0.5, 0.5, -0.35, 0.35),
                                    frameColor = (0, 0, 0, 0.25),
                                    pos = (0, 0, 0) )
        self.mainBox.reparentTo(self.mainFrame)

        self.blackFrame = DirectFrame( frameSize = (-2, 2, -2, 2),
                                       frameColor = (0, 0, 0, 0.3),
                                       pos = (0, 0, 0),
                                       state = DGG.NORMAL )
        self.blackFrame.reparentTo(self.mainFrame, 1)
        self.blackFrame.hide()

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
                                'eat': 'models/sparrow/sparrow-eat',
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
        interval07 = self.actorObject.actorInterval('eat',
                                                    loop = 0,
                                                    duration = 2.0, 
                                                    startFrame = 0,
                                                    endFrame = 2.0)
        intervalStill = self.actorObject.actorInterval('eat', loop = 0,
                                                       duration = 3.0,
                                                       startTime = 2.0, 
                                                       endTime = 3.0)
        intervalDie = self.actorObject.actorInterval('die', loop=0, duration = 2.0)
        intervalStartWalking = Func(self.controlAnimation, 1, self.actorObject, 'walk')
        intervalStartFlaping = Func(self.controlAnimation, 1, self.actorObject, 'flap')
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
        self.headerText = DirectLabel(text='World of Balance',
                                       text_align=TextNode.ACenter,
                                       frameSize=(-0.2, 0.2, 0.2, 0.2),
                                       text_fg=Constants.TEXT_COLOR,
                                       text_font=Constants.FONT_TYPE_01,
                                       text_scale=0.07,
                                       frameColor=(0, 0, 0, 0),
                                       pos=(0, 0, 0.23))
        self.headerText.reparentTo(self.mainFrame)

        self.usernameText = DirectLabel(text='User ID',
                                        text_align = TextNode.ARight,
                                         text_fg=Constants.TEXT_COLOR,
                                         text_font=Constants.FONT_TYPE_01,
                                         text_scale=0.06,
                                         frameColor=(0, 0, 0, 0),
                                         pos=(-0.19, 0, 0.067))
        self.usernameText.reparentTo(self.mainFrame)

        self.passwordText = DirectLabel(text='Password',
                                        text_align = TextNode.ARight,
                                         text_fg=Constants.TEXT_COLOR,
                                         text_font=Constants.FONT_TYPE_01,
                                         text_scale=0.06,
                                         frameColor=(0, 0, 0, 0),
                                         pos=(-0.19, 0, -0.075))
        self.passwordText.reparentTo(self.mainFrame)


    def createTextEntry(self):
        """Create entry boxes for credentials."""
        self.usernameEntry = DirectTextField(self.mainFrame,
                                              text_font=Constants.FONT_TYPE_01,
                                              scale=0.055,
                                              pos=(-0.14, 0, 0.055),
                                              command=self.submit,
                                              focus=1,
                                              focusInCommand=self.setFocus,
                                              focusInExtraArgs=[0],
                                              rolloverSound = None)
        self.usernameEntry.reparentTo(self.mainFrame)
        self.loginEntry.append(self.usernameEntry)
        
        self.passwordEntry = DirectTextField(self.mainFrame,
                                              text_font=Constants.FONT_TYPE_01,
                                              scale=0.055,
                                              pos=(-0.14, 0, -0.08),
                                              command=self.submit,
                                              obscured=1,
                                              focusInCommand=self.setFocus,
                                              focusInExtraArgs=[1],
                                              rolloverSound = None)
        self.passwordEntry.reparentTo(self.mainFrame)
        self.loginEntry.append(self.passwordEntry)

    def createButtons(self):
        """Create some buttons."""
        self.validateLoginFrame = DirectFrame( frameSize = (-0.131, 0.131, -0.056, 0.056),
                                               frameColor = Constants.BG_COLOR,
                                               pos = (-0.2, 0, -0.22) )
        self.validateLoginFrame.reparentTo(self.mainBox)

        self.validateLogin = DirectBasicButton (text='Log In',
                                                 text_fg=Constants.TEXT_COLOR,
                                                 text_font=Constants.FONT_TYPE_01,
                                                 text_pos=(0, -0.015),
                                                 text_scale=0.05,
                                                 frameSize=(-0.125, 0.125, -0.05, 0.05),
                                                 frameColor=(0, 0, 0, 0.2),
                                                 relief=DGG.FLAT,
                                                 pos=(0, 0, 0),
                                                 command=self.submit,
                                                 clickSound = None,
                                                 rolloverSound = None)
        self.validateLogin.reparentTo(self.validateLoginFrame)

        self.registerButtonFrame = DirectFrame( frameSize = (-0.131, 0.131, -0.056, 0.056),
                                                frameColor = Constants.BG_COLOR,
                                                pos = (0.2, 0, -0.22) )
        self.registerButtonFrame.reparentTo(self.mainBox)

        self.registerButton = DirectBasicButton(text='Register',
                                                 text_fg=Constants.TEXT_COLOR,
                                                 text_font=Constants.FONT_TYPE_01,
                                                 text_pos=(0, -0.015),
                                                 text_scale=0.05,
                                                 frameSize=(-0.125, 0.125, -0.05, 0.05),
                                                 frameColor=(0, 0, 0, 0.2),
                                                 relief=DGG.FLAT,
                                                 pos=(0, 0, 0),
                                                 command=self.register,
                                                 clickSound = None,
                                                 rolloverSound = None)
        self.registerButton.reparentTo(self.registerButtonFrame)

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
        if self.loginMsgBox == None:
            if self.usernameEntry.get().strip() == '':
                result = DatabaseHelper.dbSelectRowByID('msg', 'msg_id', 55)
                main.createMessageBox(0, 'User ID Required', self.selectEntry, [self.eFocus])
                self.setFocus(0)
            elif self.passwordEntry.get().strip() == '':
                result = DatabaseHelper.dbSelectRowByID('msg', 'msg_id', 57)
                main.createMessageBox(0, result['msg_text'], self.selectEntry, [self.eFocus])
                self.setFocus(1)
            elif main.startConnection():
                main.login(self.usernameEntry.get().strip(), self.passwordEntry.get().strip())
                self.loginMsgBox = main.createMessageBox(2, 'Connecting...')
                self.blackFrame.show()
            else:
                result = DatabaseHelper.dbSelectRowByID('msg', 'msg_id', 45)
                main.createMessageBox(0, result['msg_text'], self.selectEntry, [self.eFocus])

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
        self.blackFrame.hide()

    def selectEntry(self, eNum):
        """Focus on a specific entry box."""
        for eObject in self.loginEntry:
            eObject['focus'] = 0

        self.loginEntry[eNum]['focus'] = 1

    def responseToLogin(self, args):
        """Create failed login box."""
        if self.loginMsgBox:
            main.removeMessageBox(self.loginMsgBox)
            self.loginMsgBox = None

        status = args['status']

        if status == 0:
            Constants.USER_ID = args['user_id']
            main.msgQ.addToPendingObj(Constants.USER_ID, Constants.USER_ID)

            self.mainFrame.hide()
            self.blackFrame.hide()

            self.menuBox.setAvatarList(args['avatarList'])
            self.menuBox.setWorldList(args['worldList'])
            self.menuBox.show()
        elif status == 1:
            result = DatabaseHelper.dbSelectRowByID('msg', 'msg_id', 68)
            main.createMessageBox(0, result['msg_text'], self.selectEntry, [self.eFocus])
        elif status == 2:
            result = DatabaseHelper.dbSelectRowByID('msg', 'msg_id', 69)
            main.createMessageBox(0, result['msg_text'], self.selectEntry, [self.eFocus])
        elif status == 3:
            result = DatabaseHelper.dbSelectRowByID('msg', 'msg_id', 81)
            main.createMessageBox(0, result['msg_text'], self.selectEntry, [self.eFocus])

    def responseJoinPvEWorld(self, status):

        if status == 0:
#            main.msgQ.addToPendingObj(Constants.WORLD_NAME, self.worldName)
#            main.msgQ.addToPendingObj(Constants.WORLD_TYPE, 0)
            main.switchEnvironment("WorldGUI")
        else:
            ## This should show the error to join the world
            main.showAlert(58)

    def unload(self):
        """Unload this instance."""
        if Constants.DEBUG:
            print 'Unloading Login...'
        main.audioManager.removeMusic()
        main.msgQ.removeEvent(Constants.CMSG_AUTH)
        
        self.actorPace.clearToInitial()

        self.actorObject.unloadAnims()
        loader.unloadModel('models/bugs/' + self.actorModelFile)

        self.actorObject.cleanup()
        self.actorObject.removeNode()
        
        loader.unloadModel('models/maps/' + self.envModel)
        self.environ.removeNode()

        self.versionLabel.destroy()
        self.mainFrame.destroy()
        self.menuBox.destroy()
        self.blackFrame.destroy()

        base.enableMouse()

        