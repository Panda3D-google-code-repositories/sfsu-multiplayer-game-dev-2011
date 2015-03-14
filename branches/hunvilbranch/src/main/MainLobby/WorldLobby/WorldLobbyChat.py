'''
Created on Oct 23, 2011

@author: Wenhui
'''
from common.Constants import Constants
from common.DirectBasicButton import DirectBasicButton
from common.DirectTextField import DirectTextField
from direct.gui.DirectEntryScroll import DirectEntryScroll
from direct.gui.DirectFrame import DirectFrame
from direct.gui.DirectLabel import DirectLabel
from direct.gui.DirectSlider import DirectSlider
from main.Chatcontrol.Chat import Chat
from panda3d.core import TextNode, TransparencyAttrib
from direct.gui.DirectGui import DGG

class WorldLobbyChat:
    
    
    def __init__(self, parent=None, worldLobbyMode=0):
        
        self.mainFrame = parent
        self.worldLobbyMode = worldLobbyMode
        self.chatButtons = []
        self.chatLines = []
        self.maxItemsVisible = 23
        self.createChatButtons()
        self.createLog()
        self.createEntry()
        self.chat = Chat(self.chatEntry, self.scrollBar, self.chatLines,
                         self.sendButton, self.maxItemsVisible, Constants.CMSG_UNIVERSAL_CHAT, 24)
        self.setCommandForChat()
        
    def createChatButtons(self):

        self.buttonFrame = DirectFrame(frameSize=(-0.5, 0.5, -0.06, 0.06),
                                        frameColor=Constants.BG_COLOR,
                                        pos=(0.65, 0, 0.775))
        self.buttonFrame.reparentTo(self.mainFrame)
        
        for i in range(3):
            self.chatButtons.append(DirectBasicButton(text='',
                                            text_fg=Constants.TEXT_COLOR,
                                            text_font=Constants.FONT_TYPE_01,
                                            text_pos=(0, -0.015),
                                            text_scale=0.05,
                                            text_shadow=Constants.TEXT_SHADOW_COLOR,
                                            frameSize=(-0.14, 0.14, -0.05, 0.05),
                                            frameColor=Constants.CHAT_BUTTON_COLOR,
                                            pos=(-0.3 + i * 0.3, 0, -0.01),
                                            relief=DGG.FLAT))
#                                            command = self.setChatMode )
            self.chatButtons[i].reparentTo(self.buttonFrame)
            self.chatButtons[i].setTransparency(TransparencyAttrib.MAlpha)

        self.worldChatButton = self.chatButtons[0]
        self.worldChatButton['text'] = 'World'
        self.gameChatButton = self.chatButtons[1]
        if self.worldLobbyMode == 0:
            self.gameChatButton['text'] = 'PvP'
        else:
            self.gameChatButton['text'] = 'PvE'
        self.universalChatButton = self.chatButtons[2]
        self.universalChatButton['text'] = 'Universal'
        self.universalChatButton['frameColor'] = Constants.CHAT_BUTTON_FOCUS
        
    def createLog(self):

        self.chatLogFrame = DirectFrame(frameSize=(-0.65, 0.65, -0.7, 0.7),
                                         frameColor=Constants.BG_COLOR,
                                         pos=(0.8, 0, 0.015))
        self.chatLogFrame.reparentTo(self.mainFrame)

        for i in range(self.maxItemsVisible):
            chatLine = DirectLabel(text='',
                                    text_align=TextNode.ALeft,
                                    text_fg=Constants.TEXT_COLOR,
                                    text_pos=(-0.6, -0.01),
                                    text_scale=0.05,
                                    text_shadow=Constants.TEXT_SHADOW_COLOR,
                                    frameSize=(-0.6, 0.6, -0.03, 0.03),
                                    frameColor=(1, 0, 0, 0),
                                    pos=(-0.025, 0, 0.65 - i * 0.06))
            chatLine.reparentTo(self.chatLogFrame)
            self.chatLines.append(chatLine)

        self.scrollBar = DirectSlider(pos=(0.62, 0, -0.01),
                                       scale=0.13,
                                       value=1,
                                       range=(1, 0),
                                       scrollSize=1,
                                       pageSize=1,
                                       frameSize=(-0.03, 0.03, -5.1, 5.1),
                                       orientation=DGG.VERTICAL,
                                       thumb_frameSize=(-0.1, 0.1, -0.25, 0.25),
                                       thumb_relief=DGG.FLAT)
