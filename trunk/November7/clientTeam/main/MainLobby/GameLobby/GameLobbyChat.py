'''
Created on Oct 23, 2011

@author: Wenhui
'''
from common.Constants import Constants
from common.DirectBasicButton import DirectBasicButton
from common.DirectTextField import DirectTextField
from direct.gui.DirectEntryScroll import DirectEntryScroll
from direct.gui.DirectFrame import DirectFrame
from direct.gui.DirectGui import DGG
from direct.gui.DirectLabel import DirectLabel
from direct.gui.DirectSlider import DirectSlider
from main.Chatcontrol.Chat import Chat
from panda3d.core import TextNode, TransparencyAttrib

class GameLobbyChat:
    
    def __init__(self, parent=None,
                 gameLobbyMode=0):
        """
        0 is pvp, 1 is pve
        """
        self.mainFrame = parent
        self.gameLobbyMode = gameLobbyMode
        self.chatLines = []
        self.maxItemsVisible=5
        self.createButtons()
        self.createEntry()
        self.createLog()
        self.chat = Chat(self.chatEntry, self.scrollBar, self.chatLines,
                         self.sendButton, self.maxItemsVisible, Constants.CMSG_UNIVERSAL_CHAT, 60)
        self.setCommandForChat()  
              
    def createButtons(self):

        self.buttonFrame = DirectFrame( frameSize = (-0.35, 0.35, -0.07, 0.07),
                                        frameColor = Constants.BG_COLOR,
                                        pos = (-1.1, 0, -0.3) )
        self.buttonFrame.reparentTo(self.mainFrame)

        self.universalChatButton = DirectBasicButton( text = 'Universal',
                                            text_fg = Constants.TEXT_COLOR,
                                            text_font = Constants.FONT_TYPE_01,
                                            text_pos = (0, -0.015),
                                            text_scale = 0.05,
                                            text_shadow = Constants.TEXT_SHADOW_COLOR,
                                            frameSize = (-0.14, 0.14, -0.05, 0.05),
                                            frameColor = Constants.CHAT_BUTTON_FOCUS,
                                            pos = (-0.17, 0, 0),
                                            relief = DGG.FLAT)
