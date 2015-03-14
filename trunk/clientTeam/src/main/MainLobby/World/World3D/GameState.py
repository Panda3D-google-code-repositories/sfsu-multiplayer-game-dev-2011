'''
Created on Nov 20, 2011

@author: hunvil
'''
import __builtin__

from calendar import month_name
from math import ceil
from math import sqrt
from random import random

from common.Constants import Constants
from common.DatabaseHelper import DatabaseHelper
from common.MousePicker3D import MousePicker3D

from main.MainLobby.World.World3D.Avatar import Avatar
from main.MainLobby.World.World3D.Animal3D import Animal3D
from main.MainLobby.World.World3D.AnimalType import AnimalType
from main.MainLobby.World.World3D.Env3D import Env3D
from main.MainLobby.World.World3D.Plant3D import Plant3D
from main.MainLobby.World.World3D.PlantType import PlantType

class GameState:

    def __init__(self, worldGui):

        if Constants.DEBUG:
            print 'Loading Game State'

        __builtin__.game = self

        self.worldGui = worldGui 
        self.debugMode = "OFF"   
#1. CharName is going to be store as global variable in Main class.
#2. AvatarID should be retireve from server when we start loading the game, 
#   becuase one player may have different avatar for different world.
#3. WorldType will put into messageQueue pendingobj.
#4. WorldName will put into messageQueue pendingobj.
        self.directionalLight   = None
        self.ambientLight       = None
        base.enableParticles()
        self.rainParticles      = None        
        self.charName           =None#= main.charName    
        self.avatarID           =None#Comes from Server as a first paramter in ResponseGetEnvironment
        self.worldName          =None#= main.msgQ.getObjFromPendingObj(Constants.WORLD_NAME)
        self.worldType          =None#= main.msgQ.getObjFromPendingObj(Constants.WORLD_TYPE)
        self.timeRate = 1
        

        self.listOfZones        = {}   # listOfZones[unique zone ID ] = self.listOfEnv[envID].zone[0]
        self.listOfAvatars      = {}   #listOfAvatarIDs[avatarID] = avatarObject 
        self.listOfEnv          = {}   # list of environments
        self.listOfPlants       = {}   # listOfPlants[plantID] = zoneID
        self.listOfAnimals      = {}   # listOfAnimals[animalID] = zoneID
        self.waterSourceArray   = []
        self.avatarObj = Avatar()
        self.putCommandToMsgQ()

        self.worldName = main.msgQ.getObjFromPendingObj(Constants.WORLD_NAME)
        self.worldType = main.msgQ.getObjFromPendingObj(Constants.WORLD_TYPE)
        self.scoreInfo = main.msgQ.getObjFromPendingObj(Constants.SMSG_CHANGE_AVATAR_TYPE)
        self.ownAvatarID = main.msgQ.getObjFromPendingObj(Constants.USER_ID)
        self.requestReady()

        self.mPicker = MousePicker3D(self)

        self.animalNameList = {}
        self.plantNameList = {}

        self.listOfAnimalTypes  = {}    # listOfAnimalTypes[animalType] = animalTypeID
        self.listOfPlantTypes   = {}    # listOfPlantTypes[plantType] = plantTypeID
    
        self.animalTypes = {}       # animalTypes[animalTypeID] = animalType object
        self.plantTypes  = {}       # plantTypes[plantTypeID] = plantType object
        
        #uncomment the two line when integrating with server
        #self.listOfPlantCount = {}  #listOfPlantCount[plantType] = number of plants of this type
        #self.listOfAnimalCount = {} #listOfAnimalCount[animalType] = number of animals of this type
        
        #The below two lines for local testing purposes
        self.listOfAnimalCount = {}
        self.listOfPlantCount = {}
                                  
        self.animalStatistics = []
        self.plantStatistics  = []
        self.listOfModelIds= {}
        self.currentDay = None

        self.predatorList = {}
        self.preyList = {}
#        self.herbivore = ['Select Herbivore']
#        self.carnivore = ['Select Carnivore']
#        self.omnivore = ['Select Omnivore']
        self.herbivore = []
        self.carnivore = []
        self.omnivore = []
        self.animalTypeId = {}
        self.plantList = []
        
    def getCurrentDay(self):
        return self.currentDay

    def requestReady(self):
        self.debugPrint("requestReady")
        main.cManager.sendRequest(Constants.CMSG_READY)

    def requestHighScore(self, type):
        main.cManager.sendRequest(Constants.CMSG_HIGH_SCORE, {'type' : type})

    def responseHighScore(self, args):

        self.worldGui.setBestEnvScore(args['scoreList'])
        self.worldGui.setBestTotalEnvScore(args['totalScoreList'])
        self.worldGui.setBestCurrentEnvScore(args['currentScoreList'])

        self.worldGui.startScoreSequence()

    def responseShopUnlock(self, unlockList):

        self.worldGui.gameShop.clearNewItems()

        for species in unlockList:
            if species['organism_type'] == 1:
                self.worldGui.gameShop.loadPlantItemInfo({'items' : [species], 'initial' : False})
                self.responseShopListPlant([species])
            else:
                self.worldGui.gameShop.loadAnimalItemInfo({'items' : [species], 'initial' : False})
                self.responseShopListAnimal([species])

    def requestRestart(self, status):
        main.cManager.sendRequest(Constants.CMSG_RESTART, {'status' : status})

        if status and self.worldGui.restartButton != None:
            self.worldGui.restartButton.destroy()
            self.worldGui.restartButton = None

    def responseRestart(self, status):
        if status:
            self.worldGui.createRestartBox()

#    def responseReady(self, status, username):
    def responseReady(self, status):
        self.debugPrint("responseReady")
        print status
