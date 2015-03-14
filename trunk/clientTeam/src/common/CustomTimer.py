'''
Created on Nov 24, 2011

@author: Wenhui
'''
from direct.interval.IntervalGlobal import Func
from direct.interval.IntervalGlobal import Sequence
from direct.interval.IntervalGlobal import Wait

from threading import Thread
from time import sleep
from time import time

class CountDownTimer(Thread):
    """
    Use to for time count down.
    To reset timer, call stopTimer() first, then instantiate a new CountDownTimer object
    """
    def __init__(self, _range, label=None, command=None, extraArgs=[],):
        """
        label is the object to display count-down time, it should be DirectLabel instance,
        command is the function need to be execute after time runs up.
        """
        Thread.__init__(self)
        self.label = label
        self.range = _range
        self.command=command
        self.args = extraArgs
        self.toStop=False

    def run(self):
        _endTime = time()+self.range
        _elpase=self.range
        while _elpase > 0 and not self.toStop:
            self.label['text']='Game will start at '+str(_elpase)+'s'
            _elpase=int(_endTime - time())
            sleep(1)

        if self.command and not self.toStop:  
            apply(self.command, self.args) 

    def stop(self):
        self.toStop = True
 
class CountUpTimer:

    def __init__(self, label):
        """
        label is the object to display count-up time, it should be DirectLabel instance
        command is the function need to be execute after time runs up
        """
        self.label = label
        
        self.commandList = {}

        self.startDay = 1
        self.startHour = 0

        self.rate = 1.0

        self.day = self.startDay
        self.hour = self.startHour

        self.timeSequence = Sequence()

    def addCommand(self, name, interval, command, extraArgs = []):
        self.commandList[name] = (interval, command, extraArgs)

    def removeCommand(self, name):
        if name in self.commandList:
            del self.commandList[name]

    def increment(self):
        self.hour = (self.hour + 1) % 24

        if self.hour == 0:
            self.day = self.day + 1

        self.label['text'] = 'Day: ' + str(self.day) + '  HR: ' + str(self.hour)

        for command in self.commandList.values():
            (interval, command, extraArgs) = command

            if (self.hour + 1) % interval == 0:
                apply(command, extraArgs)

    def setTime(self, hour, rate):

        self.startDay = hour / 24 + 1
        self.startHour = hour % 24

        self.rate = float(rate)

        self.day = self.startDay
        self.hour = self.startHour

    def start(self):
        self.timeSequence.clearToInitial()
        self.timeSequence = Sequence(Wait(3600 / self.rate), Func(self.increment))
        self.timeSequence.loop()

    def stop(self):
        self.timeSequence.clearToInitial()
