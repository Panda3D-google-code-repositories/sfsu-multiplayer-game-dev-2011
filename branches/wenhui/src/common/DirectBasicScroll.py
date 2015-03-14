from direct.gui.DirectGui import DGG
from direct.gui.DirectSlider import DirectSlider

class DirectBasicScroll(DirectSlider):
    
    def __init__(self, **kw):
        
        DirectSlider.__init__(self, **kw)

        self.bind(DGG.ENTER, self.onMouseOverExecute)
        self.bind(DGG.EXIT, self.onMouseOutExecute)
        
    def onMouseOverExecute(self, pos):
        print ''
        
    def onMouseOutExecute(self, pos):
        print ''