#        print username, 'is', status

    def responseStartGame(self, args):
        self.debugPrint("responseStartGame")
        if args['status']:
            self.worldGui.startWorld(args)

    def requestChartBiomass(self, type):
        main.cManager.sendRequest(Constants.CMSG_CHART_BIOMASS, {'type' : type})

    def responseChartBiomass(self, args):

        csvList = self.worldGui.chart.parseCSV(args['csv'])

        for i in range(len(csvList.values()[0])):
            month = int(csvList['.xLabels'][i])
            csvList['.xLabels'][i] = month_name[(month - 1) % 12 + 1][:3] + ' \'%02d' % ((month - 1) / 12 + 1)

        if args['type'] == 0:
            self.worldGui.chart.setInitialChartData(csvList)
        elif args['type'] == 1:
            self.worldGui.chartTwo.setInitialChartData(csvList)
        elif args['type'] == 2:
            self.worldGui.chartThree.setInitialChartData(csvList)

    def requestChat(self, type, message):
        main.cManager.sendRequest(Constants.CMSG_CHAT, {'type' : type, 'message' : message})

    def responseChat(self, args):

        if args['type'] == 0:
            self.worldGui.chat.setUserMessage(args['type'], args['name'], args['message'])
        else:
            self.worldGui.chat.setSystemMessage(args['type'], args['message'])

    def requestPlayers(self):
        main.cManager.sendRequest(Constants.CMSG_SEEONLINEPLAYERS)

    def responsePlayers(self, args):
        self.worldGui.setOnlinePlayers(args)

    def putCommandToMsgQ(self):
        main.msgQ.addToCommandList(Constants.OWN_AVATARID,self.responseOwnAvatarId)
        main.msgQ.addToCommandList(Constants.SMSG_RESPONSE_GET_ENVIRONMENT,self.responseCreateEnvironment)
        main.msgQ.addToCommandList(Constants.SMSG_CREATE_ENV,self.responseCreateEnv)
        main.msgQ.addToCommandList(Constants.CMSG_REQUESTWATERSOURCES,self.responseWaterSources)
        main.msgQ.addToCommandList(Constants.SMSG_UPDATE_WATER_SOURCE,self.updateWaterSource)
        main.msgQ.addToCommandList(Constants.SMSG_UPDATE_ENV_SCORE,self.responseUpdateEnvScore)
        main.msgQ.addToCommandList(Constants.SMSG_UPDATE_GOLD,self.responseUpdateGold)                
        main.msgQ.addToCommandList(Constants.SMSG_UPDATE_XP,self.responseUpdateXP)
        main.msgQ.addToCommandList(Constants.SMSG_UPDATE_TIME,self.responseUpdateTime)
        main.msgQ.addToCommandList(Constants.SMSG_RESTART,self.responseRestart)
        main.msgQ.addToCommandList(Constants.SMSG_HIGH_SCORE,self.responseHighScore)
        main.msgQ.addToCommandList(Constants.SMSG_SHOP_UNLOCK, self.responseShopUnlock)
        main.msgQ.addToCommandList(Constants.SMSG_CHART_BIOMASS, self.responseChartBiomass)
        main.msgQ.addToCommandList(Constants.SMSG_CHAT, self.responseChat)
        main.msgQ.addToCommandList(Constants.CMSG_SEEONLINEPLAYERS, self.responsePlayers)

        main.msgQ.addToCommandList(Constants.SMSG_UPDATE_LEVEL,self.responseUpdateLevel)
        main.msgQ.addToCommandList(Constants.SMSG_UPDATE_ANIMAL_NO_WATER_COUNT ,self.responseUpdateAnimalNoWaterCount)
        main.msgQ.addToCommandList(Constants.SMSG_UPDATE_PLANT_NO_WATER_COUNT ,self.responseUpdatePlantNoWaterCount)
        main.msgQ.addToCommandList(Constants.SMSG_UPDATE_PLANT_NO_LIGHT_COUNT ,self.responseUpdatePlantNoLightCount)
        main.msgQ.addToCommandList(Constants.SMSG_UPDATE_ANIMAL_BIOMASS,self.responseUpdateAnimalBiomass)
        main.msgQ.addToCommandList(Constants.SMSG_UPDATE_PLANT_BIOMASS,self.responseUpdatePlantBiomass)
        main.msgQ.addToCommandList(Constants.SMSG_BIRTH_ANIMAL,self.resBirthAnimal)
        main.msgQ.addToCommandList(Constants.SMSG_BIRTH_PLANT,self.resBirthPlant)
        main.msgQ.addToCommandList(Constants.SMSG_KILL_ANIMAL,self.responseKillAnimal)
        main.msgQ.addToCommandList(Constants.SMSG_KILL_PLANT,self.responseKillPlant)
        main.msgQ.addToCommandList(Constants.CMSG_START_GAME,self.responseStartGame)
        main.msgQ.addToCommandList(Constants.SMSG_WEATHER_PREDICTION,self.weatherPrediction)
        main.msgQ.addToCommandList(Constants.CMSG_SHOP_LIST_ANIMAL_GAMESTATE,self.responseShopListAnimal)
        main.msgQ.addToCommandList(Constants.CMSG_SHOP_LIST_PLANT_GAMESTATE,self.responseShopListPlant)
        main.msgQ.addToCommandList(Constants.CMSG_READY,self.responseReady)
        main.msgQ.addToCommandList(Constants.SMSG_TARGET_REWARD,self.responseTargetReward)
        main.msgQ.addToCommandList(Constants.SMSG_BUY_ANIMAL,self.responseBuyAnimal)
        main.msgQ.addToCommandList(Constants.SMSG_BUY_PLANT,self.responseBuyPlant)
###############  RequestBuyAnimal #################################
#animalType - "cow"
#avatarId = 20    
#requestBuyAnimal() method to be called by 2D interface
#RequestBuyAnimal Protocol- client sends animalType and avatarId to server 
#Server checks whether avatarId has enough money to buy animal
#then sends ResponseBuyAnimal Protocol
#paramters to send to server - animalType, avatarID
    def requestBuyAnimal(self,animalTypeID,zoneID,targetPoint):
            self.debugPrint("requestBuyAnimal")
            msg = "zoneID - ",zoneID," targetPoint- ",targetPoint,animalTypeID
            self.debugPrint(msg)

            #animalTypeID = self.listOfAnimalTypes[self.buyAnimalType]        #uncomment this during server integration
            xCoor = targetPoint[0]
            yCoor = targetPoint[1]
            rContents = {'animalTypeID'     : animalTypeID,        #uncomment this during server integration
                         'zoneID'           : zoneID,
                         'xCoor'            : xCoor,
                         'yCoor'            : yCoor}
            if(self.debugMode == "OFF"):
                self.debugPrint(rContents)
                main.cManager.sendRequest(Constants.CMSG_BUY_ANIMAL, rContents)
            elif(self.debugMode == "ON"):
                self.debugPrint("debugMode ON, buy Animal")
                animalID = len(self.listOfAnimals) + 1
                rContents = {'zCoor': 0.0, 'animalID': animalID, 'xCoor': xCoor, 'yCoor': yCoor, 'animalTypeID': animalTypeID, 'avatarID': 1, 'biomass': 10, 'zoneID': zoneID, 'modelID':self.animalTypes[int(animalTypeID)].getModelID() }
                print(rContents)
                self.resBirthAnimal(rContents)   
