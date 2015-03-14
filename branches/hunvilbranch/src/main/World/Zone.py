#@PydevCodeAnalysisIgnore
'''
Created on Oct 22, 2011

@author: hunvil
'''
from panda3d.core import Texture, TextureStage
from common.Constants import Constants

class Zone():
    def __init__(self,envId,zoneId):
        if Constants.DEBUG:
            print 'Loading Environment No. ' + str(envId) + ' , Zone No.' + str(zoneId)
        self.xoff = 0
        self.yoff = 0
        self.size = 513
        self.playerBuffer = 5
        self.zoneId = zoneId
        self.plantListZone = {}     #keeps track of plants added to World
        self.animalListZone = {}    #keeps track of animals added to world        
        
        self.AICharacterList = {}   #keeps tracks of all the AICharaters in a Zone
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

    def getAnimal(self, animalId):
        if animalId in self.animalListZone:
            return self.animalListZone[animalId]

    def createActor(self,animal,startPosX,startPosY):
        id = animal+self.modelAnimationsList.__len__()
        self.actorModel[id] = Actor(self.modelAnimationsList[animal][0],self.modelAnimationsList[animal][1])
        
        self.dummy = dummy
        startPosZ = self.terrain.getElevation(startPosX, startPosY) * root.getSz()
        self.elephant = Actor("models/elephant/elephant",
                                 {"walk":"models/elephant/elephant-walk",
                                  "die":"models/elephant/elephant-die"})        
        self.elephant.reparentTo(self.dummy)
        self.elephant.setScale(.9)
        self.elephant.setPos(startPosX, startPosY, startPosZ)
        self.elephantHeight = 1.2  # to locate the top of elephant's head for the camera to point at        
        self.elephantactor = ActorProperties(self.elephant,self.elephantHeight,startPosX,startPosY,startPosZ)
        
        self.elephantHead = NodePath(PandaNode("elephantHead"))
        self.elephantHead.reparentTo(self.dummy)         

    def setAnimal(self, animal):
        if animal.getID() not in self.animalListZone:
            self.animalListZone[animal.getID()] = animal
                        
    def removeAnimal(self, animalId):
        if animalId in self.animalListZone:
            self.animalListZone[animalId].unload()
            del self.animalList[animalId]
            
    def getAnimalCountZone(self):
        return self.animalListZone.__len__()

    def getAnimalList(self):
        return self.animalListZone
     
    def getPlant(self, plantId):
        if plantId in self.plantListZone:
            return self.plantListZone[plantId]

    def setPlant(self, plant):
        if plant.getID() not in self.plantListZone:
            self.plantListZone[plant.getID()] = plant
                        
    def removePlant(self, plantId):
        if plantId in self.plantListZone:
            self.plantListZone[plantId].unload()
            del self.plantList[plantId]

    def getPlantList(self):
        return self.plantListZone
    
    def getPlantCountInZone(self):
        return self.plantListZone.__len__()
    
    def setAICharacter(self,aiWorld,animalInstance):
        #eg : AICharacter("elephant1",self.elephant1, 30, 5, 5)
        animalInstance.setAICharacter(aiWorld)
        
    def getAICharacter(self,modelNodePath):
        return self.AICharacterList[modelNodePath]