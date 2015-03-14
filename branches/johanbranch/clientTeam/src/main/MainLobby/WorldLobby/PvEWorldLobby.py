
from common.Constants import Constants
from common.DirectBasicButton import DirectBasicButton
from common.DirectTextField import DirectTextField
from common.DirectWindow import DirectWindow
from direct.gui.DirectEntryScroll import DirectEntryScroll
from direct.gui.DirectFrame import DirectFrame
from direct.gui.DirectGui import DGG
from direct.gui.DirectLabel import DirectLabel
from direct.gui.DirectOptionMenu import DirectOptionMenu
from direct.gui.DirectSlider import DirectSlider
from main.Chatcontrol.Chat import Chat
from panda3d.core import TextNode, TransparencyAttrib

class PvEWorldLobby:
    '''
    classdocs
    '''

    def __init__(self):
        
                
        self.chatButtons = []
        self.chatLines = []
        self.maxItemsVisible=23
#        self.createBackground()
        self.createMainFrame()
        self.createMainFrameButtons()
        self.createChatBox()
        self.createMainFrameLabel()
        self.createPlayerMaps()
        self.createAvatarType()
        self.chat = Chat(self.chatEntry, self.scrollBar, self.chatLines,
                         self.sendButton, self.maxItemsVisible, Constants.CMSG_UNIVERSAL_CHAT, 24)
        self.setCommandForChat()
        
    def createBackground(self):
        
        base.setBackgroundColor( 1.0, 1.0, 1.0 )
    def createMainFrame(self):
        
        self.mainFrame = DirectWindow(frameSize=(0,0,0,0),
                                     frameColor = (0,0,0,0),
                                      pos=(0,0,0))
    def createChatBox(self):
        
        self.createChatButtons()
        self.createLog()
        self.createEntry()
    
    def createMainFrameButtons(self):
        
        self.backButton = DirectBasicButton(text = 'Back',
                                            text_fg = Constants.TEXT_COLOR,
                                            text_font = Constants.FONT_TYPE_02,
                                            text_pos = ( 0, -0.018),
                                            text_scale = 0.08,
                                            text_shadow = Constants.TEXT_SHADOW_COLOR,
                                            frameSize = ( -0.2, 0.2, -0.06, 0.06),
                                            frameColor = (0.8, 0.2, 0, 0.7),
                                            pos = (-1.35, 0, 0.9),
                                            relief = DGG.FLAT,
                                            command=self.switchBackToLobby)
        self.backButton.reparentTo(self.mainFrame)
        
        self.joinButton = DirectBasicButton(text = 'Ready',
                                            text_fg = Constants.TEXT_COLOR,
                                            text_font = Constants.FONT_TYPE_02,
                                            text_pos = ( 0, -0.015),
                                            text_scale = 0.08,
                                            text_shadow = Constants.TEXT_SHADOW_COLOR,
                                            frameSize = ( -0.25, 0.25, -0.06, 0.06),
                                            frameColor = (0.8, 0.2, 0, 0.7),
                                            pos = (-0.5, 0, -0.8),
                                            relief = DGG.FLAT,
                                            command=self.switchToWorld)
        self.joinButton.reparentTo(self.mainFrame)
    
    def createMainFrameLabel(self):
        
        self.gameNameLable = DirectLabel(text = "Game Name",
                                         text_fg = (0,0,0,1),
                                         text_font = Constants.FONT_TYPE_01,
                                         text_pos = (0, -0.015),
                                         text_scale = 0.1,
                                         text_shadow = (0.1, 0.1, 0.1,0.7),
                                         frameColor = (0,0,0,0),
                                         pos=(-1.2, 0, 0.75))
        self.gameNameLable.reparentTo(self.mainFrame)
        
        self.ecosystemNameLabel = DirectLabel(text = "( ecosys name )",
                                         text_fg = (0,0,0,1),
                                         text_font = Constants.FONT_TYPE_01,
                                         text_pos = (0, -0.015),
                                         text_scale = 0.07,
                                         text_shadow = (0.1, 0.1, 0.1,0.7),
                                         frameColor = (0,0,0,0),
                                         pos=(-1.2, 0, 0.67))
        self.ecosystemNameLabel.reparentTo(self.mainFrame)
        
        self.timerLabel = DirectLabel(text = "4 player currently active",
                                      text_fg = (0,0,0,1),
                                      text_font = Constants.FONT_TYPE_01,
                                      text_pos = (0, -0.015),
                                      text_scale = 0.05,
                                      text_shadow = (0.1, 0.1, 0.1,0.7),
                                      frameColor = (0,0,0,0),
                                      pos=(-1.05, 0, -0.8))
        self.timerLabel.reparentTo(self.mainFrame)
        
    def setCommandForChat(self):
        self.scrollBar['command']=self.chat.scrollChatLog
        self.chatEntry['command']=self.chat.sendEvent
        self.sendButton['command']=self.chat.sendEvent
        self.worldChatButton['command']=self.setChatMode
        self.worldChatButton['extraArgs']=[Constants.CMSG_PVEWORLD_CHAT, 0]
        self.pveChatButton['command']=self.setChatMode
        self.pveChatButton['extraArgs']=[Constants.CMSG_PVEGAME_CHAT, 1] 
        self.universalChatButton['command']=self.setChatMode
        self.universalChatButton['extraArgs']=[Constants.CMSG_UNIVERSAL_CHAT, 2]      

    def setChatMode(self, mode, modeIndex):
        
        if modeIndex == 0:
            self.worldChatButton['frameColor']=Constants.CHAT_BUTTON_FOCUS
            self.pveChatButton['frameColor'] = Constants.CHAT_BUTTON_COLOR
            self.universalChatButton['frameColor']=Constants.CHAT_BUTTON_COLOR
        elif modeIndex == 1:
            self.worldChatButton['frameColor'] = Constants.CHAT_BUTTON_COLOR
            self.universalChatButton['frameColor']=Constants.CHAT_BUTTON_COLOR
            self.pveChatButton['frameColor'] = Constants.CHAT_BUTTON_FOCUS
        else:
            self.worldChatButton['frameColor'] = Constants.CHAT_BUTTON_COLOR
            self.universalChatButton['frameColor']=Constants.CHAT_BUTTON_FOCUS
            self.pveChatButton['frameColor'] = Constants.CHAT_BUTTON_COLOR
            