##############  RequestBuyPlant  ##################################
#plantType - "acacia"
#avatarId = 20 
#requestBuyPlant() method to be called by 2D interface
#RequestBuyPlant Protocol - client sends plantType and avatarId to server, 
#Server checks whether avatarId has enough money to buy plant
#then sends ResponseBuyPlant protocol
#paramters to send to server - plantType, avatarID,useAbilityPoints
    def requestBuyPlant(self, plantTypeID, zoneID, targetPoint):
            self.debugPrint("requestBuyPlant") 
            msg = "zoneID - ",zoneID," targetPoint- ",targetPoint
            self.debugPrint(msg)

            #plantTypeID = self.listOfPlantTypes[self.buyPlantType]        #uncomment this during server integration
            xCoor = targetPoint[0]
            yCoor = targetPoint[1]
            rContents = {'plantTypeID'     : plantTypeID,        #uncomment this during server integration
                         'zoneID'           : zoneID,
                         'xCoor'            : xCoor,
                         'yCoor'            : yCoor}
            if(self.debugMode == "OFF"):
                self.debugPrint(rContents)
                main.cManager.sendRequest(Constants.CMSG_BUY_PLANT, rContents)    
            elif(self.debugMode == "ON"):
                self.debugPrint("debugMode ON, buy Plant") 
                plantID = len(self.listOfPlants) + 1      
                rContents = {'zCoor': 0.0, 'plantTypeID': plantTypeID, 'plantID': plantID, 'xCoor': xCoor, 'yCoor': yCoor, 'avatarID': 1, 'biomass': 10, 'zoneID': zoneID, 'modelID':self.plantTypes[int(plantTypeID)].getModelID()}
                print rContents
                self.resBirthPlant(rContents)

    def responseTargetReward(self, args):
        target_id = args['target_id']
        type = args['type']
        amount = args['amount']

        target = None

        if target_id in self.listOfAnimals:
            target = self.listOfZones[self.listOfAnimals[target_id]].getAnimal(target_id)
        elif target_id in self.listOfPlants:
            target = self.listOfZones[self.listOfPlants[target_id]].getPlant(target_id)

        if type == Constants.REWARD_TYPE_XP:
            type = ' Exp'
        elif type == Constants.REWARD_TYPE_MONEY:
            type = ' Gold'

        if target:
            self.worldGui.floatingText.createText(Constants.TEXT_TYPE_EXPERIENCE, '+' + str(amount) + type, target)

###############  ResponseBuyAnimal #################################
#responseBuyAnimal() method to be called by client Network
#Buy is success or failure, animalId,animalType, avatarId, zoneId, biomass, xCoor, yCoor
#client to create a instance of animal here
#since animal was shopped, inform 2D, so that animal can be placed on terrain
    def responseBuyAnimal(self, args):
        self.debugPrint("responseBuyAnimal")

        status = args['status']
        animalTypeID = args['animalTypeID']
        amount = args['amount']

        if status == 0:
            self.worldGui.rightPendingText.createPendingText(Constants.TEXT_TYPE_BIRTH, self.listOfAnimalTypes[animalTypeID] + ' [Purchase]')

            if amount > 0:
                self.worldGui.leftPendingText.createPendingText(Constants.TEXT_TYPE_DAMAGE, '-' + str(amount) + ' Gold')
        elif status == 1:
            self.worldGui.rightPendingText.createPendingText(Constants.TEXT_TYPE_DAMAGE, self.listOfAnimalTypes[animalTypeID] + ' [Purchase Failed]')

###############  ResponseBuyPlant #################################
#responseBuyPlant() method to be called by client Network
#Buy is success or failure, plantId,plantType, avatarId, zoneId, biomass, xCoor, yCoor
#client to create a instance of plant here
#since plant was shopped from Shop UI, inform 2D, so that plant can be placed on terrain
    #def responseBuyPlant(self,plantId,plantType,avatarId,zoneId,biomass,xCoor,yCoor):
    def responseBuyPlant(self, args):
        self.debugPrint("responseBuyPlant")

        status = args['status']
        plantTypeID = args['plantTypeID']
        amount = args['amount']

        if status == 0:
            self.worldGui.rightPendingText.createPendingText(Constants.TEXT_TYPE_BIRTH, self.listOfPlantTypes[plantTypeID] + ' [Purchase]')

            if amount > 0:
                self.worldGui.leftPendingText.createPendingText(Constants.TEXT_TYPE_DAMAGE, '-' + str(amount) + ' Gold')
        elif status == 1:
            self.worldGui.rightPendingText.createPendingText(Constants.TEXT_TYPE_DAMAGE, self.listOfPlantTypes[plantTypeID] + ' [Purchase Failed]')

###############  ResponseBirthAnimal #################################
#responseBirthAnimal() is called by client network, 
#if normal birth animal, randomly select x,y,z
#create an instance of Animal object and add to listOfZones[zoneId](has instance of zoneID object)
#add animalID to listOfObstacles[animalID] in the listOfZones[zoneId] object
#client to send server x,y,z for the animalId
    #Original - def responseBirthAnimal(self,animalId,animalType,avatarId,zoneId,biomass,xCoor,yCoor):
    def responseBirthAnimal(self,status,animal_id,name,modelID,type,avatarID,zoneID,biomass,xCoor,yCoor,group_size,count):
        self.debugPrint("responseBirthAnimal")
        #find the mapping of the zone Id
        #create a instance of animalObject and add to self.listOfZones[zoneId]
        #listOfZones[zoneId]has instance of zoneID object
        zone = self.listOfZones[zoneID]

        if animal_id not in self.listOfAnimals:
            if name not in self.animalNameList:
                self.animalNameList[type] = name

            result = DatabaseHelper.dbSelectRowByID('animal', 'animal_id', modelID)

            if not result:
                result = DatabaseHelper.dbSelectRowByID('animal', 'animal_id', 999)

            model_dir = str(result['model_dir'])
            model_file = str(result['model_file'])
            animation = str(result['animation']).split(',')
            scale = float(result['scale'])

            animal = Animal3D(animal_id,name,type,avatarID,zoneID,biomass,model_dir,model_file,animation,scale)
            animal.reparentTo(zone)
            animal.setPos(xCoor, yCoor, zone.getElevation(xCoor, yCoor))
            animal.setStartPos(animal.getPos())
            animal.setGroupSize(group_size)

            if model_file == 'dummy':
                animal.setTexture(loader.loadTexture('models/shoppingcart/animal/' + name + '.jpg'), 1)

            zone.addAnimalToAI(animal)

            self.listOfAnimals[animal_id] = zoneID
        else:
            animal = zone.getAnimal(animal_id)
            animal.setGroupSize(group_size)

            zone.addMoreAnimal(animal, count)

        if status == 1:
            self.worldGui.floatingText.createText(Constants.TEXT_TYPE_BIRTH, '!', animal)
            self.worldGui.rightPendingText.createPendingText(Constants.TEXT_TYPE_BIRTH, name + ' [Birth]')
        elif status == 2:
            self.worldGui.floatingText.createText(Constants.TEXT_TYPE_MONEY, '$', animal)

#to be used with server    
    def resBirthAnimal(self,obj):
        self.debugPrint("resBirthAnimal")
        for key, value in obj.items(): # returns the dictionary as a list of value pairs -- a tuple.
            msg = key, value
            self.debugPrint(msg)

        status      = obj['status']
        animalID    = obj['animalID']
        name        = obj['name']
        modelID     = obj['modelID']
        animalTypeID= obj['animalTypeID']
        avatarID    = obj['avatarID']
        zoneID      = obj['zoneID']
        biomass     = obj['biomass']
        xCoor       = obj['xCoor']
        yCoor       = obj['yCoor']
        group_size  = obj['group_size']
        count       = obj['count']

        self.responseBirthAnimal(status,animalID,name,modelID,animalTypeID,avatarID,zoneID,biomass,xCoor,yCoor, group_size, count)

