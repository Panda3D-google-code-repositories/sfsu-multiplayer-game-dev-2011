
from common.Constants import Constants
from common.DirectBasicButton import DirectBasicButton
from common.DirectTextField import DirectTextField
from direct.gui.DirectButton import DirectButton
from direct.gui.DirectEntryScroll import DirectEntryScroll
from direct.gui.DirectFrame import DirectFrame
from direct.gui.DirectGui import DGG
from direct.gui.DirectLabel import DirectLabel
from direct.gui.DirectSlider import DirectSlider
from main.Chatcontrol.Chat import Chat
from main.MainLobby.GameLobby.NewGameWindow import NewGameWindow
from main.MainLobby.GameLobby.PlayerWindow import PlayerWindow
from panda3d.core import TextNode, TransparencyAttrib

class PvPGameLobby:
    '''
    classdocs
    '''

    def __init__(self, parent):
        
        self.mainFrame = parent
        
        self.chatButtons = []
        self.chatLines = []
        self.gameList = []
        self.gameLog = []
        self.joinButtons = []
        self.maxItemsVisible = 5
        self.maxGameVisible = 7
        self.listIsLoaded=False
        self.newGameWindow = NewGameWindow()
        
        self.createLog()
        self.createEntry()
        self.createButtons()
        self.createGameBoard()
        self.createPvPGameButton()
        self.createPlayerButton()
        self.chat = Chat(self.chatEntry, self.scrollBar, self.chatLines,
                         self.sendButton, self.maxItemsVisible, Constants.CMSG_UNIVERSAL_CHAT, 60)
        self.setCommandForChat()
        self.playerInfo = PlayerWindow((0, 0, 0), parent)
        self.hide()
        
    def loadGameList(self):
        
        for i in range(15):
            self.gameLog.append(GameObject('Game'+str(i), 'Player'+str(i), 'Ecosystem'+str(i)))
        
        if self.maxGameVisible <= len(self.gameLog):
            maxItems = self.maxGameVisible
        else:
            maxItems = len(self.gameLog)
            
        for i in range(maxItems):
            self.gameList[i]['game']['text']=self.gameLog[i].gameName
            self.gameList[i]['player']['text']=self.gameLog[i].players
            self.gameList[i]['ecosystem']['text']=self.gameLog[i].ecosystem
            
        self.updateScrollBar1()
        
    def createButtons(self):

        self.buttonFrame = DirectFrame(frameSize=(-0.35, 0.35, -0.07, 0.07),
                                        frameColor=Constants.BG_COLOR,
                                        pos=(-1.1, 0, -0.3))
        self.buttonFrame.reparentTo(self.mainFrame)

        self.universalChatButton = DirectBasicButton(text='Universal',
                                            text_fg=Constants.TEXT_COLOR,
                                            text_font=Constants.FONT_TYPE_01,
                                            text_pos=(0, -0.015),
                                            text_scale=0.05,
                                            text_shadow=Constants.TEXT_SHADOW_COLOR,
                                            frameSize=(-0.14, 0.14, -0.05, 0.05),
                                            frameColor=Constants.CHAT_BUTTON_FOCUS,
                                            pos=(-0.17, 0, 0),
                                            relief=DGG.FLAT)
        self.universalChatButton.reparentTo(self.buttonFrame)
        self.universalChatButton.setTransparency(TransparencyAttrib.MAlpha)

        self.pvpChatButton = DirectBasicButton(text='PvP',
                                            text_fg=Constants.TEXT_COLOR,
                                            text_font=Constants.FONT_TYPE_01,
                                            text_pos=(0, -0.015),
                                            text_scale=0.05,
                                            text_shadow=Constants.TEXT_SHADOW_COLOR,
                                            frameSize=(-0.14, 0.14, -0.05, 0.05),
                                            frameColor=Constants.CHAT_BUTTON_COLOR,
                                            pos=(0.15, 0, 0),
                                            relief=DGG.FLAT)
        self.pvpChatButton.reparentTo(self.buttonFrame)
        self.pvpChatButton.setTransparency(TransparencyAttrib.MAlpha)
        
