#!/usr/bin/python

import math

#for Pandai
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

class EcoActor(Actor):
    def __init__(self, m, d):
        super(EcoActor, self).__init__(m, d)
class World(DirectObject):
    def __init__(self):
        self.doSky()
        base.enableParticles()
        self.pspawn = loader.loadModel("models/square")
        self.r = 0
        self.terrain = GeoMipTerrain("myDynamicTerrain")
        self.wterrain = GeoMipTerrain("waterTerrain")
        self.terrain.setHeightfield("tests/models/height129.png")
        self.wterrain.setHeightfield("tests/models/height129_river.png")
        tex = loader.loadTexture("tests/models/sav.jpg")
        watertex = loader.loadTexture("../models/water/water.png")
        self.sparrow = EcoActor('../models/sparrow/sparrow', {
        'walk':'../models/sparrow/sparrow-walk',
          'run':'../models/sparrow/sparrow-flap',})
        self.elephant = EcoActor('../models/elephant/elephant', {
        'walk':'../models/elephant/elephant-walk',
          'eat':'../models/elephant/elephant-eat',})
        self.zebra = EcoActor('../models/zebra/zebra', {
        'walk':'../models/zebra/zebra-walk',
          'eat':'../models/zebra/zebra-eat',})
        tex.setWrapU(Texture.WMRepeat)
        tex.setWrapV(Texture.WMRepeat)
        tex.setWrapW(Texture.WMRepeat)
        watertex.setWrapU(Texture.WMRepeat)
        watertex.setWrapV(Texture.WMRepeat)
        watertex.setWrapW(Texture.WMRepeat)
        self.terrain.setBruteforce(True)
        self.terrain.setBlockSize(32)
        self.terrain.setNear(40)
        self.terrain.setFar(100)
        self.wterrain.setBruteforce(True)
        self.wterrain.setBlockSize(32)
        self.wterrain.setNear(40)
        self.wterrain.setFar(100)
        base.disableMouse()
        camera.setPosHpr(50, 50, 70, 0, -45, 0)
        root = self.terrain.getRoot()
        root.setTexture(TextureStage.getDefault(), tex) 
        root.setTexScale(TextureStage.getDefault(), 10)
        root.reparentTo(render)
        root.setSz(50)
        root.setSx(4)
        root.setSy(4)
        wroot = self.wterrain.getRoot()
        wroot.setTexture(TextureStage.getDefault(), watertex) 
        wroot.setTexScale(TextureStage.getDefault(), 10)
        wroot.reparentTo(render)
        wroot.setSz(50)
        wroot.setSx(4)
        wroot.setSy(4)
        self.root2 = render.attachNewNode("root2")
        self.terrain.generate()
        self.wterrain.generate()
        wroot.setTransparency(1)
        wroot.setAlphaScale(0.5)
        self.steam = ParticleEffect()
        self.loadParticleConfig('tests/models/steam.ptf')
        self.sparrow.reparentTo(self.root2)
        self.sparrow.setPos(Point3(200,200,50))
        self.sparrow.setScale(scaleFactor)
        intervalRun = self.sparrow.actorInterval("run",loop=1,duration=1)
        animSequence = Sequence(intervalRun)
        animSequence.loop()
        self.zebra.reparentTo(self.root2)
        self.zebra.setPos(Point3(100,100,15))
        self.zebra.setScale(scaleFactor)
        intervalRunZebra = self.zebra.actorInterval("walk",loop=1,duration=1)
        animSequenceZebra = Sequence(intervalRunZebra)
        animSequenceZebra.loop()
        self.elephant.reparentTo(self.root2)
        self.elephant.setPos(Point3(150,125,18))
        self.elephant.setScale(scaleFactor)
        intervalRunelephant = self.elephant.actorInterval("walk",loop=1,duration=1)
        animSequenceelephant = Sequence(intervalRunelephant)
        animSequenceelephant.loop()
        self.setupLights()
        taskMgr.add(self.updateTask, "update")
        taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        base.enableMouse()
        self.setAI()
    def updateTask(self, task):
        self.terrain.update()
        return task.cont
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        #base.camera.setHpr(angleDegrees, -45, 0)
        return Task.cont
    def doSky(self):
        skysphere = loader.loadModel('../models/bluesky/blue-sky-sphere')
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
        self.steam.cleanup()
        self.steam = ParticleEffect()
        self.steam.loadConfig(Filename(file)) 
    def setAI(self):
        #Creating AI World
        self.AIworld = AIWorld(render)
        
        # Adding Zeebra to the AI World
        self.AIzebra = AICharacter("zebra",self.zebra, 100, 0.05, 5)
        self.AIworld.addAiChar(self.AIzebra)
        self.AIZebraBehaviors = self.AIzebra.getAiBehaviors()
        # Adding sparrow to the AI World
        self.AIsparrow = AICharacter("sparrow",self.sparrow, 100, 0.05, 5)
        self.AIworld.addAiChar(self.AIsparrow)
        self.AISparrowBehaviors = self.AIsparrow.getAiBehaviors()
 
        # Wandering
        self.AIZebraBehaviors.wander(10, 0, 50, 1.0)
        
        # Obstacle avoidance
        self.AIZebraBehaviors.obstacleAvoidance(5.0)
        self.AIworld.addObstacle(self.terrain.getRoot())
        self.AIworld.addObstacle(self.wterrain.getRoot())
        self.AIworld.addObstacle(self.sparrow)
        self.AIworld.addObstacle(self.zebra)
        
        # Seeking
        self.AISparrowBehaviors.seek(self.zebra, 1)
 
        #AI World update        
        taskMgr.add(self.AIUpdate,"AIUpdate")
        
    #to update the AIWorld    
    def AIUpdate(self,task):
        self.AISparrowBehaviors.seek(self.zebra, 0.5)
        self.AIworld.update()            
        return Task.cont
scaleFactor = 0.5        
w = World()
run()
