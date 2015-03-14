#@PydevCodeAnalysisIgnore
import direct.directbase.DirectStart
from pandac.PandaModules import CardMaker
from pandac.PandaModules import Filename
from pandac.PandaModules import PandaNode,NodePath,Camera,TextNode
from pandac.PandaModules import Vec3,Vec4,BitMask32
from pandac.PandaModules import TextureStage
from pandac.PandaModules import TexGenAttrib
from pandac.PandaModules import GeoMipTerrain
from pandac.PandaModules import Texture
from pandac.PandaModules import TextureStage
from pandac.PandaModules import WindowProperties
from pandac.PandaModules import TransparencyAttrib
from pandac.PandaModules import AmbientLight
from pandac.PandaModules import DirectionalLight
from pandac.PandaModules import VBase4,VBase3
from pandac.PandaModules import Vec4
from pandac.PandaModules import Point3

from pandac.PandaModules import Spotlight

from pandac.PandaModules import Plane
from pandac.PandaModules import PlaneNode
from pandac.PandaModules import PStatClient
from pandac.PandaModules import CullFaceAttrib
from pandac.PandaModules import RenderState
from pandac.PandaModules import ShaderAttrib
from pandac.PandaModules import CollisionTraverser,CollisionNode
from pandac.PandaModules import CollisionHandlerQueue,CollisionSphere

from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
from direct.task.Task import Task
from direct.showbase.DirectObject import DirectObject

from direct.interval.IntervalGlobal import *

import random, sys, os, math
from panda3d.ai import *


SPEED = 0.5

# Figure out what directory this program is in.
MYDIR=os.path.abspath(sys.path[0])
MYDIR=Filename.fromOsSpecific(MYDIR).getFullpath()
print('running from:'+MYDIR)

# Function to put instructions on the screen.
def addInstructions(pos, msg):
    return OnscreenText(text=msg, style=1, fg=(1,1,1,1),
            pos=(-1.3, pos), align=TextNode.ALeft, scale = .05)

def addTextField(pos, msg):
    return OnscreenText(text=msg, style=1, fg=(1,1,1,1),
            pos=(-1.3, pos), align=TextNode.ALeft, scale = .05, mayChange=True)

# Function to put title on the screen.
def addTitle(text):
    return OnscreenText(text=text, style=1, fg=(1,1,1,1),
                    pos=(1.3,-0.95), align=TextNode.ARight, scale = .07)

##############################################################################
class myGeoMipTerrain(GeoMipTerrain):

    def __init__(self, name):
        GeoMipTerrain.__init__(self, name)

    def update(self, dummy):
        GeoMipTerrain.update(self)

    def setMonoTexture(self):
        root = self.getRoot()
        ts = TextureStage('ts')
        tex = loader.loadTexture('textures/mountainoustexture.jpg')#textures/land01_tx_512.png
        root.setTexture(ts, tex)

    def setMultiTexture(self):
        root = self.getRoot()
            #root.setShader(loader.loadShader('shaders/splut3Normal.sha'))
        root.setShaderInput('tscale', Vec4(100.0, 100.0, 100.0, 1.0))    # texture scaling

        tex1 = loader.loadTexture('textures/SandPebbles0072_3_L.jpg')
        #tex1.setMinfilter(Texture.FTLinearMipmapLinear)
        tex1.setMinfilter(Texture.FTNearestMipmapLinear)
        tex1.setMagfilter(Texture.FTLinear)
        tex2 = loader.loadTexture('textures/rock_02.jpg')
        tex2.setMinfilter(Texture.FTNearestMipmapLinear)
        tex2.setMagfilter(Texture.FTLinear)
        tex3 = loader.loadTexture('textures/sable_et_gravier.jpg')
        tex3.setMinfilter(Texture.FTNearestMipmapLinear)
        tex3.setMagfilter(Texture.FTLinear)

        alp1 = loader.loadTexture('textures/testalpha.png')#alpha1
        alp2 = loader.loadTexture('textures/testalpha2.png')#alpha2
        alp3 = loader.loadTexture('textures/alpha3.png')#alpha3

        ts = TextureStage('tex1')    # stage 0
        root.setTexture(ts, tex1)
        ts = TextureStage('tex2')    # stage 1
        root.setTexture(ts, tex2)
        ts = TextureStage('tex3')    # stage 2
        root.setTexture(ts, tex3)
        ts = TextureStage('alp1')    # stage 3
        root.setTexture(ts, alp1)
        ts = TextureStage('alp2')    # stage 4
        root.setTexture(ts, alp2)
        ts = TextureStage('alp3')    # stage 5
        root.setTexture(ts, alp3)

        # enable use of the two separate tagged render states for our two cameras
        root.setTag( 'Normal', 'True' )
        root.setTag( 'Clipped', 'True' )
