'''
Created on Nov 20, 2011

@author: hunvil
'''
import random,sys, os, math
from random import Random
from panda3d.ai import *
from direct.particles.ParticleEffect import ParticleEffect
from panda3d.core import Filename

from common.Constants import Constants
from common.MousePicker3D import MousePicker3D
from main.MainLobby.World.World3D.Env3D import Env3D
from main.MainLobby.World.World3D.Models import Models
from main.MainLobby.World.World3D.Avatar import Avatar

class GameState():
    def __init__(self):
        if Constants.DEBUG:
            print 'Loading Game State'
#1. CharName is going to be store as global variable in Main class.
#2. AvatarID should be retireve from server when we start loading the game, 
#   becuase one player may have different avatar for different world.
#3. WorldType will put into messageQueue pendingobj.
#4. WorldName will put into messageQueue pendingobj.
        self.charName           =None#= main.charName    
        self.avatarID           =None#= main.avatarID
        self.worldName          =None#= main.msgQ.getObjFromPendingObj(Constants.WORLD_NAME)
        self.worldType          =None#= main.msgQ.getObjFromPendingObj(Constants.WORLD_TYPE)
        self.listOfAvatarIDs    = {}   #listOfAvatarIDs[avatarID] = avatarObject
        self.listOfEnvironments = {}
        self.listOfZones        = {}   # listOfZones[unique zone ID ] = self.listOfEnv[envID].zone[0]
        self.listOfEnv          = {}   # list of environments
        self.listOfPlants       = {}   # listOfPlants[plantID] = zoneID
        self.listOfAnimals      = {}   # listOfAnimals[animalID] = zoneID
        self.Models = Models()
        self.waterSourceArray   = []
        #self.putCommandToMsgQ()
        self.requestGetEnvironment()
        #self.mPicker = MousePicker3D(self)
        
    def requestGetEnvironment(self):
        rContents = {'worldName':self.worldName}
        main.cManager.sendRequest(Constants.CMSG_REQUEST_GET_ENVIRONMENT,rContents)
        return None   
     
#@hunvil - todo create enviornment object for client network
    def responseGetEnvironment(self,obj):
        #self.createEnvironment(rowID,columnID,zone0ID,zone1ID,zone2ID,zone3ID,\
        #                  zone4ID,zone5ID,zone6ID,zone7ID,zone8ID,avatarID,mapID)
        return None

           
    def putCommandToMsgQ(self):
        main.msgQ.addToCommandList(Constants.CMSG_REQUEST_ENVIRONMENT_SCORE,self.responseEnvScore)
        main.msgQ.addToCommandList(Constants.CMSG_REQUEST_FREE_PLANT,self.responseFreePlant)
        main.msgQ.addToCommandList(Constants.CMSG_REQUEST_FREE_ANIMAL,self.responseFreeAnimal)
        return None
    
#not used currently
    def getPlantModels(self):
        return self.Models.plantModels

#not used currently
#modelAnimationsList - is the list of the model path and different animations for each animal    
    def getAnimalModels(self):
        return self.Models.modelAnimationsList
    
#suggestion keep AnimalType seperately listOfAnimalTypes['elephant'], listOfAnimalTypes['zebra'], listOfAnimalTypes['cow'] etc
###############  RequestBuyAnimal #################################
#animalType - "cow"
#avatarId = 20    
#requestBuyAnimal() method to be called by 2D interface
#RequestBuyAnimal Protocol- client sends animalType and avatarId to server 
#Server checks whether avatarId has enough money to buy animal
#then sends ResponseBuyAnimal Protocol
#paramters to send to server - animalType, avatarID
    def requestBuyAnimal(self):
        rContents = {'avatarId': self.avatarID, 'animalType' : animalType}
        main.cManager.sendRequest(Constants.CMSG_BUY_ANIMAL, rContents)
        return None
    
#suggestion keep PlantType seperately listOfPlantTypes['acacia'], listOfPlantTypes['boabab'] etc
##############  RequestBuyPlant  ##################################
#plantType - "acacia"
#avatarId = 20 
#requestBuyPlant() method to be called by 2D interface
#RequestBuyPlant Protocol - client sends plantType and avatarId to server, 
#Server checks whether avatarId has enough money to buy plant
#then sends ResponseBuyPlant protocol
#paramters to send to server - plantType, avatarID,useAbilityPoints
    def requestBuyPlant(self):
        rContents = {'avatarId': self.avatarID, 'plantType' : animalType}
        main.cManager.sendRequest(Constants.CMSG_BUY_PLANT, rContents)        
        return None    


