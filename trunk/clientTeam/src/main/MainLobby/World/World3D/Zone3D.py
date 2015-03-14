from random import randint

from panda3d.ai import AICharacter
from panda3d.ai import AIWorld
from panda3d.core import NodePath

from common.Constants import Constants
from common.Events import Events

from main.MainLobby.World.World3D.WaterModel import WaterModel

class Zone3D(NodePath):

    def __init__(self, env, zone_id, type):

        NodePath.__init__(self, 'Zone')

        self.zone_id = zone_id

        self.setTag('type', 'Zone')
        self.setTag('object_id', str(self.zone_id))

        self.env = env
        self.size = 32

        self.animals = {}
        self.flora = {}

        self.totalAnimalList = {}
        self.totalPlantList = {}

        self.listOfStaticObstacles = {}
        self.listOfDynamicObstacles = {}
        #Creating AI World
        self.AIworld = AIWorld(render)
        self.dictBehaviors = {} #this Dictionary have all the behaviors of the animals
        self.dictAiChars = {} #this Dictionary have all the AIchars of the animals 

        self.hasWater = True
        #AI World update
        taskMgr.doMethodLater(0, self.AIUpdate, 'AIUpdate', sort = 1, priority = 2)
        taskMgr.doMethodLater(0.1, self.moveAnimals, 'moveAnimals', sort = 1, priority = 1)
        self.attackers = 0

        self.type = type

        self.zoneInfo = {1 : [4.28692, 7.39727, 4, 4],
                         2 : [12.432, 11.8066, 3, 3],
                         3 : [10.9268, 4.4861, 5, 7]}

        self.terrainNode = self.attachNewNode('Terrain')
        self.terrainNode.setScale(2)

        self.createTerrain()

        taskMgr.add(self.updateRoutine, 'updateRoutine-Z' + str(self.zone_id))

    def sethighlight(self):
        self.terrain_c.setColorScale(1, 0, 0, 0.5)
        return
    
    def createTerrain(self):

        self.terrain = loader.loadModel('models/terrain/' + 'terrain_0' + str(self.type))
        self.terrain.reparentTo(self.terrainNode)
#        self.terrain.setCollideMask(Constants.CLICKABLE_MASK)

        self.terrain_c = loader.loadModel('models/terrain/' + 'terrain_0' + str(self.type) + '_c')
        self.terrain_c.reparentTo(self.terrainNode)
        self.terrain_c.setCollideMask(Constants.ZONE_MASK)

        self.terrain_c.setTag('type', 'Zone')
        self.terrain_c.setTag('object_id', str(self.zone_id))
        self.terrain_c.setTag('env_id', str(self.env.env_id))

        x = randint(1, 3)
        if x == 1:
            terrainTexture = loader.loadTexture('models/terrain/' + 'grass1.jpg')
        elif x == 2:
            terrainTexture = loader.loadTexture('models/terrain/' + 'grass1-dry.jpg')
        elif x == 3:
            terrainTexture = loader.loadTexture('models/terrain/' + 'grass1-lush.jpg')
        self.terrain.setTextureOff(1)
        self.terrain.setTexture(terrainTexture, 1)

        if self.hasWater:
            self.createWater()

    def createWater(self):

        waterInfo = self.zoneInfo[self.type]

        self.water = WaterModel(self.type, -0.4, -0.2)
        self.water.reparentTo(self.terrainNode)

        self.water.setX(waterInfo[0])
        self.water.setY(waterInfo[1])
        self.water.setSx(waterInfo[2])
        self.water.setSy(waterInfo[3])

        #to do set the self.water as an obstacle
        self.listOfStaticObstacles['waterID' +str(self.zone_id)] = self.AIworld.addObstacle(self.water.getWaterSphere())

    def getWater(self):
        return self.water

    def getSize(self):
        return self.size

    def addWater(self):    
        #Since all zones don't have water, this has been separated out
        self.hasWater = True
        self.createWater()

    def getID(self):
        return self.zone_id

    def getElevation(self, x, y):
        newPos = self.env.getRelativePoint(self, (x, y, 0))
        return self.env.getElevation(newPos.getX(), newPos.getY())

    def getRelativePoint(self, x, y):
        return self.env.getRelativePoint(self, (x, y, 0))

    def getWorldPoint(self, x, y):
        return render.getRelativePoint(self, (x, y, 0))

#have to integrate with AI over here
    def addToListOfStaticObstacles(self,plantID):
        self.listOfStaticObstacles[plantID] = plantID;
        
