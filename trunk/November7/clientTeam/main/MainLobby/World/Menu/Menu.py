
from common.Constants import Constants
from common.DirectBasicButton import DirectBasicButton
from common.DirectControls import DirectControls
from common.DirectWindow import DirectWindow
from direct.gui.DirectGui import DGG
from direct.gui.DirectLabel import DirectLabel
from direct.gui.DirectRadioButton import DirectRadioButton
from direct.gui.DirectSlider import DirectSlider
from panda3d.core import TransparencyAttrib, TextNode


class MenuControl(DirectControls):
    def __init__(self, parent):

        DirectControls.__init__(self, parent)
        self.accept('q', parent.toggleMenuVisibility) 
    
class Menu:
    
    def __init__(self, parent, world):
        
        self.pos = (-1.48, 0, 0.945)
        self.musicOn=[1]
        self.soundOn=[1]
        self.gameScale=5
        self.soundScale=6
        self.musicVolume=5
        self.buttons=[]
        self.bottomHidden = False
        self.parent=parent
        self.world = world
        self.createMenuButton()
        self.createMenuFrame()
        self.createMusicOption()
        self.createSoundOptions()
        self.createGameScale()
        self.createButtons()
        
        self.control = MenuControl(self)
        
    def createMenuButton(self):
        """ create menu button """
        self.menuButton = DirectBasicButton(text = 'Menu',
                                            text_fg = Constants.TEXT_COLOR,
                                            text_font = Constants.FONT_TYPE_01,
                                            text_pos = (0, -0.015),
                                            text_scale = 0.045,
                                            text_shadow = Constants.TEXT_SHADOW_COLOR,
                                            frameSize = (-0.1, 0.1, -0.045, 0.045),
                                            frameColor = Constants.BG_COLOR,
                                            pos = self.pos,
                                            relief = DGG.FLAT,
                                            command=self.toggleMenuVisibility)
        self.menuButton.reparentTo(self.parent)
        
    def createMenuFrame(self):
        self.menuFrame = DirectWindow(frameSize=(-0.3, 0.3, -0.43, 0.4),
                                      frameColor=Constants.BG_COLOR,
                                      pos=(-1.28, 0, 0.5))
        self.menuFrame.reparentTo(self.parent)
        self.menuFrame.hide() 
    
    def hideMenuFrame(self):
        self.menuFrame.hide()
    
    def toggleMenuVisibility(self):
        if self.menuFrame.isHidden():
            self.menuFrame.show()
        else:
            self.menuFrame.hide()
        
    def createMusicOption(self):
        
        self.musicLabel = DirectLabel(text='Music:',
                                      text_scale=0.045,
                                      text_pos=(0,-0.015),
                                    text_fg = Constants.TEXT_COLOR,
                                    text_font = Constants.FONT_TYPE_01,
                                    text_shadow = Constants.TEXT_SHADOW_COLOR,
                                    text_align=TextNode.ALeft,
                                    frameSize = (-0.1, 0.1, -0.04, 0.04),
                                    frameColor = (0,0,0,0),
                                    pos = (-0.29, 0, 0.33))
        self.musicLabel.setTransparency(TransparencyAttrib.MAlpha)
        self.musicLabel.reparentTo(self.menuFrame)
        
        self.musicScaleBar = DirectSlider( pos = (0.1, 0, 0.33-0.005),
                                       scale = 0.13,
                                       value = self.musicVolume,
                                       range = (1, 10),
#                                       scrollSize = 1,
                                       frameSize = (-1.4,1.4,-0.06,0.06),
                                       pageSize = 1,
                                       orientation = DGG.HORIZONTAL,
                                       thumb_frameSize = (-0.15, 0.15, -0.2, 0.2),
                                       thumb_relief = DGG.FLAT,
                                       command = self.setMusicVolume )
        self.musicScaleBar.reparentTo(self.menuFrame) 
               
#        self.musicOptions = [DirectRadioButton(text = 'On', 
#                                               text_scale=0.05,
#                                               text_fg=(0,0,0,1),
#                                               variable=self.musicOn, 
#                                               value=[1], 
#                                               scale=0.05,
#                                               indicatorValue=1,
##                                               frameSize=(-0.1,0.1, -0.05,0.05),
##                                               boxPlacement='rignt',
#                                               pos=(0,0,0.33),
#                                               boxBorder=0,
#                                               command=self.setMusicOnOff),
#                             DirectRadioButton(text = 'Off',
#                                               text_scale=0.05, 
#                                               text_fg=(0,0,0,1),
#                                               variable=self.musicOn,
#                                               indicatorValue=0,
##                                               frameSize=(-0.1,0.1, -0.05,0.05), 
#                                               value=[0], 
#                                               scale=0.05, 
##                                               boxPlacement='right',
#                                               pos=(0.2,0,0.33),
#                                               boxBorder=0,
#                                               command=self.setMusicOnOff)]
#        self.musicOptions[0].reparentTo(self.menuFrame)
#        self.musicOptions[1].reparentTo(self.menuFrame)
#        for button in self.musicOptions:        
#            button.setOthers(self.musicOptions)
    
