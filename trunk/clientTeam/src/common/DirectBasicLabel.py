from direct.gui.DirectGui import DGG
from direct.gui.DirectGui import DirectFrame
from direct.gui.DirectGui import DirectLabel

from direct.interval.IntervalGlobal import Func
from direct.interval.IntervalGlobal import Sequence
from direct.interval.LerpInterval import LerpFunc

class DirectBasicLabel(DirectLabel):

    def __init__(self, onMouseOverGlow = True, onMouseText = '', onMouseOver = None, onMouseOverExtraArgs = [], 
                 onMouseOut = None, onMouseOutExtraArgs = [], **kw):

        self.onMouseOverGlow = onMouseOverGlow
        self.onEnterText = onMouseText
        self.onEnter = onMouseOver
        self.onEnterExtraArgs = onMouseOverExtraArgs
        self.onExit = onMouseOut
        self.onExitExtraArgs = onMouseOutExtraArgs

        DirectLabel.__init__(self, **kw)
        self.initialiseoptions(DirectBasicLabel)

        self.textScale = self['text_scale']

        self.onMouseLabel = DirectFrame( frameSize = self['frameSize'],
                                         frameColor = (1, 1, 1, 0.3),
                                         pos = (0, 0, 0) )
        self.onMouseLabel.reparentTo(self)
        self.onMouseLabel.hide()

        self.bind(DGG.ENTER, self.onMouseOver)
        self.bind(DGG.EXIT, self.onMouseOut)

        self.counterSequence = Sequence()

    def enable(self):

        self['text_fg'] = Constants.TEXT_COLOR
        self['state'] = DGG.NORMAL

    def disable(self):

        self['text_fg'] = (1, 1, 1, 0.3)
        self['state'] = DGG.DISABLED

    def destroy(self):

        DirectLabel.destroy(self)
        self.counterSequence.clearToInitial()

    def onMouseOver(self, pos):

        if self.onMouseOverGlow:
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

        if self.onMouseOverGlow:
            self.onMouseLabel.hide()

        if self.onExit:
            apply(self.onExit, self.onExitExtraArgs)

        if len(self.onEnterText) > 0:
            main.mPicker2D.handleHoverExit()

    def setMouseText(self, text):

        self.onEnterText = text

    def setCounterValue(self, value):

        self.stopCounterSequence()

        if value != int(self['text'].replace(',', '')):
            self.counterSequence = Sequence( LerpFunc(self.setCounterText, duration = 1.0, fromData = int(self['text'].replace(',', '')), toData = value),
                                             Func(self.stopCounterSequence) )
            self.counterSequence.start()

    def setCounterText(self, value):

        self['text'] = self.format(value)

        if self.counterSequence.isPlaying():
            self['text_scale'] = (self.textScale[0] * 1.15, self.textScale[1] * 1.15)

    def format(self, value):

        value = str(int(value))

        if len(value) <= 3:
            return value

        return self.format(value[:-3]) + ',' + value[-3:]

    def stopCounterSequence(self):

        self.counterSequence.clearToInitial()
        self['text_scale'] = self.textScale

    def setPaddedCounterValue(self, value):

        self.stopCounterSequence()

        if value != int(self['text']):
            self.counterSequence = Sequence( LerpFunc(self.setPaddedCounterText, duration = 1.0, fromData = int(self['text']), toData = value),
                                             Func(self.stopCounterSequence) )
            self.counterSequence.start()

    def setPaddedCounterText(self, value):

        self['text'] = '%05d' % value

        if self.counterSequence.isPlaying():
            self['text_scale'] = (self.textScale[0] * 1.15, self.textScale[1] * 1.15)