###############  ResponseBuyAnimal #################################
#responseBuyAnimal() method to be called by client Network
#Buy is success or failure, animalId,animalType, avatarId, zoneId, biomass, xCoor, yCoor
#client to create a instance of animal here
#since animal was shopped, inform 2D, so that animal can be placed on terrain
    def responseBuyAnimal(self,animalID,animalType,avatarID,zoneID,biomass):
        #find the mapping of the zone Id
        #create a instance of animal Object and add to self.listOfZones[zoneId]
        self.listOfZones[zoneID] = None         #listOfZones[zoneId]has instance of zoneID object
        return None
 

###############  ResponseBuyPlant #################################
#responseBuyPlant() method to be called by client Network
#Buy is success or failure, plantId,plantType, avatarId, zoneId, biomass, xCoor, yCoor
#client to create a instance of plant here
#since plant was shopped from Shop UI, inform 2D, so that plant can be placed on terrain
    #def responseBuyPlant(self,plantId,plantType,avatarId,zoneId,biomass,xCoor,yCoor):
    def responseBuyPlant(self,plantID,plantType,avatarID,zoneID,biomass):
        #find the mapping of the zone Id
        #create a instance of plant Object and add to self.listOfZones[zoneId]
        self.listOfZones[zoneID] = None     #listOfZones[zoneId]has instance of zoneID object
        return None    
    
###############  ResponseBirthAnimal #################################
#responseBirthAnimal() is called by client network, 
#if normal birth animal, randomly select x,y,z
#create an instance of Animal object and add to listOfZones[zoneId](has instance of zoneID object)
#add animalID to listOfDynamicObstacles[animalID] in the listOfZones[zoneId] object
#client to send server x,y,z for the animalId
    #def responseBirthAnimal(self,animalId,animalType,avatarId,zoneId,biomass,xCoor,yCoor):
    def responseBirthAnimal(self,animalID,animalType,avatarID,zoneID,biomass):
        #find the mapping of the zone Id
        #create a instance of animalObject and add to self.listOfZones[zoneId]
        #listOfZones[zoneId]has instance of zoneID object
        modelPathAndAnimation = self.Models.modelAnimationsList[animalType]
        scaleValue = self.Models.scaleValues[animalType]
        self.listOfZones[zoneID].addAnimal(animalID, animalType, avatarID, zoneID, biomass,modelPathAndAnimation,scaleValue)
        self.listOfAnimals[animalID] = zoneID
        self.listOfZones[zoneID].addAnimalToAI(animalID)
        return None
    

###############  ResponseBirthPlant #################################
#responseBirthPlant() method to be called by client Network
#Buy is success or failure,plantId,plantType, avatarId, zoneId, biomass
#client to create a instance of plant here
#if normal birth plant, randomly select x,y,z
#add plantId to listOfStaticObstacles[animalID] in the listOfZones[zoneId] object
#client to send server x,y,z for the plantId
    def responseBirthPlant(self,plantID,plantType,avatarID,zoneID,biomass):
        #find the mapping of the zone Id
        #create a instance of plant object and add to self.listOfZones[zoneId]
        #listOfZones[zoneId]has instance of zoneID object
        modelPath = self.Models.plantModels[plantType]
        scaleValue = self.Models.scaleValues[plantType]
        self.listOfZones[zoneID].addPlant(plantID, plantType, avatarID, zoneID, biomass,modelPath,scaleValue)
        self.listOfPlants[plantID] = zoneID
        return None    

###############  RequestUpdateAnimalCoors #################################  
#requestUpdateAnimalCoors() sends animal coors to client network
#Client to send animal x, y, z to server  
#It will happen only after end of shop UI,end of player placing plant on terrain
#Also it will be called if animal changes zone
#parameters to send to server - animalID, zoneID, xCoor, yCoor 
    def requestUpdateAnimalCoors(self):
        return None
    
###############  RequestUpdatePlantCoors  ################################# 
#requestUpdatePlantCoors() sends plant coors to client network 
#Client to send plant x, y, z to server  
#It will happen only after end of shop UI,end of player placing animal on terrain
#parameters to send to server - plantID, zoneID, xCoor, yCoor
    def requestUpdatePlantCoors(self):
        return None    

#@hunvil - todo not sure what kind of animations to show    
###############  ResponseUpdateAnimalBiomass #################################     
#responseUpdateAnimalBiomass() will be called by client network
#The animal ID should increase its current biomass to targetBiomass in targetTime 
    def responseUpdateAnimalBiomass(self,animalID,biomass,targetBiomass,targetTime):
        return None
    