###############  ResponseBirthPlant #################################
#responseBirthPlant() method to be called by client Network
#Buy is success or failure,plantId,plantType, avatarId, zoneId, biomass
#client to create a instance of plant here
#if normal birth plant, randomly select x,y,z
#add plantId to listOfStaticObstacles[animalID] in the listOfZones[zoneId] object
#client to send server x,y,z for the plantId
    def responseBirthPlant(self,status,plantID,name,modelID,type,avatarID,zoneID,biomass,xCoor,yCoor, group_size,count):
        self.debugPrint("responseBirthPlant")
        #find the mapping of the zone Id
        #create a instance of plant object and add to self.listOfZones[zoneId]
        #listOfZones[zoneId]has instance of zoneID object
        zone = self.listOfZones[zoneID]

        if plantID not in self.listOfPlants:
            if name not in self.plantNameList:
                self.plantNameList[type] = name

            result = DatabaseHelper.dbSelectRowByID('plant', 'plant_id', modelID)

            if not result:
                result = DatabaseHelper.dbSelectRowByID('animal', 'animal_id', 999)

            model_dir = str(result['model_dir'])
            model_file = str(result['model_file'])
            animation = str(result['animation']).split(',')
            scale = float(result['scale'])

            plant = Plant3D(plantID, name, type, avatarID, zoneID, biomass, model_dir, model_file, animation, scale)
            plant.reparentTo(zone)
            plant.setPos(xCoor, yCoor, zone.getElevation(xCoor, yCoor))
            plant.setGroupSize(group_size)

            if model_file == 'dummy':
                plant.setTexture(loader.loadTexture('models/shoppingcart/plant/' + name + '.jpg'), 1)

            zone.addPlant(plant)

            self.listOfPlants[plantID] = zoneID
        else:
            plant = zone.getPlant(plantID)
            plant.setGroupSize(group_size)

            zone.addMorePlant(plant, count)

        if status == 1:
            self.worldGui.floatingText.createText(Constants.TEXT_TYPE_BIRTH, '!', plant)
            self.worldGui.rightPendingText.createPendingText(Constants.TEXT_TYPE_BIRTH, name + ' [Birth]')
        elif status == 2:
            self.worldGui.floatingText.createText(Constants.TEXT_TYPE_MONEY, '$', plant)

#to be used with server    
    def resBirthPlant(self,obj):
        self.debugPrint("resBirthPlant")
        for key, value in obj.items(): # returns the dictionary as a list of value pairs -- a tuple.
            msg = key, value
            self.debugPrint(msg)
        status      = obj['status']
        plantID     = obj['plantID']
        name        = obj['name']
        modelID     = obj['modelID']
        plantTypeID = obj['plantTypeID']
        avatarID    = obj['avatarID']
        zoneID      = obj['zoneID']
        biomass     = obj['biomass']
        xCoor       = obj['xCoor']
        yCoor       = obj['yCoor']
        group_size  = obj['group_size']
        count       = obj['count']

        self.responseBirthPlant(status,plantID,name,modelID,plantTypeID,avatarID,zoneID,biomass,xCoor,yCoor,group_size,count)

###############  RequestUpdateAnimalCoors #################################  
#requestUpdateAnimalCoors() sends animal coors to client network
#Client to send animal x, y, z to server  
#It will happen only after end of shop UI,end of player placing plant on terrain
#Also it will be called if animal changes zone
#parameters to send to server - animalID, zoneID, xCoor, yCoor 
    def requestAnimalCoors(self):
        self.debugPrint("requestAnimalCoors")
        #this function is triggered when the zone changes
        rContents = {'animalID': animalID, 'zoneID' : zoneID,'xCoor' : xCoor, 'yCoor' : yCoor}
        return None
    
###############  RequestUpdatePlantCoors  ################################# 
#requestUpdatePlantCoors() sends plant coors to client network 
#Client to send plant x, y, z to server  
#It will happen only after end of shop UI,end of player placing animal on terrain
#parameters to send to server - plantID, zoneID, xCoor, yCoor
    def requestPlantCoors(self):
        self.debugPrint("requestPlantCoors")
        return None    

#@hunvil - todo not sure what kind of animations to show    
###############  ResponseUpdateAnimalBiomass #################################     
#responseUpdateAnimalBiomass() will be called by client network
#The animal ID should increase its current biomass to targetBiomass in targetTime 
    def responseUpdateAnimalBiomass(self,obj):
        self.debugPrint("responseUpdateAnimalBiomass")
        animalID = obj['animalID']
        biomass = obj['biomass']
        targetBiomass = obj['targetBiomass']
        targetTime = obj['targetTime']
        zoneID = self.listOfAnimals[animalID]
        #depending upon the variation in biomass in targetTime, the animal should look skinnier or healthy
        #change the scale value currently
        #Function = biomass + amnt of interpol * (targetBiomass - biomass)
        interval = targetTime/4
        if (biomass < targetBiomass):  
            interpol1 = biomass + 0.25 * (targetBiomass - biomass)       #0.25
            interpol2 = biomass + 0.5 * (targetBiomass - biomass)        #0.5
            interpol3 = biomass + 0.75 * (targetBiomass - biomass)       #0.75
            interpol4 = targetBiomass
            
            taskMgr.doMethodLater(interval, self.setBiomassForAnimals,"biomass", extraArgs = [animalID,interpol1,0.1])
            taskMgr.doMethodLater(interval*2, self.setBiomassForAnimals,"biomass", extraArgs = [animalID,interpol2,0.25])
            taskMgr.doMethodLater(interval*3, self.setBiomassForAnimals,"biomass", extraArgs = [animalID,interpol3,0.4])
            taskMgr.doMethodLater(interval*4, self.setBiomassForAnimals,"biomass", extraArgs = [animalID,interpol4,0.5])
        elif(targetBiomass < biomass):
            interpol1 = targetBiomass + 0.25 * (biomass - targetBiomass)       #0.25
            interpol2 = targetBiomass + 0.5 * (biomass - targetBiomass)        #0.5
            interpol3 = targetBiomass + 0.75 * (biomass - targetBiomass)       #0.75
            interpol4 = biomass
            
            taskMgr.doMethodLater(interval, self.setBiomassForAnimals,"biomass", extraArgs = [animalID,interpol1,-0.2])
            taskMgr.doMethodLater(interval*2, self.setBiomassForAnimals,"biomass", extraArgs = [animalID,interpol2,-0.35])
            taskMgr.doMethodLater(interval*3, self.setBiomassForAnimals,"biomass", extraArgs = [animalID,interpol3,-0.5])
            taskMgr.doMethodLater(interval*4, self.setBiomassForAnimals,"biomass", extraArgs = [animalID,interpol4,-0.75])            
        return None
    
    def setBiomassForAnimals(self,animalID,biomass,scalePercentage):
        self.debugPrint("setBiomassForAnimals")
        if animalID in self.listOfAnimals:
            zoneID = self.listOfAnimals[animalID]
            self.listOfZones[zoneID].setAnimalBiomass(animalID,biomass,scalePercentage)
        return None

    def setBiomassForPlants(self,plantID,biomass,scalePercentage):
        self.debugPrint("setBiomassForPlants")
        if plantID in self.listOfPlants:
            zoneID = self.listOfPlants[plantID]
            self.listOfZones[zoneID].setPlantBiomass(plantID,biomass,scalePercentage)
        return None    
    
