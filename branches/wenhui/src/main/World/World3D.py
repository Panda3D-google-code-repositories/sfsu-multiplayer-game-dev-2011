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

class Env():
    def __init__(self, xo, yo):
        if Constants.DEBUG:
            print "Creating environment"
        self.zones = []
        self.terrainFiles = []
        self.terrainFiles.append('models/terrain/tropical01.png.bam')
        self.terrainFiles.append('models/terrain/desert01.png.bam')
        #szones[0].setup(random.sample(self.terrainFiles,1)[0])
        for x in range(3):
            for y in range(3):
                self.zones.append(Zone())
                self.zones[y+x*3].xoff = xo
                self.zones[y+x*3].yoff = yo
                self.zones[y+x*3].setup(self.terrainFiles[(y+x*3)%2])
                self.zones[y+x*3].move(x,y)

class Zone():
    def __init__(self):
        if Constants.DEBUG:
            print 'creating zone'
        self.xoff = 0
        self.yoff = 0
        self.size = 513
        self.playerBuffer = 5
    def moveDown(self):
        self.terrain.setY(self.y-self.size)
        self.y-= self.size
    def moveRight(self):
        self.terrain.setX(self.x+self.size)
        self.x+= self.size
    def move(self,x,y):
        self.x = (x*self.size)+(self.size*3*self.xoff)+(self.xoff*self.playerBuffer)
        self.y = (y*self.size)+(self.size*3*self.yoff)+(self.yoff*self.playerBuffer)
        self.terrain.setX(self.x)
        self.terrain.setY(self.y)
    def setup(self, model):
        self.modelName = model
        self.terrain = loader.loadModel(self.modelName)
        self.root = self.terrain
        self.root.setTexScale(TextureStage.getDefault(), 1)
        self.root.reparentTo(render)
        self.x = self.terrain.getX()
        self.y = self.terrain.getY()

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
        self.scaleFactor = 0.5  
        self.env = []
        self.proot = render.attachNewNode('proot')
        self.plants = []
        self.plants.append(loader.loadModel("models/bigTree/bigTree"))
        self.plants[0].reparentTo(self.proot)
        self.plants[0].setX(100)
        self.plants[0].setY(356)
        self.plants[0].setZ(20)
        self.env.append(Env(0,0))
        self.env.append(Env(0,1))
        self.doSky()
        base.enableParticles()
        self.pspawn = loader.loadModel("models/square")
        self.r = 0
        watertex = loader.loadTexture("models/bluesky/sky-material-24-cl.png")
        watertex.setWrapU(Texture.WMRepeat)
        watertex.setWrapV(Texture.WMRepeat)
        watertex.setWrapW(Texture.WMRepeat)
        self.root2 = render.attachNewNode("root2")
        self.setupLights()
        taskMgr.add(self.updateTask, "update")
        taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        camera.reparentTo(render)
        camera.setPosHpr(129,-129, 400, 12, -45, 0)
        base.disableMouse()
        #base.enableMouse()
    def animateTex(self, task):
        currentFrame = int(task.time * task.fps)
        task.obj.setTexture(task.textures[currentFrame % len(task.textures)],1)
        return task.cont
    def updateTask(self, task):
        return task.cont
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        return Task.cont
    def doSky(self):
        self.skysphere = loader.loadModel('models/bluesky/blue-sky-sphere')
        self.skysphere.setEffect(CompassEffect.make(render))
        self.skysphere.setScale(1)
        self.skysphere.reparentTo(camera)
        self.skyTask = taskMgr.add(self.animateTex, "skyTask")
        self.skyTask.fps = 0.2
        self.skyTask.obj = self.skysphere
        self.daytex = loader.loadTexture("models/bluesky/day.png")
        self.nighttex = loader.loadTexture("models/bluesky/night.png")
        self.skyTask.textures = [self.daytex, self.nighttex]
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
