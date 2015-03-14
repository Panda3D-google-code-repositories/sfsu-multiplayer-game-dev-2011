
from common.Constants import Constants
from common.DirectBasicButton import DirectBasicButton
from common.DirectWindow import DirectWindow
from direct.gui.DirectFrame import DirectFrame
from direct.gui.DirectGui import DGG
from direct.gui.DirectSlider import DirectSlider
from pandac.PandaModules import TransparencyAttrib, TextNode

        
class PlayerWindow:
    '''
    a window that will display a list of current active players
    '''

    def __init__(self, pos,chatEntry, parent=None):
        
        self.pos = pos
        self.imageDir='models/2d/'
        self.players=[]
        self.playerInfo=[]
        self.maxItemsVisible=17
        self.parent = parent
        self.chatEntry = chatEntry
        self.createMainFrame()
        self.createComponents()
        self.loadListOfPlayers()
        
    def createMainFrame(self):
        self.mainFrame = DirectFrame(image=self.imageDir+'online_player_bg.jpg',
                                     image_pos=(0,0,0),
                                     image_scale=(0.5, 0.08, 0.75),
                                      frameSize = (-0.5, 0.5, -0.75,0.75),
                                      pos=self.pos)
        self.mainFrame.reparentTo(self.parent)
        self.mainFrame.hide()
        
    def updatePlayersFromServer(self, _list=[]):
        self.playerInfo = _list
        self.fillPlayers()
        
    def createComponents(self):

        self.hideButton = DirectBasicButton(text = " - ",
                                       text_fg=(1,1,1,1),
                                       text_pos=(-0.007,-0.015),
                                       text_scale=0.06,
                                       frameColor=(0.5,0.5,0.5,0.2),
                                       frameSize =(-0.05,0.05, -0.025,0.025),
                                       pos = (0.42,0,0.7),
                                       relief=DGG.FLAT,
                                       command=self.hide)
        self.hideButton.setTransparency(TransparencyAttrib.MAlpha)
        self.hideButton.reparentTo(self.mainFrame)
        
        self.scrollBar = DirectSlider( pos = (0.46, 0, 0),
                                       scale = 0.13,
                                       value = 1,
                                       range = (1, 0),
                                       frameSize =(-0.05,0.05,-5.2,5.2),
                                       scrollSize = 1,
                                       pageSize = 1,
                                       orientation = DGG.VERTICAL,
                                       thumb_frameSize = (-0.1, 0.1, -0.25, 0.25),
                                       thumb_relief = DGG.FLAT)
        self.scrollBar.reparentTo(self.mainFrame)
    
    def loadListOfPlayers(self):
        
        self.playerFrame = DirectWindow(frameSize=(0,0,0,0),
                                        frameColor=(0,0,0,0),
                                        pos=(0,0,0))
        self.playerFrame.reparentTo(self.mainFrame)
        

        for i in range(self.maxItemsVisible):
            self.players.append(DirectBasicButton(text='',
                                                   text_scale=0.05,
                                                   text_pos=(-0.41, -0.01),
                                                   text_fg=Constants.TEXT_COLOR,
                                                   text_font=Constants.FONT_TYPE_01,
                                                   text_shadow=Constants.TEXT_SHADOW_COLOR,
                                                   text_align=TextNode.ALeft,
                                                   frameSize = (-0.44, 0.46, -0.041, 0.041),
                                                   frameColor=(0.7,0.7,0.7,0),
                                                   pos = (-0.03, 0, 0.65-i*0.082),
                                                   relief=DGG.FLAT,
                                                   command=self.playerButtonClickResponse))
            self.players[i].reparentTo(self.playerFrame)
            self.players[i].setTransparency(TransparencyAttrib.MAlpha)
            self.players[i].hide()
        
            
    def fillPlayers(self):

        if len(self.playerInfo) > self.maxItemsVisible:
            maxItems = self.maxItemsVisible
        else:
            maxItems = len(self.playerInfo)
            
        for i in range(maxItems):
            print 'player: '+self.playerInfo[i]
            self.players[i]['text']=self.playerInfo[i]
            self.players[i]['extraArgs']=[self.playerInfo[i]]
            self.players[i].show()
            
    def playerButtonClickResponse(self, player):
        if not (self.chatEntry is None):
            self.chatEntry.enterText("/w["+player+"]")
        
    def hide(self):
        self.mainFrame.hide()
    
    def show(self):
        self.mainFrame.show()

    def hideHideButton(self):
        self.hideButton.hide()
        
    def unload(self):
        self.mainFrame.destroy()