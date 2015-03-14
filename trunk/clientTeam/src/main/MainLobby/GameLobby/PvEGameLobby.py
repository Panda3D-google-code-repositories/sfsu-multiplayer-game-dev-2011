from common.Constants import Constants
from common.DirectBasicButton import DirectBasicButton
from direct.gui.DirectFrame import DirectFrame
from direct.gui.DirectGui import DGG
from direct.gui.DirectLabel import DirectLabel
from direct.gui.DirectSlider import DirectSlider
from main.MainLobby.GameLobby.GameLobbyChat import GameLobbyChat
from main.MainLobby.GameLobby.MessageBoxWithEntry import MessageBoxWithEntry
from main.MainLobby.GameLobby.NewPvEWorldWindow import NewPvEWorldWindow
from main.MainLobby.GameLobby.PlayerWindow import PlayerWindow
from main.MainLobby.GameLobby.PvPGameLobby import GameObject
from panda3d.core import TextNode, TransparencyAttrib
from main.MainLobby.WorldLobby.PvPWorldLobby import WorldObj

class PvEGameLobby:
    '''
    classdocs
    '''
    
    def __init__(self, parent):

        self.mainFrame = parent
        
        self.chatButtons = []
        self.chatLines = []
        self.maxItemsVisible = 5
        self.maxClosedWorldVisible = 3
        self.maxOpenedWorldVisible = 3
        self.closedWorldList = []
        self.openedWorldList = []
        self.joinButtons1 = []
        self.joinButtons2 = []
        self.closedWorldLog = []
        self.openedWorldLog = []
        self.topIndexOfList = [0, 0]
        self.allJoinButtonsShown1 = False
        self.allJoinButtonsShown2 = False
        self.gameChat = GameLobbyChat(self.mainFrame, 1)
        
        self.newWorldWindow = NewPvEWorldWindow(self.mainFrame)
        self.createClosedWorldBoard()
        self.createOpenWorldBoard()
        self.createPvPGameButton()
        self.createPlayerButton()
        self.createPvETitle()
        self.playerWindow = PlayerWindow((0, 0, 0), self.gameChat.chatEntry, parent)
        
        main.msgQ.addToCommandList(Constants.CMSG_GET_PLAYER_WORLDS, self.loadClosedWorldList)
        main.msgQ.addToCommandList(Constants.CMSG_GETPVEWORLDS, self.loadOpenedWorldList)
        main.msgQ.addToCommandList(Constants.CMSG_SEE_PVP_ONLINE_PLAYERS, self.receiveMessage)
        main.msgQ.addToCommandList(Constants.CMSG_JOIN_PVE_WORLD, self.responseJoinPvEWorld)

        self.hide()
        
    def receiveListOfWorld(self, _list1, _list2):
        self.loadClosedWorldList(_list1)
        self.loadOpenedWorldList(_list2)
        
    def loadClosedWorldList(self, _list=[]):

        self.closedWorldLog = _list
#        for i in range(10):
#            self.closedWorldLog.append(GameObject('Game' + str(i), i, 10, 'Ecosystem' + str(i)))
        
        if self.maxClosedWorldVisible <= len(self.closedWorldLog):
            maxItems = self.maxClosedWorldVisible
        else:
            maxItems = len(self.closedWorldLog)
            
        for i in range(maxItems):
            self.closedWorldList[i]['game']['text'] = self.closedWorldLog[i].gameName
            self.closedWorldList[i]['player']['text'] = str(self.closedWorldLog[i].players) + "/" + str(self.closedWorldLog[i].maxPlayers)
            self.closedWorldList[i]['ecosystem']['text'] = self.closedWorldLog[i].ecosystem
            if self.closedWorldLog[i].isReturned == 0:
                self.joinButtons1[i]['text'] = 'Continue'
            else :
                self.joinButtons1[i]['text'] = 'Join' 
        self.updateScrollBar1()  

    def loadOpenedWorldList(self, _list=[]):

        self.openedWorldLog = _list