###############  ResponseUpdateAnimalBiomass #################################     
#responseUpdatePlantBiomass() will be called by client network
#The plant ID should increase its current biomass to targetBiomass in targetTime 
    def responseUpdatePlantBiomass(self,plantID,biomass,targetBiomass,targetTime):
        return None    
    
#@hunvil - todo not sure what this method does
############### RequestUpdateAnimalTarget ###################################
#Request is from client to server
#parameters to send to server - animalId,zoneId,xTarg,yTarg
    def requestUpdateAnimalTarget(self):
        return None

############### ResponseUpdateAnimalNoWaterCount ###################################
#responseUpdateAnimalNoWaterCount() is called by client network
    def responseUpdateAnimalNoWaterCount(self,animalID,noWaterCount):
        return None
    
############### ResponseUpdatePlantNoWaterCount ###################################
#responseUpdatePlantNoWaterCount() is called by client network
    def responseUpdatePlantNoWaterCount(self,plantID,noWaterCount):
        return None   
    
############### ResponseUpdatePlantNoLightCount ###################################
#responseUpdatePlantNoLightCount() is called by client network
    def responseUpdatePlantNoLightCount(self,plantID,noLightCount):
        zoneID = self.listOfAnimals[plantID]
        self.listOfZones[zoneID].updatePlantNoLightCount(plantID,noLightCount)
        return None       

############### ResponseUpdateAnimalZone ###########################################
#responseUpdateAnimalZone() is called by client network
    def responseUpdateAnimalZone(self,animalID,newZoneID):
        #remember to update listOfAnimals[animalID] = newZOneID
        return None    
    
############### ResponseUpdateAnimalOwner ###########################################
#responseUpdateAnimalOwner() is called by client network
    def responseUpdateAnimalOwner(self,animalID,newAvatarID):
        return None
    
############### ResponseKillAnimal    ################################################
#responseKillAnimal() is called by client network
    def responseKillAnimal(self,animalID,preyAnimalID):
        #find animalID = idAttacker in which zone
        #find preyAnimalId = idTarget in which zone
        zoneIDSourceAnimal = self.listOfAnimals[animalID]
        zoneIDTargetAnimal = self.listOfAnimals[preyAnimalID]
        if (zoneIDSourceAnimal == zoneIDTargetAnimal):
            #Both animals are in same zone
            #self.listOfZones[zoneIDSourceAnimal].attack(animalID, preyAnimalID)
            #taskMgr.doMethodLater(20,self.testCase1,"testCase1")
            self.listOfZones[zoneIDSourceAnimal].attackAnimal(animalID,preyAnimalID)
            return None
        else:
            self.alertError("Error in Response Kill Animal because animals weren't in same zone")
            return None
    
############### ResponseKillPlant    ################################################
#responseKillPlant() is called by client network
    def responseKillPlant(self,plantID):
        return None    
    
    def responseUpdateAvatarXP(self,avatarXP):
        return None
    
    def responseUpdateAvatarCash(self,cash):
        return None
    
    def responseUpdateEnvironmentScore(self,avatarID,envScore):
        self.listOfAvatarIDs[avatarID].updateEnvScore(envScore)
        return None

#@hunvil - todo where do we retrieve the vote of the player from? 
############### RequestGameScaleVote    ################################################    
#Client to send server the game scale vote for the avatarID
#Parameters to send to server are - avatarID, vote(1-10)    
    def requestGameScaleVote(self):
        return None

################ ResponseShopAnimal #####################################################
#responseShopAnimal() is to be called by client network
    def responseShopAnimal(self,animalType,description,cost,preyList,predatorList):
        return None

################ ResponseShopPlant #####################################################
    #responseShopPlant() is to be called by client network    
    def responseShopPlant(self,plantType,description,cost,preyList):
        return None    
    
############### RequestFreeAnimal   ######################################################
    def requestFreeAnimal(self):
        #request free animal
        main.cManager.sendRequest(Constants.REQUEST_FREE_ANIMAL)        
        return None
    
############### RequestFreePlant   ######################################################
    def requestFreePlant(self):
        #request free plant
        main.cManager.sendRequest(Constants.REQUEST_FREE_PLANT)
        return None

