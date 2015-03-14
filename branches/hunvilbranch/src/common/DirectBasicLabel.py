from direct.gui.DirectGui import DGG
from direct.gui.DirectGui import DirectFrame
from direct.gui.DirectGui import DirectLabel

class DirectBasicLabel(DirectLabel):

    def __init__(self, onMouseText = '', onMouseOver = None, onMouseOverExtraArgs = [], 
                 onMouseOut = None, onMouseOutExtraArgs = [], **kw):

        self.onEnterText = onMouseText
        self.onEnter = onMouseOver
        self.onEnterExtraArgs = onMouseOverExtraArgs
        self.onExit = onMouseOut
        self.onExitExtraArgs = onMouseOutExtraArgs

        DirectLabel.__init__(self, **kw)
        self.initialiseoptions(DirectBasicLabel)

        self.onMouseLabel = DirectFrame( frameSize = self['frameSize'],
                                         frameColor = (1, 1, 1, 0.3),
                                         pos = (0, 0, 0) )
        self.onMouseLabel.reparentTo(self)
        self.onMouseLabel.hide()

        self.bind(DGG.ENTER, self.onMouseOver)
        self.bind(DGG.EXIT, self.onMouseOut)

    def enable(self):

        self['text_fg'] = Constants.TEXT_COLOR
        self['state'] = DGG.NORMAL

    def disable(self):

        self['text_fg'] = (1, 1, 1, 0.3)
        self['state'] = DGG.DISABLED

    def onMouseOver(self, pos):

        print 'onMouseOver called'
        if self.onMouseLabel:
            self.onMouseLabel.show()
            
        if self.onEnter:
            apply(self.onEnter, self.onEnterExtraArgs)

        if len(self.onEnterText) > 0:
            main.mPicker2D.handleTextHoverEnter(self, self.onEnterText)
    
    def setOnMouseOver(self, onMouseOver):
        
        self.onEnter = onMouseOver
    
    def setOnMouseOverExtraArgs(self, extraArgs):
        self.onEnterExtraArgs = extraArgs
    
    def setOnMouseOut(self, onMouseOut):
        self.onExit = onMouseOut
        
    def setOnMouseOutExtraArgs(self, extraArgs):
        self.onExitExtraArgs = extraArgs
        
    def onMouseOut(self, pos):

        self.onMouseLabel.hide()

        if self.onExit:
            apply(self.onExit, [self.onExitExtraArgs])

        if len(self.onEnterText) > 0:
            main.mPicker2D.handleHoverExit()

    def setMouseText(self, text):

        self.onEnterText = text
