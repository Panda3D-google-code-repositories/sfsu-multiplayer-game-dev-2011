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
    def tree(self, myzone, x, y):
        self.models.append(loader.loadModel("models/bigTree/bigTree"))
        self.models[0].reparentTo(render)
        self.x = x
        self.y = y
        self.zone = myzone
        self.terrain = self.zone.terrain
        self.root = self.zone.root
        self.models[0].setX(self.zone.getX(self.x))
        self.models[0].setY(self.zone.getY(self.y))
        self.models[0].setZ(self.terrain.getElevation(self.x,self.y)*50)
        #print "tree in zone " + str(self.zone.x) + ", " + str(self.zone.y)
        return self