#        self.chatButtons=[self.universalChatButton, self.pvpChatButton]
#        self.chatButtons.append(self.universalChatButton)
#        self.chatButtons.append(self.pvpChatButton)
#        print 'button len after append '+str(len(self.chatButtons))
    def createLog(self):

        self.chatLogFrame = DirectFrame(frameSize=(-1.45, 1.45, -0.18, 0.18),
                                         frameColor=Constants.BG_COLOR,
                                         pos=(0, 0, -0.55))
        self.chatLogFrame.reparentTo(self.mainFrame)

        for i in range(self.maxItemsVisible):
            chatLine = DirectLabel(text='',
                                    text_align=TextNode.ALeft,
                                    text_fg=Constants.TEXT_COLOR,
                                    text_pos=(-1.38, -0.01),
                                    text_scale=0.05,
                                    text_shadow=Constants.TEXT_SHADOW_COLOR,
                                    frameSize=(-1.39, 1.41, -0.03, 0.03),
                                    frameColor=(1, 0, 0, 0),
                                    pos=(-0.015, 0, 0.106 - i * 0.06))
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
        
        self.scrollBar['command'] = self.chat.scrollChatLog
        self.chatEntry['command'] = self.chat.sendEvent
        self.sendButton['command'] = self.chat.sendEvent
        self.universalChatButton['command'] = self.setChatMode
        self.universalChatButton['extraArgs'] = [Constants.CMSG_UNIVERSAL_CHAT, 0]
        self.pvpChatButton['command'] = self.setChatMode
        self.pvpChatButton['extraArgs'] = [Constants.CMSG_PVPGAME_CHAT, 1]
    
    def setChatMode(self, mode, modeIndex):
        
        if modeIndex == 0:
            self.universalChatButton['frameColor'] = Constants.CHAT_BUTTON_FOCUS
            self.pvpChatButton['frameColor'] = Constants.CHAT_BUTTON_COLOR
        else:
            self.universalChatButton['frameColor'] = Constants.CHAT_BUTTON_COLOR
            self.pvpChatButton['frameColor'] = Constants.CHAT_BUTTON_FOCUS
            
        self.chat.setChatMode(mode, modeIndex)
        
    def createGameBoard(self):
        
        self.gameBoardFrame = DirectFrame(frameSize=(-1.45, 1.45, -0.43, 0.45),
                                          frameColor=Constants.BG_COLOR,
                                          pos=(0, 0, 0.3))
        self.gameBoardFrame.reparentTo(self.mainFrame)
        
        self.gameNameLabel = DirectLabel(text='Game Name',
                                         text_fg=Constants.TEXT_COLOR,
                                         text_shadow=Constants.TEXT_SHADOW_COLOR,
                                         text_pos=(0, -0.015),
                                         text_scale=0.06,
#                                         frameSize = (-0.3, 0.3, -0.06, 0.06),
                                         frameColor=(0, 0, 0, 0),
                                         pos=(-1.25, 0, 0.39))
        self.gameNameLabel.reparentTo(self.gameBoardFrame)
        
        self.playerLabel = DirectLabel(text='Player',
                                         text_fg=Constants.TEXT_COLOR,
                                         text_shadow=Constants.TEXT_SHADOW_COLOR,
                                         text_pos=(0, -0.015),
                                         text_scale=0.06,
#                                         frameSize = (-0.3, 0.3, -0.06, 0.06),
                                         frameColor=(0, 0, 0, 0),
                                         pos=(-0.2, 0, 0.39))
        self.playerLabel.reparentTo(self.gameBoardFrame)
        
        self.ecosystemLabel = DirectLabel(text='EcoSystem',
                                         text_fg=Constants.TEXT_COLOR,
                                         text_shadow=Constants.TEXT_SHADOW_COLOR,
                                         text_pos=(0, -0.015),
                                         text_scale=0.06,
#                                         frameSize = (-0.3, 0.3, -0.06, 0.06),
                                         frameColor=(0, 0, 0, 0),
                                         pos=(0.4, 0, 0.39))
        self.ecosystemLabel.reparentTo(self.gameBoardFrame)
        
        self.scrollBar1 = DirectSlider(pos=(1.4, 0, -0.03),
                                       scale=0.13,
                                       value=0,
                                       range=(0, 1),
                                       scrollSize=1,
                                       frameSize=(-0.05, 0.05, -2.9, 2.9),
                                       pageSize=1,
                                       orientation=DGG.VERTICAL,
                                       thumb_frameSize=(-0.1, 0.1, -2.0, 2.0),
                                       thumb_relief=DGG.FLAT,
                                       command=self.scrollGameList)
        self.scrollBar1.reparentTo(self.gameBoardFrame) 
        self.createGameList()
        
    def createGameList(self):
        
        for i in range (self.maxGameVisible):
            z = 0.3  - i * 0.11
            self.joinButtons.append(DirectBasicButton(text='Join',
                                                      text_fg=Constants.TEXT_COLOR,
                                                     text_font=Constants.FONT_TYPE_02,
                                                     text_pos=(0, -0.015),
                                                     text_scale=0.07,
                                                     text_shadow=Constants.TEXT_SHADOW_COLOR,
                                                     frameSize=(-0.15, 0.15, -0.045, 0.045),
                                                     frameColor=(1,0,0,1),
                                                     pos=(1.2, 0, z),
                                                     relief=DGG.FLAT))
            self.joinButtons[i].reparentTo(self.gameBoardFrame)
            
            ## this will take dictionary objects
            _gameLabel = DirectLabel(text='',
                                    text_fg=Constants.TEXT_COLOR,
                                    text_shadow=Constants.TEXT_SHADOW_COLOR,
                                    text_pos=(0, -0.015),
                                    text_scale=0.055,
                                    frameSize = (-0.3, 0.3, -0.045, 0.045),
                                    frameColor=(0, 0, 0, 0),
                                    pos=(-1.25, 0, z))
            _gameLabel.reparentTo(self.gameBoardFrame)
            _playerLabel = DirectLabel(text='',
                                         text_fg=Constants.TEXT_COLOR,
                                         text_shadow=Constants.TEXT_SHADOW_COLOR,
                                         text_pos=(0, -0.015),
                                         text_scale=0.055,
                                         frameSize = (-0.3, 0.3, -0.045, 0.045),
                                         frameColor=(0, 0, 0, 0),
                                         pos=(-0.2, 0, z))
            _playerLabel.reparentTo(self.gameBoardFrame)
            _ecosystemLabel = DirectLabel(text='',
                                         text_fg=Constants.TEXT_COLOR,
                                         text_shadow=Constants.TEXT_SHADOW_COLOR,
                                         text_pos=(0, -0.015),
                                         text_scale=0.055,
                                         frameSize = (-0.3, 0.3, -0.045, 0.045),
                                         frameColor=(0, 0, 0, 0),
                                         pos=(0.4, 0, z))
            _ecosystemLabel.reparentTo(self.gameBoardFrame)
            self.gameList.append({'game':_gameLabel, 'player': _playerLabel, 'ecosystem':_ecosystemLabel})
            
                      
    def createPlayerButton(self):
        
        self.playerButton = DirectBasicButton(text='Online Player',
                                              text_pos=(0, -0.015),
                                              text_fg=Constants.TEXT_COLOR,
                                              text_font=Constants.FONT_TYPE_01,
                                              text_shadow=Constants.TEXT_SHADOW_COLOR,
                                              text_scale=0.05,
                                              frameSize=(-0.2, 0.2, -0.06, 0.06),
                                              frameColor=Constants.BG_COLOR,
                                              pos=(-0.2, 0, -0.28),
                                              relief=DGG.FLAT,
                                              command=self.showOnlinePlayer)
        self.playerButton.reparentTo(self.mainFrame)
        
    def createPvPGameButton(self):
        _imageDir = 'models/buttons'
        self.newPvPGameButton = DirectButton(text='',
                                             image=(_imageDir+'/bt_create_game_unpressed.jpg',
                                                    _imageDir+'/bt_create_game_pressed.jpg',
                                                    _imageDir+'/bt_create_game_pressed.jpg',
                                                    _imageDir+'/bt_create_game_pressed.jpg',),
                                             image_pos=(0,0,0),
                                             image_scale=(0.3, 0, 0.06),
                                            frameSize=(-0.4, 0.4, -0.06, 0.06),
                                            frameColor=(0,0,0,0),
                                            pos=(1.15, 0, -0.22),
                                            relief=DGG.FLAT,
                                            command=self.showNewGameWindow)
        self.newPvPGameButton.reparentTo(self.mainFrame)
        
        