#        for i in range(10):
#            self.openedWorldLog.append(GameObject('Game' + str(i), i, 10, 'Ecosystem' + str(i)))
        
        if self.maxOpenedWorldVisible <= len(self.openedWorldLog):
            maxItems = self.maxOpenedWorldVisible
        else:
            maxItems = len(self.openedWorldLog)
            
        for i in range(maxItems):
            self.openedWorldList[i]['game']['text'] = self.openedWorldLog[i].gameName
            self.openedWorldList[i]['player']['text'] = str(self.openedWorldLog[i].players) + "/" + str(self.openedWorldLog[i].maxPlayers)
            self.openedWorldList[i]['ecosystem']['text'] = self.openedWorldLog[i].ecosystem
            print "isReturned: " + str(self.openedWorldLog[i].isReturned)
            if self.openedWorldLog[i].isReturned == 0:
                print "change join button to Continue"
                print "old button text: " + self.joinButtons2[i]['text']
                self.joinButtons2[i]['text'] = 'Cont'
            else :
                self.joinButtons2[i]['text'] = 'Join'             
        self.updateScrollBar2()  
                
    def createClosedWorldBoard(self):
        
        self.closedWorldBoardFrame = DirectFrame(frameSize=(-1.45, 1.45, -0.24, 0.24),
                                          frameColor=Constants.BG_COLOR,
                                          pos=(0, 0, 0.55))
        self.closedWorldBoardFrame.reparentTo(self.mainFrame)
        
        _text_fg = (0, 0, 0, 1)
        _text_shadow = (0.2, 0.2, 0.2, 0.4)
        self.gameNameLabel = DirectLabel(text='Your Worlds',
                                         text_fg=Constants.TEXT_COLOR,
                                         text_shadow=Constants.TEXT_SHADOW_COLOR,
                                         text_pos=(0, -0.015),
                                         text_scale=0.06,
#                                         frameSize = (-0.3, 0.3, -0.06, 0.06),
                                         frameColor=(0, 0, 0, 0),
                                         pos=(-1.15, 0, 0.18))
        self.gameNameLabel.reparentTo(self.closedWorldBoardFrame)
        
        self.playerLabel = DirectLabel(text='Player',
                                       text_fg=Constants.TEXT_COLOR,
                                         text_shadow=Constants.TEXT_SHADOW_COLOR,
                                         text_pos=(0, -0.015),
                                         text_scale=0.06,
#                                         frameSize = (-0.3, 0.3, -0.06, 0.06),
                                         frameColor=(0, 0, 0, 0),
                                         pos=(-0.2, 0, 0.18))
        self.playerLabel.reparentTo(self.closedWorldBoardFrame)
        
        self.ecosystemLabel = DirectLabel(text='EcoSystem',
                                          text_fg=Constants.TEXT_COLOR,
                                         text_shadow=Constants.TEXT_SHADOW_COLOR,
                                         text_pos=(0, -0.015),
                                         text_scale=0.06,
#                                         frameSize = (-0.3, 0.3, -0.06, 0.06),
                                         frameColor=(0, 0, 0, 0),
                                         pos=(0.4, 0, 0.18))
        self.ecosystemLabel.reparentTo(self.closedWorldBoardFrame)
        
        self.scrollBar1 = DirectSlider(pos=(1.4, 0, -0.04),
                                       scale=0.13,
                                       value=0,
                                       range=(0, 1),
                                       scrollSize=1,
                                       frameSize=(-0.05, 0.05, -1.25, 1.25),
                                       pageSize=1,
                                       orientation=DGG.VERTICAL,
                                       thumb_frameSize=(-0.1, 0.1, -0.3, 0.3),
                                       thumb_relief=DGG.FLAT,
                                       command=self.scrollClosedWorldList)
        self.scrollBar1.reparentTo(self.closedWorldBoardFrame) 
        self.createClosedWorldList()
        
    def receiveMessage(self, _list=[]):
        print "message from pve: " + _list[0]
        self.playerWindow.updatePlayersFromServer(_list)    
            
    def createOpenWorldBoard(self):
        self.openWorldBoardFrame = DirectFrame(frameSize=(-1.45, 1.45, -0.24, 0.24),
                                          frameColor=Constants.BG_COLOR,
                                          pos=(0, 0, 0.05))
        self.openWorldBoardFrame.reparentTo(self.mainFrame)
        
        _text_fg = (0, 0, 0, 1)
        _text_shadow = (0.2, 0.2, 0.2, 0.4)
        self.gameNameLabel = DirectLabel(text='Active Worlds',
                                         text_fg=Constants.TEXT_COLOR,
                                         text_shadow=Constants.TEXT_SHADOW_COLOR,
                                         text_pos=(0, -0.015),
                                         text_scale=0.06,
#                                         frameSize = (-0.3, 0.3, -0.06, 0.06),
                                         frameColor=(0, 0, 0, 0),
                                         pos=(-1.15, 0, 0.18))
        self.gameNameLabel.reparentTo(self.openWorldBoardFrame)
        
        self.playerLabel = DirectLabel(text='Player',
                                       text_fg=Constants.TEXT_COLOR,
                                         text_shadow=Constants.TEXT_SHADOW_COLOR,
                                         text_pos=(0, -0.015),
                                         text_scale=0.06,
#                                         frameSize = (-0.3, 0.3, -0.06, 0.06),
                                         frameColor=(0, 0, 0, 0),
                                         pos=(-0.2, 0, 0.18))
        self.playerLabel.reparentTo(self.openWorldBoardFrame)
        
        self.ecosystemLabel = DirectLabel(text='EcoSystem',
                                        text_fg=Constants.TEXT_COLOR,
                                         text_shadow=Constants.TEXT_SHADOW_COLOR,
                                         text_pos=(0, -0.015),
                                         text_scale=0.06,
#                                         frameSize = (-0.3, 0.3, -0.06, 0.06),
                                         frameColor=(0, 0, 0, 0),
                                         pos=(0.4, 0, 0.18))
        self.ecosystemLabel.reparentTo(self.openWorldBoardFrame)
        
        self.scrollBar2 = DirectSlider(pos=(1.4, 0, -0.04),
                                       scale=0.13,
                                       value=0,
                                       range=(0, 1),
                                       scrollSize=1,
                                       frameSize=(-0.05, 0.05, -1.25, 1.25),
                                       pageSize=1,
                                       orientation=DGG.VERTICAL,
                                       thumb_frameSize=(-0.1, 0.1, -0.3, 0.3),
                                       thumb_relief=DGG.FLAT,
                                       command=self.scrollOpenedWorldList)
        self.scrollBar2.reparentTo(self.openWorldBoardFrame) 
        self.createOpenedWorldList()
        
    def createPvPGameButton(self):
        self.newPvPGameButton = DirectBasicButton(text='Create New World',
                                                     text_fg=Constants.TEXT_COLOR,
                                                     text_font=Constants.FONT_TYPE_02,
                                                     text_pos=(0, -0.015),
                                                     text_scale=0.08,
                                                     text_shadow=Constants.TEXT_SHADOW_COLOR,
                                                     frameSize=(-0.4, 0.4, -0.06, 0.06),
                                                     frameColor=Constants.BG_COLOR,
                                                     pos=(1.05, 0, -0.28),
                                                     relief=DGG.FLAT,
                                                     command=self.showNewWorldDialog)
        self.newPvPGameButton.reparentTo(self.mainFrame)
        
 
    def createPvETitle(self):
        self.gameTitle = DirectLabel(text='World Of Balance',
                                         text_fg=Constants.TEXT_COLOR,
                                         text_shadow=Constants.TEXT_SHADOW_COLOR,
                                         text_font=Constants.FONT_TYPE_02,
                                         text_pos=(0, -0.015),
                                         text_scale=0.1,
#                                         frameSize = (-0.3, 0.3, -0.06, 0.06),
                                         frameColor=(0, 0, 0, 0),
                                         pos=(0, 0, 0.88))
        self.gameTitle.reparentTo(self.mainFrame)
   
           
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
        
    def createClosedWorldList(self):
        
        for i in range (self.maxClosedWorldVisible):
            z = 0.07 - i * 0.11
            self.joinButtons1.append(DirectBasicButton(text='Join',
                                                      text_fg=Constants.TEXT_COLOR,
                                                     text_font=Constants.FONT_TYPE_02,
                                                     text_pos=(0, -0.015),
                                                     text_scale=0.07,
                                                     text_shadow=Constants.TEXT_SHADOW_COLOR,
                                                     frameSize=(-0.15, 0.15, -0.045, 0.045),
                                                     frameColor=(1, 0, 0, 1),
                                                     pos=(1.2, 0, z),
                                                     relief=DGG.FLAT,
                                                     extraArgs=[0, i],
                                                     command=self.requestToJoinWorld))
            self.joinButtons1[i].reparentTo(self.closedWorldBoardFrame)
            self.joinButtons1[i].hide()
            
            ## this will take dictionary objects
            _gameLabel = DirectLabel(text='',
                                    text_fg=Constants.TEXT_COLOR,
                                    text_shadow=Constants.TEXT_SHADOW_COLOR,
                                    text_pos=(0, -0.015),
                                    text_scale=0.055,
                                    frameSize=(-0.3, 0.3, -0.045, 0.045),
                                    frameColor=(0, 0, 0, 0),
                                    pos=(-1.15, 0, z))
            _gameLabel.reparentTo(self.closedWorldBoardFrame)
            _playerLabel = DirectLabel(text='',
                                         text_fg=Constants.TEXT_COLOR,
                                         text_shadow=Constants.TEXT_SHADOW_COLOR,
                                         text_pos=(0, -0.015),
                                         text_scale=0.055,
                                         frameSize=(-0.3, 0.3, -0.045, 0.045),
                                         frameColor=(0, 0, 0, 0),
                                         pos=(-0.2, 0, z))
            _playerLabel.reparentTo(self.closedWorldBoardFrame)
            _ecosystemLabel = DirectLabel(text='',
                                         text_fg=Constants.TEXT_COLOR,
                                         text_shadow=Constants.TEXT_SHADOW_COLOR,
                                         text_pos=(0, -0.015),
                                         text_scale=0.055,
                                         frameSize=(-0.3, 0.3, -0.045, 0.045),
                                         frameColor=(0, 0, 0, 0),
                                         pos=(0.4, 0, z))
            _ecosystemLabel.reparentTo(self.closedWorldBoardFrame)
            self.closedWorldList.append({'game':_gameLabel, 'player': _playerLabel, 'ecosystem':_ecosystemLabel})
            
    def createOpenedWorldList(self):
        
        for i in range (self.maxOpenedWorldVisible):
            z = 0.07 - i * 0.11
            self.joinButtons2.append(DirectBasicButton(text='Join',
                                                      text_fg=Constants.TEXT_COLOR,
                                                     text_font=Constants.FONT_TYPE_02,
                                                     text_pos=(0, -0.015),
                                                     text_scale=0.07,
                                                     text_shadow=Constants.TEXT_SHADOW_COLOR,
                                                     frameSize=(-0.15, 0.15, -0.045, 0.045),
                                                     frameColor=(1, 0, 0, 1),
                                                     pos=(1.2, 0, z),
                                                     relief=DGG.FLAT,
                                                     extraArgs=[1, i],
                                                     command=self.requestToJoinWorld))
            self.joinButtons2[i].reparentTo(self.openWorldBoardFrame)
            self.joinButtons2[i].hide()
            
            ## this will take dictionary objects
            _gameLabel = DirectLabel(text='',
                                    text_fg=Constants.TEXT_COLOR,
                                    text_shadow=Constants.TEXT_SHADOW_COLOR,
                                    text_pos=(0, -0.015),
                                    text_scale=0.055,
                                    frameSize=(-0.3, 0.3, -0.045, 0.045),
                                    frameColor=(0, 0, 0, 0),
                                    pos=(-1.15, 0, z))
            _gameLabel.reparentTo(self.openWorldBoardFrame)
            _playerLabel = DirectLabel(text='',
                                         text_fg=Constants.TEXT_COLOR,
                                         text_shadow=Constants.TEXT_SHADOW_COLOR,
                                         text_pos=(0, -0.015),
                                         text_scale=0.055,
                                         frameSize=(-0.3, 0.3, -0.045, 0.045),
                                         frameColor=(0, 0, 0, 0),
                                         pos=(-0.2, 0, z))
            _playerLabel.reparentTo(self.openWorldBoardFrame)
            _ecosystemLabel = DirectLabel(text='',
                                         text_fg=Constants.TEXT_COLOR,
                                         text_shadow=Constants.TEXT_SHADOW_COLOR,
                                         text_pos=(0, -0.015),
                                         text_scale=0.055,
                                         frameSize=(-0.3, 0.3, -0.045, 0.045),
                                         frameColor=(0, 0, 0, 0),
                                         pos=(0.4, 0, z))
            _ecosystemLabel.reparentTo(self.openWorldBoardFrame)
            self.openedWorldList.append({'game':_gameLabel, 'player': _playerLabel, 'ecosystem':_ecosystemLabel})
    
    def scrollClosedWorldList(self):
        
        sliderValue = int(round(self.scrollBar1['value']))
        self.topIndexOfList[0] = sliderValue
        
        if len(self.closedWorldLog) < self.maxClosedWorldVisible:
            maxItems = len(self.closedWorldLog)
        else:
            maxItems = self.maxClosedWorldVisible
        
        for i in range(maxItems):
            if len(self.closedWorldLog) > self.maxClosedWorldVisible:
                index = sliderValue + i
                if self.closedWorldLog[index].isReturned == 0:
                    self.joinButtons1[i]['text'] = 'Cont'
                else :
                    self.joinButtons1[i]['text'] = 'Join'
                self.closedWorldList[i]['game']['text'] = self.closedWorldLog[index].gameName
                self.closedWorldList[i]['player']['text'] = str(self.closedWorldLog[index].players) + "/" + str(self.closedWorldLog[index].maxPlayers)
                self.closedWorldList[i]['ecosystem']['text'] = self.closedWorldLog[index].ecosystem
            else:
                if self.closedWorldLog[i].isReturned == 0:
                    self.joinButtons1[i]['text'] = 'Cont'
                else :
                    self.joinButtons1[i]['text'] = 'Join'
                self.closedWorldList[i]['game']['text'] = self.closedWorldLog[i].gameName
                self.closedWorldList[i]['player']['text'] = str(self.closedWorldLog[i].players) + "/" + str(self.closedWorldLog[i].maxPlayers)
                self.closedWorldList[i]['ecosystem']['text'] = self.closedWorldLog[i].ecosystem 
                
    def scrollOpenedWorldList(self):
        
        sliderValue = int(round(self.scrollBar2['value']))
        self.topIndexOfList[1] = sliderValue
        
        if len(self.openedWorldLog) < self.maxOpenedWorldVisible:
            maxItems = len(self.openedWorldLog)
        else:
            maxItems = self.maxOpenedWorldVisible

        index = 0
        for i in range(maxItems):
            if len(self.openedWorldLog) > self.maxOpenedWorldVisible:
                index = sliderValue + i
                if self.openedWorldLog[index].isReturned == 0:
                    self.joinButtons2[i]['text'] = 'Cont'
                else :
                    self.joinButtons2[i]['text'] = 'Join'
                self.openedWorldList[i]['game']['text'] = self.openedWorldLog[index].gameName
                self.openedWorldList[i]['player']['text'] = str(self.openedWorldLog[index].players) + "/" + str(self.openedWorldLog[index].maxPlayers)
                self.openedWorldList[i]['ecosystem']['text'] = self.openedWorldLog[index].ecosystem
            else:
                if self.openedWorldLog[index].isReturned == 0:
                    self.joinButtons2[i]['text'] = 'Cont'
                else :
                    self.joinButtons2[i]['text'] = 'Join'
                self.openedWorldList[i]['game']['text'] = self.openedWorldLog[i].gameName
                self.openedWorldList[i]['player']['text'] = str(self.openedWorldLog[i].players) + "/" + str(self.openedWorldLog[i].maxPlayers)
                self.openedWorldList[i]['ecosystem']['text'] = self.openedWorldLog[i].ecosystem 
                                 
    def updateScrollBar1(self):

        if len(self.closedWorldLog) > self.maxClosedWorldVisible:
            if self.scrollBar1.isHidden():
                self.scrollBar1.show()
                
            if not self.allJoinButtonsShown1:
                self.showAllJoinButtons1()
                
            scrollRange = len(self.closedWorldLog) - self.maxClosedWorldVisible
            
            currentSize = self.scrollBar1['thumb_frameSize'][3] - self.scrollBar1['thumb_frameSize'][2]
            if currentSize > 0.2:
                scrollRatio = float(self.maxClosedWorldVisible) / len(self.closedWorldLog)
                if (scrollRatio * currentSize) > 0.2:
                    self.scrollBar1['thumb_frameSize'] = (self.scrollBar1['thumb_frameSize'][0], self.scrollBar1['thumb_frameSize'][1],
                                           self.scrollBar1['frameSize'][2]*scrollRatio,
                                           self.scrollBar1['frameSize'][3]*scrollRatio)
                else:
                    self.scrollBar1['thumb_frameSize'] = (self.scrollBar1['thumb_frameSize'][0], self.scrollBar1['thumb_frameSize'][1],
                                           - 0.1, 0.1)
        else:
            self.scrollBar1.hide()
            self.hideJoinButtons1()
            scrollRange = 1

