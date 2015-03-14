from random import randint

from direct.interval.IntervalGlobal import Func
from direct.interval.IntervalGlobal import Sequence
from direct.interval.LerpInterval import LerpFunc
from direct.particles.ParticleEffect import ParticleEffect

from panda3d.core import AmbientLight
from panda3d.core import DirectionalLight
from panda3d.core import VBase4

from common.Constants import Constants

class World3D:

    def __init__(self, parent):

        self.parent = parent

        self.timePeriod = {Constants.T_NIGHT    : [0, 4, 4],
                           Constants.T_DAWN     : [4, 5, 1],
                           Constants.T_MORNING  : [5, 6, 1],
                           Constants.T_DAY      : [6, 12, 6]}

        self.lightEffects = []
        self.lightEffects.append([Constants.T_NIGHT, VBase4(0.1, 0.1, 0.1, 1), VBase4(0.25, 0.25, 0.45, 1)])
        self.lightEffects.append([Constants.T_DAWN, VBase4(0.96, 0.64, 0.38, 1), VBase4(0.3, 0.3, 0.3, 1)])
        self.lightEffects.append([Constants.T_MORNING, VBase4(0.7, 0.6, 0.8, 1), VBase4(0.4, 0.4, 0.4, 1)])
        self.lightEffects.append([Constants.T_DAY, VBase4(0.9, 0.8, 0.9, 1), VBase4(0.7, 0.7, 0.7, 1)])

        self.rainParticles = None
        self.rate = 1

        self.createSky()
        self.createLights()

        self.parent.soundMgr.playSound('nature', None)
        self.lightSequence = Sequence()
        self.timeSequence = Sequence()
#        self.rainEffects('rain')

    def loadRain(self):

        base.enableParticles()

        self.rainParticles = ParticleEffect()
        self.rainParticles.loadConfig('models/rain/rain.ptf')
        self.rainParticles.start(render)
        self.rainParticles.setZ(100)
        
    def createSky(self):

        self.skysphere = loader.loadModel('models/bluesky/blue-sky-sphere')
        self.skysphere.reparentTo(render)

        self.daytex = loader.loadTexture('models/bluesky/day.png')
        self.nighttex = loader.loadTexture('models/bluesky/night.png')
        self.raintex = loader.loadTexture('models/bluesky/day.png')

    def createLights(self):

        self.ambientLight = AmbientLight('ambLight')
        render.setLight(render.attachNewNode(self.ambientLight))

        self.directionalLight = DirectionalLight('dirLight')
        render.setLight(render.attachNewNode(self.directionalLight))

    def createTimeEffect(self, effect_1, effect_2, duration):

        lightEffect = self.lightEffects[effect_1]
        nextLightEffect = self.lightEffects[effect_2]

        dirLightDiff = nextLightEffect[1] - lightEffect[1]
        dirLightDiff[3] = 1
        ambLightDiff = nextLightEffect[2] - lightEffect[2]
        ambLightDiff[3] = 1

        return LerpFunc(self.setLighting, duration = duration * 3600 / self.rate, extraArgs = [lightEffect, dirLightDiff, ambLightDiff])

    def startTime(self, hour, rate = 1):

        self.rate = float(rate)

        self.directionalLight.setColor(VBase4(0.9, 0.8, 0.9, 1))
        self.ambientLight.setColor(VBase4(0.7, 0.7, 0.7, 1))

        return

        self.timeSequence = Sequence(self.createTimeEffect(Constants.T_NIGHT, Constants.T_NIGHT, 4),
                                     self.createTimeEffect(Constants.T_NIGHT, Constants.T_DAWN, 2),
                                     self.createTimeEffect(Constants.T_DAWN, Constants.T_MORNING, 2),
                                     self.createTimeEffect(Constants.T_MORNING, Constants.T_DAY, 4),
                                     self.createTimeEffect(Constants.T_DAY, Constants.T_MORNING, 6),
                                     self.createTimeEffect(Constants.T_MORNING, Constants.T_DAWN, 2),
                                     self.createTimeEffect(Constants.T_DAWN, Constants.T_NIGHT, 2),
                                     self.createTimeEffect(Constants.T_NIGHT, Constants.T_NIGHT, 2),
                                     Func(self.loopTime))
        self.timeSequence.start(startT = (hour % 24) * 3600 / self.rate)

    def loopTime(self):
        self.timeSequence.start()

    def setLighting(self, value, lightEffect, dirLightDiff, ambLightDiff):

        self.directionalLight.setColor(lightEffect[1] + dirLightDiff * value)
        self.ambientLight.setColor(lightEffect[2] + ambLightDiff * value)

    def rainEffects(self, effect):

        if effect == 'rain':
#            self.directionalLight.setColor(VBase4(0.6, 0.5, 0.9, 1))
#            self.ambientLight.setColor(VBase4(0.3, 0.3, 0.5, 1))
            self.loadRain()
            self.parent.soundMgr.playSound('rain', None)

            if randint(0, 25) % 5 == 0:
                self.parent.soundMgr.playSound('thunder', None)
        elif effect == 'stop-rain':
            self.parent.soundMgr.stopSound('thunder', None)
            self.parent.soundMgr.stopSound('rain', None)

            if self.rainParticles is not None:
                self.rainParticles.cleanup()
                self.rainParticles = None

            taskMgr.remove('RainTask')
