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

class Grass3D():
    def __init__(self):
        self.models = []
        self.healthy = True

class Plant3D():
    def __init__(self):
        self.models = []
        self.healthy = True
        self.x = 0
        self.y = 0
        self.zone = None
    def bigTree(self, myzone, x, y):
        self.type = 'bigTree'
        self.models.append(loader.loadModel("models/bigTree/bigTree"))
        self.models.append(loader.loadModel("models/bigTree/bigTree"))
        self.models[0].reparentTo(render)
        self.models[1].reparentTo(render)
        self.models[1].hide()
        self.x = x
        self.y = y
        self.zone = myzone
        self.models[0].setX(self.zone.getX(self.x))
        self.models[0].setY(self.zone.getY(self.y))
        self.models[0].setZ(self.zone.getElevation(self.x, self.y))
        self.models[1].setX(self.zone.getX(self.x))
        self.models[1].setY(self.zone.getY(self.y))
        self.models[1].setZ(self.zone.getElevation(self.x, self.y))
        self.healthyScale = random.random()*0.2+0.8
        self.unhealthyScale = self.healthyScale/2
        self.models[0].setScale(self.healthyScale)
        self.models[1].setScale(self.unhealthyScale)
        return self
    def baobabTree(self, myzone, x, y):
        self.type = 'baobab'
        self.models.append(loader.loadModel("models/trees/with_leaves/baobabtree"))
        self.models.append(loader.loadModel("models/trees/brownleaves/baobabtree"))
        self.models[0].reparentTo(render)
        self.models[1].reparentTo(render)
        self.models[1].hide()
        self.x = x
        self.y = y
        self.zone = myzone
        self.models[0].setX(self.zone.getX(self.x))
        self.models[0].setY(self.zone.getY(self.y))
        self.models[0].setZ(self.zone.getElevation(self.x, self.y))
        self.models[1].setX(self.zone.getX(self.x))
        self.models[1].setY(self.zone.getY(self.y))
        self.models[1].setZ(self.zone.getElevation(self.x, self.y))
        self.healthyScale = (random.random()*0.2+0.8)*10
        self.unhealthyScale = self.healthyScale/2
        self.models[0].setScale(self.healthyScale)
        self.models[1].setScale(self.unhealthyScale)
        return self
    def setHealthy(self, h):
        self.healthy = h
        if h == True:
            self.models[1].hide()
            self.models[0].show()
        if h == False:
            self.models[1].show()
            self.models[0].hide()

