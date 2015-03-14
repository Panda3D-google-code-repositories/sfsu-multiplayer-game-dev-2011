"""Ai module: contains the Ai class"""
#__all__ = ['Ai']

#for Pandai
from panda3d.ai import *

#for tasks
from direct.task import Task
class Ai:
    def __init__(self, render):
        #self.initAI(render)
        self.AIworld = AIWorld(render)
        self.dicBehaviors = {}  #List of all the animal behaviors
    
    #
    #   This function must to be called when the game start,
    #   Add to the AIworld all the models of the list     
    #def initAI(self,render):
    
    def addAnimal(self, id, model):
        self.AIchar = AICharacter(id, model, 100, 0.05, 5)
        self.AIworld.addAiChar(self.AIchar)
        self.AIbehavior = self.AIchar.getAiBehaviors()
        self.AIbehavior.wander(5, 0, 10, 1.0)
        #self.addObstacles()
        #self.dicBehaviors[id:self.AIbehavior]
        
    def AIupdate(self,task):
        self.AIworld.update()
        return Task.cont
    
    #def addObstacles(self, id):
        
    def seek(self, id, target):
        self.dicBehaviors[id].seek(target,0.5)
        
    #def deleteAnimal(self, id):
    
    #def pathfinding(self):
    
    #def seekAnimal(self):