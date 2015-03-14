from common.Constants import Constants
from common.DirectBasicButton import DirectBasicButton
from common.DirectControls import DirectControls
from common.DirectTextField import DirectTextField
from common.DirectWindow import DirectWindow
from direct.gui.DirectGui import DGG
from direct.gui.DirectLabel import DirectLabel
from direct.gui.DirectOptionMenu import DirectOptionMenu
from direct.showbase.DirectObject import DirectObject
from main.MainLobby.WorldLobby.PvPWorldLobby import WorldObj
from panda3d.core import TextNode

class NewGameWindowControl(DirectControls):
    
    def __init__(self, parent):

        DirectControls.__init__(self, parent)
        self.accept('tab', parent.toggleEntry, [1])
        self.accept('shift-tab', parent.toggleEntry, [-1])
        
class NewGameWindowListener(DirectObject):
        
    def __init__(self, parent):
        self.accept(Constants.LISTENER_CREATE_NEW_GAME_RESPONSE, parent.receiveMessageFromServer, [])

class NewPvPWorldWindow:
    '''
    classdocs
    '''

    def __init__(self,parent):

        self.mainFrame = parent
        self.entryFocus = -1
        self.textLabelList = []
        self.registerEntry = []
        self.optionMenus = []
        self.privateSet = 1
        self.maxPlayer = 10
        self.worldName=""
        self.ecosystem = 'Savana'
        self.createNewWorldWindow()
        self.createTextLabelForNewWorldWindow()
        self.createTextEntryForNewWorldWindow()
        self.createNewWorldWindowButtons()
        self.listener = NewGameWindowListener(self)
        self.createOptionsMenus()
        
    def createNewWorldWindow(self):
        """Create the main base frame."""
        self.newWorldFrame = DirectWindow(pos = (0,0,0),
#                                          image='models/edgespattern_632.png',
#                                          image_scale=(0.94, 0.9, 0.5),
                                          frameSize=(-0.85, 0.85, -0.6, 0.6),
                                          frameColor=Constants.BG_COLOR,
                                          state=DGG.NORMAL)
        self.newWorldFrame.reparentTo(self.mainFrame)
        self.newWorldFrame.hide()
    
    def toggleVisibility(self):
        
        if self.newWorldFrame.isHidden():
            self.newWorldFrame.show()
        else:
            self.newWorldFrame.hide()
            
    def show(self):
        self.newWorldFrame.show()
