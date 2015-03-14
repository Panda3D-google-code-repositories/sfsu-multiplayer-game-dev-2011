from common.Constants import Constants
from direct.actor.Actor import Actor
from pandac.PandaModules import ClockObject
from direct.task import Task

class Animal3D():
    def __init__(self):
        if Constants.DEBUG:
            print 'creating animal'        
        self.models = []
        self.healthy = True
        self.x = 0
        self.y = 0
        self.zone = None
        self.modelPath = None
        self.modelAnimation = None
        self.actor = None
        
    def animal(self, myzone, x, y,modelPath,modelAnimation,scaleValue):
        print "Animal Model Path is- ",modelPath
        print "Animal Model Animations are- ",modelAnimation
        self.actor = Actor(modelPath,modelAnimation)         
        self.models.append(self.actor)
        self.models[0].reparentTo(render)
        self.models[0].setScale(scaleValue)
        self.x = x
        self.y = y
        self.zone = myzone
        self.terrain = self.zone.terrain
        self.root = self.zone.root
        self.models[0].setX(self.zone.getX(self.x))
        self.models[0].setY(self.zone.getY(self.y))
        self.models[0].setZ(self.terrain.getElevation(self.x,self.y)*50)
        #print "tree in zone " + str(self.zone.x) + ", " + str(self.zone.y)
        return self
    
    def getActor(self):
        return self.actor

    