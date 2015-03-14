#@PydevCodeAnalysisIgnore
from direct.gui.DirectGui import DGG
from direct.gui.DirectGui import DirectButton
from direct.gui.DirectGui import DirectFrame


class DirectBasicButton(DirectButton):

    def __init__(self, onMouseText = '', onMouseOver = None, onMouseOverExtraArgs = [], 
                 onMouseOut = None, onMouseOutExtraArgs = [], **kw):

        self.onEnterText = onMouseText
        self.onEnter = onMouseOver
        self.onEnterExtraArgs = onMouseOverExtraArgs
        self.onExit = onMouseOut
        self.onExitExtraArgs = onMouseOutExtraArgs

        DirectButton.__init__(self, **kw)
        self.initialiseoptions(DirectBasicButton)

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

        if self.onMouseLabel:
            self.onMouseLabel.show()

        if self.onEnter:
            apply(self.onEnter, self.onEnterExtraArgs)

        if len(self.onEnterText) > 0:
            main.mPicker2D.handleTextHoverEnter(self, self.onEnterText)

    def onMouseOut(self, pos):

        if self.onMouseLabel:
            self.onMouseLabel.hide()

        if self.onExit:
            # get rid of []
            apply(self.onExit, self.onExitExtraArgs)
        if len(self.onEnterText) > 0:
            main.mPicker2D.handleHoverExit()

    def setOnMouseOverExtraArgs(self, extraArgs):
        
        self.onEnterExtraArgs = extraArgs
        
    def setMouseText(self, text):

        self.onEnterText = text
             
    def removeMouseLabel(self):

        self.onMouseLabel.destroy()
        self.onMouseLabel = None