#                                            command = self.setChatMode )
        self.universalChatButton.setTransparency(TransparencyAttrib.MAlpha)
        self.universalChatButton.reparentTo(self.buttonFrame)

        self.gameChatButton = DirectBasicButton( text ='',
                                            text_fg = Constants.TEXT_COLOR,
                                            text_font = Constants.FONT_TYPE_01,
                                            text_pos = (0, -0.015),
                                            text_scale = 0.05,
                                            text_shadow = Constants.TEXT_SHADOW_COLOR,
                                            frameSize = (-0.14, 0.14, -0.05, 0.05),
                                            frameColor = Constants.CHAT_BUTTON_COLOR,
                                            pos = (0.15, 0, 0),
                                            relief = DGG.FLAT)
        self.gameChatButton.reparentTo(self.buttonFrame)
        self.gameChatButton.setTransparency(TransparencyAttrib.MAlpha)
        
        if self.gameLobbyMode == 0:
            self.gameChatButton['text'] = 'PvP'
        else:
            self.gameChatButton['text'] = 'PvE'
    
    def getChatEntry(self):
        
        return self.chatEntry
    
    def createLog(self):

        self.chatLogFrame = DirectFrame( frameSize = (-1.45, 1.45, -0.18, 0.18),
                                         frameColor = Constants.BG_COLOR,
                                         pos = (0, 0, -0.55) )
        self.chatLogFrame.reparentTo(self.mainFrame)

        for i in range(self.maxItemsVisible):
            chatLine = DirectLabel( text = '',
                                    text_align = TextNode.ALeft,
                                    text_fg = Constants.TEXT_COLOR,
                                    text_pos = (-1.38, -0.01),
                                    text_scale = 0.05,
                                    text_shadow = Constants.TEXT_SHADOW_COLOR,
                                    frameSize = (-1.39, 1.41, -0.03, 0.03),
                                    frameColor = (1, 0, 0, 0),
                                    pos = (-0.035, 0, 0.106 - i * 0.06) )
            chatLine.reparentTo(self.chatLogFrame)
            self.chatLines.append(chatLine)

        self.scrollBar = DirectSlider(pos=(1.4, 0, -0.013),
                                       scale=0.13,
                                       value=1,
                                       range=(1, 0),
                                       scrollSize=1,
                                       frameSize=(-0.05, 0.05, -1.1, 1.1),
                                       pageSize=1,
                                       orientation=DGG.VERTICAL,
                                       thumb_frameSize=(-0.1, 0.1, -0.8, 0.8),
                                       thumb_relief=DGG.FLAT)
        self.scrollBar.reparentTo(self.chatLogFrame) 
           
    def createEntry(self):

        self.bottomFrame = DirectFrame(frameSize=(-1.45, 1.45, -0.08, 0.08),
                                        frameColor=Constants.BG_COLOR,
                                        pos=(0, 0, -0.81))
        self.bottomFrame.reparentTo(self.mainFrame)

        self.chatEntry = DirectTextField(self.mainFrame,
                                          text='',
                                          text_font=Constants.FONT_TYPE_01,
                                          frameColor=(0.8, 0.8, 0.8, 0.4),
                                          width=90,
#                                          command = self.chat.sendMsg,
                                          focusInCommand=self.onFocus,
                                          focusOutCommand=self.onFocusOut)

        self.chatEntryScroll = DirectEntryScroll(self.chatEntry,
                                                  pos=(-1.42, 0, -0.013),
                                                  scale=0.05,
                                                  clipSize=(0.0, 51.5, -1.05, 1.05))
        self.chatEntryScroll.reparentTo(self.bottomFrame)

        self.sendButton = DirectBasicButton(text='Send',
                                             text_fg=Constants.TEXT_COLOR,
                                             text_font=Constants.FONT_TYPE_01,
                                             text_pos=(0, -0.015),
                                             text_scale=0.045,
                                             text_shadow=Constants.TEXT_SHADOW_COLOR,
                                             frameSize=(-0.1, 0.1, -0.04, 0.04),
                                             frameColor=(0, 0, 0, 0.2),
                                             pos=(1.29, 0, 0.005),
                                             relief=DGG.FLAT)
        self.sendButton.reparentTo(self.bottomFrame)
        
    def setCommandForChat(self):
        
        self.scrollBar['command']=self.chat.scrollChatLog
        self.chatEntry['command']=self.chat.sendEvent
        self.sendButton['command']=self.chat.sendEvent
        self.universalChatButton['command']=self.setChatMode
        self.universalChatButton['extraArgs']=[Constants.CMSG_UNIVERSAL_CHAT, 0]
        self.gameChatButton['command']=self.setChatMode
        
        if self.gameLobbyMode == 0:
            self.gameChatButton['extraArgs']=[Constants.CMSG_PVPGAME_CHAT, 1]
        else:
            self.gameChatButton['extraArgs']=[Constants.CMSG_PVEGAME_CHAT, 1]
        
    def setChatMode(self, mode, modeIndex):
        
        if modeIndex == 0:
            self.universalChatButton['frameColor']=Constants.CHAT_BUTTON_FOCUS
            self.gameChatButton['frameColor'] = Constants.CHAT_BUTTON_COLOR
        else:
            self.universalChatButton['frameColor']=Constants.CHAT_BUTTON_COLOR
            self.gameChatButton['frameColor'] = Constants.CHAT_BUTTON_FOCUS
        self.chat.setChatMode(mode, modeIndex)
          
    def onFocus(self):
        self.chatEntry['frameColor'] = (0.8, 0.8, 0.8, 0.9)
#        self.mainFrame.getControls().enable()

    def onFocusOut(self):

        self.chatEntry['frameColor'] = (0.8, 0.8, 0.8, 0.4)
#        self.mainFrame.getControls().disable()  
             
    def hide(self):
        self.bottomFrame.hide()
        self.chatLogFrame.hide()
        self.buttonFrame.hide()
        
    def show(self):
        self.bottomFrame.show()
        self.chatLogFrame.show()
        self.buttonFrame.show()