
from common.Constants import Constants
from common.DirectBasicButton import DirectBasicButton
from common.DirectControls import DirectControls
from common.DirectTextField import DirectTextField
from common.DirectWindow import DirectWindow
from direct.gui.DirectGui import DGG
from direct.gui.DirectLabel import DirectLabel
from direct.gui.DirectOptionMenu import DirectOptionMenu
from direct.showbase.DirectObject import DirectObject
from panda3d.core import TextNode

#class NewWorldWindowControl(DirectControls):
#    
#    def __init__(self, parent):
#
#        DirectControls.__init__(self, parent)
#        self.accept('tab', parent.toggleEntry, [1])
#        self.accept('shift-tab', parent.toggleEntry, [-1])

class NewWorldWindowListener(DirectObject):
        
    def __init__(self, parent):
        self.accept(Constants.LISTENER_CREATE_NEW_WORLD_RESPONSE, parent.receiveMessageFromServer, [])

class NewWorldWindow:
    
    def __init__(self, parent):

        self.mainFrame = parent
        self.entryFocus = -1
        self.textLabelList = []
        self.registerEntry = []
        self.optionMenus = []
        self.privateSet = 1
        self.ecosystem = 'Savana'
        self.createNewWorldWindow()
        self.createTextLabelForNewWorldWindow()
        self.createTextEntryForNewWorldWindow()
        self.createNewWorldWindowButtons()
        
        self.createOptionsMenus()
        
    def createNewWorldWindow(self):
        """Create the main base frame."""
        self.newWorldFrame = DirectWindow(pos = (0,0,0),
#                                          image='models/edgespattern_632.png',
#                                          image_scale=(0.94, 0.9, 0.5),
                                          frameSize=(-0.8, 0.8, -0.5, 0.5),
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

        for i in range(4):
            self.textLabelList.append(DirectLabel(text='',
                                                   text_align=TextNode.ALeft,
                                                   text_fg=(0, 0, 0, 1),
                                                   text_font=Constants.FONT_TYPE_01,
                                                   text_scale=0.055,
                                                   frameColor=(0, 0, 0, 0),
                                                   pos=(-0.6, 0, 0.3 - i*0.15)))
            self.textLabelList[i].reparentTo(self.newWorldFrame)

        self.textLabelList[0]['text'] = 'World Name'
        self.textLabelList[1]['text'] = 'EcoSystem'
        self.textLabelList[2]['text'] = 'Public/Private'
        self.textLabelList[3]['text'] = 'Password'
        self.textLabelList[3].hide()
    
    def createTextEntryForNewWorldWindow(self):
        """Create entry boxes."""
#        for i in range(2):

        self.worldEntry = DirectTextField(self.newWorldFrame,
                                                       text_font=Constants.FONT_TYPE_01,
                                                       frameColor=(0.8, 0.8, 0.8, 0.7),
                                                       pos=(-0.1, 0, 0.3),
                                                       scale=0.055,
                                                       width=13,
                                                       numLines = 1,
                                                       focusInCommand=self.onWorldEntryFocus,
                                                       focusOutCommand=self.onWorldEntryFocusOut)
#                                                       command=self.submitText,))
        self.worldEntry.reparentTo(self.newWorldFrame)
        
        self.passwordEntry = DirectTextField(self.newWorldFrame,
                                                       text_font=Constants.FONT_TYPE_01,
                                                       frameColor=(0.8, 0.8, 0.8, 0.7),
                                                       pos=(-0.1, 0, -0.16),
                                                       obscured = 1,
                                                       numLines = 1,
                                                       scale=0.055,
                                                       width=13,
                                                       focusInCommand=self.onPasswordEntryFocus,
                                                       focusOutCommand=self.onPasswordEntryFocusOut)
        self.passwordEntry.reparentTo(self.newWorldFrame)

        self.passwordEntry.hide()
        
    def receiveMessageFromServer(self, success):
        
        if success == 0:
            self.unload()
            main.switchEnvironment("PvEWorldLobby")
        else:
            main.showAlert(58)    
             
    def createOptionsMenus(self):
        """create option menus for max players, ecosystem, and public/private world"""
        for i in range(2):
            self.optionMenus.append(DirectOptionMenu(text = "",
                                             text_pos = (-0.95, -0.22),
                                             text_scale = 0.75,
                                             scale = 0.1,
                                             initialitem = 0,
                                             frameSize = (-3.2, 3.2, -0.55, 0.55), 
                                             highlightColor = (0.9, 0.2, 0.1, 0.8),
                                             pos = (0.22, 0, 0.17 - i*0.15)))
            self.optionMenus[i].reparentTo(self.newWorldFrame)
            
        self.optionMenus[0]['items'] = ['Savana']
        self.optionMenus[1]['items'] = ['Public', 'Private']
        self.optionMenus[1]['command'] = self.showPasswordEntry 
        
    def createNewWorldWindowButtons(self):
        """Create some buttons."""
        self.submitButton = DirectBasicButton(text='Submit',
                                         text_font=Constants.FONT_TYPE_01,
                                         text_pos=(0, -0.015),
                                         text_scale=0.05,
                                         frameSize=(-0.13, 0.13, -0.05, 0.05),
                                         frameColor=(0.8, 0.8, 0.8, 0.7),
                                         pos=(-0.35, 0, -0.35),
                                         relief=DGG.FLAT,
                                         command=self.submit)
        self.submitButton.reparentTo(self.newWorldFrame)

        self.cancel = DirectBasicButton(text='Cancel',
                                         text_font=Constants.FONT_TYPE_01,
                                         text_pos=(0, -0.015),
                                         text_scale=0.05,
                                         frameSize=(-0.13, 0.13, -0.05, 0.05),
                                         frameColor=(0.8, 0.8, 0.8, 0.7),
                                         pos=(0, 0, -0.35),
                                         relief=DGG.FLAT,
                                         command=self.hide)
        self.cancel.reparentTo(self.newWorldFrame)

        self.reset = DirectBasicButton(text='Reset',
                                        text_font=Constants.FONT_TYPE_01,
                                        text_pos=(0, -0.015),
                                        text_scale=0.05,
                                        frameSize=(-0.13, 0.13, -0.05, 0.05),
                                        frameColor=(0.8, 0.8, 0.8, 0.7),
                                        pos=(0.35, 0, -0.35),
                                        relief=DGG.FLAT,
                                        command=self.resetText)
        self.reset.reparentTo(self.newWorldFrame)
         
    def resetText(self):
        """Clear all entry text fields."""
        self.worldEntry.set('')
        self.passwordEntry.set('')
        self.worldEntry['focus'] = 1

    def submit(self):
        
        if self.worldEntry.get().strip() == '':
            main.createMessageBox(0, 'World name cannot be empty')
            return;
        elif self.privateSet == 0 and self.passwordEntry.get().strip() == '':
            main.createMessageBox(0, 'Password cannot be empty')
            return;
        
        worldName = self.worldEntry.get().strip()
        password = ''
        if self.privateSet == 0:
                password = self.passwordEntry.get().strip()
        rContents = {'worldType' : 1, 'worldName': worldName, 'ecosystem' : self.ecosystem, 
                   'maxPlayerNumber': 1, 'privacyType' : self.privateSet,
                   'password' :  password}
        main.cManager.sendRequest(Constants.CMSG_CREATE_NEW_WORLD, rContents)

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
         
    def showPasswordEntry(self, arg):
        
        if arg == 'Private':
            self.privateSet = 0
            self.textLabelList[3].show()
            self.passwordEntry.show()
        else:
            self.privateSet = 1
            self.textLabelList[3].hide()
            self.passwordEntry.hide()
        
    def unload(self):
        self.newWorldFrame.destroy()    