###############################################################################        
class ActorProperties:
    def __init__(self,actor,actorHeight,startPosX,startPosY,startPosZ):
        self.actor = actor
        self.actorHeight = actorHeight
        self.startPosX = startPosX
        self.startPosY = startPosY
        self.startPosZ = startPosZ
        self.previousZ = 0
        self.direction = 20
        self.prevtime = 0
        self.steps=0
        self.isMoving = False
        self.dead = False
        self.detachNode = False
        # I don't think that this is necesary because you can noew the persue statuts with "aiBehaviors.behaviorStatus(string AIName)"
        self.pursueStart = False
        self.pursueComplete = False
        
    def getActor(self):
        return self.actor
    
    def getActorHeight(self):
        return self.actorHeight          
       
###############################################################################

class World(DirectObject):

    def __init__(self):
        print(str(base.win.getGsg().getMaxTextureStages()) + ' texture stages available')
        self.keyMap = {"left":0, "right":0, "forward":0, "back":0, "invert-y":0, "mouse":0 }
        base.win.setClearColor(Vec4(0,0,0,1))
        self.title = addTitle("Yet Another Roaming Ralph (Walking on uneven terrain too)")
        self.inst1 = addInstructions(0.95, "[ESC]: Quit")
        self.steps_text = addTextField(0.90, "[Steps]: ")
        self.hpr_text = addTextField(0.85, "[Hpr]: ")
        self.xyz_text = addTextField(0.80, "[XYZ]: ")
        self.md_text = addTextField(0.75, "[MouseXY]: ")
 
        self.dummy = NodePath(PandaNode("dummy"))
        self.dummy.setPos(-100,45,-150)
        self.dummy.reparentTo(render) 
        
        self.terrain = myGeoMipTerrain('terrain')
        self.terrain.setHeightfield('models/terrain/mip01_height.png') #models/land01-map.png
        self.terrain.setBlockSize(32)#128
        self.terrain.setFactor(100)
        self.terrain.setFocalPoint(base.camera)
        root = self.terrain.getRoot()
        root.reparentTo(self.dummy)
        root.setSz(50)    # z (up) scale original = 30
        self.terrain.generate()
        self.terrain.setMultiTexture()
        self.environ = self.terrain    # make available for original Ralph code below
        ambient = Vec4(0.34, 0.3, 0.3, 1)
        direct = Vec4(0.74, 0.7, 0.7, 1)
        alight = AmbientLight('alight')
        alight.setColor(ambient)
        alnp = render.attachNewNode(alight)
        render.setLight(alnp)
            
        self.centerOfWorld = NodePath("centerOfTheWorld")
        self.centerOfWorld.reparentTo(render)
        self.centerOfWorld.setPos(0,0,-10)

        worldRotationInterval = self.centerOfWorld.hprInterval(24, Point3(0,-180,0), startHpr=Point3(0,180,0))
        spinWorld = Sequence(worldRotationInterval, name="spinWorld")
        spinWorld.loop()

        self.dlight = render.attachNewNode(Spotlight("Spot"))
        self.dlight.setPos(0,0,800)
        self.dlight.lookAt(self.centerOfWorld)
        render.setLight(self.dlight)
        self.dlight.reparentTo(self.centerOfWorld)

        self.dlight.node().setShadowCaster(True, 2048, 2048)
        self.dlight.node().showFrustum()
        self.dlight.node().getLens().setNearFar(80,800)
        self.dlight.node().getLens().setFilmSize(800, 800)

        self.alight = render.attachNewNode(AmbientLight("Ambient"))
        self.alight.node().setColor(Vec4(0.4, 0.4, 0.4, 1))
        render.setLight(self.alight)
        
        root.setShaderInput('lightvec', Vec4(0.7, 0.2, -0.2, 1))
        root.setShaderInput('lightcolor', direct)
        root.setShaderInput('ambientlight', ambient)

        self.skybox = loader.loadModel('models/bluesky/skybox.egg')#skybox.egg

        self.skybox.setScale(10)
        self.skybox.setBin('background', 0)
        self.skybox.setDepthWrite(0)
        self.skybox.setLightOff()
        self.skybox.reparentTo(render)
 
        #grass