#    def createGameBoardLabel(self, gameName, player, ecosystem):
        
    def onFocus(self):
        self.chatEntry['frameColor'] = (0.8, 0.8, 0.8, 0.9)
        self.mainFrame.getControls().enable()

    def onFocusOut(self):

        self.chatEntry['frameColor'] = (0.8, 0.8, 0.8, 0.4)
        self.mainFrame.getControls().disable()
    
    def showNewGameWindow(self):
        self.newGameWindow.show()
        
    def showOnlinePlayer(self):
        self.playerInfo.show()
    
    
    def scrollGameList(self):
        
        sliderValue = int(round(self.scrollBar1['value']))
        if len(self.gameLog) < self.maxGameVisible:
            maxItems = len(self.gameLog)
        else:
            maxItems = self.maxGameVisible
        
        for i in range(maxItems):
            if len(self.gameLog) > self.maxItemsVisible:
                self.gameList[i]['game']['text'] = self.gameLog[sliderValue + i].gameName
                self.gameList[i]['player']['text'] = self.gameLog[sliderValue + i].players
                self.gameList[i]['ecosystem']['text'] = self.gameLog[sliderValue + i].ecosystem
            else:
                self.gameList[i]['game']['text'] = self.gameLog[i].gameName
                self.gameList[i]['player']['text'] = self.gameLog[i].players
                self.gameList[i]['ecosystem']['text'] = self.gameLog[i].ecosystem
                
    def updateScrollBar1(self):

        if len(self.gameLog) > self.maxGameVisible:
            if self.scrollBar1.isHidden():
                self.scrollBar1.show()
            scrollRange = len(self.gameLog) - self.maxGameVisible
            
            currentSize=self.scrollBar1['thumb_frameSize'][3]-self.scrollBar1['thumb_frameSize'][2]
            if currentSize > 0.2:
                scrollRatio = float(self.maxGameVisible)/len(self.gameLog)
                if (scrollRatio * currentSize) > 0.2:
                    self.scrollBar1['thumb_frameSize'] = (self.scrollBar1['thumb_frameSize'][0], self.scrollBar1['thumb_frameSize'][1],
                                           self.scrollBar1['frameSize'][2]*scrollRatio,
                                           self.scrollBar1['frameSize'][3]*scrollRatio)
                else:
                    self.scrollBar1['thumb_frameSize'] = (self.scrollBar1['thumb_frameSize'][0], self.scrollBar1['thumb_frameSize'][1],
                                           -0.1,0.1)
        else:
            self.scrollBar1.hide()
            scrollRange = 1