############### ResponseFreeAnimal   ######################################################
    #def responseFreeAnimal(self,(self,plantID,plantType,avatarID,zoneID,biomass):):
    def responseFreeAnimal(self,obj):
        #create a new instance of plant and place on the terrain
        return None
    
############### ResponseFreePlant   ######################################################
    #def responseFreePlant(self,plantID,plantType,avatarID,zoneID,biomass):
    def responseFreePlant(self,obj):
        #create a new instance of plant and place on the terrain
        return None            
 
############### ResponseUpdateWaterSource #################################################
    def responseWaterSource(self,waterSourceID,zoneID,waterAmount,targetWaterAmount,targetTime):
        return None
     
    def createEnvironment(self,rowID,columnID,zone0ID,zone1ID,zone2ID,zone3ID,\
                          zone4ID,zone5ID,zone6ID,zone7ID,zone8ID,avatarID,mapID):
        #avatar instance Avatar(avatarID,cash,abilityPoints)
        avatarIDObject = Avatar(avatarID,0,0)
        self.listOfAvatarIDs[avatarID] = avatarIDObject
        
        envID = (rowID * 10 + (columnID + 1))
        self.listOfEnv[envID] = Env3D(rowID,columnID)
        self.listOfZones[zone0ID] = self.listOfEnv[envID].zones[0]
        self.listOfZones[zone1ID] = self.listOfEnv[envID].zones[1]
        self.listOfZones[zone2ID] = self.listOfEnv[envID].zones[2]
        self.listOfZones[zone3ID] = self.listOfEnv[envID].zones[3]
        self.listOfZones[zone4ID] = self.listOfEnv[envID].zones[4]
        self.listOfZones[zone5ID] = self.listOfEnv[envID].zones[5]
        self.listOfZones[zone6ID] = self.listOfEnv[envID].zones[6]
        self.listOfZones[zone7ID] = self.listOfEnv[envID].zones[7]
        self.listOfZones[zone8ID] = self.listOfEnv[envID].zones[8]
        numArr = []
        numArr.append(zone0ID)
        numArr.append(zone1ID)
        numArr.append(zone2ID)
        numArr.append(zone3ID)
        numArr.append(zone4ID)
        numArr.append(zone5ID)
        numArr.append(zone6ID)
        numArr.append(zone7ID)
        numArr.append(zone8ID)
        self.waterSourceArray = self.pickNums(6,numArr)
        print "Water Source Array -",self.waterSourceArray
        self.requestWaterSources()

    def responseWaterSources(self,obj):
        if (obj[0]):
            self.requestFreeAnimal()
            self.requestFreePlant()
        else:
            self.alertError("could not send request free animal")   
           
#requestWaterSources() calls the client network to send water source info to server        
    def requestWaterSources(self):
        hasWater = True;
        rContents = {}
        for index in range(len(self.waterSourceArray)):
            print index," - ",self.waterSourceArray[index]
            #send to server the array of zoneID
            rContents[self.waterSourceArray[index]] = hasWater
        #call the client network with constant code and the contents    
        main.cManager.sendRequest(Constants.CMSG_REQUESTWATERSOURCES,rContents)    
        return None 
   
#pickNums picks unique numbers from an array of given numbers.
#This is used to pick 6 unique zones from 9 zones
#nums = 6, numArr = array of zoneID's of 9 zones   
#return parameter = array of zoneID's of 6 zones out of 9        
    def pickNums(self,nums, numArr):
        if(nums > len(numArr)):
            return 0
        pickArr = []
        tempArr = numArr
        i = 0
        while(i < nums):
            g = Random()
            pickArr.append(tempArr[int(round((len(tempArr) - 1) * g.random()))])
            temp = pickArr[len(pickArr)-1]
            count = 0
            for x in tempArr:
                if(x == temp):
                    tempArr[count] = 'null'
                    tempArr2 = []
                    for y in tempArr:
                            if(y != 'null'):
                                    tempArr2.append(y)
                    tempArr=tempArr2;
                    break
                count = count + 1
            i = i + 1
        return pickArr
    
    def alertError(self,alertMessage):
        print alertMessage
        return None
    
    def responseEnvScore(self):
        #parse the contents from List received from Network
        return None    

#2D will pass animaltype,avatarId-> Gamestate,
#Gamestate disable mouse click
#Gamestate should pass to client n/w
#client n/w will receive reply from server with animal instance and inform gamestate
#Gamestate will enable mouse click
#user will place animal on terrain
#Gamestate get the zoneID , xCoor,yCoor from mouse click
#Gamestate will send the zoneID,xCoor,yCoor to server