#        self.testgrass = loader.loadModel('models/testgrass.egg')
#        treeposz = self.terrain.getElevation(182, 697) * root.getSz()
#        self.testgrass.setPos(182,697,treeposz)
#        self.testgrass.setScale(10)
#        self.testgrass.reparentTo(self.dummy)
        #treesagain
        self.baobabtree = loader.loadModel('models/trees/with_leaves/baobabtree.egg')
        treeposz = self.terrain.getElevation(44, 153) * root.getSz()
        self.baobabtree.setPos(44,153,treeposz)
        self.baobabtree.setScale(10)
        self.baobabtree.reparentTo(self.dummy)

        self.baobabtree = loader.loadModel('models/trees/with_leaves/baobabtree.egg')
        treeposz = self.terrain.getElevation(37, 148) * root.getSz()
        self.baobabtree.setPos(37,148,treeposz)
        self.baobabtree.setScale(10)
        self.baobabtree.reparentTo(self.dummy)
        
        self.cTrav = CollisionTraverser()
        self.collisionHandlerQueue = CollisionHandlerQueue()
        
        elephant3StartPosX = 60
        elephant3StartPosY = 140
        elephant3StartPosZ = self.terrain.getElevation(elephant3StartPosX, elephant3StartPosY) * root.getSz()
        self.elephant3 = Actor("models/elephant/elephant",
                                 {"walk":"models/elephant/elephant-walk",
                                  "die":"models/elephant/elephant-die"})        
        self.elephant3.reparentTo(self.dummy)
        self.elephant3.setScale(.9)
        self.elephant3.setPos(elephant3StartPosX, elephant3StartPosY, elephant3StartPosZ)
        self.elephant3Height = 1.2  # to locate the top of elephant's head for the camera to point at        
        self.elephant3actor = ActorProperties(self.elephant3,self.elephant3Height,elephant3StartPosX,elephant3StartPosY,elephant3StartPosZ)
        
        self.elephant3Head = NodePath(PandaNode("elephant3Head"))
        self.elephant3Head.reparentTo(self.dummy) 
        
        elephant1StartPosX = 250
        elephant1StartPosY = 100
        elephant1StartPosZ = self.terrain.getElevation(elephant1StartPosX, elephant1StartPosY) * root.getSz()
        self.elephant1 = Actor("models/elephant/elephant",
                                 {"walk":"models/elephant/elephant-walk",
                                  "die":"models/elephant/elephant-die"})        
        self.elephant1.reparentTo(self.dummy)
        self.elephant1.setScale(.9)
        self.elephant1.setPos(elephant1StartPosX, elephant1StartPosY, elephant1StartPosZ)
        self.skybox.setPos(elephant1StartPosX, elephant1StartPosY, elephant1StartPosZ)
        self.elephant1Height = 1.2  # to locate the top of Ralph's head for the camera to point at
        self.elephant1actor = ActorProperties(self.elephant1,self.elephant1Height,elephant1StartPosX,elephant1StartPosY,elephant1StartPosZ)
        
        self.elephant1Head = NodePath(PandaNode("elephant1Head"))
        self.elephant1Head.reparentTo(self.dummy)
        