#    
    def hide(self):
        self.newWorldFrame.hide()
            
    def createTextLabelForNewWorldWindow(self):
        """Create label for the text entry."""

        for i in range(5):
            self.textLabelList.append(DirectLabel(text='',
                                                   text_align=TextNode.ALeft,
                                                   text_fg=(0, 0, 0, 1),
                                                   text_font=Constants.FONT_TYPE_01,
                                                   text_scale=0.055,
                                                   frameColor=(0, 0, 0, 0),
                                                   pos=(-0.6, 0, 0.35 - i*0.15)))
            self.textLabelList[i].reparentTo(self.newWorldFrame)

        self.textLabelList[0]['text'] = 'World Name'
        self.textLabelList[1]['text'] = 'Max Players'
        self.textLabelList[2]['text'] = 'EcoSystem'
        self.textLabelList[3]['text'] = 'Public/Private'
        self.textLabelList[4]['text'] = 'Password'
        self.textLabelList[4].hide()
    
    def receiveMessageFromServer(self, success):
        print 'pve world status: '+str(success)
        if success == 0:
            self.unload()
            main.switchEnvironment("PvPWorldLobby")
        else:
            main.showAlert(58)
        
    def createTextEntryForNewWorldWindow(self):
        """Create entry boxes."""
        self.worldEntry = DirectTextField(self.newWorldFrame,
                                                       text_font=Constants.FONT_TYPE_01,
                                                       frameColor=(0.8, 0.8, 0.8, 0.7),
                                                       pos=(-0.1, 0, 0.35),
                                                       scale=0.055,
                                                       width=13,
                                                       numLines = 1,
                                                       focusInCommand=self.onWorldEntryFocus,
                                                       focusOutCommand=self.onWorldEntryFocusOut)
        self.worldEntry.reparentTo(self.newWorldFrame)
        
        self.passwordEntry = DirectTextField(self.newWorldFrame,
                                                       text_font=Constants.FONT_TYPE_01,
                                                       frameColor=(0.8, 0.8, 0.8, 0.7),
                                                       pos=(-0.1, 0, -0.27),
                                                       obscured = 1,
                                                       numLines = 1,
                                                       scale=0.055,
                                                       width=13,
                                                       focusInCommand=self.onPasswordEntryFocus,
                                                       focusOutCommand=self.onPasswordEntryFocusOut)
        self.passwordEntry.reparentTo(self.newWorldFrame)

        self.passwordEntry.hide()
        
    def createOptionsMenus(self):
        """create option menus for max players, ecosystem, and public/private world"""
        for i in range(3):
            self.optionMenus.append(DirectOptionMenu(text = "",
                                             text_pos = (-0.95, -0.22),
                                             text_scale = 0.75,
                                             scale = 0.1,
                                             initialitem = 0,
                                             frameSize = (-3.2, 3.2, -0.55, 0.55), 
                                             highlightColor = (0.9, 0.2, 0.1, 0.8),
                                             pos = (0.22, 0, 0.22 - i*0.15)))
            self.optionMenus[i].reparentTo(self.newWorldFrame)
            
        self.optionMenus[0]['items'] = ['10', '8', '6', '4', '2']
        self.optionMenus[1]['items'] = ['Savana']
        self.optionMenus[2]['items'] = ['Public', 'Private']
        
        self.optionMenus[0]['command'] = self.getMaxPlayers
        self.optionMenus[1]['command'] = self.getEcosystem
        self.optionMenus[2]['command'] = self.showPasswordEntry 
        
    def createNewWorldWindowButtons(self):
        """Create some buttons."""
        self.submit = DirectBasicButton(text='Submit',
                                         text_font=Constants.FONT_TYPE_01,
                                         text_pos=(0, -0.015),
                                         text_scale=0.05,
                                         frameSize=(-0.13, 0.13, -0.05, 0.05),
                                         frameColor=(0.8, 0.8, 0.8, 0.7),
                                         pos=(-0.35, 0, -0.45),
                                         relief=DGG.FLAT,
                                         command=self.submit)
        self.submit.reparentTo(self.newWorldFrame)

        self.cancel = DirectBasicButton(text='Cancel',
                                         text_font=Constants.FONT_TYPE_01,
                                         text_pos=(0, -0.015),
                                         text_scale=0.05,
                                         frameSize=(-0.13, 0.13, -0.05, 0.05),
                                         frameColor=(0.8, 0.8, 0.8, 0.7),
                                         pos=(0, 0, -0.45),
                                         relief=DGG.FLAT,
                                         command=self.hide)
        self.cancel.reparentTo(self.newWorldFrame)

        self.reset = DirectBasicButton(text='Reset',
                                        text_font=Constants.FONT_TYPE_01,
                                        text_pos=(0, -0.015),
                                        text_scale=0.05,
                                        frameSize=(-0.13, 0.13, -0.05, 0.05),
                                        frameColor=(0.8, 0.8, 0.8, 0.7),
                                        pos=(0.35, 0, -0.45),
                                        relief=DGG.FLAT,
                                        command=self.resetText)
        self.reset.reparentTo(self.newWorldFrame)
         
    def resetText(self):
        """Clear all entry text fields."""
        self.worldEntry.set('')
        self.passwordEntry.set('')
        self.worldEntry['focus'] = 1

    def onWorldEntryFocus(self):
        self.worldEntry['frameColor'] = (0.8, 0.8, 0.8, 0.9)
        self.newWorldFrame.getControls().enable()

    def onWorldEntryFocusOut(self):
        self.worldEntry['frameColor'] = (0.8, 0.8, 0.8, 0.4)
        self.newWorldFrame.getControls().disable()
    def onPasswordEntryFocus(self):
        self.passwordEntry['frameColor'] = (0.8, 0.8, 0.8, 0.9)
        self.newWorldFrame.getControls().enable()

    def onPasswordEntryFocusOut(self):
        self.passwordEntry['frameColor'] = (0.8, 0.8, 0.8, 0.4)
        self.newWorldFrame.getControls().disable()  
    
    def submit(self):
        print "submit request"
        if self.worldEntry.get().strip() == '':
            main.createMessageBox(0, 'World name cannot be empty')
            return;
        
        if (self.privateSet == 0) and (self.passwordEntry.get().strip() == ''):
            main.createMessageBox(0, 'Password cannot be empty')
            return;
        
        self.worldName = self.worldEntry.get().strip()
        password = ''
        if self.privateSet == 0:
            password = self.passwordEntry.get().strip()
            print 'password: '+str(password)
        rContents = {'worldType' : 2, 'worldName': self.worldName, 'ecosystem' : self.ecosystem, 
                   'maxPlayerNumber': self.maxPlayer, 'privacyType' : self.privateSet,
                   'password' :  password}
        main.cManager.sendRequest(Constants.CMSG_CREATE_NEW_WORLD, rContents)
            
    def getEcosystem(self, arg):
        self.ecosystem = arg
        
    def getMaxPlayers(self, arg):
        self.maxPlayer = arg
        
    def showPasswordEntry(self, arg):
        
        if arg == 'Private':
            self.privateSet = 0
            self.textLabelList[4].show()
            self.passwordEntry.show()
        else:
            self.privateSet = 1
            self.textLabelList[4].hide()
            self.passwordEntry.hide()
        
    def unload(self):
        self.newWorldFrame.destroy()