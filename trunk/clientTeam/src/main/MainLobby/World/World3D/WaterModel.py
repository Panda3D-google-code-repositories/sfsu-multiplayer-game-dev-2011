from direct.interval.IntervalGlobal import Sequence
from direct.interval.LerpInterval import LerpFunc

from panda3d.core import NodePath
from panda3d.core import TransparencyAttrib

from common.Constants import Constants

class WaterModel(NodePath):

    def __init__(self, type, height_min, height_max):

        NodePath.__init__(self, 'Water')

        self.height_min = height_min
        self.height_max = height_max
        self.percent = 0

        self.waterModel = loader.loadModel('models/square')
        self.waterModel.reparentTo(self)
        self.waterModel.setColor(1, 1, 1, 0.8)
        self.waterModel.setTexture(loader.loadTexture('models/water/water.png'))
        self.waterModel.setTransparency(TransparencyAttrib.MAlpha)

        self.waterSphere = loader.loadModel('models/smiley')
        self.waterSphere.reparentTo(self)
        self.waterSphere.setScale(0.3)
        self.waterSphere.hide()

        self.waterSequence = Sequence()
        self.setLevel(100)

    def getWaterSphere(self):
        return self.waterSphere

    def getSize(self):
        return self.waterSphere.getBounds().getRadius() * (2 * self.waterSphere.getSx(render))

    def getLevel(self):
        return self.percent

    def setLevel(self, percent):
        self.percent = percent

        self.waterSequence.clearToInitial()

        lerpRaise = LerpFunc(self._setLevel,
                             duration = 3.0,
                             fromData = self.percent,
                             toData = self.percent * 1.05)

        lerpLower = LerpFunc(self._setLevel,
                             duration = 3.0,
                             fromData = self.percent * 1.05,
                             toData = self.percent)
        self.waterSequence = Sequence(lerpRaise, lerpLower)
        self.waterSequence.loop()

    def _setLevel(self, percent):
        self.setZ(self.height_min + (self.height_max - self.height_min) * float(percent) / 100)