#have to integrate with AI here        
    def addToListOfDynamicObstacles(self,animalID,actorObject):
        return None
        
    def addPlant(self, plant):
        plant.setZone(self)
        #create instance for Plant object
        self.flora[plant.getID()] = plant

        plantModel = plant.getPlantModel()
        self.listOfStaticObstacles[plant.getID()] = self.AIworld.addObstacle(plantModel)

        if plant.plantType in self.totalPlantList:
            self.setTotalPlantList(plant.plantType, self.totalPlantList[plant.plantType] + plant.getGroupSize())
        else:
            self.setTotalPlantList(plant.plantType, plant.getGroupSize())

    def addMorePlant(self, plant, amount):
        self.setTotalPlantList(plant.plantType, self.totalPlantList[plant.plantType] + amount)

    def setTotalPlantList(self, species_id, amount):

        self.totalPlantList[species_id] = amount
        messenger.send(Events.EVENT_TOTAL_PLANT, [self.zone_id, species_id, amount])

    def addAnimal(self,animal):
        #create instance of Animal Object
        animal.setSoundMgr(self.soundMgr)
        animal.setZone(self)

        self.animals[animal.getID()] = animal

        if animal.animalType in self.totalAnimalList:
            self.setTotalAnimalList(animal.animalType, self.totalAnimalList[animal.animalType] + animal.getGroupSize())
        else:
            self.setTotalAnimalList(animal.animalType, animal.getGroupSize())

    def addMoreAnimal(self, animal, amount):
        self.setTotalAnimalList(animal.animalType, self.totalAnimalList[animal.animalType] + amount)

    def setTotalAnimalList(self, species_id, amount):

        self.totalAnimalList[species_id] = amount
        messenger.send(Events.EVENT_TOTAL_ANIMAL, [self.zone_id, species_id, amount])

    def setSoundMgr (self, soundMgr):
        self.soundMgr = soundMgr

#parameters are - animalID, actor object,mass,movement force, maximumm force
#default behaviour of animal is set to wander. 
#wander(double wander_radius, int flag, double aoe, float priority)
#Wander Radius represents the degree of wandering. 
#This is implemented via a guiding circle in front of the AI Character.
#Flag represents which plane to wander in (0 - XY, 1 - YZ, 2 - XZ, 3 - XYZ). 
#By default, it is in the XY plane.
#Area of Effect is the radius from the starting point where the AICharacter would wander within.
#priority is by default set to 1.0 and is used when using two or more steering behaviors on an AICharacter.
    def addAnimalToAI(self, animal, mass = 50, movt_force = 0.05, max_force = 1):
        self.addAnimal(animal)
        animalInstance = animal.getAnimalInstance()

        #create a AI character
        aiChar = AICharacter(animalInstance, animal, mass, movt_force, max_force)
        self.dictAiChars[animalInstance] = aiChar
        #add the AI character to AI world
        self.AIworld.addAiChar(aiChar)
        #add to the list of behaviours to keep track
        animal.setAIChar(aiChar)
        aiBehaviors = aiChar.getAiBehaviors()
        self.dictBehaviors[animalInstance] = aiBehaviors
        #set up obstacle avoidance
        aiBehaviors.obstacleAvoidance(1.0)
        self.listOfDynamicObstacles[animal.getID()] = self.AIworld.addObstacle(animal)

        animal.wander()
#        animal.drinkWater()

    def attackAnimal(self, animalID, preyAnimalID, count):

        attacker = self.animals[animalID]
        target = self.animals[preyAnimalID]

        attacker.attack(target, count)

    def updateAnimalList(self,animalID,animalTypeID):
        del self.animals[animalID]
#        del self.gameState.listOfAnimals[animalID]                  
        return None

    def attackPlant(self, animalID, plantID, count):
        attacker = self.animals[animalID]
        target = self.flora[plantID]

        attacker.attack(target, count)
    #
    # Migrates an animal with animalID from its current
    # position to the target position.
    #
    def migrate(self, animalID, target, zone_id, gameState):
        print "Animal " + str(animalID) + " is migrating..."

        self.animals[animalID].setBoundaryRestrict(False)

        if self.dictBehaviors[self.animals[animalID].getAnimalInstance()].behaviorStatus("seek") == "active" :
            self.dictBehaviors[self.animals[animalID].getAnimalInstance()].removeAi("seek")
        if self.dictBehaviors[self.animals[animalID].getAnimalInstance()].behaviorStatus("wander") == "active" :
            self.dictBehaviors[self.animals[animalID].getAnimalInstance()].removeAi("wander")

        self.dictBehaviors[self.animals[animalID].getAnimalInstance()].seek(target, 1.0)
        taskMgr.add(self.checkBoundary, "checkBoundary" + str(animalID), extraArgs=[animalID, target, zone_id, gameState], appendTask=True)

    #
    # A task used to check the position of the migrating animal and
    # report coordinates for the duration of the migration.
    #
    def checkBoundary(self, animalID, target, zone_id, gameState, task):

        if ( (self.isOnTarget(animalID, target)) | (self.dictBehaviors[self.animals[animalID].getAnimalInstance()].behaviorStatus("seek") == "done") ) :
            print "Animal " + str(animalID) + " completed migration."

            self.dictBehaviors[self.animals[animalID].getAnimalInstance()].removeAi("seek")

            obj = {}
            obj['animalID'] = animalID
            obj['newzone_id'] = self.env.getUniquezone_id(zone_id)

            self.AIworld.removeAiChar(str(self.dictAiChars[self.animals[animalID].getAnimalInstance()]))
            gameState.responseUpdateAnimalZone(obj)

            taskMgr.remove("checkBoundary" + str(animalID))
            return task.done

        #print str(target) + " but now at " + str(self.animals[animalID].get3DAnimalActor().getPos())
        self.dictBehaviors[self.animals[animalID].getAnimalInstance()].removeAi("seek")
        self.dictBehaviors[self.animals[animalID].getAnimalInstance()].seek(target, 1.0)

        return task.cont

    #
    # Checks if the animal with the given animal ID
    # has crossed a zone boundary.
    #
    def isOnTarget(self, animalID, target):
        targetX = round(target.getX())
        targetY = round(target.getY())

        animalX = round(self.animals[animalID].getX())
        animalY = round(self.animals[animalID].getY())

        return (( targetX == animalX ) & ( targetY == animalY ))

    
    def AIUpdate(self,task):
        try:
            self.AIworld.update()
        except:
            pass