#        lastRange = self.scrollBar1['range'][0]
        self.scrollBar1['range'] = (scrollRange, 0)

#        if round(self.scrollBar['value']) >= lastRange:
#            self.scrollBar1['value'] = scrollRange
#        elif round(self.scrollBar['value']) > 0:
#            self.scrollBar1['value'] = round(self.scrollBar1['value']) - 1
                
                
    def switchToPvPWorldLobby(self):
        
        main.switchEnvironment("PvPWorldLobby")

    def hide(self):
        self.bottomFrame.hide()
        self.chatLogFrame.hide()
        self.buttonFrame.hide()
        self.gameBoardFrame.hide()
        self.newPvPGameButton.hide()
        self.playerButton.hide()
        self.newGameWindow.hide()
        self.playerInfo.hide()       

    def show(self):
        if not self.listIsLoaded:
            self.loadGameList()
            self.listIsLoaded=True
        self.bottomFrame.show()
        self.chatLogFrame.show()
        self.buttonFrame.show()
        self.gameBoardFrame.show()
        self.newPvPGameButton.show()
        self.playerButton.show()
#        self.newGameWindow.show()
#        self.playerInfo.show()         
#    def unload(self):
#        
#        if Constants.DEBUG:
#            print 'unload PvPGameLobby'
#        self.bottomFrame.destroy()
#        self.chatLogFrame.destroy()
#        self.buttonFrame.destroy()
#        self.gameBoardFrame.destroy()
#        self.newPvPGameButton.destroy()
#        self.playerButton.destroy()
#        self.newGameWindow.unload()
#        self.playerInfo.unload()
    
class GameObject:
    
    def __init__(self, gameName, players, ecosystem):
        
        self.gameName = gameName
        self.players = players
        self.ecosystem = ecosystem
        