#        for i in range(3):
#            
#            if modeIndex == i:
#                self.chatButtons[i]['frameColor'] = Constants.CHAT_BUTTON_FOCUS
#            else:
#                self.chatButtons[i]['frameColor'] = Constants.CHAT_BUTTON_COLOR
                
        self.chat.setChatMode(mode, modeIndex)
        
    def createPlayerMaps(self):
        self.playerMap = DirectLabel(image = "models/maps/minimap.png",
                                     image_scale=(0.2, 0.2,0.2),
                                     image_hpr = (0 ,-70, 30),
                                     frameSize = (-0.3, 0.3, 0.03, 0.03),
                                     frameColor = (0,0,0,1),
                                     pos=(-1.05, 0, 0))
#                                     hpr=(-70, -45, 10))
        self.playerMap.reparentTo(self.mainFrame)
    
    def createAvatarType(self):
        
        self.avatarTypeLabel = DirectLabel(text = "Avatar Type",
                                           text_fg = (1,1,1,1),
                                           text_font = Constants.FONT_TYPE_02,
                                           text_pos = ( 0, -0.015),
                                           text_scale = 0.09,
                                           frameSize = ( -0.25, 0.25, -0.06, 0.06),
                                           frameColor = (0,0,0,0),
                                           pos = (-1.15, 0, -0.65),
                                           relief = DGG.FLAT)
        self.avatarTypeLabel.reparentTo(self.mainFrame)
        
        self.avatarChoice = DirectOptionMenu(text = "Avatar Type",
                                             text_pos = (-0.95, -0.22),
                                             text_scale = 0.75,
                                             scale = 0.1,
                                             items=['Animal', 'Plant', 'Water'],
                                             initialitem = 0,
                                             frameSize = (-2.0, 2.0, -0.65, 0.65), 
                                             highlightColor = (0.9, 0.2, 0.1, 0.8),
                                             pos = (-0.6, 0 , -0.63),
                                             popupMarker_scale=0.3)
        self.avatarChoice.reparentTo(self.mainFrame)
        
    def createChatButtons(self):

        self.buttonFrame = DirectFrame( frameSize = (-0.5, 0.5, -0.06, 0.06),
                                        frameColor = Constants.BG_COLOR,
                                        pos = (0.65, 0, 0.775) )
        self.buttonFrame.reparentTo(self.mainFrame)
        
        for i in range(3):
            self.chatButtons.append(DirectBasicButton( text = '',
                                            text_fg = Constants.TEXT_COLOR,
                                            text_font = Constants.FONT_TYPE_01,
                                            text_pos = (0, -0.015),
                                            text_scale = 0.05,
                                            text_shadow = Constants.TEXT_SHADOW_COLOR,
                                            frameSize = (-0.14, 0.14, -0.05, 0.05),
                                            frameColor = Constants.CHAT_BUTTON_COLOR,
                                            pos = (-0.3+i*0.3, 0, -0.01),
                                            relief = DGG.FLAT))
