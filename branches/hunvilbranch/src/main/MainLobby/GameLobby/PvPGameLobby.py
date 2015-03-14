
from common.Constants import Constants
from common.DirectBasicButton import DirectBasicButton
from direct.gui.DirectButton import DirectButton
from direct.gui.DirectFrame import DirectFrame
from direct.gui.DirectGui import DGG
from direct.gui.DirectLabel import DirectLabel
from direct.gui.DirectSlider import DirectSlider
from main.MainLobby.GameLobby.GameLobbyChat import GameLobbyChat
from main.MainLobby.GameLobby.NewGameWindow import NewGameWindow
from main.MainLobby.GameLobby.PlayerWindow import PlayerWindow
from panda3d.core import TextNode, TransparencyAttrib
from main.MainLobby.GameLobby.MessageBoxWithEntry import MessageBoxWithEntry

        
class PvPGameLobby:

    def __init__(self, parent):
        
        self.mainFrame = parent
        
        self.gameList = []
        self.gameLog = []
        self.joinButtons = []
        self.maxGameVisible = 7
        self.listIsLoaded = False
        self.newGameWindow = NewGameWindow(self.mainFrame)
        self.allJoinButtonsShown = False
        self.gameChat = GameLobbyChat(self.mainFrame, 0)
        self.topIndexOfList = 0
        self.createGameBoard()
        self.createPvPGameButton()
        self.createPlayerButton()
        self.playerWindow = PlayerWindow((0, 0, 0), self.gameChat.chatEntry, parent)
#        self.listener = PvPGameLobbyListener(self)
        
        main.msgQ.addToCommandList(Constants.CMSG_GETPVPWORLDS, self.loadGameList)
        main.msgQ.addToCommandList(Constants.CMSG_SEE_PVP_ONLINE_PLAYERS, self.receiveMessage)
        
#        self.loadGameList()
        self.hide()
        
    def loadGameList(self, _list=[]):
        
