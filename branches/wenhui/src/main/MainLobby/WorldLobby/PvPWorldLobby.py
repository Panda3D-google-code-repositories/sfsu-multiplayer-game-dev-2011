from common.Constants import Constants
from common.DirectBasicButton import DirectBasicButton
from common.DirectWindow import DirectWindow
from direct.gui.DirectFrame import DirectFrame
from direct.gui.DirectGui import DGG
from direct.gui.DirectLabel import DirectLabel
from direct.gui.DirectOptionMenu import DirectOptionMenu
from direct.showbase.DirectObject import DirectObject
from main.MainLobby.WorldLobby.WorldLobbyChat import WorldLobbyChat
from panda3d.core import TextNode, TransparencyAttrib
from threading import Thread
import time

class PvPWorldLobbyListener(DirectObject):
    """
    Not been used yet
    """
    def __init__(self, parent=None):
        self.accept(Constants.LISTENER_WORLD_LOBBY_INFO, parent.receiveMessage, [])
            
class PvPWorldLobby:
    '''
    classdocs
    '''

    def __init__(self):
        self.chatButtons = []
        self.chatLines = []
        self.maxItemsVisible = 14
        self.countDownTimer=None
        self.timerInterrupted = False
        self.maxPlayer=10
        self.numOfPlayers = 0
        self.team=[[],[]]
        self.team_num = 0;
        self.map_pos = 0;
        self.avatarTypes=['Choose Avatar', 'Planter', 'Breeder', 'Weather Man']
        self.worldInfo = None
        self.createMainFrame()
        self.worldChat = WorldLobbyChat(self.mainFrame, 0)
        self.createMainFrameButtons()
        self.createMainFrameLabel()
        self.createAvatarType()
#        self.receiveMessage(main.worldObj)
        self.createPlayerMaps()
        self.initPlayerMaps()
        
    def createMainFrame(self):
        
        self.mainFrame = DirectWindow(frameSize=(0, 0, 0, 0),
                                     frameColor=(0, 0, 0, 0),
                                      pos=(0, 0, 0))
    
    def createMainFrameButtons(self):
        
        self.backButton = DirectBasicButton(text='Back',
                                            text_fg=Constants.TEXT_COLOR,
                                            text_font=Constants.FONT_TYPE_02,
                                            text_pos=(0, -0.018),
                                            text_scale=0.08,
                                            text_shadow=Constants.TEXT_SHADOW_COLOR,
                                            frameSize=(-0.2, 0.2, -0.06, 0.06),
                                            frameColor=(0.8, 0.2, 0, 0.7),
                                            pos=(-1.35, 0, 0.9),
                                            relief=DGG.FLAT,
                                            command=self.switchBackToLobby)
        self.backButton.reparentTo(self.mainFrame)
        
        self.readyButton = DirectBasicButton(text='Ready',
                                            text_fg=Constants.TEXT_COLOR,
                                            text_font=Constants.FONT_TYPE_02,
                                            text_pos=(0, -0.015),
                                            text_scale=0.08,
                                            text_shadow=Constants.TEXT_SHADOW_COLOR,
                                            frameSize=(-0.25, 0.25, -0.06, 0.06),
                                            frameColor=(0.8, 0.2, 0, 0.7),
                                            pos=(-0.5, 0, -0.8),
                                            relief=DGG.FLAT,
                                            command=self.startCountDown)
        self.readyButton.reparentTo(self.mainFrame)
    
    def startCountDown(self):
        
        self.team[self.team_num][self.map_pos].readyLabel['text'] = 'Ready'
        ## send message to server
        
#        self.readyButton['state']=DGG.DISABLED
#        self.countDownTimer = CountDownTimer(20, self.gameStart, self.timerLabel)
#        self.countDownTimer.start()

    def createMainFrameLabel(self):
        
        self.gameNameLable = DirectLabel(text="Game Name",
                                         text_fg=(0, 0, 0, 1),
                                         text_font=Constants.FONT_TYPE_01,
                                         text_pos=(0, -0.015),
                                         text_scale=0.1,
                                         text_shadow=(0.1, 0.1, 0.1, 0.7),
                                         frameColor=(0, 0, 0, 0),
                                         pos=(-1.2, 0, 0.7))
        self.gameNameLable.reparentTo(self.mainFrame)
        
        self.ecosystemNameLabel = DirectLabel(text="( ecosys name )",
                                         text_fg=(1, 0.5, 0, 1),
                                         text_font=Constants.FONT_TYPE_01,
                                         text_pos=(0, -0.015),
                                         text_scale=0.07,
                                         text_shadow=(0.1, 0.1, 0.1, 0.7),
                                         frameColor=(0, 0, 0, 0),
                                         pos=(-1.2, 0, 0.62))
        self.ecosystemNameLabel.reparentTo(self.mainFrame)
        
        self.timerLabel = DirectLabel(text="please be ready",
                                      text_fg=(0, 0, 0, 1),
                                      text_font=Constants.FONT_TYPE_01,
                                      text_pos=(0, -0.015),
                                      text_scale=0.05,
                                      text_shadow=(0.1, 0.1, 0.1, 0.7),
                                      frameColor=(0, 0, 0, 0),
                                      pos=(-1.05, 0, -0.8))
        self.timerLabel.reparentTo(self.mainFrame)
        
    def receiveMessage(self, _obj):
        print 'Receive Message'
        self.worldInfo = _obj
        self.gameNameLable['text'] = self.worldInfo.worldName
        self.ecosystemNameLabel['text']=self.worldInfo.ecosystem
        self.maxPlayer = self.worldInfo.maxPlayer
        self.numOfPlayers = self.worldInfo.currentPlayer
        self.createPlayerMaps()
        self.initPlayerMaps()
        self.readyButton['text'] = 'Start'
        
    def initPlayerMaps(self):
        """
        This is called when create a new pvp game
        """
