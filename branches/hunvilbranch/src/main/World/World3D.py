from panda3d.ai import *
from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionRay
from panda3d.core import AmbientLight, DirectionalLight, LightAttrib
from panda3d.core import TextNode
from panda3d.core import Point3, Vec3, Vec4, BitMask32
from panda3d.core import GeoMipTerrain, Filename
from panda3d.core import Texture, TextureStage
from pandac.PandaModules import CompassEffect
from panda3d.physics import BaseParticleEmitter,BaseParticleRenderer
from panda3d.physics import PointParticleFactory,SpriteParticleRenderer
from panda3d.physics import LinearNoiseForce,DiscEmitter
from direct.particles.Particles import Particles
from direct.particles.ParticleEffect import ParticleEffect
from direct.particles.ForceGroup import ForceGroup
from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.DirectObject import DirectObject
from direct.task.Task import Task
from direct.interval.ActorInterval import ActorInterval
import direct.directbase.DirectStart
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import *
from math import *
import sys

from common.Constants import Constants
from common.DatabaseHelper import DatabaseHelper
from common.DirectBasicButton import DirectBasicButton
from common.DirectTextField import DirectTextField
from common.DirectWindow import DirectWindow
import random

from main.World.Environment3D import Env3D
from main.World.Environment3D import Zone3D
from main.World.Flora3D import Grass3D
from main.World.Flora3D import Plant3D

class Weather3D():
    def __init__(self):
        self.rain = False

class World3D(DirectObject):

    def __init__(self):

        if Constants.DEBUG:
            print 'Loading World...'
        self.main = main
        base.disableMouse()
        self.createMainFrame()
        self.createBackground()
        self.displayGame()
         
    def PointAtZ(self, z, point, vec):
        return point + vec * ((z-point.getZ()) / vec.getZ())
    def SquarePos(self, i):
        return Point3((i%12) - 5, int(i/12) - 5, 0)
    
    def getControls(self):
        return self.controls
    
    def createMainFrame(self):
        """Create the main base frame."""

        
    def createBackground(self):
        """Create a background for the login screen."""
        
    def displayGame(self):      
        self.effectStatus = 'day'
        self.scaleFactor = 0.5
        self.env = []
        self.env.append(Env3D(0,0))
        zone1 = self.env[0].zones[0]
        zone1.demo_addBigTree()
        zone2 = self.env[0].zones[5]
        #zone2.demo_addTree()
        zone3 = self.env[0].zones[4]
        zone3.demo_addBaobabTree()
        zone3.demo_randomHealth()
        #self.env.append(Env3D(0,1))
        self.doSky()
        base.enableParticles()
        self.rainParticles = None
        #self.loadRain()
        self.pspawn = loader.loadModel("models/square")
        self.r = 0
        watertex = loader.loadTexture("models/bluesky/sky-material-24-cl.png")
        watertex.setWrapU(Texture.WMRepeat)
        watertex.setWrapV(Texture.WMRepeat)
        watertex.setWrapW(Texture.WMRepeat)
        self.root2 = render.attachNewNode("root2")
        self.setupLights()
        taskMgr.add(self.updateTask, "update")
        camera.setPosHpr(256,256, 500, 80, -40, 0)
        camera.reparentTo(render)
        base.enableMouse()
        #base.disableMouse()
        #taskMgr.add(self.spinCameraTask, "SpinCameraTask")
    def animateTex(self, task):
        currentFrame = int(task.time * task.fps)
        task.obj.setTexture(task.textures[currentFrame % len(task.textures)],1)
        return task.cont
    def tempTask(self, task):
        currentFrame = int(task.time * task.fps)
        if currentFrame % 3 == 0 and self.effectStatus != 'day':
            self.globalEffects('day')
            self.effectStatus = 'day'
        if currentFrame % 3 == 1 and self.effectStatus != 'night':
            self.globalEffects('night')
            self.effectStatus = 'night'
        if currentFrame % 3 == 2 and self.effectStatus != 'rain':
            self.globalEffects('rain')
            self.effectStatus = 'rain'
        return task.cont
    def updateTask(self, task):
        return task.cont
    def spinCameraTask(self, task):
        angleDegrees = task.time * 12.0
        angleRadians = angleDegrees * (pi / 180.0)
        camera.setHpr(angleDegrees, -40, 0)
        return Task.cont
    def loadRain(self):
        self.rainModel = loader.loadModel('models/square')
        off = 256+512
        offz = 100
        self.rainModel.setPos(off, off, offz)
        self.rainModel.reparentTo(render)
        self.rainParticles = ParticleEffect()
        self.rainParticles.loadConfig(Filename('models/rain/rain.ptf'))  
        self.rainParticles.setSx(4)
        self.rainParticles.setSy(4)
        self.rainParticles.setSz(4)      
        self.rainParticles.start(self.rainModel)
        self.rainParticles.setPos(0, 0, offz)
    def doSky(self):
        self.skysphere = loader.loadModel('models/bluesky/blue-sky-sphere')
        self.skysphere.setEffect(CompassEffect.make(render))
        self.skysphere.setScale(1)
        self.skysphere.reparentTo(camera)
        self.skyTask = taskMgr.add(self.animateTex, "skyTask")
        self.tempTask1 = taskMgr.add(self.tempTask, "tempTask")
        self.skyTask.fps = 0.2
        self.tempTask1.fps = 0.2
        self.skyTask.obj = self.skysphere
        self.daytex = loader.loadTexture("models/bluesky/day.png")
        self.nighttex = loader.loadTexture("models/bluesky/night.png")
        self.raintex = loader.loadTexture("models/bluesky/day.png")
        self.skyTask.textures = [self.daytex, self.nighttex, self.raintex]
    def setupLights(self):
        self.ambientLight = AmbientLight("ambientLight")
        self.ambientLight.setColor(Vec4(.4, .4, .35, 1))
        self.directionalLight = DirectionalLight("directionalLight")
        self.directionalLight.setDirection(Vec3( 0, 8, -2.5 ) )
        self.directionalLight.setColor(Vec4( 0.9, 0.8, 0.9, 1 ) )
        render.setLight(render.attachNewNode( self.directionalLight ) )
        render.setLight(render.attachNewNode( self.ambientLight ) )
    def globalEffects(self, effect):
        if effect == 'day':
            self.directionalLight.setColor(Vec4( 0.9, 0.8, 0.9, 1 ) )
            self.ambientLight.setColor(Vec4(.4, .4, .35, 1))
            if self.rainParticles is not None:
                self.rainParticles.cleanup()
                self.rainParticles = None
            print 'Day lights'
        if effect == 'night':
            self.directionalLight.setColor(Vec4( 0.4, 0.3, 0.5, 1 ) )
            self.ambientLight.setColor(Vec4(.2, .2, .2, 1))
            if self.rainParticles is not None:
                self.rainParticles.cleanup()
                self.rainParticles = None
            print 'Night lights'
        if effect == 'rain':
            self.directionalLight.setColor(Vec4( 0.6, 0.5, 0.9, 1 ) )
            self.ambientLight.setColor(Vec4(.3, .3, .5, 1))
            self.loadRain()
            print 'Rain lights'
        #render.setLight(render.attachNewNode( self.directionalLight ) )
    def loadParticleConfig(self, file):
	    print('not yet implemented')
    def unload(self):
        """Unload this instance."""
        if Constants.DEBUG:
            print 'Unloading World...'
        main.removeGameControls()