#        print "receive list of game from server"
        self.gameLog = _list
        for i in range(10):
            self.gameLog.append(GameObject('Game' + str(i), i, 10, 'Ecosystem' + str(i)))
        
        if self.maxGameVisible <= len(self.gameLog):
            maxItems = self.maxGameVisible
        else:
            maxItems = len(self.gameLog)
            
        for i in range(maxItems):
            self.gameList[i]['game']['text'] = self.gameLog[i].gameName
            self.gameList[i]['player']['text'] = str(self.gameLog[i].players) + "/" + str(self.gameLog[i].maxPlayers)
            self.gameList[i]['ecosystem']['text'] = self.gameLog[i].ecosystem
            
        self.updateScrollBar1()
        
    def receiveMessage(self, _list=[]):
        print "message for pvp!"
        self.playerWindow.updatePlayersFromServer(_list) 
    
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
        
        defaultColor = (1,1,1,1)
        rolloverColor = (0.3, 0.3, 0.3, 1)
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
                                       thumb_frameColor=[defaultColor, rolloverColor, rolloverColor, rolloverColor],
                                       command=self.scrollGameList)
        self.scrollBar1.reparentTo(self.gameBoardFrame) 
        self.createGameList()
        
    def createGameList(self):
        
        for i in range (self.maxGameVisible):
            z = 0.3 - i * 0.11
            self.joinButtons.append(DirectBasicButton(text='Join',
                                                      text_fg=Constants.TEXT_COLOR,
                                                     text_font=Constants.FONT_TYPE_02,
                                                     text_pos=(0, -0.015),
                                                     text_scale=0.07,
                                                     text_shadow=Constants.TEXT_SHADOW_COLOR,
                                                     frameSize=(-0.15, 0.15, -0.045, 0.045),
                                                     frameColor=(1, 0, 0, 1),
                                                     pos=(1.2, 0, z),
                                                     relief=DGG.FLAT,
                                                     extraArgs=[i],
                                                     command=self.switchToPvPWorldLobby))
            self.joinButtons[i].reparentTo(self.gameBoardFrame)
            self.joinButtons[i].hide()
            
            ## this will take dictionary objects
            _gameLabel = DirectLabel(text='',
                                    text_fg=Constants.TEXT_COLOR,
                                    text_shadow=Constants.TEXT_SHADOW_COLOR,
                                    text_pos=(0, -0.015),
                                    text_scale=0.055,
                                    frameSize=(-0.3, 0.3, -0.045, 0.045),
                                    frameColor=(0, 0, 0, 0),
                                    pos=(-1.25, 0, z))
            _gameLabel.reparentTo(self.gameBoardFrame)
            _playerLabel = DirectLabel(text='',
                                         text_fg=Constants.TEXT_COLOR,
                                         text_shadow=Constants.TEXT_SHADOW_COLOR,
                                         text_pos=(0, -0.015),
                                         text_scale=0.055,
                                         frameSize=(-0.3, 0.3, -0.045, 0.045),
                                         frameColor=(0, 0, 0, 0),
                                         pos=(-0.2, 0, z))
            _playerLabel.reparentTo(self.gameBoardFrame)
            _ecosystemLabel = DirectLabel(text='',
                                         text_fg=Constants.TEXT_COLOR,
                                         text_shadow=Constants.TEXT_SHADOW_COLOR,
                                         text_pos=(0, -0.015),
                                         text_scale=0.055,
                                         frameSize=(-0.3, 0.3, -0.045, 0.045),
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
        _imageDir = 'models/2d'
        self.newPvPGameButton = DirectButton(text='',
                                             image=(_imageDir + '/bt_create_game_unpressed.jpg',
                                                    _imageDir + '/bt_create_game_pressed.jpg',
                                                    _imageDir + '/bt_create_game_pressed.jpg',
                                                    _imageDir + '/bt_create_game_pressed.jpg',),
                                             image_pos=(0, 0, 0),
                                             image_scale=(0.3, 0, 0.06),
                                            frameSize=(-0.4, 0.4, -0.06, 0.06),
                                            frameColor=(0, 0, 0, 0),
                                            pos=(1.15, 0, -0.22),
                                            relief=DGG.FLAT,
                                            command=self.showNewGameWindow)
        self.newPvPGameButton.reparentTo(self.mainFrame)
        
    def onFocus(self):
        self.chatEntry['frameColor'] = (0.8, 0.8, 0.8, 0.9)
        self.mainFrame.getControls().enable()

    def onFocusOut(self):

        self.chatEntry['frameColor'] = (0.8, 0.8, 0.8, 0.4)
        self.mainFrame.getControls().disable()
    
    def showNewGameWindow(self):
        self.newGameWindow.show()
        
    def showOnlinePlayer(self):
        main.cManager.sendRequest(Constants.CMSG_SEEONLINEPLAYERS)
        self.playerWindow.show()
    
    
    def scrollGameList(self):
        
        sliderValue = int(round(self.scrollBar1['value']))
        self.topIndexOfList = sliderValue
        
        if len(self.gameLog) < self.maxGameVisible:
            maxItems = len(self.gameLog)
        else:
            maxItems = self.maxGameVisible
        
        for i in range(maxItems):
            if len(self.gameLog) > self.maxGameVisible:
                index = sliderValue + i
                self.gameList[i]['game']['text'] = self.gameLog[index].gameName
                self.gameList[i]['player']['text'] = str(self.gameLog[index].players)+"/"+str(self.gameLog[index].maxPlayers)
                self.gameList[i]['ecosystem']['text'] = self.gameLog[index].ecosystem
            else:
                self.gameList[i]['game']['text'] = self.gameLog[i].gameName
                self.gameList[i]['player']['text'] = str(self.gameLog[i].players)+"/"+str(self.gameLog[i].maxPlayers)
                self.gameList[i]['ecosystem']['text'] = self.gameLog[i].ecosystem
          
    def updateScrollBar1(self):

        if len(self.gameLog) > self.maxGameVisible:
            if self.scrollBar1.isHidden():
                self.scrollBar1.show()
                
            if not self.allJoinButtonsShown:
                self.showAllJoinButtons()
                
            scrollRange = len(self.gameLog) - self.maxGameVisible
            
            currentSize = self.scrollBar1['thumb_frameSize'][3] - self.scrollBar1['thumb_frameSize'][2]
            if currentSize > 0.2:
                scrollRatio = float(self.maxGameVisible) / len(self.gameLog)
                if (scrollRatio * currentSize) > 0.2:
                    self.scrollBar1['thumb_frameSize'] = (self.scrollBar1['thumb_frameSize'][0], self.scrollBar1['thumb_frameSize'][1],
                                           self.scrollBar1['frameSize'][2]*scrollRatio,
                                           self.scrollBar1['frameSize'][3]*scrollRatio)
                else:
                    self.scrollBar1['thumb_frameSize'] = (self.scrollBar1['thumb_frameSize'][0], self.scrollBar1['thumb_frameSize'][1],
                                           - 0.1, 0.1)
        else:
            self.scrollBar1.hide()
            self.hideJoinButtons()
            scrollRange = 1

#        lastRange = self.scrollBar1['range'][0]
        self.scrollBar1['range'] = (scrollRange, 0)

#        if round(self.scrollBar['value']) >= lastRange:
#            self.scrollBar1['value'] = scrollRange
#        elif round(self.scrollBar['value']) > 0:
#            self.scrollBar1['value'] = round(self.scrollBar1['value']) - 1
                
    def hideJoinButtons(self):
        
        self.allJoinButtonsShown = False
        for i in range(len(self.gameLog)):
            self.joinButtons[i].show()
            
        for i in range(len(self.gameLog), self.maxGameVisible):
            self.joinButtons[i].hide()
        
    def showAllJoinButtons(self):
        for i in range(self.maxGameVisible):
            self.joinButtons[i].show()
            
        self.allJoinButtonsShown = True
        
    def switchToPvPWorldLobby(self, index):
        
        rContents = self.gameLog[self.topIndexOfList + index].gameName
        main.cManager.sendRequest(Constants.CMSG_JOIN_PVP_WORLD, rContents)
        main.switchEnvironment("PvPWorldLobby")

    def hide(self):
        
        self.gameChat.hide()
        self.gameBoardFrame.hide()
        self.newPvPGameButton.hide()
        self.playerButton.hide()
        self.newGameWindow.hide()
        self.playerWindow.hide()       

    def show(self):
        self.gameChat.show()
        self.gameBoardFrame.show()
        self.newPvPGameButton.show()
        self.playerButton.show()
        main.cManager.sendRequest(Constants.CMSG_GETPVPWORLDS);
#        messenger.send(Constants.LISTENER_PVP_2D)
    def unload(self):
        self.newGameWindow.unload()
    
class GameObject:
    
    def __init__(self, gameName, players, maxPlayers, ecosystem, isReturned=0):
        
        self.gameName = gameName
        self.players = players
        self.maxPlayers = maxPlayers
        self.ecosystem = ecosystem
        self.isReturned = isReturned