#                                            command = self.setChatMode )
            self.chatButtons[i].reparentTo(self.buttonFrame)
            self.chatButtons[i].setTransparency(TransparencyAttrib.MAlpha)

        self.worldChatButton = self.chatButtons[0]
        self.worldChatButton['text'] = 'World'
        self.pveChatButton = self.chatButtons[1]
        self.pveChatButton['text'] = 'PvE'
        self.universalChatButton = self.chatButtons[2]
        self.universalChatButton['text']='Universal'
        self.universalChatButton['frameColor']=Constants.CHAT_BUTTON_FOCUS
        
    def createLog(self):

        self.chatLogFrame = DirectFrame( frameSize = (-0.65, 0.65, -0.7, 0.7),
                                         frameColor = Constants.BG_COLOR,
                                         pos = (0.8, 0, 0.015) )
        self.chatLogFrame.reparentTo(self.mainFrame)

        for i in range(self.maxItemsVisible):
            chatLine = DirectLabel( text = '',
                                    text_align = TextNode.ALeft,
                                    text_fg = Constants.TEXT_COLOR,
                                    text_pos = (-0.6, -0.01),
                                    text_scale = 0.05,
                                    text_shadow = Constants.TEXT_SHADOW_COLOR,
                                    frameSize = (-0.6, 0.6, -0.03, 0.03),
                                    frameColor = (1, 0, 0, 0),
                                    pos = (-0.025, 0, 0.65 - i * 0.06) )
            chatLine.reparentTo(self.chatLogFrame)
            self.chatLines.append(chatLine)

        self.scrollBar = DirectSlider( pos = (0.62, 0, -0.01),
                                       scale = 0.13,
                                       value = 1,
                                       range = (1, 0),
                                       scrollSize = 1,
                                       pageSize = 1,
                                       frameSize = (-0.03, 0.03, -5.1, 5.1),
                                       orientation = DGG.VERTICAL,
                                       thumb_frameSize = (-0.1, 0.1, -0.25, 0.25),
                                       thumb_relief = DGG.FLAT)
#                                       command = self.scrollChatLog )
        self.scrollBar.reparentTo(self.chatLogFrame) 
           
    def createEntry(self):

        self.bottomFrame = DirectFrame( frameSize = (-0.65, 0.65, -0.08, 0.08),
                                        frameColor = Constants.BG_COLOR,
                                        pos = (0.8, 0, -0.765) )
        self.bottomFrame.reparentTo(self.mainFrame)

        self.chatEntry = DirectTextField( self.mainFrame,
                                          text = '',
                                          text_font = Constants.FONT_TYPE_01,
                                          frameColor = (0.8, 0.8, 0.8, 0.4),
                                          width = 50,
                                          focusInCommand = self.onFocus,
                                          focusOutCommand = self.onFocusOut )

        self.chatEntryScroll = DirectEntryScroll( self.chatEntry,
                                                  pos = (-0.62, 0, -0.02),
                                                  scale = 0.045,
                                                  clipSize = (0, 22, -6.05, 6.05) )
        self.chatEntryScroll.reparentTo(self.bottomFrame)

        self.sendButton = DirectBasicButton( text = 'Send',
                                             text_fg = Constants.TEXT_COLOR,
                                             text_font = Constants.FONT_TYPE_01,
                                             text_pos = (0, -0.01),
                                             text_scale = 0.045,
                                             text_shadow = Constants.TEXT_SHADOW_COLOR,
                                             frameSize = (-0.1, 0.1, -0.04, 0.04),
                                             frameColor = (0, 0, 0, 0.2),
                                             pos = (0.52, 0, -0.003),
                                             relief = DGG.FLAT)
#                                             command = self.switchToPvPWorldLobby)
        self.sendButton.reparentTo(self.bottomFrame)
        
    def onFocus(self):
        self.chatEntry['frameColor'] = (0.8, 0.8, 0.8, 0.9)
        self.mainFrame.getControls().enable()

    def onFocusOut(self):

        self.chatEntry['frameColor'] = (0.8, 0.8, 0.8, 0.4)
        self.mainFrame.getControls().disable() 
      
    def switchBackToLobby(self):
        main.switchEnvironment("LobbyHeader")
    def switchToWorld(self):
        main.switchEnvironment("WorldGUI") 
    def unload(self):
        # mainFrame is the parent to all directGuiWidget, so destroy mainFrame
        # will destroy everything
        self.mainFrame.destroy()