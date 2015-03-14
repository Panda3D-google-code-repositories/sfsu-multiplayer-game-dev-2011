from common.Constants import Constants
from common.DirectBasicButton import DirectBasicButton
from common.DirectTextField import DirectTextField
from common.DirectWindow import DirectWindow
from direct.gui.DirectGui import DGG, DirectLabel
from panda3d.core import TextNode



class MessageBoxWithEntry:

    def __init__(self, text):
        """
        PvP is 0, PvE is 1
        
        """
        
        self.text = text # this is the name of the game

        self.maxWidth = 18

        self.textNode = TextNode('textNode')
        self.textNode.setText(self.text)
        self.textNode.setWordwrap(self.maxWidth)


        self.createMainFrame()
        self.createButtons()
        self.createPasswordEntry()
        
    def createMainFrame(self):

        self.mainFrame = DirectWindow( frameSize = (-0.4, 0.4, -0.3, 0.3),
                                       frameColor = Constants.BG_COLOR,
                                       pos = (0, 0, 0),
                                       state = DGG.NORMAL )
        self.mainFrame.reparentTo(aspect2d, 10)

        self.textBox = DirectLabel( text = 'Password require',
                                    text_fg = Constants.TEXT_COLOR,
                                    text_font = Constants.FONT_TYPE_01,
                                    text_pos = (0, 0.15),
                                    text_scale = 0.05,
                                    text_shadow = Constants.TEXT_SHADOW_COLOR,
                                    text_wordwrap = self.maxWidth,
                                    frameSize = (self.mainFrame['frameSize'][0] + 0.01, self.mainFrame['frameSize'][1] - 0.01,
                                                 self.mainFrame['frameSize'][2] + 0.01, self.mainFrame['frameSize'][3] - 0.01),
                                    frameColor = (0, 0, 0, 0.3) )
        self.textBox.reparentTo(self.mainFrame)

    def createPasswordEntry(self):
        
        self.passwordEntry = DirectTextField(self.mainFrame,
                                                       text_font=Constants.FONT_TYPE_01,
                                                       frameColor=(0.8, 0.8, 0.8, 0.7),
                                                       pos=(-0.27, 0, -0.01),
                                                       obscured = 1,
                                                       numLines = 1,
                                                       scale=0.055,
                                                       width=10,
                                                       command = self.submit,
                                                       focusInCommand=self.onPasswordEntryFocus,
                                                       focusOutCommand=self.onPasswordEntryFocusOut)
        self.passwordEntry.reparentTo(self.mainFrame)
        
    def createButtons(self):

#        if self.type == 0:
#            buttonList = ['Continue']
#        else:
        buttonList = ['Cancel', 'OK']

        text = ''
        for button in buttonList:
            text += button + '\n'

        self.textNode.setText(text)

        buttonWidth = 0.05 * self.textNode.getWidth()
        buttonHeight = 0.05

        self.button01 = DirectBasicButton( text = buttonList[0],
                                           text_fg = Constants.TEXT_COLOR,
                                           text_font = Constants.FONT_TYPE_01,
                                           text_pos = (0, -0.015),
                                           text_scale = 0.05,
                                           text_shadow = Constants.TEXT_SHADOW_COLOR,
                                           frameSize = (-buttonWidth / 2 - 0.025, buttonWidth / 2 + 0.025,
                                                        -buttonHeight / 2 - 0.025, buttonHeight / 2 + 0.025),
                                           frameColor = (0, 0, 0, 0.2),
                                           relief = DGG.FLAT,
                                           command = self.cancel)
        self.button01.reparentTo(self.mainFrame)


        self.button01.setPos(-0.1 - buttonWidth / 2, 0, self.mainFrame['frameSize'][2] + 0.11)

        self.button02 = DirectBasicButton( text = buttonList[1],
                                               text_fg = Constants.TEXT_COLOR,
                                               text_font = Constants.FONT_TYPE_01,
                                               text_pos = (0, -0.015),
                                               text_scale = 0.05,
                                               text_shadow = Constants.TEXT_SHADOW_COLOR,
                                               frameSize = (-buttonWidth / 2 - 0.025, buttonWidth / 2 + 0.025,
                                                            -buttonHeight / 2 - 0.025, buttonHeight / 2 + 0.025),
                                               frameColor = (0, 0, 0, 0.2),
                                               relief = DGG.FLAT,
                                               pos = (0.1 + buttonWidth / 2, 0, self.mainFrame['frameSize'][2] + 0.11),
                                               command = self.submit)
        self.button02.reparentTo(self.mainFrame)
            
    def onPasswordEntryFocus(self):
        self.passwordEntry['frameColor'] = (0.8, 0.8, 0.8, 0.9)

    def onPasswordEntryFocusOut(self):
        self.passwordEntry['frameColor'] = (0.8, 0.8, 0.8, 0.4)
         
    def submit(self, extraArgs = []):
        
#        if self.worldType == 0:
#            msgType = Constants.CMSG_SEARCH_PRIVATE_WORLD
#        else:
#            msgType = Constants.CMSG_PVE_JOIN_REQUEST
            
        if self.passwordEntry.get().strip() != '':
#            print 'submit request for private world: worldname is: '+self.text +' password is: '+str(self.passwordEntry.get().strip())
            rContents = {'worldName' : self.text, 'password': self.passwordEntry.get().strip()}
            main.cManager.sendRequest(Constants.CMSG_SEARCH_PRIVATE_WORLD, rContents)
            self.destroy()

    def cancel(self):
        self.mainFrame.destroy()

    def destroy(self):
        self.mainFrame.destroy()
