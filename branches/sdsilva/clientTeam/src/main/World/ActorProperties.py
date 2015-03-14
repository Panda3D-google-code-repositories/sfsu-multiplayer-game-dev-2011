#@PydevCodeAnalysisIgnore
'''
Created on Oct 28, 2011

@author: hunvil
'''
import direct.directbase.DirectStart
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
        self.pursueStart = False
        self.pursueComplete = False
        
    def getActor(self):
        return self.actor
    
    def getActorHeight(self):
        return self.actorHeight  