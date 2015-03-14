'''
Created on Nov 13, 2011

@author: lloyd
'''
from ActorProperties import ActorProperties
from direct.actor.Actor import Actor
from direct.task.Task import Task
from panda3d.ai import *
from pandac.PandaModules import PandaNode, NodePath
import direct.directbase.DirectStart
from common.Constants import Constants
from pandac.PandaModules import CollisionTraverser
from pandac.PandaModules import CollisionHandlerQueue, CollisionNode, BitMask32
from pandac.PandaModules import CollisionPlane, CollisionSphere, CollisionRay
from pandac.PandaModules import Plane, Vec3, Point3
import random


class Animal3D:
    i = 3
    def __init__(self,actorName,root,terrain,dummy,skybox,startPosX,startPosY,animal):
        self.keyMap = {"left":0, "right":0, "forward":0, "back":0, "invert-y":0, "mouse":0 } 
        self.animal = animal
        self.actorName = actorName 
        self.actorModel = None
        self.actorHeight = 0
        self.actorHead = None
        self.actorProperties=None
        self.skybox = skybox
        self.setModels()
        self.object_id = Animal3D.i #should be animal_instanceID
        Animal3D.i=Animal3D.i+1
        self.createActor(root,terrain,dummy,startPosX,startPosY)
 
    def setModels(self):        
        modelName = "models/" + self.actorName + "/" + self.actorName;
        walk = self.actorName +"-walk";
        walkAnim = "models/"+ self.actorName+"/"+self.actorName+"-walk";
        die = self.actorName +"-die";
        dieAnim = "models/"+ self.actorName+"/"+self.actorName+"-die";        
        self.actorModel = Actor(modelName,
                                 {walk:walkAnim,
                                  die:dieAnim})  
        
    def getActorHeight(self):
        return self.actorHeight
       
    def getActorName(self):
        return self.actorName
    
    def getActorModel(self):
        return self.actorModel
    
    def getActorProperties(self):
        return self.actorProperties
    
    def getActorHead(self):
        return self.actorHead
                 
    def createActor(self,root,terrain,dummy,startPosX,startPosY):
        self.terrain = terrain
        self.dummy = dummy
        startPosZ = self.terrain.getElevation(startPosX, startPosY) * root.getSz()
        self.actorModel.reparentTo(self.dummy)
        self.actorModel.setScale(2)
        self.actorModel.setPos(startPosX, startPosY, startPosZ)
        print startPosX, startPosY , startPosZ
        self.actorHeight = 1.2  # to locate the top of elephant's head for the camera to point at        
        self.actorProperties = ActorProperties(self.actorName,self.actorHeight,startPosX,startPosY,startPosZ)
        
        self.actorHead = NodePath(PandaNode(self.actorName + "Head"))
        self.actorHead.reparentTo(self.dummy) 
        self.actorModel.setCollideMask(Constants.CLICKABLE_MASK)
        self.actorModel.setTag('type', str('Animal'))
        self.actorModel.setTag('object_id', str(self.object_id))