###############  ResponseUpdatePlantBiomass #################################     
#responseUpdatePlantBiomass() will be called by client network
#The plant ID should increase its current biomass to targetBiomass in targetTime 
    def responseUpdatePlantBiomass(self,obj):
        self.debugPrint("responseUpdatePlantBiomass")
        plantID =obj['plantID']
        biomass =obj['biomass']
        targetBiomass = obj['targetBiomass']
        targetTime = obj['targetTime']  
        zoneID = self.listOfPlants[plantID]   
        #depending upon the variation in biomass in targetTime, the plant should look skinnier or healthy
        #change the scale value currently
        interval = targetTime/4
        if (biomass < targetBiomass):  
            interpol1 = biomass + 0.25 * (targetBiomass - biomass)       #0.25
            interpol2 = biomass + 0.5 * (targetBiomass - biomass)        #0.5
            interpol3 = biomass + 0.75 * (targetBiomass - biomass)       #0.75
            interpol4 = targetBiomass
            
            taskMgr.doMethodLater(interval, self.setBiomassForPlants,"biomass", extraArgs = [plantID,interpol1,0.1])
            taskMgr.doMethodLater(interval*2, self.setBiomassForPlants,"biomass", extraArgs = [plantID,interpol2,0.25])
            taskMgr.doMethodLater(interval*3, self.setBiomassForPlants,"biomass", extraArgs = [plantID,interpol3,0.4])
            taskMgr.doMethodLater(interval*4, self.setBiomassForPlants,"biomass", extraArgs = [plantID,interpol4,0.5])
        elif(targetBiomass < biomass):
            interpol1 = targetBiomass + 0.25 * (biomass - targetBiomass)       #0.25
            interpol2 = targetBiomass + 0.5 * (biomass - targetBiomass)        #0.5
            interpol3 = targetBiomass + 0.75 * (biomass - targetBiomass)       #0.75
            interpol4 = biomass
            
            taskMgr.doMethodLater(interval, self.setBiomassForPlants,"biomass", extraArgs = [plantID,interpol1,-0.1])
            taskMgr.doMethodLater(interval*2, self.setBiomassForPlants,"biomass", extraArgs = [plantID,interpol2,-0.25])
            taskMgr.doMethodLater(interval*3, self.setBiomassForPlants,"biomass", extraArgs = [plantID,interpol3,-0.4])
            taskMgr.doMethodLater(interval*4, self.setBiomassForPlants,"biomass", extraArgs = [plantID,interpol4,-0.5])          
        return None    
    
#@hunvil - todo not sure what this method does
############### RequestUpdateAnimalTarget ###################################
#Request is from client to server
#parameters to send to server - animalId,zoneId,xTarg,yTarg
    def requestUpdateAnimalTarget(self):
        self.debugPrint("requestUpdateAnimalTarget")
        return None

############### ResponseUpdateAnimalNoWaterCount ###################################
#responseUpdateAnimalNoWaterCount() is called by client network
    def responseUpdateAnimalNoWaterCount(self,obj):
        self.debugPrint("responseUpdateAnimalNoWaterCount")
        animalID = obj['animalID']
        noWaterCount = obj['noWaterCOunt']
        zoneID = self.listOfAnimals[animalID]
        self.listOfZones[zoneID].setAnimalNoWaterCount(noWaterCount,animalID)
        return None
    
############### ResponseUpdatePlantNoWaterCount ###################################
#responseUpdatePlantNoWaterCount() is called by client network
    def responseUpdatePlantNoWaterCount(self,obj):
        self.debugPrint("responseUpdatePlantNoWaterCount")
        plantID = obj['plantID']
        noWaterCount = obj['noWaterCount']
        zoneID = self.listOfPlants[plantID]
        self.listOfZones[zoneID].setPlantNoWaterCount(noWaterCount,plantID)
        return None   
    
############### ResponseUpdatePlantNoLightCount ###################################
#responseUpdatePlantNoLightCount() is called by client network
    def responseUpdatePlantNoLightCount(self,obj):
        self.debugPrint("responseUpdatePlantNoLightCount")
        plantID     = obj['plantID']
        noLightCount = obj['noLightCount']
        zoneID = self.listOfAnimals[plantID]
        self.listOfZones[zoneID].setPlantNoLightCount(noLightCount,plantID)
        return None       

############### ResponseUpdateAnimalZone ###########################################
#responseUpdateAnimalZone() is called by client network
    def responseUpdateAnimalZone(self,obj):
        self.debugPrint("responseUpdateAnimalZone")
        #remember to update listOfAnimals[animalID] = newZOneID
        animalID = obj['animalID']
        newZoneID = obj['newZoneID']

        zoneID  = self.listOfAnimals[animalID]
        tempAnimalObject  = self.listOfZones[zoneID].getAnimal(animalID)
        tempAnimalObject.setZoneID(newZoneID)
        #cleanUp The animalObject from the old zone
        self.listOfZones[zoneID].killAnimal(animalID)
        #Add the tempAnimalObject to the new zone
        self.listOfZones[newZoneID].addAnimalObject(animalID, tempAnimalObject)
        self.listOfZones[newZoneID].addAnimalToAI(animalID, mass = 30, movt_force = 10, max_force = 20)
        #now add a new Animal to newZoneID
        self.listOfAnimals[animalID] = newZoneID

        #apply new zone-bound restriction
#        self.listOfZones[newZoneID].animals[animalID].setBoundaryRestrict(True)

        return None    
    
############### ResponseUpdateAnimalOwner ###########################################
#responseUpdateAnimalOwner() is called by client network
    def responseUpdateAnimalOwner(self,obj):
        self.debugPrint("responseUpdateAnimalOwner")
        animalID = obj['animalID']
        newAvatarID = obj['newAvatarID']
        #Step 1: find the zoneID of animalID
        zoneID = self.listOfAnimals[animalID]
        #Step 2: Update the owner of the animal
        self.listOfZones[zoneID].updateOwnerOfAnimal(animalID,newAvatarID)
        return None
    
############### ResponseKillAnimal    ################################################
#responseKillAnimal() is called by client network
    def responseKillAnimal(self, args):
        self.debugPrint("responseKillAnimal")

        animal_id = args['animalID']
        predator_id = args['predatorID']
        count = args['count']

        if animal_id in self.listOfAnimals:
            if predator_id != 0 and predator_id in self.listOfAnimals:
                zoneIDSourceAnimal = self.listOfAnimals[predator_id]
                zoneIDTargetAnimal = self.listOfAnimals[animal_id]

                if zoneIDSourceAnimal == zoneIDTargetAnimal:
                    predator = self.listOfZones[zoneIDSourceAnimal].getAnimal(predator_id)
                    target = self.listOfZones[zoneIDTargetAnimal].getAnimal(animal_id)

                    self.worldGui.rightPendingText.createPendingText(Constants.TEXT_TYPE_DEATH, predator.getName() + ' eats ' + target.getName())
                    self.worldGui.floatingText.createText(Constants.TEXT_TYPE_DAMAGE, '!', predator)
                    self.worldGui.floatingText.createText(Constants.TEXT_TYPE_LEVEL_UP, '!', target)

                    self.listOfZones[zoneIDSourceAnimal].attackAnimal(predator_id, animal_id, count)
            else:
                zone_id = self.listOfAnimals[animal_id]

                animal = self.listOfZones[zone_id].getAnimal(animal_id)
                animal.reduceGroupSize(count)

                if animal.getGroupSize() - count <= 0:
                    self.worldGui.rightPendingText.createPendingText(Constants.TEXT_TYPE_DEATH, animal.getName() + ' [Death]')

