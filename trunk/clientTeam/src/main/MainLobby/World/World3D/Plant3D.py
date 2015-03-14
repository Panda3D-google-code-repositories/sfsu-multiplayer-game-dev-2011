from direct.interval.IntervalGlobal import Func
from direct.interval.IntervalGlobal import Sequence
from direct.interval.IntervalGlobal import Wait

from panda3d.core import FadeLODNode
from panda3d.core import NodePath
from panda3d.core import TransparencyAttrib

from common.Constants import Constants

from main.MainLobby.World.World3D.Plant import Plant

class Plant3D(Plant, NodePath):

    def __init__(self, plantID, name, plantType, avatarID, zoneID, biomass, model_dir, model_file, animation, scale):

        Plant.__init__(self, plantID, name, plantType, avatarID, zoneID, biomass)

        self.models = []
        self.model_dir = model_dir
        self.model_file = model_file
        self.animation = animation
        self.healthy = True
        self.scale = scale

        self.createPlant()

        tightBounds = self.getChild(0).getTightBounds()
        self.lowerBound = tightBounds[0]
        self.upperBound = tightBounds[1]

        self.plantModel.setColorScale(1, 1, 1, 0)
        self.enterSequence = self.plantModel.colorScaleInterval(1, (1, 1, 1, 1))
        self.exitSequence = self.plantModel.colorScaleInterval(2, (0, 0, 0, 0.1))

        self.enterSequence.start()

        self.deathSequence = Sequence()

    def createPlant(self):

        fadeLoD = FadeLODNode('Plant')
        fadeLoD.addSwitch(Constants.LOD_FAR, Constants.LOD_NEAR)
        NodePath.__init__(self, fadeLoD)

        self.plantModel = loader.loadModel('models/' + self.model_dir + '/' + self.model_file)
        self.plantModel.reparentTo(self)

        self.setScale(self.scale / 20.0)

        self.setCollideMask(Constants.CLICKABLE_MASK)
        self.setTag('type', 'Plant')
        self.setTag('object_id', str(self.plantID))
        self.plantModel.setTransparency(TransparencyAttrib.MAlpha)

    def setAttackAware(self, attacker):
        pass

    def getPlantModel(self):
        return self.plantModel

    def death(self):

        self.deathSequence = Sequence(Wait(1.0), self.exitSequence, Func(self.setGroupSize, self.groupSize - self.numDead))
        self.deathSequence.start()

        game.worldGui.floatingText.createText(Constants.TEXT_TYPE_DEATH, '!', self)

        self.lifeStatus = Constants.LIFE_STATUS_DYING

    def reduceGroupSize(self, amount):

        self.numDead = min(amount, self.groupSize)

        if self.numDead < self.groupSize:
            self.setGroupSize(self.groupSize - self.numDead)
        else:
            self.death()

    def unload(self):

        self.enterSequence.clearToInitial()
        self.exitSequence.clearToInitial()
        self.deathSequence.clearToInitial()

        self.removeNode()