#        lastRange = self.scrollBar1['range'][0]
        self.scrollBar1['range'] = (scrollRange, 0)
        
    def hideJoinButtons1(self):
        
        self.allJoinButtonsShown1 = False
        for i in range(len(self.closedWorldLog)):
            self.joinButtons1[i].show()
            
        for i in range(len(self.closedWorldLog), self.maxClosedWorldVisible):
            self.joinButtons1[i].hide()
        
    def showAllJoinButtons1(self):
        for i in range(self.maxClosedWorldVisible):
            self.joinButtons1[i].show()
            
        self.allJoinButtonsShown1 = True 

    def updateScrollBar2(self):

        if len(self.openedWorldLog) > self.maxOpenedWorldVisible:
            if self.scrollBar2.isHidden():
                self.scrollBar2.show()
                
            if not self.allJoinButtonsShown2:
                self.showAllJoinButtons2()
                
            scrollRange = len(self.openedWorldLog) - self.maxOpenedWorldVisible
            
            currentSize = self.scrollBar2['thumb_frameSize'][3] - self.scrollBar2['thumb_frameSize'][2]
            if currentSize > 0.2:
                scrollRatio = float(self.maxOpenedWorldVisible) / len(self.openedWorldLog)
                if (scrollRatio * currentSize) > 0.2:
                    self.scrollBar2['thumb_frameSize'] = (self.scrollBar2['thumb_frameSize'][0], self.scrollBar2['thumb_frameSize'][1],
                                           self.scrollBar2['frameSize'][2]*scrollRatio,
                                           self.scrollBar2['frameSize'][3]*scrollRatio)
                else:
                    self.scrollBar2['thumb_frameSize'] = (self.scrollBar2['thumb_frameSize'][0], self.scrollBar2['thumb_frameSize'][1],
                                           - 0.1, 0.1)
        else:
            self.scrollBar2.hide()
            self.hideJoinButtons2()
            scrollRange = 1

