
from common.Constants import Constants
from common.DirectTextField import DirectTextField
from common.DirectWindow import DirectWindow
from direct.gui.DirectButton import DirectButton
from direct.gui.DirectEntryScroll import DirectEntryScroll
from direct.gui.DirectGui import DGG
from main.MainLobby.GameLobby.MainLobby import MainLobby
from main.MainLobby.GameLobby.PvEGameLobby import PvEGameLobby
from main.MainLobby.GameLobby.PvPGameLobby import PvPGameLobby
from panda3d.core import TextNode
from direct.gui.OnscreenImage import OnscreenImage

class LobbyHeader:
    '''
    classdocs
    '''
    
    def __init__(self):
        
        self.createBackground()
        self._focusColor = (0.5, 0.5, 0.5, 0.6)
        self._imageDir='models/2d'
        # this keeps track of what mode the user is currently viewing
        self.createButtonsPressedImages()
        self.currentMode = 0
        self.createMainFrame()
        self.createButtons()
        self.createSearchEntry()
        
#        self.lobby=MainLobby(self.mainFrame)
        self.mainLobby = MainLobby(self.mainFrame)
        self.pvpGameLobby = PvPGameLobby(self.mainFrame)
        self.pveGameLobby = PvEGameLobby(self.mainFrame)
        messenger.send(Constants.LISTENER_LOGIN_2D)
        self.lobby = self.mainLobby
        self.lobby.show()
        
    def createBackground(self):
        
        bgImage = 'models/2d/Background.png'
        self.bg = OnscreenImage(image = bgImage, pos = (0, 0, 0), scale=(3, 0, 7))
        self.bg.reparentTo(aspect2d)
        
    def createMainFrame(self):    
        _mainFrameSize = (0,0,0,0)
        _mainFrameColor = (0,0,0,0)
        _pos = (0, 0, 0)
        self.mainFrame = DirectWindow( frameSize = _mainFrameSize,
                                       frameColor = _mainFrameColor,
                                       pos = _pos )
        self.mainFrame.reparentTo(aspect2d)
    
    def createButtonsPressedImages(self):
        
        self.mainPressed = self._imageDir +'/bt_main_menu_pressed.jpg'
        self.pvpPressed = self._imageDir+'/bt_pvp_pressed.jpg'
        self.pvePressed = self._imageDir+'/bt_pve_pressed.jpg'
        self._mainImage=(self._imageDir+'/bt_main_menu_unpressed.jpg',
                   self.mainPressed,
                   self.mainPressed,
                   self.mainPressed)
        self. _pvpImage=(self._imageDir+'/bt_pvp_unpressed.jpg',
                   self.pvpPressed,
                   self.pvpPressed,
                   self.pvpPressed)
        self._pveImage=(self._imageDir+'/bt_pve_unpressed.jpg',
                   self.pvePressed,
                   self.pvePressed,
                   self.pvePressed)
           
    def createButtons(self, focusButton=None):
        

        self.mainButton = DirectButton( text = '',
                                             image = self.mainPressed,
                                             image_scale=(0.25,0.08,0.07),
                                             image_pos=(0,0,0),
                                             frameSize = (-0.25, 0.25, -0.07, 0.07),
                                             frameColor = (0,0,0,0),
                                             pos = (-1.3, 0, 0.9),
                                             relief = DGG.FLAT,
                                             extraArgs = [0],
                                             command = self.switchLobby)
        self.mainButton.reparentTo(self.mainFrame)

        self.pvpButton = DirectButton( text = '',
                                             image = self._pvpImage,
                                             image_scale=(0.25,0.08,0.07),
                                             image_pos=(0,0,0),
                                             frameSize = (-0.25, 0.25, -0.07, 0.07),
                                             frameColor = (0,0,0,0),
                                             pos = (-0.75, 0, 0.9),
                                             relief = DGG.FLAT,
                                             extraArgs = [1],
                                             command = self.switchLobby)
        self.pvpButton.reparentTo(self.mainFrame)

        self.pveButton = DirectButton( text = '',
                                             image = self._pveImage,
                                             image_scale=(0.25,0.08,0.07),
                                             image_pos=(0,0,0),
                                             frameSize = (-0.25, 0.25, -0.07, 0.07),
                                             frameColor = (0,0,0,0),
                                             pos = (-0.2, 0, 0.9),
                                             relief = DGG.FLAT,
                                             extraArgs = [2],
                                             command = self.switchLobby)
        self.pveButton.reparentTo(self.mainFrame)
        
    def createSearchEntry(self):
        
        self.searchEntry = DirectTextField( self.mainFrame,
                                          text_align = TextNode.ALeft,
                                          text_font = Constants.FONT_TYPE_01,
                                          frameColor = (0.8, 0.8, 0.8, 0.4),
                                          width = 90,
                                          focusInCommand = self.onSearchEntryFocus,
                                          focusOutCommand = self.onSearchEntryFocusOut )

        self.searchEntryScroll = DirectEntryScroll( self.searchEntry,
                                                  pos = (0.2, 0, 0.875),
                                                  scale = 0.07,
                                                  clipSize = (0, 15.7, -1.2, 1.2) )
        self.searchEntryScroll.reparentTo(self.mainFrame)
        
        _goImages=(self._imageDir+'/bt_go_unpressed.jpg',
                   self._imageDir+'/bt_go_pressed.png',
                   self._imageDir+'/bt_go_pressed.png',
                   self._imageDir+'/bt_go_pressed.png') 
        self.goButton = DirectButton( text = '',
                                           image = _goImages,
                                           image_pos=(0,0,0),
                                             image_scale=(0.1,0.08,0.06),
                                             frameSize = (-0.1, 0.1, -0.065, 0.065),
                                             frameColor = Constants.BG_COLOR,
                                             pos = (1.45, 0, 0.899),
                                             relief = DGG.FLAT,
                                             command=self.switchToPvPWorldLobby)
        self.goButton.reparentTo(self.mainFrame)
    def onSearchEntryFocus(self):
        self.searchEntry['frameColor'] = (0.8, 0.8, 0.8, 0.9)
        self.mainFrame.getControls().enable()

    def onSearchEntryFocusOut(self):
        self.searchEntry['frameColor'] = (0.8, 0.8, 0.8, 0.4)
        self.mainFrame.getControls().disable()
        
    def switchToPvPWorldLobby(self):
        main.switchEnvironment("PvEWorldLobby")   
#        _list=["player1", 'player2', 'player3', 'player4']
#        messenger.send(Constants.UPDATE_PVE_ONLINE_PLAYERS, [_list])
        
    def switchLobby(self, buttonNum):
        
        if buttonNum == self.currentMode:
            return
        
        if self.currentMode == 0:
            self.mainButton['image'] = self._mainImage
        elif self.currentMode == 1:
            self.pvpButton['image'] = self._pvpImage
        else:
            self.pveButton['image'] = self._pveImage
            
        self.lobby.hide()
        
        if buttonNum == 0:
            self.mainButton['image'] = self.mainPressed
            self.currentMode = 0
            self.lobby = self.mainLobby
        elif buttonNum == 1:
            self.pvpButton['image'] =  self.pvpPressed
            self.currentMode = 1
            self.lobby = self.pvpGameLobby
        else :
            self.pveButton['image'] = self.pvePressed
            self.currentMode = 2
            self.lobby =self.pveGameLobby
        self.lobby.show()
        
    def unload(self):
        self.bg.destroy()
        self.mainFrame.destroy()