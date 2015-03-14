#@PydevCodeAnalysisIgnore
from panda3d.core import Texture, TextureStage
from pandac.PandaModules import PandaNode,NodePath
from pandac.PandaModules import Filename
from pandac.PandaModules import GeoMipTerrain
from direct.showbase.DirectObject import DirectObject
from panda3d.core import Vec4,Vec3
from direct.task import Task
from pandac.PandaModules import VBase3

from common.Constants import Constants
from main.MainLobby.World.World3D.Plant3D import Plant3D
from main.MainLobby.World.World3D.Animal3D import Animal3D
from main.MainLobby.World.World3D.MyGeoMipTerrain import MyGeoMipTerrain
from main.MainLobby.World.World3D.Plant import Plant
from main.MainLobby.World.World3D.Animal import Animal
from main.MainLobby.World.World3D.Models import Models
import random

#for Pandai
from panda3d.ai import *
class Zone3D():
    def __init__(self, env1,x,y):
        if Constants.DEBUG:
            print 'creating zone ',y+x*3
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
        self.animals = {}
        self.flora = {}
        #self.root = render.attachNewNode('root')
        self.listOfStaticObstacles = {}
        self.listOfDynamicObstacles = {}
        #Creating AI World
        self.AIworld = AIWorld(render)
        self.dictBehaviors = dict() #this Dictionary have all the behaviors of the animals
        self.dictAiChars = dict() #this Dictionary have all the AIchars of the animals 
        
        self.hasWater = False
        #AI World update        
        taskMgr.add(self.AIUpdate,"AIUpdate")  
        self.object_id = "2"  
        self.attackers = 0
        
    def makeTerrain(self):
        i1 = random.randint(1,self.numTerrains)
        self.terrain = GeoMipTerrain("terrain")
        self.terrain.setHeightfield('models/terrain/mip0'+str(i1)+'_height.png')
        #self.terrain.setHeightfield('models/terrain1/terrain1.jpg')
        self.terrainTex = loader.loadTexture('models/terrain/mip0'+str(i1)+'_texture.png')
        #self.terrainTex = loader.loadTexture('models/terrain1/terrain1texture.jpg')
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

        self.terrain.getRoot().setCollideMask(Constants.MOUSE_CLICK_MASK)
        self.terrain.getRoot().setTag('sObject', str(self.object_id))          
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

#have to integrate with AI over here
    def addToListOfStaticObstacles(self,plantID):
        self.listOfStaticObstacles[plantID] = plantID;
        
#have to integrate with AI here        
    def addToListOfDynamicObstacles(self,animalID,actorObject):
        return None
        
    def addPlant(self,plantID, plantType, avatarID, zoneID, biomass,modelPath,scaleValue):
        #create instance for Plant object
        plantObject = Plant(plantID, plantType, avatarID, zoneID, biomass)
        xCoor = random.randint(20,500)
        yCoor = random.randint(20,500)
        xCoor = 0
        yCoor = 512       
        plantObject.setXCoor(xCoor) 
        plantObject.setYCoor(yCoor)
        #create a 3D object for the plant
        print "creating plant at x = ", xCoor ,", y = ",yCoor
        plantObject.createPlant3D(self,modelPath,scaleValue)
        self.flora[plantID] = plantObject
        
        plantModel = plantObject.get3DPlantModel()
        self.listOfStaticObstacles[plantID] = self.AIworld.addObstacle(plantModel)

    def updatePlantNoLightCount(self,plantID,noLightCount):
        return None

    def addAnimal(self,animalID,animalType,avatarID,zoneID,biomass,modelPathAndAnimation,scaleValue):
        #create instance of Animal Object
        animalObject = Animal(animalID,animalType,avatarID,zoneID,biomass,self.terrain)
        xCoor = random.randint(20,500)
        yCoor = random.randint(20,500)
        animalObject.setXCoor(xCoor)
        animalObject.setYCoor(yCoor)
        animalObject.sentZoneObj(self)
        print "creating animal at x = ", xCoor ,", y = ",yCoor
        animalObject.createAnimal3D(self,modelPathAndAnimation,scaleValue)
        self.animals[animalID] = animalObject