#        for i in range(2, self.maxPlayer/2):
#            self.team[0][i].frame.hide()
#            self.team[1][i].frame.hide()
        self.team[0][0].nameLabel['text']='Host'
        self.team[0][0].nameLabel.show()
        self.team[0][0].button['state']=DGG.DISABLED
        
    def createPlayerMaps(self):
        
        if self.maxPlayer == 10:
            _x = -1.34
        elif self.maxPlayer == 8:
            _x = -1.19
        elif self.maxPlayer == 6:
            _x = -1.04
        elif self.maxPlayer == 4:
            _x = -0.89
        else:
            _x = -0.74
        
        for i in range (self.maxPlayer/2):
            _playerFrame1 = DirectFrame(frameColor=(0, 0, 0, 1),
                                     pos=(_x+i*0.3, 0, 0.2))
            _playerFrame1.reparentTo(self.mainFrame)
            
            _player1 = DirectBasicButton(
#                                         image=_map,
#                                     image_scale=(0.15, 0, 0.15),
#                                     image_pos=(0,0,0),
                                     frameSize=(-0.15, 0.15, -0.15, 0.15),
                                     frameColor=(1, 0, 0, 1),
#                                     pos=(_x+i*0.3, 0, 0.2),
                                     relief=DGG.SUNKEN,
                                     borderWidth=(1,1),
                                     extraArgs = [0, i],
                                     command=self.repositionPlayer)
            _player1.reparentTo(_playerFrame1)
            
            _playerLabel = []
            for k in range(3):
                _playerLabel.append( DirectLabel(text='',
                                     text_font=Constants.FONT_TYPE_02,
                                     text_scale=0.06,
                                     text_fg=(1,1,1,1),
                                     text_pos=(0,0,0),
                                     frameColor = (0,0,0,0),
                                     pos=(0,0, 0.05-k*0.07)))
                _playerLabel[k].reparentTo(_playerFrame1)
                
            self.team[0].append(PlayerObj(_playerFrame1, _player1, 
                                        _playerLabel[0], _playerLabel[1], _playerLabel[2]))
            
            self.team[0][i].nameLabel['text']=''
            self.team[0][i].avatarLabel['text']=''
            self.team[0][i].avatarLabel['text_scale']=0.04
            self.team[0][i].readyLabel['text']=''
            self.team[0][i].readyLabel['text_fg']=(0,1,1,1)
    
        for j in range (self.maxPlayer/2):
            _playerFrame2 = DirectFrame(frameColor=(0, 0, 0, 1),
                                     pos=(_x+j*0.3, 0, -0.1))
            _playerFrame2.reparentTo(self.mainFrame)
            
            _player2 = DirectBasicButton(
#                                     image=_map,
#                                     image_scale=(0.15, 0, 0.15),
#                                     image_pos=(0,0,0),
                                     frameSize=(-0.15, 0.15, -0.15, 0.15),
                                     frameColor=(0, 1, 0, 1),
                                     relief=DGG.SUNKEN,
                                     extraArgs=[1, j],
                                     command=self.repositionPlayer)
            _player2.reparentTo(_playerFrame2)
            
            _playerLabel = []
            for k in range(3):
                _playerLabel.append( DirectLabel(text='',
                                     text_font=Constants.FONT_TYPE_02,
                                     text_scale=0.06,
                                     text_fg=(1,1,1,1),
                                     text_pos=(0,0,0),
                                     frameColor = (0,0,0,0),
                                     pos=(0,0, 0.05-k*0.07)))
                _playerLabel[k].reparentTo(_playerFrame2)
                
            self.team[1].append(PlayerObj(_playerFrame2, _player2, 
                                        _playerLabel[0], _playerLabel[1], _playerLabel[2]))
            self.team[1][j].nameLabel['text']=''
            self.team[1][j].avatarLabel['text']=''
            self.team[1][j].avatarLabel['text_scale']=0.04
            self.team[1][j].readyLabel['text']=''
            self.team[1][j].readyLabel['text_fg']=(0,1,1,1)
        
    def chooseAvatar(self, avatar):
        
        if avatar != self.avatarTypes[0]:
            
            self.team[self.team_num][self.map_pos].avatarLabel['text'] = avatar
            
    def createAvatarType(self):
        self.avatarTypeLabel = DirectLabel(text="Avatar Type",
                                           text_fg=(1, 1, 1, 1),
                                           text_font=Constants.FONT_TYPE_02,
                                           text_pos=(0, -0.015),
                                           text_scale=0.09,
                                           frameSize=(-0.25, 0.25, -0.06, 0.06),
                                           frameColor=(0, 0, 0, 0),
                                           pos=(-1.15, 0, -0.65),
                                           relief=DGG.FLAT)
        self.avatarTypeLabel.reparentTo(self.mainFrame)
        
        self.avatarChoice = DirectOptionMenu(text = "Avatar Type",
                                             text_pos = (-1.6, -0.22),
                                             text_scale = 0.55,
                                             scale = 0.1,
                                             items=self.avatarTypes,
                                             initialitem = 0,
                                             frameSize = (-2.0, 2.0, -0.65, 0.65), 
                                             highlightColor = (0.9, 0.2, 0.1, 0.8),
                                             pos = (-0.6, 0 , -0.63),
                                             popupMarker_scale=0.3,
                                             command=self.chooseAvatar)
        self.avatarChoice.reparentTo(self.mainFrame)
        
    def repositionPlayer(self, team_num, pos):
        
        if self.team_num != team_num:
            for i in range(pos+1):
                if self.team[team_num][i].nameLabel != "":
                    self.team[team_num][i].nameLabel['text'] = self.team[self.team_num][self.map_pos].nameLabel['text']
                    self.team[team_num][i].avatarLabel['text'] = self.team[self.team_num][self.map_pos].avatarLabel['text']
                    self.team[team_num][i].readyLabel['text'] = self.team[self.team_num][self.map_pos].readyLabel['text']
                    self.team[team_num][i].button['state'] = DGG.DISABLED
                    self.team[self.team_num][self.map_pos].nameLabel['text'] = ''
                    self.team[self.team_num][self.map_pos].avatarLabel['text'] = ''
                    self.team[self.team_num][self.map_pos].readyLabel['text'] = ''
                    self.team[self.team_num][self.map_pos].button['state']=DGG.NORMAL
                    self.team_num = team_num
                    self.map_pos = i
                    # send message to server side to update all players for the team change
                    # info need to be update: user's new team
                    break;
                
        
    def stopTimer(self):
        
        if not (self.countDownTimer is None):
            self.countDownTimer.stopTimer()
            self.timerInterrupted = True
            
    def onFocus(self):
        self.chatEntry['frameColor'] = (0.8, 0.8, 0.8, 0.9)

    def onFocusOut(self):
        self.chatEntry['frameColor'] = (0.8, 0.8, 0.8, 0.4)
      
    def switchBackToLobby(self):
        main.switchEnvironment("LobbyHeader")

    def switchToWorld(self):
        main.switchEnvironment("WorldGUI");
        
    def gameStart(self):
        
        if not self.timerInterrupted:
            print 'game start!!!'
            self.timerLabel['text']='Game Start!!'
        else:
            self.timerLabel['text']='Timer Interrupt'
            
        self.readyButton['state']=DGG.NORMAL  
        self.countDownTimer = None
        
    def unload(self):
        """ 
        mainFrame is the parent to all directGuiWidget, so destroy mainFrame
        will destroy everything
        """
        self.mainFrame.destroy()