#        self.moveAnimals()
        return task.cont
    
    def moveAnimals(self, task):
        #print "zone_id - ",self.zone_id
        for animalID in self.animals:
            self.animals[animalID].updateTask(None)
            #self.animals[animalID].oldMove(task)
#            self.animals[animalID].move()
            #print "animalID",animalID
        return task.again

    def setHasWater(self,bool):
        self.hasWater = bool
        
    def setPlantNoWaterCount(self,noWaterCount,plantID):
        self.flora[plantID].setNoWaterCount(noWaterCount)
        
    def setPlantNoLightCount(self,noLightCount,plantID):
        self.flora[plantID].setNoLightCount(noLightCount)
    
    def setAnimalNoWaterCount(self,noWaterCount,animalID):
        self.animals[animalID].setNoWaterCount(noWaterCount)    
     
    def setAnimalBiomass(self,animalID,biomass,scalePercentage):
        self.animals[animalID].setAnimalBiomass(biomass,scalePercentage)
        
    def setPlantBiomass(self,plantID,biomass,scalePercentage):
        self.flora[plantID].setPlantBiomass(biomass,scalePercentage)
        
    def getListOfAnimals(self):
        return self.animals
    
    def getListOfPlants(self):
        return self.flora

    def revealAnimalDisease(self,animalID,diseaseID):
        #change the scale value of the animal to 1/2 from Models file
        return None
    def cureAnimalDisease(self,animalID,diseaseID):
        #restore the scale value of the animalID from Models file
        return None    
    def revealPlantDisease(self,plantID,diseaseID):
        #change the scale value of the animal to 1/2 from Models file
        #change the leaves of the tree brown
        return None
    def cureAnimalDisease(self,plantID,diseaseID):
        #restore the scale value of the animalID from Models file
        #set the plants to healthy
        return None
    
    def getAnimal(self, animalID):
        if animalID in self.animals:
            return self.animals[animalID]

    def getPlant(self, plant_id):
        if plant_id in self.flora:
            return self.flora[plant_id]

    def removePlant(self, plantID):

        if plantID in self.flora:
            plant = self.flora[plantID]
            #remove from list of obstacles
            self.AIworld.removeObstacle(plant.getPlantModel())
            del self.listOfStaticObstacles[plantID]
            #remove from list of flora
            plant.unload()
            del self.flora[plantID]
            del game.listOfPlants[plantID]

    def removeAnimal(self, animalID):

        if animalID in self.animals:
            animal = self.animals[animalID]
            aiID = animal.getAnimalInstance()

            self.AIworld.removeObstacle(animal)
            del self.listOfDynamicObstacles[animalID]
            self.AIworld.removeAiChar(str(aiID))
            del self.dictBehaviors[aiID]
            del self.dictAiChars[aiID]

            animal.unload()
            del self.animals[animalID]
            del game.listOfAnimals[animalID]

    def addAnimalObject(self,animalID,tempAnimalObject):
        self.animals[animalID] = tempAnimalObject
        
    def getAnimalType(self,animalID):
        return self.animals[animalID].getAnimalType()
    
    def getPlantType(self,plantID):
        return self.flora[plantID].getPlantType()
    
    def updateOwnerOfAnimal(self,animalID,newAvatarID):
        self.animals[animalID].setAvatarID(newAvatarID)

    def updateRoutine(self, task):
        
        for animal in self.animals.values():
            if animal.numDead > 0:
                if animal.getLifeStatus() == Constants.LIFE_STATUS_DEAD or animal.getLifeStatus() != Constants.LIFE_STATUS_DYING:
                    self.setTotalAnimalList(animal.animalType, self.totalAnimalList[animal.animalType] - animal.numDead)
                    animal.numDead = 0

                if animal.getLifeStatus() == Constants.LIFE_STATUS_DEAD:
                    self.removeAnimal(animal.getID())

        for plant in self.flora.values():
            if plant.numDead > 0:
                if plant.getLifeStatus() == Constants.LIFE_STATUS_DEAD or plant.getLifeStatus() != Constants.LIFE_STATUS_DYING:
                    self.setTotalPlantList(plant.plantType, self.totalPlantList[plant.plantType] - plant.numDead)
                    plant.numDead = 0

                if plant.getLifeStatus() == Constants.LIFE_STATUS_DEAD:
                    self.removePlant(plant.getID())

        return task.cont