#parameters are - animalID, actor object,mass,movement force, maximumm force
#default behaviour of animal is set to wander. 
#wander(double wander_radius, int flag, double aoe, float priority)
#Wander Radius represents the degree of wandering. 
#This is implemented via a guiding circle in front of the AI Character.
#Flag represents which plane to wander in (0 - XY, 1 - YZ, 2 - XZ, 3 - XYZ). 
#By default, it is in the XY plane.
#Area of Effect is the radius from the starting point where the AICharacter would wander within.
#priority is by default set to 1.0 and is used when using two or more steering behaviors on an AICharacter.
    def addAnimalToAI(self, animalID,mass = 30, movt_force = 10, max_force = 20):
        model = self.animals[animalID].get3DAnimalActor()
        id = self.animals[animalID].getAnimalInstance()
        print "id-",id," model-",model
        #create a AI character
        self.dictAiChars[id] = AICharacter(id, model, mass, movt_force, max_force)
        #add the AI character to AI world
        self.AIworld.addAiChar(self.dictAiChars[id])
        #add to the list of behaviours to keep track 
        self.dictBehaviors[id] = self.dictAiChars[id].getAiBehaviors()
        #set up obstacle avoidance
        self.dictBehaviors[id].obstacleAvoidance(1.0)
        self.listOfDynamicObstacles[animalID] = self.AIworld.addObstacle(model)
        #start wandering around
        self.dictBehaviors[id].wander(100, 0, 100, 0.5)
        #set up animation
        walk = self.animals[animalID].getAnimalWalk()
        model.loop(walk)

    def attackAnimal(self, animalID,preyAnimalID):
        idAttacker = self.animals[animalID].getAnimalInstance()
        idTarget     = self.animals[preyAnimalID].getAnimalInstance()
        print idAttacker,"attacking",idTarget
        modelAttacker = self.animals[animalID].get3DAnimalActor()
        modelTarget = self.animals[preyAnimalID].get3DAnimalActor()
        print "attacker-",modelAttacker," target-",modelTarget        
        #set up all animations
        eatAnim = self.animals[animalID].getAnimalEat()
        dieAnim = self.animals[preyAnimalID].getAnimalDie()
        walkAnim = self.animals[animalID].getAnimalWalk()
        print "eatAnim-",eatAnim, " dieAnim-",dieAnim," walkAnim-",walkAnim
        self.attackers = self.attackers + 1
        self.dictBehaviors[idAttacker].pursue(modelTarget,1.0)
        self.dictBehaviors[idAttacker].pauseAi("wander")
        self.dictBehaviors[idTarget].evade(modelAttacker,50,20,1.0)
        taskMgr.add(self.eatAnimal,"eatAnimal" + str(self.attackers), extraArgs = [idAttacker, idTarget, modelAttacker, modelTarget,eatAnim,dieAnim,walkAnim,animalID,preyAnimalID], appendTask = True)

    def eatAnimal(self, idAttacker, idTarget, modelAttacker, modelTarget, eatAnim,dieAnim,walkAnim,animalID,preyAnimalID,task):
        if (self.dictBehaviors[idAttacker].behaviorStatus("pursue")  == "done"):
            #print "Finishing Attacker: " + idAttacker + " Target: " + idTarget
            modelTarget.play(dieAnim)
            #scale = self.elephant1.getScale()
            modelAttacker.loop(eatAnim)
            if preyAnimalID in self.animals:
                del self.animals[preyAnimalID]            
            self.dictBehaviors[idAttacker].removeAi("wander")
            self.AIworld.removeAiChar(idTarget)
            print "I am inside eat animal"
            taskMgr.doMethodLater(5 , self.callWander, "callWander" + str(self.attackers), extraArgs = [ idAttacker, idTarget, modelAttacker, modelTarget,walkAnim,animalID])
            taskMgr.remove("eatAnimal" + str(self.attackers))
        return Task.cont  
    
    def callWander(self,idAttacker, idTarget, modelAttacker, modelTarget,walkAnim,animalID):
        modelTarget.detachNode()
        self.dictBehaviors[idAttacker].removeAi("pursue")
        self.dictBehaviors[idAttacker].resumeAi("wander")
        modelAttacker.loop(walkAnim)
        self.attackers = self.attackers - 1
        taskMgr.remove("callWander" + str(self.attackers))
                      
    def AIUpdate(self,task):
        self.AIworld.update()
        self.moveAnimals(task)
        return Task.cont  
    
    def moveAnimals(self,task):
        for animalID in self.animals:
            self.animals[animalID].move(task)
        return None  
    
    def setHasWater(self,bool):
        self.hasWater = bool    