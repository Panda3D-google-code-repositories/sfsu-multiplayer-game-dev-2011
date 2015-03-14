from direct.gui.DirectGui import DirectWaitBar

from direct.interval.IntervalGlobal import Func
from direct.interval.IntervalGlobal import Sequence
from direct.interval.LerpInterval import LerpFunc

class DirectMeterBar(DirectWaitBar):

    def __init__(self, command = None, extraArgs = [], **kw):

        DirectWaitBar.__init__(self, **kw)
        self.initialiseoptions(DirectMeterBar)

        self['barColor'] = self['barColor']

        self.command = command
        self.extraArgs = extraArgs

        self.textScale = self['text_scale']
        self.maxValueText = str(self['range'])

        self.rangeList = []
        self.lastValue = 0
        self.lastTarget = 0
        self.isMax = False

        self.barSequence = Sequence()

    def destroy(self):

        DirectWaitBar.destroy(self)
        self.barSequence.clearToInitial()

    def setMaxValue(self, range):

        self['range'] = range

        self.maxValueText = self.format(range)
        self['text'] = self.format(self['value']) + ' / ' + self.maxValueText

    def setInitialValue(self, value, range):

        self.setMaxValue(range)

        self['value'] = value
        self.setBarText(value)

    def setCurrentValue(self, value):

        self.stopBarSequence()

        self.lastTarget = self.lastTarget - self.lastValue + value
        self.lastValue = 0

        if self.lastTarget != 0:
            self.barSequence = Sequence( LerpFunc(self.setBarValue, duration = 1.0, fromData = 0, toData = self.lastTarget),
                                         Func(self.stopBarSequence) )
            self.barSequence.start()

    def setRangeList(self, rangeList):

        self.isMax = False
        self.rangeList.extend(rangeList)

    def setBarValue(self, value):

        value = int(value)
        diff = value - self.lastValue
        self.lastValue = value

        newValue = self['value'] + diff
        isOverflow = newValue >= self['range']

        isMax = isOverflow and len(self.rangeList) == 0

        if isMax:
            self['value'] = self['range']
            self.barSequence.clearToInitial()
        else:
            self['value'] = newValue % self['range']

        if isOverflow and not self.isMax:
            if self.command:
                apply(self.command, self.extraArgs)

            if len(self.rangeList) > 0:
                self.setMaxValue(self.rangeList.pop(0))

        if value >= self.lastTarget:
            self.lastValue = 0
            self.lastTarget = 0

        if isMax:
            self['text'] = 'MAX'
            self['text_scale'] = self.textScale
        else:
            self.setBarText(self['value'])

        self.isMax = isMax

    def setBarText(self, value):

        self['text'] = self.format(value) + ' / ' + self.maxValueText

        if self.barSequence.isPlaying():
            self['text_scale'] = (self.textScale[0] * 1.15, self.textScale[1] * 1.15)

    def format(self, value):

        value = str(int(value))

        if len(value) <= 3:
            return value

        return self.format(value[:-3]) + ',' + value[-3:]

    def stopBarSequence(self):

        self.barSequence.clearToInitial()
        self['text_scale'] = self.textScale