#        self.elephant1Np = self.elephant1.attachNewNode(CollisionNode("elephant1"))
#        self.elephant1Np.node().addSolid(CollisionSphere(0,7,2,1.1))
#        self.elephant1Np.node().addSolid(CollisionSphere(0,-7,2,1.1))
#        self.elephant1Np.node().addSolid(CollisionSphere(0,0,0,1.1))
#        self.elephant1Np.show()
#        self.cTrav.addCollider(self.elephant1Np, self.collisionHandlerQueue) 
        # bitmasks 
        self.elephant1.setCollideMask(BitMask32.bit(0))        
        
        elephant2StartPosX = 70
        elephant2StartPosY = 100
        elephant2StartPosZ = self.terrain.getElevation(elephant2StartPosX, elephant2StartPosY) * root.getSz()
        self.elephant2 = Actor("models/elephant/elephant",
                                 {"walk":"models/elephant/elephant-walk",
                                  "die":"models/elephant/elephant-die"})        
        self.elephant2.reparentTo(self.dummy)
        self.elephant2.setScale(.9)
        self.elephant2.setPos(elephant2StartPosX, elephant2StartPosY, elephant2StartPosZ)
        self.elephant2Height = 1.2  # to locate the top of elephant's head for the camera to point at        
        self.elephant2actor = ActorProperties(self.elephant2,self.elephant2Height,elephant2StartPosX,elephant2StartPosY,elephant2StartPosZ)
        
        self.elephant2Head = NodePath(PandaNode("elephant2Head"))
        self.elephant2Head.reparentTo(self.dummy) 
        
        ###############
        #root,terrain,dummy,startPosX,startPosY,count)
#        self.listOfElephants ={}
#        self.elephantCount=0
#        
#        self.elephantCount= self.elephantCount+1
#        self.listOfElephants[self.elephantCount]= Elephant("elephant"+str(self.elephantCount))
#        self.listOfElephants[self.elephantCount].createActor(root,self.terrain,self.dummy,80,100)
        
        ###################
        cheetahStartPosX = 70
        cheetahStartPosY = 100
        cheetahStartPosZ = self.terrain.getElevation(cheetahStartPosX, cheetahStartPosY) * root.getSz()
        self.cheetah = Actor("models/cheetah/cheetah",
                                 {"cheetah-walk":"models/cheetah/cheetah-walk",
                                  "cheetah-attack":"models/cheetah/cheetah-attack",
                                  "cheetah-die":"models/cheetah/cheetah-die",
                                  "cheetah-eat":"models/cheetah/cheetah-eat"})        
        self.cheetah.reparentTo(self.dummy)
        self.cheetah.setScale(3)
        self.cheetah.setPos(cheetahStartPosX, cheetahStartPosY, cheetahStartPosZ)
        self.cheetahHeight = 1.2  # to locate the top of elephant's head for the camera to point at        
        self.cheetahactor = ActorProperties(self.cheetah,self.cheetahHeight,cheetahStartPosX,cheetahStartPosY,cheetahStartPosZ)
        
        self.cheetahHead = NodePath(PandaNode("cheetahHead"))
        self.cheetahHead.reparentTo(self.dummy) 
        
        self.cheetahNp = self.cheetah.attachNewNode(CollisionNode("cheetah"))
        self.cheetahNp.node().addSolid(CollisionSphere(0,0,0,1.1))
        #self.cheetahNp.show()
        self.cTrav.addCollider(self.cheetahNp, self.collisionHandlerQueue)        
        self.cheetahNp.node().setFromCollideMask(BitMask32.bit(0)) 
        self.cheetahNp.node().setIntoCollideMask(BitMask32.allOff())         
                
        self.camDistTarg = 6  # desired camera distance if no obsacles in the way
        self.camDist = self.camDistTarg
        self.testCamDist = self.camDistTarg
        self.mincamDist = 1.5 # for 3rd person camera
        self.maxcamDist = 30
        self.zcam = 0 # height of camera due to camera pitch in 3rd person
        self._setup_camera()
        base.camera.setPos(self.elephant1.getX(), self.elephant1.getY()+self.camDist, \
                                        self.elephant1.getZ()+self.elephant1Height)
        
        base.camera.lookAt(self.elephant1)
        self.heading = base.camera.getH()
        self.oldheading = 0
        self.pitch = 0
        self.oldPitch = 0
        self.maxPitch = 70  # and used for minimum camera pitch too
        self.mousebtn = [0,0,0,0]
        self.mouseNotInvertY = 1
        
        self.accept("escape", sys.exit)
        
#        taskMgr.add(self.move,"moveTask")
        taskMgr.add(self.terrain.update, "update")

