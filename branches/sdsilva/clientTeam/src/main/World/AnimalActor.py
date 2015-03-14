#@PydevCodeAnalysisIgnore
'''
Created on Oct 28, 2011

@author: hunvil
'''
import direct.directbase.DirectStart
from ActorProperties import ActorProperties
from direct.actor.Actor import Actor
from direct.task.Task import Task
from pandac.PandaModules import PandaNode,NodePath

class Animal:
    def __init__(self,actorName,root,terrain,dummy,skybox,startPosX,startPosY):
       self.keyMap = {"left":0, "right":0, "forward":0, "back":0, "invert-y":0, "mouse":0 } 
       self.actorName = actorName 
       self.actorModel = None
       self.actorHeight = 0
       self.actorHead = None
       self.actorProperties=None
       self.skybox = skybox
       self.setModels()
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
        self.actorModel.setScale(.9)
        self.actorModel.setPos(startPosX, startPosY, startPosZ)
        self.actorHeight = 1.2  # to locate the top of elephant's head for the camera to point at        
        self.actorProperties = ActorProperties(self.actorName,self.actorHeight,startPosX,startPosY,startPosZ)
        
        self.actorHead = NodePath(PandaNode(self.actorName + "Head"))
        self.actorHead.reparentTo(self.dummy) 
        
    def move(self, actor, actorProperties, actorHead, task):
        self.actor = actor
        self.actorProperties = actorProperties
        self.actorHeight = self.actorProperties.actorHeight
        self.actorHead = actorHead
        elapsed = task.time - self.actorProperties.prevtime
        startpos = self.actor.getPos()

        self.actorProperties.steps = self.actorProperties.steps + 1 
        if self.actorProperties.steps%20 == 0 :
            self.actorProperties.direction = self.actorProperties.direction +90
        self.actor.setHpr(self.actorProperties.direction,0,0)
        self.actor.setY(self.actor, -elapsed*25)

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