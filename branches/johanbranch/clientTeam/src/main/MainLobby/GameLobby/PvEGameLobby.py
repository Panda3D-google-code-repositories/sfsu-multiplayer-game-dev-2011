
#from GameClient.common.DirectBasicWindow import DirectBasicWindow
from common.Constants import Constants
from common.DirectBasicButton import DirectBasicButton
from common.DirectTextField import DirectTextField
from direct.gui.DirectEntryScroll import DirectEntryScroll
from direct.gui.DirectFrame import DirectFrame
from direct.gui.DirectGui import DGG
from direct.gui.DirectLabel import DirectLabel
from direct.gui.DirectSlider import DirectSlider
from main.Chatcontrol.Chat import Chat
from main.MainLobby.GameLobby.NewWorldWindow import NewWorldWindow
from main.MainLobby.GameLobby.PlayerWindow import PlayerWindow
from panda3d.core import TextNode, TransparencyAttrib


class PvEGameLobby:
    '''
    classdocs
    '''


    def __init__(self, parent):

        
        self.mainFrame = parent
        
        self.chatButtons = []
        self.chatLines = []
        self.maxItemsVisible=5

        self.createLog()
        self.createEntry()
        self.createButtons()
        
        self.newWorldWindow = NewWorldWindow()
        self.createClosedWorldBoard()
        self.createOpenWorldBoard()
        self.createPvPGameButton()
        self.createPlayerButton()
        self.chat = Chat(self.chatEntry, self.scrollBar, self.chatLines,
                         self.sendButton, self.maxItemsVisible, Constants.CMSG_UNIVERSAL_CHAT, 60)
        self.setCommandForChat()
        self.playerInfo = PlayerWindow((0,0,0), parent)
        self.hide()
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

        self.pveGameChatButton = DirectBasicButton( text = 'PvE',
                                            text_fg = Constants.TEXT_COLOR,
                                            text_font = Constants.FONT_TYPE_01,
                                            text_pos = (0, -0.015),
                                            text_scale = 0.05,
                                            text_shadow = Constants.TEXT_SHADOW_COLOR,
                                            frameSize = (-0.14, 0.14, -0.05, 0.05),
                                            frameColor = Constants.CHAT_BUTTON_COLOR,
                                            pos = (0.15, 0, 0),
                                            relief = DGG.FLAT)
        self.pveGameChatButton.reparentTo(self.buttonFrame)
        self.pveGameChatButton.setTransparency(TransparencyAttrib.MAlpha)
        