############### ResponseKillPlant    ################################################
#responseKillPlant() is called by client network
    def responseKillPlant(self, args):
        self.debugPrint( "responseKillPlant")

        plant_id = args['plantID']
        predator_id = args['predatorID']
        count = args['count']

        if plant_id in self.listOfPlants:
            if predator_id != 0 and predator_id in self.listOfAnimals:
                zoneIDAnimal = self.listOfAnimals[predator_id]
                zoneIDPlant = self.listOfPlants[plant_id]

                if zoneIDAnimal == zoneIDPlant:
                    predator = self.listOfZones[zoneIDAnimal].getAnimal(predator_id)
                    target = self.listOfZones[zoneIDPlant].getPlant(plant_id)

                    self.worldGui.rightPendingText.createPendingText(Constants.TEXT_TYPE_DEATH, predator.getName() + ' eats ' + target.getName())
                    self.worldGui.floatingText.createText(Constants.TEXT_TYPE_DAMAGE, '!', predator)
                    self.worldGui.floatingText.createText(Constants.TEXT_TYPE_LEVEL_UP, '!', target)

                    if not predator.isHunting:
                        self.listOfZones[zoneIDAnimal].attackPlant(predator_id, plant_id, count)
                    else:
                        target.reduceGroupSize(count)

                        if target.getGroupSize() - count <= 0:
                            self.worldGui.rightPendingText.createPendingText(Constants.TEXT_TYPE_DEATH, target.getName() + ' [Death]')
            else:
                zone_id = self.listOfPlants[plant_id]

                plant = self.listOfZones[zone_id].getPlant(plant_id)
                plant.reduceGroupSize(count)

                if plant.getGroupSize() - count <= 0:
                    self.worldGui.rightPendingText.createPendingText(Constants.TEXT_TYPE_DEATH, plant.getName() + ' [Death]')

#Not being used in v1 of the game
############### RequestGameScaleVote    ################################################    
#Client to send server the game scale vote for the avatarID
#Parameters to send to server are - avatarID, vote(1-10)    
    def requestGameScaleVote(self):
        self.debugPrint( "requestGameScaleVote")
        return None

################ ResponseShopAnimal #####################################################
#responseShopAnimal() is to be called by client network
    def responseShopListAnimal(self,obj):
        self.debugPrint( "responseShopListAnimal")
#        for animalList in obj:
#            print animalList
        #obj is of array of dictionary type
        for var in range(len(obj)):
            i = obj[var]        
            animalTypeID    = i['animalTypeID']
            animalType      = i['itemName']
            desc            = i['desc']    
            cost            = i['priceOfItem']
            predators       = i['predatorList']
            preys           = i['preyList']        
            maxBiomass      = i['biomass']
            mass            = i['mass']
            movementForce   = i['movement_force']
            maxForce        = i['max_force']
            model_id        = i['model_id']
            animalCategory  = i['animal_category']
            self.animalTypes[animalTypeID] = AnimalType(animalTypeID, animalType,desc, cost, maxBiomass, mass, movementForce, maxForce,predators,preys, model_id,animalCategory)        
            self.animalTypeId[animalType] = animalTypeID
            self.listOfAnimalTypes[animalTypeID] = animalType   
            self.listOfAnimalCount[animalTypeID] = 0    
            self.preyList[animalType] = preys
            self.predatorList[animalType] = predators
            if 'Herbivore' in animalCategory:
#                print 'Herbivore ',animalType
                self.herbivore.append(animalType)
            elif 'Carnivore' in animalCategory:
#                print 'Carnivore ',animalType
                self.carnivore.append(animalType)
            elif 'Omnivore' in animalCategory:
#                print 'Omnivore ',animalType
                self.omnivore.append(animalType)
                
        return None
    
    def getAnimalTypeID(self,animalType):
        if animalType in self.animalTypeId:
            return self.animalTypeId[animalType]
        
    def getListOfPreys(self,animalType):
        return self.preyList[animalType]
    
    def getListOfAnimalTypesByCategory(self,category):
        if category == 'Herbivore':
            return self.herbivore
        elif category == 'Carnivore':
            return self.carnivore
        elif category == 'Omnivore':
            return self.omnivore
        return 'None'
    
    def getListOfPlants(self):
        return self.plantList
    
################ ResponseShopPlant #####################################################
    #responseShopPlant() is to be called by client network    
    def responseShopListPlant(self,obj):
        self.debugPrint( "responseShopListPlant")
#        for animalList in obj:
#            print animalList        
        #obj is of array of dictionary type
        for var in range(len(obj)):
            i = obj[var]          
            plantTypeID    = i['plantTypeID']
            plantType      = i['itemName']
            description     = i['desc']    
            cost            = i['priceOfItem']
            maxBiomass      = None
            predators        = i['predatorList']
            model_id         = i['model_id']
            plantType.replace(' ', '')    
            self.plantTypes[plantTypeID] = PlantType(plantTypeID, plantType, description, cost, maxBiomass,predators,model_id)

            self.listOfPlantTypes[plantTypeID] = plantType 
            self.listOfPlantCount[plantTypeID] = 0 
            self.plantList.append(plantType)        
        return None        
 
