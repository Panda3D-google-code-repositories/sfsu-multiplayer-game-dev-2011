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
import pickle

from main.World.Flora3D import Grass3D
from main.World.Flora3D import Plant3D
from main.World.Terrain3D import TerrainModel

class Env3D():
    def __init__(self, xo, yo):
        self.s = 100
        if Constants.DEBUG:
            print "Creating environment"
        self.numTerrains = 4
        self.zones = []
        self.zoneDict = dict()
        self.setupMip(xo,yo)
        self.setupTerrain(xo,yo)
        taskMgr.add(self.updateTask, "updateTerrain")
    def setupTerrain(self,xo,yo):
        self.makeTerrain()
        self.root.reparentTo(render)
        self.x = self.root.getX()
        self.y = self.root.getY()
    def makeTerrain(self):
        self.tmodel = TerrainModel(self, 512)
        self.terrain = GeoMipTerrain("terrain")
        self.terrain.setHeightfield('models/terrain/current_height.png')
        self.terrainTex = loader.loadTexture('models/terrain/current_texture.png')
        self.terrain.setBruteforce(True)
        self.terrain.setBlockSize(32)
        self.terrain.setNear(40)
        self.terrain.setFar(100)
        self.root = self.terrain.getRoot()
        self.root.setSz(self.s)
        self.root.setSx(4)
        self.root.setSy(4)
        self.root.setTexture(TextureStage.getDefault(), self.terrainTex)
        self.terrain.generate()
        self.makeWater()
    def setupMip(self,xo,yo):
        for x in range(3):
            for y in range(3):
                self.zones.append(Zone3D(self,x,y))
                self.zoneDict[(x,y)] = self.zones[y+x*3]
                self.zones[y+x*3].xoff = xo
                self.zones[y+x*3].yoff = yo
                if y == 2:
                    self.zones[y+x*3].water = True
    def getWaterHeight(self, (x,y)):
        if self.zoneDict[(x,y)].water:
            h = self.zoneDict[(x,y)].waterHeight
            h = h*self.s*50/100
            return h
        return 0
    def makeWater(self):
        self.water = []
        i = 0
        for x in range(3):
            for y in range(3):
                if self.zoneDict[(x,y)].water:
                    h = self.zoneDict[(x,y)].waterHeight
                    self.water.append(WaterModel(h, (x,y)))
                    realx = self.zones[y+x*3].getX(256)
                    realy = self.zones[y+x*3].getY(256)
                    print realx, realy
                    self.water[i].model.setX(realx)
                    self.water[i].model.setSx(512)
                    self.water[i].model.setY(realy)
                    self.water[i].model.setSy(512)
                    self.water[i].model.setZ(self.getWaterHeight((x,y)))
                    self.water[i].model.reparentTo(render)
                    self.water[i].model.setTransparency(1)
                    i = i+1
    def updateTask(self, task):
        self.terrain.update()
        return task.cont

class WaterModel():
    def __init__(self, h, (x,y)):
        self.model = loader.loadModel("models/square")
        self.tex = loader.loadTexture("models/water/water.png")
        self.model.setColor(Vec4(1,1,1,0.5))
        self.model.setTexture(self.tex)
        self.height = h
        self.x = x
        self.y = y
        
class Zone3D():
    def __init__(self, env1,x,y):
        if Constants.DEBUG:
            print 'creating zone'
        self.zonetype = random.randint(0,4)
        self.grass = random.randint(0,5)
        self.water = False
        self.waterHeight = 0.5
        self.envx = x
        self.envy = y
        self.numTerrains = 4
        self.env = env1
        self.xoff = 0
        self.yoff = 0
        self.size = 513.0/3.0
        self.playerBuffer = 0
        self.plants = []
        self.grasses = []
        self.x = x*self.size*4
        self.y = y*self.size*4
        #self.root = render.attachNewNode('root')
    def addBigTree(self, x, y):
        self.plants.append(Plant3D().bigTree(self, x, y))
    def addBaobabTree(self, x, y):
        self.plants.append(Plant3D().baobabTree(self, x, y))
    def demo_randomHealth(self):
        for p in self.plants:
            p.setHealthy(bool(random.getrandbits(1)))
    def demo_addBigTree(self):
        x = self.getX(0)
        y = self.getY(0)
        for i in range(20):
            self.plants.append(Plant3D().bigTree(self, random.randint(40,480), random.randint(40,480)))
    def demo_addBaobabTree(self):
        x = self.getX(0)
        y = self.getY(0)
        for i in range(20):
            self.plants.append(Plant3D().baobabTree(self, random.randint(40,480), random.randint(40,480)))
    def getX(self,x):
        return self.x + x
    def getY(self,y):
        return self.y + y
    def getElevation(self, x, y):
        cx = x / 4
        cy = y / 4
        return self.env.terrain.getElevation(cx, cy)*100