#        self.setAI(self.actorModel)
        
    def setAI(self, actorModel):
        self.AIworld = AIWorld(render)
        self.AIchar1 = AICharacter("actor",actorModel, 30, 5, 5)
        self.AIworld.addAiChar(self.AIchar1)
        
        self.AIbehaviors1 = self.AIchar1.getAiBehaviors()
        
        self.AIbehaviors1.wander(2, 0, 5, 1.0)
        
        self.actorModel.loop("walk")
        taskMgr.add(self.AIUpdate,"AIUpdate")
        
    def AIUpdate(self,task):
        self.AIworld.update()    
        self.move(self.actorModel, self.actorProperties, self.actorHead, task)       
        return Task.cont
        
    def move(self, actor, actorProperties, actorHead, task):
        self.actor = actor
        self.actorProperties = actorProperties
        self.actorHeight = self.actorProperties.actorHeight
        self.actorHead = actorHead
        elapsed = task.time - self.actorProperties.prevtime

        startpos = self.actor.getPos()

        self.actorProperties.steps = self.actorProperties.steps + 1 
        if self.actorProperties.steps%1000 == 0 :
            self.actorProperties.direction = self.actorProperties.direction +90
        self.actor.setHpr(self.actorProperties.direction,0,0)
        self.actor.setY(self.actor, -0.03*25)

        if self.actorProperties.isMoving is False:
            if (self.keyMap["forward"]!=0) or (self.keyMap["left"]!=0) \
            or (self.keyMap["right"]!=0):
                self.actor.loop(self.actorName+"-walk")
            else:
                self.actor.setPlayRate(-1, self.actorName+"-walk")
                self.actor.loop(self.actorName+"-walk")
            self.actorProperties.isMoving = True
        else:
            if self.actorProperties.isMoving:
                self.actor.stop()
                self.actor.pose(self.actorName+"-walk",5)
                self.actorProperties.isMoving = False

        x = self.actor.getX()
        y = self.actor.getY()
        z = self.terrain.getElevation(x,y)*self.terrain.getRoot().getSz()
        if z< 40 :
            z = 41        
        modelZone = self.animal.getZoneId()
        modelEnv = self.animal.getEnvId()
        print modelZone
        print modelEnv
        id = self.getZoneEnvId(x,y)
        
        if((id['zoneId']!=modelZone)):
            print "here1"
            if((id['envid']!=modelEnv)):
                print "here2"
                self.actor.setH(90)
        
        diff = self.actorProperties.previousZ - z
        
        #Multiplication factor for uphill and downhill
        self.actor.setP(diff*20)
        
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
    
    
    def getZoneEnvId(self,xCoor,yCoor):
        self.Id = {}
        self.zoneId = 0
        ENVIRONMENT_SIZE = 512 * 2
        zoneId = None
        envId = None
        ids = {}
        
        j = int(xCoor/(ENVIRONMENT_SIZE))
        i = int(yCoor/(ENVIRONMENT_SIZE))
        envId = (j*10) +(i+1)
        
        zoneX_1 = j *(ENVIRONMENT_SIZE)               #top left corner x,y
        zoneY_1 = i *(ENVIRONMENT_SIZE)
        
        zoneX_2 = j *(ENVIRONMENT_SIZE) + (512 *2)    #top right corner x,y
        zoneY_2 = i *(ENVIRONMENT_SIZE)
        
        zoneX_3 = j *(ENVIRONMENT_SIZE)               #bottom left corner x,y
        zoneY_3 = i *(ENVIRONMENT_SIZE) + (512 *2)
        
        zoneX_4 = j *(ENVIRONMENT_SIZE)+ (512 *2)     #bottom right corner x,y
        zoneY_4 = i *(ENVIRONMENT_SIZE)+ (512 *2)
        
        
        for j in range(2):
            envXStart = zoneX_1
            envYStart = zoneY_1 + (512*j)
            for i in range(2):
                zone0_X1 = envXStart
                zone0_Y1 = envYStart
                
                zone0_X2 = envXStart + 512
                zone0_Y2 = envYStart
                
                zone0_X3 = envXStart  
                zone0_Y3 = envYStart + 512
                
                zone0_X4 = envXStart + 512
                zone0_Y4 = envYStart + 512
                
                #do the comparision here, if it falls within the four boundaries
                #then it belongs to the zone and break, else continue through all nine zones
                if(xCoor>zone0_X1 and xCoor<zone0_X2):
                    if(yCoor>zone0_Y1 and yCoor<zone0_Y3):
                        zoneId = i + j*2
                        print "zone", zoneId
                envXStart = zone0_X2
                envYStart = zone0_Y2
        ids['zoneId'] = zoneId
        ids['envid'] = envId 
        return ids