#        base.disableMouse()
        props = WindowProperties()
        props.setCursorHidden(True)
        base.win.requestProperties(props)
        self.setAI()

    def _setup_camera(self):
        sa = ShaderAttrib.make( )
        sa = sa.setShader(loader.loadShader('shaders/splut3Normal.sha'))
        cam = base.cam.node()
        cam.getLens().setNear(1)
        cam.getLens().setFar(5000)
        cam.setTagStateKey('Normal')
        cam.setTagState('True', RenderState.make(sa))
                
    def setAI(self):
        #I change all the AI names to something more easy to understand#
        self.attackers = 0 #this variable is for multiple animals attaking
        self.AIworld = AIWorld(render)
        self.dicBehaviors = dict() #this Dictionary have all the behaviors of the animals
        self.dicAiChars = dict() #this Dictionary have all the AIchars of the animals

        self.addAnimal("elephant1", self.elephant1)
        self.addAnimal("elephant2", self.elephant2)
        self.addAnimal("elephant3", self.elephant3)
        self.addAnimal("cheetah", self.cheetah)
        
        self.elephant1.loop("walk")
        self.elephant2.loop("walk")
        self.elephant3.loop("walk")
        self.cheetah.loop("cheetah-walk")
        
        self.attackAnimal("cheetah", "elephant1", self.cheetah, self.elephant1)
        self.attackPlant("elephant2", "baobabtree", self.elephant2, self.baobabtree)
        
        
        base.camera.setPos(self.elephant1.getX(), self.elephant1.getY()+self.camDist, \
                                        self.elephant1.getZ()+self.elephant1Height)
        taskMgr.add(self.AIUpdate,"AIUpdate")
    
    def addAnimal(self, id, model, mass = 20, movt_force = 5, max_force = 10):
        #print "Este es el id: ", id
        self.dicAiChars[id] = AICharacter(id, model, mass, movt_force, max_force)
        self.AIworld.addAiChar(self.dicAiChars[id])
        #self.AIworld.addObstacle(model)
        self.dicBehaviors[id] = self.dicAiChars[id].getAiBehaviors()
        #self.AIbehavior.obstacleAvoidance(0.5)
        self.dicBehaviors[id].wander(100, 0, 10, 0.5)
        #print "Lista del mundo: "
        #self.AIworld.printList()
    
    def attackAnimal(self, idAttacker, idTarget, modelAttacker, modelTarget): # P for predator or V for Vegetarian
        #print "Attacker: " + idAttacker + " Target: " + idTarget
        #modelAttacker = self.listOfAnimals[idAttacker].getModelName()
        self.attackers = self.attackers + 1
        self.dicBehaviors[idAttacker].pursue(modelTarget,1.0)
        self.dicBehaviors[idAttacker].pauseAi("wander")
        self.dicBehaviors[idTarget].evade(modelAttacker,50,20,1.0)

        taskMgr.add(self.eatAnimal,"eatAnimal" + str(self.attackers), extraArgs = [idAttacker, idTarget, modelAttacker, modelTarget], appendTask = True)

    def attackPlant(self, idAttacker, idTarget, modelAttacker, modelTarget):
        #print "Attacker: " + idAttacker + " Target: " + idTarget
        #modelAttacker = self.listOfAnimals[idAttacker].getModelName()
        self.attackers = self.attackers + 1
        self.dicBehaviors[idAttacker].pursue(modelTarget,1.0)
        self.dicBehaviors[idAttacker].pauseAi("wander")

        #self.finish()
        taskMgr.add(self.eatPlant,"eatPlant" + str(self.attackers), extraArgs = [idAttacker, idTarget, modelAttacker, modelTarget], appendTask = True)
    
    def eatPlant(self, idAttacker, idTarget, modelAttacker, modelTarget, task):
        if (self.dicBehaviors[idAttacker].behaviorStatus("pursue")  == "done"):
            #print "Finishing Attacker: " + idAttacker + " Target: " + idTarget
            #scale = self.elephant1.getScale()
            modelAttacker.loop("cheetah-eat")
            self.dicBehaviors[idAttacker].removeAi("pursue")
            self.AIworld.removeAiChar(idTarget)
            print "nom nom nom nom nomnomnomnom"
            
            taskMgr.doMethodLater(20 , self.callWander, 'callWander' + str(self.attackers), extraArgs = [ idAttacker, idTarget, modelAttacker, modelTarget])
            taskMgr.remove("finish")
            
        return Task.cont
    
    def eatAnimal(self, idAttacker, idTarget, modelAttacker, modelTarget, task):
        if (self.dicBehaviors[idAttacker].behaviorStatus("pursue")  == "done"):
            #print "Finishing Attacker: " + idAttacker + " Target: " + idTarget
            modelTarget.play("die")
            #scale = self.elephant1.getScale()
            modelAttacker.loop("cheetah-eat")
            self.dicBehaviors[idAttacker].removeAi("pursue")
            self.AIworld.removeAiChar(idTarget)
            print "nom nom nom nom nomnomnomnom"
            
            taskMgr.doMethodLater(20 , self.callWander, 'callWander' + str(self.attackers), extraArgs = [ idAttacker, idTarget, modelAttacker, modelTarget])
            taskMgr.remove("finish")
            
        return Task.cont
    
    def callWander(self,idAttacker, idTarget, modelAttacker, modelTarget):
        #modelTarget.detachNode()
        self.dicBehaviors[idAttacker].resumeAi("wander")
        modelAttacker.loop(idAttacker + "-walk")
        self.attackers = self.attackers - 1
        taskMgr.remove("callWander")
        
    def addToDynamicObstacles(self, idAnimal, animal):
        self.listOfDynamicObstacles[idAnimal] = animal
    
    def AIUpdate(self,task):
        self.AIworld.update()
        self.move(self.elephant1, self.elephant1actor, self.elephant1Head, task)
        self.move(self.elephant2, self.elephant2actor, self.elephant2Head, task)      
        self.move(self.elephant3, self.elephant3actor, self.elephant3Head, task)
        self.move(self.cheetah, self.cheetahactor, self.cheetahHead, task) 
 

        self.cTrav.traverse(self.dummy) 

        return Task.cont
    
    def move(self, actor, actorProperties, actorHead, task):
        #We really need to copy all the same data again? why don't work directly with the same variables received?
        self.actor = actor
        self.actorProperties = actorProperties
        self.actorHeight = self.actorProperties.actorHeight
        self.actorHead = actorHead
        
        ### Excelent Wandering function but we don't need because we already have a wandering ####
        