#        lastRange = self.scrollBar1['range'][0]
        self.scrollBar2['range'] = (scrollRange, 0)
        
    def hideJoinButtons2(self):
        
        self.allJoinButtonsShown2 = False
        for i in range(len(self.openedWorldLog)):
            self.joinButtons2[i].show()
            
        for i in range(len(self.openedWorldLog), self.maxOpenedWorldVisible):
            self.joinButtons2[i].hide()
        
    def showAllJoinButtons2(self):
        for i in range(self.maxOpenedWorldVisible):
            self.joinButtons2[i].show()
            
        self.allJoinButtonsShown2 = True 
              
    def showNewWorldDialog(self):
        """create a window allows for creating new world when click Create New World button"""
        self.newWorldWindow.show()
    
    def showOnlinePlayer(self):
        self.playerWindow.show()  
         
    def requestToJoinWorld(self, isClosed, index):
        
        if isClosed == 0:
            self.isReturned = self.closedWorldLog[self.topIndexOfList[0] + index].isReturned
            gameObj = self.closedWorldLog[self.topIndexOfList[0] + index]
            self.worldName = gameObj.gameName
            if self.isReturned == 1:
                ecosys = gameObj.ecosystem
                maxPlayer = gameObj.maxPlayers
                player = gameObj.players
                _object = WorldObj(self.worldName, ecosys, maxPlayer, player)
                main.msgQ.addToPendingObj(Constants.PENDING_WORLD_LOBBY_OBJ, _object)
            obj = {"worldName": self.worldName, "password": ""}
            ## This should route player to PvE World instead of worldLobby
            main.cManager.sendRequest(Constants.CMSG_JOIN_PVE_WORLD, obj)
        else:
            self.isReturned = self.openedWorldLog[self.topIndexOfList[1] + index].isReturned
            gameObj = self.openedWorldLog[self.topIndexOfList[1] + index]
            self.worldName = gameObj.gameName
            if self.isReturned == 1:
                ecosys = gameObj.ecosystem
                maxPlayer = gameObj.maxPlayers
                player = gameObj.players
                _object = WorldObj(self.worldName, ecosys, maxPlayer, player)
                main.msgQ.addToPendingObj(Constants.PENDING_WORLD_LOBBY_OBJ, _object)

            self.isReturned = self.openedWorldLog[self.topIndexOfList[1] + index].isReturned
            obj = {"worldName": self.worldName, "password": ""}
            main.cManager.sendRequest(Constants.CMSG_JOIN_PVE_WORLD, obj)
