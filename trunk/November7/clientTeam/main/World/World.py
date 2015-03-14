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

class Zone():
    def __init__(self):
        if Constants.DEBUG:
            print 'creating zone'
    def moveDown(self):
        self.terrain.setY(self.y-513)
        self.y-=513
    def moveRight(self):
        self.terrain.setX(self.x+513)
        self.x+=513
    def setup(self, model):
        self.modelName = model
        self.tex = loader.loadTexture("models/terrain/sav.jpg")
        self.tex.setWrapU(Texture.WMRepeat)
        self.tex.setWrapV(Texture.WMRepeat)
        self.tex.setWrapW(Texture.WMRepeat)
        self.terrain = loader.loadModel(self.modelName)
        self.root = self.terrain
        self.root.setTexture(TextureStage.getDefault(), self.tex) 
        self.root.setTexScale(TextureStage.getDefault(), 10)
        self.root.reparentTo(render)
        self.x = self.terrain.getX()
        self.y = self.terrain.getY()

class World(DirectObject):

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
        self.scaleFactor = 0.5  
        self.zones = []
        self.terrainFiles = []
        self.terrainFiles.append('models/terrain/terrain00.png.bam')
        self.terrainFiles.append('models/terrain/terrain01.png.bam')
        self.doSky()
        base.enableParticles()
        self.pspawn = loader.loadModel("models/square")
        self.r = 0
        self.zones.append(Zone())
        #zones[0].setup(random.sample(self.terrainFiles,1)[0])
        self.zones[0].setup(self.terrainFiles[0])
        self.zones.append(Zone())
        self.zones[1].setup(self.terrainFiles[1])
        self.zones.append(Zone())
        self.zones[2].setup(self.terrainFiles[0])
        self.zones.append(Zone())
        self.zones[3].setup(self.terrainFiles[1])
        self.zones[1].moveRight()
        self.zones[2].moveDown()
        self.zones[3].moveRight()
        self.zones[3].moveDown()
        watertex = loader.loadTexture("models/bluesky/sky-material-24-cl.png")
        watertex.setWrapU(Texture.WMRepeat)
        watertex.setWrapV(Texture.WMRepeat)
        watertex.setWrapW(Texture.WMRepeat)
        camera.setPosHpr(50, 50, 70, 0, -45, 0)
        self.root2 = render.attachNewNode("root2")
        self.setupLights()
        taskMgr.add(self.updateTask, "update")
        taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        base.enableMouse()
    def updateTask(self, task):
        #for zone in self.zones:
        #    zone.terrain.update()
        return task.cont
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        return Task.cont
    def doSky(self):
        skysphere = loader.loadModel('models/bluesky/blue-sky-sphere')
        skysphere.setEffect(CompassEffect.make(render))
        skysphere.setScale(1)
        skysphere.reparentTo(camera)

    def setupLights(self):
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor(Vec4(.4, .4, .35, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(Vec3( 0, 8, -2.5 ) )
        directionalLight.setColor(Vec4( 0.9, 0.8, 0.9, 1 ) )
        render.setLight(render.attachNewNode( directionalLight ) )
        render.setLight(render.attachNewNode( ambientLight ) )
    def loadParticleConfig(self, file):
	    print('not yet implemented')
    def unload(self):
        """Unload this instance."""
        if Constants.DEBUG:
            print 'Unloading World...'
        main.removeGameControls()