############### ResponseUpdateWaterSource #################################################
    def updateWaterSource(self,obj):
        self.debugPrint( "updateWaterSource")
        waterSourceID     = obj['waterSourceID']
        zoneID            = obj['zoneID'] 
        waterAmount       = obj['waterAmount']
        targetWaterAmount = obj['targetWaterAmount']
        targetTime        = obj['targetTime']
        #if(waterAmount < targetWaterAmount) water level increases in targetTime
        #if(waterAmount > targetWaterAmount) water level decreases in targetTime
        #if self.gameMode == PvP, then one day cycle is 1 mins(1*60=60sec), 
        #if (targetTime<= 60 - 5) (there is a 5 second buffer to show the animations before day changes to night
            #t1 ===> (targetTime)/4    - every 15 second change the animation
        #if self.gameMode == PvE, then one day scale is 12 hours
        #if (targetTime <= 12*60*60 - 5*60) (there is a 5 min buffer to show the animations before day changes to night
            #t1 ===> (targetTime)/24    - every half an hour change the animation
        return None
 
    def responseOwnAvatarId(self,avatarID):
        self.debugPrint( "responseOwnAvatarId")
        #obj is of dictionary type
        self.avatarID = avatarID['ownAvatarID']       
        return None    

    def responseWaterSources(self,obj):
            
        #outer loop no of players
            #inner loop 6 zones for each player 
            #zoneID,x,y,z for all the players in the world
            #Refer to response water sources of Kelvin
        #obj is of array of dictionary type
        self.debugPrint( "responseWaterSources")
        msg = "Number of Players",len(obj)
        self.debugPrint(msg)   
        for var in range(len(obj)):
            i = obj[var]
            zoneID  = i['zoneID']
            x       = i['x']  
            y       = i['y']  
            z       = i['z']
            msg = "water zoneID-",zoneID
            self.debugPrint(msg)
            msg = "water x -",x
            self.debugPrint(msg)
            msg = "water y -",y
            self.debugPrint(msg)
            msg = "water z -",z
            self.debugPrint(msg)  
            #if the zone doesn't have water add water to the zone
            #upon request from server
            if(self.listOfZones[zoneID].hasWater == False):
                self.listOfZones[zoneID].addWater()

    def responseCreateEnvironment(self,args):
        self.debugPrint( "responseCreateEnvironment")

        for envInfo in args:
            env3D = Env3D(envInfo)
            env3D.reparentTo(render)

            size = len(self.listOfEnv)
            maxColumns = int(ceil(sqrt(size + 1)))
            env3D.setPos(size % maxColumns * 96, size / maxColumns * 96, 0)

            self.listOfEnv[env3D.getID()] = env3D
            
            for zone in env3D.getZones():
                self.listOfZones[zone.getID()] = zone
            
            self.avatarID = env3D.getAvatarID()
            self.envScore = env3D.getEnvironmentScore()
            self.listOfAvatars[self.avatarID] = env3D

            if env3D.getAvatarID() == self.ownAvatarID:
                self.worldGui.envScoreLabel.setCounterText(self.envScore)
                #highlight the user's env
                env3D.sethighlight()
            self.responseUpdateInfo(self.scoreInfo)

    def responseCreateEnv(self, args):

        env3D = Env3D(args)
        env3D.reparentTo(render)

        size = len(self.listOfEnv)
        maxColumns = int(ceil(sqrt(size + 1)))
        env3D.setPos(size % maxColumns * 96, size / maxColumns * 96, 0)

        self.listOfEnv[env3D.getID()] = env3D

        for zone in env3D.getZones():
            self.listOfZones[zone.getID()] = zone

        self.listOfAvatars[self.avatarID] = env3D

    def responseUpdateTime(self, args):
        self.currentDay = args['month']
        self.timeRate = args['rate']
        self.currentYear = args['year']
        
        self.worldGui.setMonth(args['month'])
        self.worldGui.setYear(args['year'])
        self.worldGui.setTime(args['current'], args['duration'], args['rate'])
  
    def responseUpdateLevel(self, args):
        self.debugPrint( "responseUpdateLevel")
        self.avatarObj.updateLevel(args['level'])

        self.worldGui.expBar.setRangeList(args['range'])

    def responseUpdateXP(self, args):
        self.debugPrint( "responseUpdateXP")
        self.avatarObj.updateXP(args['total'])

        self.worldGui.expBar.setCurrentValue(args['amount'])

        if args['amount'] != 0:
            self.worldGui.leftPendingText.createPendingText(Constants.TEXT_TYPE_EXPERIENCE, '+' + str(args['amount']) + ' Exp')

    def responseUpdateGold(self, args):
        self.debugPrint( "responseUpdateGold")
        self.avatarObj.updateGold(args['gold'])

        self.worldGui.goldLabel.setCounterValue(args['gold'])

        if args['amount'] != 0:
            self.worldGui.leftPendingText.createPendingText(Constants.TEXT_TYPE_MONEY, '+' + str(args['amount']) + ' Gold')

    def responseUpdateEnvScore(self, args):
        self.debugPrint( "responseUpdateEnvScore")
        #parse the contents from List received from Network
        env_id =  args['env_id']
        envScore =  args['score']       
        #Get the environment object associated with the avatar ID and update that environment score
        env3D = self.listOfEnv[env_id]

        if envScore != env3D.getEnvironmentScore():
            self.worldGui.setEnvScoreStatus(envScore > env3D.getEnvironmentScore())
        self.worldGui.envScoreLabel.setCounterValue(envScore)

        env3D.setEnvrionmentScore(envScore)

    def responseUpdateInfo(self, args):
        self.debugPrint( "responseUpdateInfo")

        avatar_id = args['avatar_id']
        Constants.AVATAR_ID = avatar_id

        self.avatarObj.updateLevel(args['level'])
        self.worldGui.levelLabel['text'] = str(args['level'])

        self.avatarObj.updateXP(args['xp'])
        self.worldGui.expBar.setInitialValue(args['xp'] - args['min_exp'], args['max_exp'])

        self.avatarObj.updateGold(args['gold'])
        self.worldGui.goldLabel['text'] = str(args['gold'])
                