#        main.switchEnvironment("PvEWorldLobby")

        main.createMessageBox(2, 'Joining World...')
    
    def responseJoinPvEWorld(self, status):

        if status == 0:
#            main.msgQ.addToPendingObj(Constants.WORLD_NAME, self.worldName)
#            main.msgQ.addToPendingObj(Constants.WORLD_TYPE, 0)
            main.switchEnvironment("WorldGUI")
        else:
            ## This should show the error to join the world
            main.showAlert(58)
        
    def hide(self):
        self.gameChat.hide() 
        self.closedWorldBoardFrame.hide() 
        self.openWorldBoardFrame.hide()
        self.newPvPGameButton.hide()
        self.newWorldWindow.hide()
        self.playerWindow.hide()
        self.playerButton.hide()   
        
    def show(self):
        main.msgQ.addToCommandList(Constants.CMSG_CHAT, self.gameChat.chat.addMessage)
        self.gameChat.show()
        self.closedWorldBoardFrame.show()
        self.openWorldBoardFrame.show()
        self.newPvPGameButton.show()
        self.playerButton.show()

        main.cManager.sendRequest(Constants.CMSG_GET_PLAYER_WORLDS, {'player_id' : 0})
        main.cManager.sendRequest(Constants.CMSG_GETPVEWORLDS)
        
    def unload(self):
#        main.msgQ.removeEvent(Constants.CMSG_CHAT)
        main.msgQ.removeEvent(Constants.CMSG_GET_PLAYER_WORLDS)
        main.msgQ.removeEvent(Constants.CMSG_GETPVEWORLDS)
        main.msgQ.removeEvent(Constants.CMSG_SEE_PVP_ONLINE_PLAYERS)
        self.newWorldWindow.unload()
        
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
    