#    def setMusicOnOff(self):
#        
#        if self.musicOn[0] == 0:
#            print 'music off'
#        else:
#            print 'music on'
    def setMusicVolume(self):
        
        self.musicVolume=int(self.musicScaleBar['value'])
        main.audioManager.setMusicVolume(self.musicVolume)
        
    def createSoundOptions(self):

        self.soundLabel = DirectLabel(text='Sound:',
                                      text_scale=0.045,
                                      text_pos=(0,-0.015),
                                    text_fg = Constants.TEXT_COLOR,
                                    text_font = Constants.FONT_TYPE_01,
                                    text_shadow = Constants.TEXT_SHADOW_COLOR,
                                    text_align=TextNode.ALeft,
                                    frameSize = (-0.1, 0.1, -0.04, 0.04),
                                    frameColor = (0,0,0,0),
                                    pos = (-0.29, 0, 0.23))
        self.soundLabel.setTransparency(TransparencyAttrib.MAlpha)
        self.soundLabel.reparentTo(self.menuFrame)
        
        self.soundScaleBar = DirectSlider( pos = (0.1, 0, 0.23-0.005),
                                       scale = 0.13,
                                       value = self.soundScale,
                                       range = (1, 10),
#                                       scrollSize = 1,
                                       frameSize = (-1.4,1.4,-0.06,0.06),
                                       pageSize = 1,
                                       orientation = DGG.HORIZONTAL,
                                       thumb_frameSize = (-0.15, 0.15, -0.2, 0.2),
                                       thumb_relief = DGG.FLAT,
                                       command = self.setSoundScale )
        self.soundScaleBar.reparentTo(self.menuFrame)

    def setSoundScale(self):
        
        self.soundScale=int(self.soundScaleBar['value'])
        main.audioManager.setSoundVolume(self.soundScale)
        print 'Sound Scale:'+str(self.soundScale)
    
    def createGameScale(self):
        
        self.gameScaleLabel = DirectLabel(text='Game Scale:',
                                      text_scale=0.045,
                                      text_pos=(0,-0.015),
                                    text_fg = Constants.TEXT_COLOR,
                                    text_font = Constants.FONT_TYPE_01,
                                    text_shadow = Constants.TEXT_SHADOW_COLOR,
                                    text_align=TextNode.ALeft,
                                    frameSize = (-0.1, 0.1, -0.04, 0.04),
                                    frameColor = (0,0,0,0),
                                    pos = (-0.29, 0, 0.13))
        self.gameScaleLabel.setTransparency(TransparencyAttrib.MAlpha)
        self.gameScaleLabel.reparentTo(self.menuFrame) 
                           
        self.scaleBar = DirectSlider( pos = (0, 0, 0.06),
                                       scale = 0.13,
                                       value = self.gameScale,
                                       range = (1, 10),
#                                       scrollSize = 1,
                                       frameSize = (-2.,2.,-0.06,0.06),
                                       pageSize = 1,
                                       orientation = DGG.HORIZONTAL,
                                       thumb_frameSize = (-0.25, 0.25, -0.2, 0.2),
                                       thumb_relief = DGG.FLAT,
                                       command = self.setGameScale )
        self.scaleBar.reparentTo(self.menuFrame)
        
    def setGameScale(self):
        
        self.gameScale=int(self.scaleBar['value'])
        self.gameScaleLabel['text']='Game Scale: '+ str(self.gameScale)
    
    
    def createButtons(self):
        """
        Create the rest of buttons
        """  
        for i in range(4):
            self.buttons.append( DirectBasicButton(text='',
                                      text_scale=0.045,
                                      text_pos=(0,-0.015),
                                    text_fg = Constants.TEXT_COLOR,
                                    text_font = Constants.FONT_TYPE_01,
                                    text_shadow = Constants.TEXT_SHADOW_COLOR,
#                                    text_align=TextNode.ALeft,
                                    frameSize = (-0.2, 0.2, -0.04, 0.04),
                                    frameColor = (0.5,0.5,0.5,0.7),
                                    pos = (0, 0, -0.05-i*0.1),
                                    relief=DGG.FLAT))
            self.buttons[i].reparentTo(self.menuFrame)
            self.buttons[i].setTransparency(TransparencyAttrib.MAlpha)
        
        self.hideBottomFrameButton = self.buttons[0]
        self.hideBottomFrameButton['text']='Hide Bottom'
        self.hideBottomFrameButton['command']=self.hideBottom
        self.leaveButton = self.buttons[1]
        self.leaveButton['text']='Leave World'
        self.leaveButton['command']=self.switchToPvEWorldLobby
        self.exitButton = self.buttons[2]
        self.exitButton['text']='Exit Game'
        self.returnButton=self.buttons[3]
        self.returnButton['text']='Return to World'
        self.returnButton['command']=self.hideMenuFrame
    
    def hideBottom(self):
        
        if not self.bottomHidden:
            self.bottomHidden = True
            self.world.hideBottom()
            self.hideBottomFrameButton['text'] = 'Show Bottom'
        else:
            self.bottomHidden = False
            self.world.showBottom()
            self.hideBottomFrameButton['text'] = 'Hide Bottom'
    
    def switchToPvEWorldLobby(self):
        main.switchEnvironment("PvEWorldLobby")
        
    def unload(self):
        self.menuButton.destroy() 
        self.menuFrame.destroy()