#        self.chatButtons.append(self.universalChatButton)
#        self.chatButtons.append( self.pveGameChatButton)
        
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
        self.pveGameChatButton['command']=self.setChatMode
        self.pveGameChatButton['extraArgs']=[Constants.CMSG_PVEGAME_CHAT, 1]
        
    def setChatMode(self, mode, modeIndex):
        
        if modeIndex == 0:
            self.universalChatButton['frameColor']=Constants.CHAT_BUTTON_FOCUS
            self.pveGameChatButton['frameColor'] = Constants.CHAT_BUTTON_COLOR
        else:
            self.universalChatButton['frameColor']=Constants.CHAT_BUTTON_COLOR
            self.pveGameChatButton['frameColor'] = Constants.CHAT_BUTTON_FOCUS
            
        self.chat.setChatMode(mode, modeIndex)
        
    def createClosedWorldBoard(self):
        
        self.closedWorldBoardFrame = DirectFrame(frameSize = (-1.45, 1.45, -0.24, 0.24),
                                          frameColor = Constants.BG_COLOR,
                                          pos = (0,0,0.55))
        self.closedWorldBoardFrame.reparentTo(self.mainFrame)
        
        _text_fg = (0,0,0,1)
        _text_shadow = (0.2,0.2,0.2,0.4)
        self.gameNameLabel = DirectLabel(text = 'Closed World',
                                         text_fg = Constants.TEXT_COLOR,
                                         text_shadow=Constants.TEXT_SHADOW_COLOR,
                                         text_pos = (0, -0.015),
                                         text_scale = 0.06,
#                                         frameSize = (-0.3, 0.3, -0.06, 0.06),
                                         frameColor = (0,0,0,0),
                                         pos = (-1.15, 0, 0.18))
        self.gameNameLabel.reparentTo(self.closedWorldBoardFrame)
        
        self.playerLabel = DirectLabel(text = 'Player',
                                       text_fg = Constants.TEXT_COLOR,
                                         text_shadow=Constants.TEXT_SHADOW_COLOR,
                                         text_pos = (0, -0.015),
                                         text_scale = 0.06,
#                                         frameSize = (-0.3, 0.3, -0.06, 0.06),
                                         frameColor = (0,0,0,0),
                                         pos = (-0.2, 0, 0.18))
        self.playerLabel.reparentTo(self.closedWorldBoardFrame)
        
        self.ecosystemLabel = DirectLabel(text = 'EcoSystem',
                                          text_fg = Constants.TEXT_COLOR,
                                         text_shadow=Constants.TEXT_SHADOW_COLOR,
                                         text_pos = (0, -0.015),
                                         text_scale = 0.06,
#                                         frameSize = (-0.3, 0.3, -0.06, 0.06),
                                         frameColor = (0,0,0,0),
                                         pos = (0.4, 0, 0.18))
        self.ecosystemLabel.reparentTo(self.closedWorldBoardFrame)
        
    def createOpenWorldBoard(self):
        self.openWorldBoardFrame = DirectFrame(frameSize = (-1.45, 1.45, -0.24, 0.24),
                                          frameColor = Constants.BG_COLOR,
                                          pos = (0,0,0.05))
        self.openWorldBoardFrame.reparentTo(self.mainFrame)
        
        _text_fg = (0,0,0,1)
        _text_shadow = (0.2,0.2,0.2,0.4)
        self.gameNameLabel = DirectLabel(text = 'Open World',
                                         text_fg = Constants.TEXT_COLOR,
                                         text_shadow=Constants.TEXT_SHADOW_COLOR,
                                         text_pos = (0, -0.015),
                                         text_scale = 0.06,
#                                         frameSize = (-0.3, 0.3, -0.06, 0.06),
                                         frameColor = (0,0,0,0),
                                         pos = (-1.15, 0, 0.18))
        self.gameNameLabel.reparentTo(self.openWorldBoardFrame)
        
        self.playerLabel = DirectLabel(text = 'Player',
                                       text_fg = Constants.TEXT_COLOR,
                                         text_shadow=Constants.TEXT_SHADOW_COLOR,
                                         text_pos = (0, -0.015),
                                         text_scale = 0.06,
#                                         frameSize = (-0.3, 0.3, -0.06, 0.06),
                                         frameColor = (0,0,0,0),
                                         pos = (-0.2, 0, 0.18))
        self.playerLabel.reparentTo(self.openWorldBoardFrame)
        
        self.ecosystemLabel = DirectLabel(text = 'EcoSystem',
                                        text_fg = Constants.TEXT_COLOR,
                                         text_shadow=Constants.TEXT_SHADOW_COLOR,
                                         text_pos = (0, -0.015),
                                         text_scale = 0.06,
#                                         frameSize = (-0.3, 0.3, -0.06, 0.06),
                                         frameColor = (0,0,0,0),
                                         pos = (0.4, 0, 0.18))
        self.ecosystemLabel.reparentTo(self.openWorldBoardFrame)
    
    def createPvPGameButton(self):
        self.newPvPGameButton = DirectBasicButton(text = 'Create New World',
                                                     text_fg = Constants.TEXT_COLOR,
                                                     text_font = Constants.FONT_TYPE_02,
                                                     text_pos = ( 0, -0.015),
                                                     text_scale = 0.08,
                                                     text_shadow = Constants.TEXT_SHADOW_COLOR,
                                                     frameSize = ( -0.4, 0.4, -0.06, 0.06),
                                                     frameColor = Constants.BG_COLOR,
                                                     pos = (1.05, 0, -0.28),
                                                     relief = DGG.FLAT,
                                                     command = self.showNewWorldDialog)
        self.newPvPGameButton.reparentTo(self.mainFrame)
        
        
    def createPlayerButton(self):
        
        self.playerButton = DirectBasicButton(text='Online Player',
                                              text_pos = (0,-0.015),
                                              text_fg = Constants.TEXT_COLOR,
                                              text_font = Constants.FONT_TYPE_01,
                                              text_shadow = Constants.TEXT_SHADOW_COLOR,
                                              text_scale = 0.05,
                                              frameSize = (-0.2, 0.2, -0.06, 0.06),
                                              frameColor = Constants.BG_COLOR,
                                              pos = (-0.2, 0, -0.28),
                                              relief=DGG.FLAT,
                                              command=self.showOnlinePlayer)
        self.playerButton.reparentTo(self.mainFrame)
        
    def onFocus(self):
        self.chatEntry['frameColor'] = (0.8, 0.8, 0.8, 0.9)
        self.mainFrame.getControls().enable()

    def onFocusOut(self):

        self.chatEntry['frameColor'] = (0.8, 0.8, 0.8, 0.4)
        self.mainFrame.getControls().disable()
        
        
    def showNewWorldDialog(self):
        """create a window allows for creating new world when click Create New World button"""
        self.newWorldWindow.show()
    
    def showOnlinePlayer(self):
        self.playerInfo.show()  
         
    def switchToPvEWorldLobby(self):
        main.switchEnvironment("PvEWorldLobby")
    
    
    def hide(self):
        self.bottomFrame.hide()
        self.chatLogFrame.hide()
        self.buttonFrame.hide()
        self.closedWorldBoardFrame.hide()
        self.openWorldBoardFrame.hide()
        self.newPvPGameButton.hide()
        self.newWorldWindow.hide()
        self.playerInfo.hide()
        self.playerButton.hide()   
        
    def show(self):
        self.bottomFrame.show()
        self.chatLogFrame.show()
        self.buttonFrame.show()
        self.closedWorldBoardFrame.show()
        self.openWorldBoardFrame.show()
        self.newPvPGameButton.show()
        self.playerButton.show()  
                   
#    def unload(self):
#        
#        if Constants.DEBUG:
#            print 'unload PvEGameLobby'
#        self.bottomFrame.destroy()
#        self.chatLogFrame.destroy()
#        self.buttonFrame.destroy()
#        self.closedWorldBoardFrame.destroy()
#        self.openWorldBoardFrame.destroy()
#        self.newPvPGameButton.destroy()
#        self.newWorldWindow.unload()
#        self.playerInfo.unload()
#        self.playerButton.destroy()
        