

from common.Constants import Constants
from common.DirectBasicButton import DirectBasicButton
from common.DirectWindow import DirectWindow
from direct.gui.DirectGui import DGG
from direct.gui.DirectLabel import DirectLabel
from direct.gui.DirectOptionMenu import DirectOptionMenu
from panda3d.core import TextNode, TransparencyAttrib
from threading import Thread
import time
from main.MainLobby.WorldLobby.WorldLobbyChat import WorldLobbyChat
        

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
        self.team1=[]
        self.team2=[]
        
        self.createMainFrame()
        self.worldChat = WorldLobbyChat(self.mainFrame, 0)
        self.createMainFrameButtons()
        self.createMainFrameLabel()
        self.createPlayerMaps()
        self.createAvatarType()
        
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
        
        self.readyButton['state']=DGG.DISABLED
        self.countDownTimer = CountDownTimer(20, self.gameStart, self.timerLabel)
        self.countDownTimer.start()

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
                                         text_fg=(0, 0, 0, 1),
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
        
        _map = 'models/maps/minimap.png'
        for i in range (self.maxPlayer/2):
            _player1 = DirectLabel(image=_map,
                                     image_scale=(0.15, 0, 0.15),
                                     image_pos=(0,0,0),
                                     text='Team1\n(avatar)',
                                     text_font=Constants.FONT_TYPE_02,
                                     text_scale=0.05,
                                     text_fg=(1,1,1,1),
                                     text_pos=(0,0,0.03),
                                     frameColor=(0, 0, 0, 1),
                                     pos=(_x+i*0.3, 0, 0.2))
            _player1.reparentTo(self.mainFrame)
            self.team1.append(_player1)
        
    
        for j in range (self.maxPlayer/2):
            _player2 = DirectLabel(image=_map,
                                     image_scale=(0.15, 0, 0.15),
                                     image_pos=(0,0,0),
                                     text='Team2\n(avatar)',
                                     text_font=Constants.FONT_TYPE_02,
                                     text_scale=0.05,
                                     text_fg=(1,1,1,1),
                                     text_pos=(0,0,0.03),
                                     frameColor=(0, 0, 0, 1),
                                     pos=(_x+j*0.3, 0, -0.1))
            _player2.reparentTo(self.mainFrame)
            self.team2.append(_player2)
        
        
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
        
        self.avatarChoice = DirectOptionMenu(text="Avatar Type",
                                             text_pos=(-0.95, -0.22),
                                             text_scale=0.75,
                                             scale=0.1,
                                             items=['Choose Avatar', 'Planter', 'Breeder', 'Weather Man'],
                                             initialitem=0,
                                             frameSize=(-2.0, 2.0, -0.65, 0.65),
                                             highlightColor=(0.9, 0.2, 0.1, 0.8),
                                             pos=(-0.6, 0 , -0.63))
        self.avatarChoice.reparentTo(self.mainFrame)
        

    def stopTimer(self):
        
        if not (self.countDownTimer is None):
            self.countDownTimer.stopTimer()
            self.timerInterrupted = True
            
    def onFocus(self):
        self.chatEntry['frameColor'] = (0.8, 0.8, 0.8, 0.9)
        self.mainFrame.getControls().enable()

    def onFocusOut(self):

        self.chatEntry['frameColor'] = (0.8, 0.8, 0.8, 0.4)
        self.mainFrame.getControls().disable() 
      
    def switchBackToLobby(self):
        main.switchEnvironment("LobbyHeader")
#        print ''
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
        # mainFrame is the parent to all directGuiWidget, so destroy mainFrame
        # will destroy everything
        self.mainFrame.destroy()
#        self.backButton.destroy()
#        self.bottomFrame.destroy()1
#        self.chatLogFrame.destroy()
#        self.playerMap.destroy()
#        self.avatarChoice.destroy()
#        self.avatarTypeLabel.destroy()

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
            
    
            
    
