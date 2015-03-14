
from common.Constants import Constants
from common.DirectBasicButton import DirectBasicButton
from common.DirectControls import DirectControls
from common.DirectWindow import DirectWindow
from direct.gui.DirectFrame import DirectFrame
from direct.gui.DirectGui import DGG
from direct.gui.DirectLabel import DirectLabel
from direct.gui.DirectSlider import DirectSlider
from panda3d.core import TransparencyAttrib, TextNode

class StatsControls(DirectControls):

    def __init__(self, parent):

        DirectControls.__init__(self, parent)

#        self.accept('escape', parent.hide)
        self.accept('s', parent.toggleVisibility)

class Stats:
    
    def __init__(self, world):
        
        self.world = world
        self.info = []
        self.maxItemsVisible=6
        self.createMainFrame()
        self.createSpecyInfo()
        self.createLog()
        
        self.control = StatsControls(self)
    def createMainFrame(self):
        
        self.statFrame = DirectWindow(frameSize=(-0.5, 0.5, -0.6, 0.6),
                                      frameColor=Constants.BG_COLOR,
                                      pos=(0, 0, 0.15),
                                      state=DGG.NORMAL)
        self.statFrame.reparentTo(self.world)
        self.statFrame.hide()
    
        self.hideButton = DirectBasicButton(text=" - ",
                                       text_fg=(1, 1, 1, 1),
                                       text_pos=(-0.007, -0.015),
                                       text_scale=0.05,
                                       frameColor=(0, 0, 0, 0.2),
                                       frameSize=(-0.04, 0.04, -0.025, 0.025),
                                       pos=(0.44, 0, 0.56),
                                       relief=DGG.FLAT,
                                       command=self.hide)
        self.hideButton.setTransparency(TransparencyAttrib.MAlpha)
        self.hideButton.reparentTo(self.statFrame)
        
    def show(self):
        self.statFrame.show()
        
    def hide(self):
        self.statFrame.hide()
    
    def toggleVisibility(self):
        
        if self.statFrame.isHidden():
            self.statFrame.show()
        else:
            self.statFrame.hide()
            
    def createSpecyInfo(self):
        
        self.specyFrame = DirectFrame(frameSize=(-0.42, 0.42, -0.3, 0.3),
                                     frameColor=(0.5, 0.5, 0.5, 0.2),
                                     pos=(0, 0, 0.22))
        self.specyFrame.reparentTo(self.statFrame)
        self.specyFrame.setTransparency(TransparencyAttrib.MAlpha)
        
        self.specy = DirectLabel(text='Specy',
                             text_scale=0.06,
                             text_pos=(0, -0.005),
                             frameSize=(-0.2, 0.2, -0.1, 0.1),
                             frameColor=(0, 0, 0, 0),
                             pos=(-0.32, 0, 0.25))
        self.specy.reparentTo(self.specyFrame)
        
        self.x = DirectLabel(text='X ',
                             text_scale=0.06,
                             text_pos=(0, -0.005),
                             frameColor=(0, 0, 0, 0),
                             pos=(0.0, 0, 0.25))
        self.x.reparentTo(self.specyFrame)
        
        self.w = DirectLabel(text='W ',
                             text_scale=0.06,
                             text_pos=(0, -0.005),
                             frameColor=(0, 0, 0, 0),
                             pos=(0.24, 0, 0.25)) 
        self.w.reparentTo(self.specyFrame)
        
        self.scrollBar = DirectSlider( pos = (0.385, 0, -0.03),
                                       scale = 0.13,
                                       value = 1,
                                       range = (1, 0),
                                       scrollSize = 1,
                                       frameSize = (-0.05,0.05,-1.80,1.8),
                                       pageSize = 1,
                                       orientation = DGG.VERTICAL,
                                       thumb_frameSize = (-0.1, 0.1, -0.2, 0.2),
                                       thumb_relief = DGG.FLAT)
#                                       command = self.scrollChatLog )
        self.scrollBar.reparentTo(self.specyFrame) 
    
    def createLog(self):
        
        
        for i in range(self.maxItemsVisible):
            _z = 0.16-i*0.08
            _specy = DirectLabel(text='Specy'+str(i),
                             text_scale=0.05,
                             text_pos=(0, -0.005),
                             frameColor=(0, 0, 0, 0),
                             pos=(-0.32, 0, _z))
            _specy.reparentTo(self.specyFrame)
        
            _x = DirectLabel(text='X'+str(i),
                             text_scale=0.05,
                             text_pos=(0, -0.005),
                             frameColor=(0, 0, 0, 0),
                             pos=(0.0, 0, _z))
            _x.reparentTo(self.specyFrame)
        
            _w = DirectLabel(text='W'+str(i),
                             text_scale=0.05,
                             text_pos=(0, -0.005),
                             frameColor=(0, 0, 0, 0),
                             pos=(0.24, 0, _z)) 
            _w.reparentTo(self.specyFrame)
        
                