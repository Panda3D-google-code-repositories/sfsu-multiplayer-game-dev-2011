#@PydevCodeAnalysisIgnore

from common.Constants import Constants
from common.DirectBasicButton import DirectBasicButton
from direct.gui.DirectFrame import DirectFrame
from direct.gui.DirectGui import DGG
from direct.gui.DirectSlider import DirectSlider
from pandac.PandaModules import TransparencyAttrib

class PlayerWindow:
    '''
    a window that will display a list of current active players
    '''

    def __init__(self, pos, parent=None):
        self.pos = pos
        self.parent = parent
        self.createMainFrame()
        self.createComponents()
    def createMainFrame(self):
        
        self.mainFrame = DirectFrame(frameColor = Constants.BG_COLOR,
                                      frameSize = (-0.5, 0.5, -0.75,0.75),
                                      pos=self.pos)
        self.mainFrame.reparentTo(self.parent)
        self.mainFrame.hide()
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
        
        self.scrollBar = DirectSlider( pos = (0.46, 0, -0.04),
                                       scale = 0.13,
                                       value = 1,
                                       range = (1, 0),
                                       frameSize =(-0.05,0.05,-5.2,5.2),
                                       scrollSize = 1,
                                       pageSize = 1,
                                       orientation = DGG.VERTICAL,
                                       thumb_frameSize = (-0.1, 0.1, -0.25, 0.25),
                                       thumb_relief = DGG.FLAT)
#                                       command = self.scrollChatLog )
        self.scrollBar.reparentTo(self.mainFrame)
            
    def hide(self):
        self.mainFrame.hide()
    
    def show(self):
        self.mainFrame.show()
    def hideHideButton(self):
        self.hideButton.hide()
        
    def unload(self):
        self.mainFrame.destroy()