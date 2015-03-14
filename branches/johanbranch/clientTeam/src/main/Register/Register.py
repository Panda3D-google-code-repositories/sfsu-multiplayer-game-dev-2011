
from hashlib import md5
from re import match

from direct.gui.DirectGui import DGG
from direct.gui.DirectGui import DirectLabel
from direct.gui.OnscreenImage import OnscreenImage

from panda3d.core import TextNode
from panda3d.core import TransparencyAttrib

from common.Constants import Constants
from common.DatabaseHelper import DatabaseHelper
from common.DirectBasicButton import DirectBasicButton
from common.DirectTextField import DirectTextField
from common.DirectWindow import DirectWindow

from main.Register.RegisterControls import RegisterControls

class Register:

    def __init__(self):

        if Constants.DEBUG:
            print 'Loading Register...'

        self.eFocus = -1
        self.registerEntry = []

        base.disableMouse()

        self.textLabelList = []

        self.createBackground()
        self.createMainFrame()
        self.createTextNodes()
        self.createTextEntries()
        self.createButtons()

        main.audioManager.setMusic('01.ogg')

        self.mainFrame.setControls(RegisterControls(self))

    def createMainFrame(self):
        """Create the main base frame."""
        self.mainFrame = DirectWindow(frameSize=(-0.95, 0.95, -0.85, 0.85),
                                       frameColor=(0, 0, 0, 0),
                                       state=DGG.NORMAL)

        self.menuTop = OnscreenImage(image='models/poc_title_signupplay_632.png',
                                      pos=(0, 0, 0.7),
                                      scale=(0.94, 1, 0.14))
        self.menuTop.reparentTo(self.mainFrame)

        self.menuEdges = OnscreenImage(image='models/edgespattern_632.png',
                                        pos=(0, 0, -0.07),
                                        scale=(0.94, 1, 0.65))
        self.menuEdges.reparentTo(self.mainFrame)

        self.menuBottom = OnscreenImage(image='models/bottom_632.png',
                                         pos=(0, 0, -0.75),
                                         scale=(0.94, 1, 0.08))
        self.menuBottom.reparentTo(self.mainFrame)

    def createBackground(self):
        """Create a background for the registration screen."""
        self.envModel = 'loginScene/environment'

        self.environ = loader.loadModel('models/maps/' + self.envModel)
        self.environ.reparentTo(render)

        self.environ.setPos(0, 42, -7)
        self.environ.setScale(0.16)

    def createTextNodes(self):
        """Create some text."""
        self.osNP = DirectLabel(text='Sign up now - it is quick, easy and free!!',
                                 text_fg=(0.3, 0, 0, 1),
                                 text_font=Constants.FONT_TYPE_01,
                                 text_scale=0.09,
                                 frameColor=(0, 0, 0, 0),
                                 pos=(0, 0, 0.45))
        self.osNP.reparentTo(self.mainFrame)

        for i in range(5):
            self.textLabelList.append(DirectLabel(text='',
                                                   text_align=TextNode.ALeft,
                                                   text_fg=(0, 0, 0, 1),
                                                   text_font=Constants.FONT_TYPE_01,
                                                   text_scale=0.055,
                                                   frameColor=(0, 0, 0, 0),
                                                   pos=(-0.65, 0, 0.25 - i * 0.15)))
            self.textLabelList[i].reparentTo(self.mainFrame)

        self.textLabelList[0]['text'] = 'Username'
        self.textLabelList[1]['text'] = 'Password'
        self.textLabelList[2]['text'] = 'Confirm Password'
        self.textLabelList[3]['text'] = 'E-mail Address'
        self.textLabelList[4]['text'] = 'Character Name'

    def createTextEntries(self):
        """Create some entry boxes."""
        for i in range(5):
            self.registerEntry.append(DirectTextField(self.mainFrame,
                                                       text_font=Constants.FONT_TYPE_01,
                                                       frameColor=(0.8, 0.8, 0.8, 0.7),
                                                       pos=(-0.1, 0, 0.25 - i * 0.15),
                                                       scale=0.055,
                                                       width=13,
                                                       command=self.submitText,
                                                       focusInCommand=self.setFocus,
                                                       focusInExtraArgs=[i]))
            self.registerEntry[i].reparentTo(self.mainFrame)

        self.registerEntry[0]['focus'] = 1
        self.registerEntry[1]['obscured'] = 1
        self.registerEntry[2]['obscured'] = 1

    def createButtons(self):
        """Create some buttons."""
        self.submit = DirectBasicButton(text='Submit',
                                         text_font=Constants.FONT_TYPE_01,
                                         text_pos=(0, -0.015),
                                         text_scale=0.05,
                                         frameSize=(-0.13, 0.13, -0.05, 0.05),
                                         frameColor=(0.8, 0.8, 0.8, 0.7),
                                         pos=(-0.35, 0, -0.55),
                                         relief=DGG.FLAT,
                                         command=self.submitText)
        self.submit.reparentTo(self.mainFrame)

        self.cancel = DirectBasicButton(text='Cancel',
                                         text_font=Constants.FONT_TYPE_01,
                                         text_pos=(0, -0.015),
                                         text_scale=0.05,
                                         frameSize=(-0.13, 0.13, -0.05, 0.05),
                                         frameColor=(0.8, 0.8, 0.8, 0.7),
                                         pos=(0, 0, -0.55),
                                         relief=DGG.FLAT,
                                         command=self.login)
        self.cancel.reparentTo(self.mainFrame)

        self.reset = DirectBasicButton(text='Reset',
                                        text_font=Constants.FONT_TYPE_01,
                                        text_pos=(0, -0.015),
                                        text_scale=0.05,
                                        frameSize=(-0.13, 0.13, -0.05, 0.05),
                                        frameColor=(0.8, 0.8, 0.8, 0.7),
                                        pos=(0.35, 0, -0.55),
                                        relief=DGG.FLAT,
                                        command=self.resetText)
        self.reset.reparentTo(self.mainFrame)


    def submitText(self, text=None):
        """Submit credentials to the server."""
        for i in range(5):
            self.registerEntry[i].enterText(self.registerEntry[i].get().strip())
            
        if self.registerEntry[0].get() == '':
            result = DatabaseHelper.dbSelectRowByID('msg', 'msg_id', 55)
            main.createMessageBox(0, result['msg_text'], self.selectEntry, [0])
            self.setFocus(0)
        elif self.registerEntry[1].get() == '':
            result = DatabaseHelper.dbSelectRowByID('msg', 'msg_id', 57)
            main.createMessageBox(0, result['msg_text'], self.selectEntry, [1])
            self.setFocus(1)
        elif self.registerEntry[2].get() == '':
            result = DatabaseHelper.dbSelectRowByID('msg', 'msg_id', 58)
            main.createMessageBox(0, result['msg_text'], self.selectEntry, [2])
            self.setFocus(2)
        elif self.registerEntry[3].get() == '':
            result = DatabaseHelper.dbSelectRowByID('msg', 'msg_id', 59)
            main.createMessageBox(0, result['msg_text'], self.selectEntry, [3])
            self.setFocus(3)
        elif match('^[a-zA-Z0-9._%-+]+@[a-zA-Z0-9._%-]+.[a-zA-Z]{2,6}$', self.registerEntry[3].get()) == None:
            result = DatabaseHelper.dbSelectRowByID('msg', 'msg_id', 60)
            main.createMessageBox(0, result['msg_text'], self.selectEntry, [3])
            self.setFocus(3)
        elif self.registerEntry[4].get() == '':
            result = DatabaseHelper.dbSelectRowByID('msg', 'msg_id', 61)
            main.createMessageBox(0, result['msg_text'], self.selectEntry, [4])
            self.setFocus(4)
        elif main.startConnection():
            rContents = {
                         'userName'     : self.registerEntry[0].get(),
                         'password'     : md5(self.registerEntry[1].get()).hexdigest(),
                         'confirm'      : md5(self.registerEntry[2].get()).hexdigest(),
                         'email'        : self.registerEntry[3].get(),
                         'charName'    : self.registerEntry[4].get()
            }
            
            main.cManager.sendRequest(Constants.CMSG_REGISTER, rContents)
        else:
            result = DatabaseHelper.dbSelectRowByID('msg', 'msg_id', 45)
            main.createMessageBox(0, result['msg_text'], self.selectEntry, [self.eFocus])

    def resetText(self):
        """Clear all entry text fields."""
        for eObject in self.registerEntry:
            eObject.set('')
        self.selectEntry(0)

    def login(self):
        """Switch to the login screen."""
        main.switchEnvironment('Login')

    def toggleEntry(self, direction):
        """Toggle through the entry boxes."""
        self.eFocus = (self.eFocus + direction + len(self.registerEntry)) % len(self.registerEntry)
        self.selectEntry(self.eFocus)

    def setFocus(self, eNum):
        """Store current entry box number."""
        self.eFocus = eNum

    def selectEntry(self, eNum):
        """Focus on a specific entry box."""
        for eObject in self.registerEntry:
            eObject['focus'] = 0

        self.registerEntry[eNum]['focus'] = 1

    def showAlert(self, status):
        """Create failed registration box."""
        if status == 1:
            result = DatabaseHelper.dbSelectRowByID('msg', 'msg_id', 47)
            main.createMessageBox(0, result['msg_text'], self.selectEntry, [self.eFocus])
        elif status == 2:
            result = DatabaseHelper.dbSelectRowByID('msg', 'msg_id', 48)
            main.createMessageBox(0, result['msg_text'], self.selectEntry, [self.eFocus])

    def showConfirm(self):
        """Display the registration complete box."""
        result = DatabaseHelper.dbSelectRowByID('msg', 'msg_id', 49)
        main.createMessageBox(0, result['msg_text'], self.login)

#    def prevImage(self):
#        """Cycle previous avatar image."""
#        self.pictureIndex -= 1
#        self.pictureIndex += len(self.characterImageArray)
#        self.pictureIndex %= len(self.characterImageArray)
#
#        self.menu.setImage('models/avatar/' + self.characterImageArray[self.pictureIndex])
#        self.menu.setTransparency(TransparencyAttrib.MAlpha)

#    def nextImage(self):
#        """Cycle next avatar image."""
#        self.pictureIndex += 1
#        self.pictureIndex %= len(self.characterImageArray)
#
#        self.menu.setImage('models/avatar/' + self.characterImageArray[self.pictureIndex])
#        self.menu.setTransparency(TransparencyAttrib.MAlpha)

    def unload(self):
        """Unload this instance."""
        if Constants.DEBUG:
            print 'Unloading Register...'

        main.audioManager.removeMusic()

        loader.unloadModel('models/maps/' + self.envModel)
        self.environ.removeNode()

        self.mainFrame.destroy()

        base.enableMouse()