class PlayerObj:
    
    def __init__(self, frame, button, nameLabel, avatarLabel, readyLabel=None):
        
        self.frame = frame;
        self.button = button;
        self.nameLabel = nameLabel
        self.avatarLabel = avatarLabel
        self.readyLabel = readyLabel

class CountDownTimer(Thread):
    
    def __init__(self, _range, command=None,  label=None, extraArgs=[],):
        """
        label is the object to display count-down time
        """
        Thread.__init__(self)
        self.label = label
        self.range = _range
        self.command=command
        self.args = extraArgs
        self.toStop=False
        
    def run(self):
        _endTime = time.time()+self.range
        _elpase=self.range
        while _endTime > time.time()and not self.toStop:
            self.label['text']='Game will start at '+str(_elpase)+'s'
            _elpase=int(_endTime - time.time())
            time.sleep(0.5)
            
        apply(self.command, self.args) 
        
    def setRange(self, _range):
        self.range = _range; 
    
    def stopTimer(self):
        self.toStop = True
            
class WorldObj:
    
    def __init__(self, worldName, ecosystem, maxplayer, currentPlayer = 0):
        """
        worldName : string
        ecosystem : string
        maxplayer : short
        """
        self.worldName = worldName
        self.ecosystem = ecosystem
        self.maxPlayer = maxplayer
        self.currentPlayer = currentPlayer
    
