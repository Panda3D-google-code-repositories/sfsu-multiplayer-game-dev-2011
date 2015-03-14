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


class Env3D():
    def __init__(self, xo, yo):
        if Constants.DEBUG:
            print "Creating environment"
        self.numTerrains = 4
        self.zones = []
        self.setupMip(xo,yo)
        taskMgr.add(self.updateTask, "updateTerrain")
    def setupMip(self,xo,yo):
        for x in range(3):
            for y in range(3):
                self.zones.append(Zone3D(self,x,y))
                self.zones[y+x*3].xoff = xo
                self.zones[y+x*3].yoff = yo
                self.zones[y+x*3].setupMip()
                self.zones[y+x*3].move(x,y)
    def updateTask(self, task):
        for z in self.zones:
            z.terrain.update()
        return task.cont

class Zone3D():
    def __init__(self, env1,x,y):
        if Constants.DEBUG:
            print 'creating zone'
        self.envx = x
        self.envy = y
        self.numTerrains = 4
        self.env = env1
        self.xoff = 0
        self.yoff = 0
        self.size = 513
        self.playerBuffer = 0
        self.plants = []
        self.grasses = []
        #self.root = render.attachNewNode('root')
    def makeTerrain(self):
        i1 = random.randint(1,self.numTerrains)
        self.terrain = GeoMipTerrain("terrain")
        self.terrain.setHeightfield('models/terrain/mip0'+str(i1)+'_height.png')
        self.terrainTex = loader.loadTexture('models/terrain/mip0'+str(i1)+'_texture.png')
        self.terrain.setBruteforce(False)
        self.terrain.setBlockSize(32)
        self.terrain.setNear(80)
        self.terrain.setFar(400)
        self.root = self.terrain.getRoot()
        self.root.setSz(50)
        self.root.setSx(1.01)
        self.root.setSy(1.01)
        self.root.setTexture(TextureStage.getDefault(), self.terrainTex)
        self.terrain.generate()
    def addTree(self, x, y):
        p = Plant3D()
        self.plants.append(p.tree(self, x, y))
    def demo_addTree(self):
        x = self.getX(0)
        y = self.getY(0)
        for i in range(20):
            self.plants.append(Plant3D().tree(self, random.randint(20,500), random.randint(20,500)))
    def getX(self,x):
        return x + self.x
    def getY(self,y):
        return y + self.y
    def getMyX(self,x):
        return (x*self.size)+(self.size*3*self.xoff)+(self.xoff*self.playerBuffer)
    def getMyY(self,y):
        return (y*self.size)+(self.size*3*self.yoff)+(self.yoff*self.playerBuffer)
    def move(self,x,y):
        self.x = self.getMyX(x)
        self.y = self.getMyY(y)
        self.root.setX(self.x)
        self.root.setY(self.y)
    def setupMip(self):
        self.makeTerrain()
        self.root.reparentTo(render)
        self.x = self.root.getX()
        self.y = self.root.getY()