#requestWaterSources() calls the client network to send water source info to server        
    def requestWaterSources(self):
        self.debugPrint( "requestWaterSources")
        rContents = []
        contents = {}
        for index in range(len(self.waterSourceArray)):
            msg = index," - ",self.waterSourceArray[index]
            self.debugPrint(msg)
            zoneID = self.waterSourceArray[index]
            #send to server the dictionary of zoneID, x,y,z
            self.listOfZones[zoneID].addWater()
            contents = { 'zoneID' : zoneID,
                         'x'      : 256,
                         'y'      : 256,
                         'z'      : 0 }
            
            rContents.append(contents)

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
            pickArr.append(tempArr[int(round((len(tempArr) - 1) * random()))])
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
    
    def moveAnimal(self, animalId, target, targetZoneID):
        msg =  "moveAnimal ",animalId, "***"
        self.debugPrint(msg)
        self.listOfZones[self.listOfAnimals[int(animalId)]].migrate(int(animalId),target,targetZoneID, self)


    def callUpdateWaterSource(self,zoneID,newWaterLevel):
        self.debugPrint( "callUpdateWaterSource")
        self.listOfZones[zoneID].setWaterHeight(newWaterLevel)
        return None
        
    def responseRevealAnimalDisease(self,obj):
        self.debugPrint( "responseRevealAnimalDisease")
        animalID = obj['animalID']
        diseaseID = obj['diseaseID']
        #find the zone where animalID lives in
        zoneID = self.listOfAnimals[animalID]
        self.listOfZones[animalID].revealAnimalDisease(animalID,diseaseID)
        return None
    
    def responseCureAnimalDisease(self,obj):
        self.debugPrint( "responseCureAnimalDisease")
        animalID = obj['animalID']
        diseaseID = obj['diseaseID']
        #find the zone where animalID lives in
        zoneID = self.listOfAnimals[animalID]
        self.listOfZones[animalID].cureAnimalDisease(animalID,diseaseID)               
        return None
    
    def responseRevealPlantDisease(self,obj):
        self.debugPrint( "responseRevealPlantDisease")
        plantID = obj['plantID']
        diseaseID = obj['diseaseID']
        #find the zone where plantID lives in
        zoneID = self.listOfPlants[plantID]
        self.listOfZones[plantID].revealPlantDisease(plantID,diseaseID)
        return None
    
    def responseCurePlantDisease(self,obj):
        self.debugPrint( "responseCurePlantDisease")
        plantID = obj['plantID']
        diseaseID = obj['diseaseID']
        #find the zone where plantID lives in
        zoneID = self.listOfAnimals[plantID]
        self.listOfZones[plantID].cureAnimalDisease(plantID,diseaseID)               
        return None
    
    def weatherPrediction(self,obj):
        self.debugPrint( "weatherPrediction")
        self.day = obj['day']
        self.lightOutput = obj['lightOutput']
        self.rainOutput  = obj['rainOutput']
        
        #Who is handling this?
        #rain has to be called for whole world
        if(self.rainOutput == 1):
            taskMgr.add(self.rainTaskFunc, 'RainTask')
        elif(self.rainOutput == 0):
            taskMgr.add(self.stopRainTaskFunc, 'StopRainTask')
        if(self.lightOutput >= 0.75 or self.lightOutput <=1):
            self.worldGui.world.lightEffect = 'night'       #assuming it to be darker
        elif(self.lightOutput >= 0.5 or self.lightOutput<0.75):
            self.worldGui.world.lightEffect = 'evening'       #assuming it to be semi dark
        else:
            self.worldGui.world.lightEffect = None
    # A task that runs forever???????
    def rainTaskFunc(self,task):
        self.debugPrint( "rainTaskFunc")
        self.worldGui.rainEffects('rain')
        return task.done
         
    def stopRainTaskFunc(self,task):
        self.debugPrint( "stopRainTaskFunc")
        self.debugPrint( "Stop-rain called")
        self.worldGui.rainEffects('stop-rain')
        return task.done

    def getGameState(self):
        return self
  
    def getStatistics(self):
        self.statistics = []
        #go through each zone, for each zone of self.avatarID,
        if self.avatarID is not None and self.listOfAvatars.__len__()!=0:
            ownZones = self.listOfAvatars[self.avatarID].getZoneIDs()    #ownZones is an array/list
            #iterate through the list of avatar's zones
            for zone in ownZones:
                for animalType in self.listOfAnimalCount:
                    self.listOfAnimalCount[animalType] = 0            
                #get the list of all animals in one zone
                listOfAnimalsInZone = self.listOfZones[zone].getListOfAnimals()
                #iterate through the list of animals
                for animalID in listOfAnimalsInZone:
                    #get the animalType for each animal Object
                    animalType = self.listOfZones[zone].getAnimalType(animalID)
                    #increment the count for each animal Type to 1
                    if animalType is not None and self.listOfAnimalCount.__len__()!=0:
                        self.listOfAnimalCount[animalType] = self.listOfAnimalCount[animalType] + 1
                for animalType in self.listOfAnimalCount:
                    count = self.listOfAnimalCount[animalType]
                    if (count != 0):
                        tuple = (zone,self.listOfAnimalTypes[animalType],count)
                        self.statistics.append(tuple)  

                for plantType in self.listOfPlantCount:
                    self.listOfPlantCount[plantType] = 0            
                #get the list of all plants in one zone
                listOfPlantsInZone = self.listOfZones[zone].getListOfPlants()
                #iterate through the list of plants
                for plantID in listOfPlantsInZone:
                    #get the plantType for each plant Object
                    plantType = self.listOfZones[zone].getPlantType(plantID)
                    #increment the count for each plant Type to 1
                    if plantType is not None and self.listOfPlantCount.__len__() != 0:
                        self.listOfPlantCount[plantType] = self.listOfPlantCount[plantType] + 1
                for plantType in self.listOfPlantCount:
                    count = self.listOfPlantCount[plantType]
                    if (count != 0):
                        tuple = (zone,self.listOfPlantTypes[plantType],count)
                        self.statistics.append(tuple) 
        return self.statistics
    
    def getUniqueZoneID(self,envID,zoneID):
        uniqueZoneID = self.listOfEnv[envID].getUniqueZoneID(zoneID)
        return uniqueZoneID
    
    def debugPrint(self,msg):
        if self.debugMode == 'ON':
            print msg
        return
    
    def getAnimalName(self,animalID):
        zoneID = self.listOfAnimals[animalID]
        animalName= None
        if zoneID is not None:
            animalType = self.listOfZones[zoneID].getAnimalType(animalID)
            if animalType is not None and (self.listOfAnimalTypes.__len__() != 0) :
                animalName = self.listOfAnimalTypes[animalType]
        return animalName
    
    def getPlantName(self,plantID):
        zoneID = self.listOfPlants[plantID]
        plantType = None
        if zoneID is not None:
            plantType = self.listOfZones[zoneID].getPlantType(plantID)
            if plantType is not None and (self.listOfPlantTypes.__len__()!=0):
                plantName = self.listOfPlantTypes[plantType]
        return plantName   
    
    def getAnimalNameAndCount(self,animal_ID):
        if animal_ID is not None and self.listOfAnimals.__len__()!=0:
            zoneID = self.listOfAnimals[animal_ID]
            if zoneID is not None:
                animal_Type = self.listOfZones[zoneID].getAnimalType(animal_ID)
                if animal_Type is not None and self.listOfAnimalTypes.__len__()!=0:
                    animalName = self.listOfAnimalTypes[animal_Type]
            
                    for animalType in self.listOfAnimalCount:
                        self.listOfAnimalCount[animalType] = 0            
                    #get the list of all animals in one zone
                    listOfAnimalsInZone = self.listOfZones[zoneID].getListOfAnimals()
                    #iterate through the list of animals
                    for animalID in listOfAnimalsInZone:
                        #get the animalType for each animal Object
                        animalType = self.listOfZones[zoneID].getAnimalType(animalID)
                        #increment the count for each animal Type to 1
                        self.listOfAnimalCount[animalType] = self.listOfAnimalCount[animalType] + 1
            
                    count = self.listOfAnimalCount[animal_Type]        
                    return animalName + '(' + str(count) + ')'
            

    def getPlantNameAndCount(self,plant_ID):
        if plant_ID is not None and self.listOfPlants.__len__()!=0:
            zoneID = self.listOfPlants[plant_ID]
            if zoneID is not None:
                plant_Type = self.listOfZones[zoneID].getPlantType(plant_ID)
                if plant_Type is not None and self.listOfPlantTypes.__len__()!=0:
                    plantName = self.listOfPlantTypes[plant_Type]
            
                    for plantType in self.listOfPlantCount:
                        self.listOfPlantCount[plantType] = 0            
                    #get the list of all plants in one zone
                    listOfPlantsInZone = self.listOfZones[zoneID].getListOfPlants()
                    #iterate through the list of plants
                    for plantID in listOfPlantsInZone:
                        #get the plantType for each plant Object
                        plantType = self.listOfZones[zoneID].getPlantType(plantID)
                        #increment the count for each plant Type to 1
                        self.listOfPlantCount[plantType] = self.listOfPlantCount[plantType] + 1
            
                    count = self.listOfPlantCount[plant_Type]        
                    return plantName + '(' + str(count) + ')'
                
                