#        elapsed = task.time - self.actorProperties.prevtime
#        startpos = self.actor.getPos()
#
#        self.actorProperties.steps = self.actorProperties.steps + 1 
#        if self.actorProperties.steps%20 == 0 :
#            self.actorProperties.direction = self.actorProperties.direction +90
#        self.actor.setHpr(self.actorProperties.direction,0,0)
#        self.actor.setY(self.actor, -elapsed*25)
        ### End wandering function
        
        #I think we don't need this
#        if self.actorProperties.isMoving is False:
#            if (self.keyMap["forward"]!=0) or (self.keyMap["left"]!=0) \
#            or (self.keyMap["right"]!=0):
#                self.actor.loop("walk")
#            else:
#                self.actor.setPlayRate(-1, "walk")
#                self.actor.loop("walk")
#            self.actorProperties.isMoving = True
#        else:
#            if self.actorProperties.isMoving:
#                self.actor.stop()
#                self.actor.pose("walk",5)
#                self.actorProperties.isMoving = False

        x = self.actor.getX()
        y = self.actor.getY()
        z = self.terrain.getElevation(x,y)*self.terrain.getRoot().getSz()
        
        diff = self.actorProperties.previousZ - z
        
        #Multiplication factor for uphill and downhill
        self.actor.setP(diff*40)
        
        self.actor.setZ(z)
        self.actorProperties.previousZ = z
        
        self.actorHead.setPos(self.actor.getPos())
        self.actorHead.setZ(self.actor.getZ() + self.actorHeight)
        self.actorHead.setHpr(self.actor.getHpr())

        campos = base.camera.getPos()
        self.skybox.setPos(campos)
        # Store the task time and continue.
        self.actorProperties.prevtime = task.time
        return Task.cont  
          
print('instancing world...')
w = World()

print('calling run()...')
run()