#                                       command = self.scrollChatLog )
        self.scrollBar.reparentTo(self.chatLogFrame) 
           
    def createEntry(self):

        self.bottomFrame = DirectFrame(frameSize=(-0.65, 0.65, -0.08, 0.08),
                                        frameColor=Constants.BG_COLOR,
                                        pos=(0.8, 0, -0.765))
        self.bottomFrame.reparentTo(self.mainFrame)

        self.chatEntry = DirectTextField(self.mainFrame,
                                          text='',
                                          text_font=Constants.FONT_TYPE_01,
                                          frameColor=(0.8, 0.8, 0.8, 0.4),
                                          width=50,
                                          focusInCommand=self.onFocus,
                                          focusOutCommand=self.onFocusOut)

        self.chatEntryScroll = DirectEntryScroll(self.chatEntry,
                                                  pos=(-0.62, 0, -0.02),
                                                  scale=0.045,
                                                  clipSize=(0, 22, -6.05, 6.05))
        self.chatEntryScroll.reparentTo(self.bottomFrame)

        self.sendButton = DirectBasicButton(text='Send',
                                             text_fg=Constants.TEXT_COLOR,
                                             text_font=Constants.FONT_TYPE_01,
                                             text_pos=(0, -0.01),
                                             text_scale=0.045,
                                             text_shadow=Constants.TEXT_SHADOW_COLOR,
                                             frameSize=(-0.1, 0.1, -0.04, 0.04),
                                             frameColor=(0, 0, 0, 0.2),
                                             pos=(0.52, 0, -0.003),
                                             relief=DGG.FLAT)
#                                             command = self.switchToPvPWorldLobby)
        self.sendButton.reparentTo(self.bottomFrame)
        
    def setCommandForChat(self):
        self.scrollBar['command']=self.chat.scrollChatLog
        self.chatEntry['command']=self.chat.sendEvent
        self.sendButton['command']=self.chat.sendEvent
        self.worldChatButton['command']=self.setChatMode
        
        self.gameChatButton['command']=self.setChatMode
        
        self.universalChatButton['command']=self.setChatMode
        self.universalChatButton['extraArgs']=[Constants.CMSG_UNIVERSAL_CHAT, 2] 
        
        if self.worldLobbyMode == 0:
            self.worldChatButton['extraArgs']=[Constants.CMSG_PVPWORLD_CHAT, 0]  
            self.gameChatButton['extraArgs']=[Constants.CMSG_PVPGAME_CHAT, 1] 
        else:
            self.worldChatButton['extraArgs']=[Constants.CMSG_PVEWORLD_CHAT, 0]  
            self.gameChatButton['extraArgs']=[Constants.CMSG_PVEGAME_CHAT, 1]
             
    def setChatMode(self, mode, modeIndex):
        
        if modeIndex == 0:
            self.worldChatButton['frameColor']=Constants.CHAT_BUTTON_FOCUS
            self.gameChatButton['frameColor'] = Constants.CHAT_BUTTON_COLOR
            self.universalChatButton['frameColor']=Constants.CHAT_BUTTON_COLOR
        elif modeIndex == 1:
            self.worldChatButton['frameColor'] = Constants.CHAT_BUTTON_COLOR
            self.universalChatButton['frameColor']=Constants.CHAT_BUTTON_COLOR
            self.gameChatButton['frameColor'] = Constants.CHAT_BUTTON_FOCUS
        else:
            self.worldChatButton['frameColor'] = Constants.CHAT_BUTTON_COLOR
            self.universalChatButton['frameColor']=Constants.CHAT_BUTTON_FOCUS
            self.gameChatButton['frameColor'] = Constants.CHAT_BUTTON_COLOR
        self.chat.setChatMode(mode, modeIndex)

    def onFocus(self):
        self.chatEntry['frameColor'] = (0.8, 0.8, 0.8, 0.9)

    def onFocusOut(self):

        self.chatEntry['frameColor'] = (0.8, 0.8, 0.8, 0.4)
