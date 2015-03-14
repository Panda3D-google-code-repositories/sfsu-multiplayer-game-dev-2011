#@PydevCodeAnalysisIgnore
'''
Created on Nov 9, 2011

@author: hunvil
'''
from direct.actor.Actor import Actor
from common.Constants import Constants
#for Pandai
from panda3d.ai import *
class Models():
    def __init__(self):
        if Constants.DEBUG:
            print 'Creating Model Paths and Animations List'
        self.modelAnimationsList = {}
        self.plantModels ={}
        self.scaleValues = {}
        self.setAnimalModels()
        self.setPlantModels()
        self.setScaleValues()
        
    def setScaleValues(self):
        self.scaleValues['elephant'] = 0.9
        self.scaleValues['cheetah'] =  3
        self.scaleValues['caracal'] = 3
        self.scaleValues['bigTree'] = 1
        self.scaleValues['boabab_L'] = 4
        self.scaleValues['boabab_NL'] =None
        self.scaleValues['ralph'] = None
        self.scaleValues['sparrow']=None
        self.scaleValues['vulture']=None
        self.scaleValues['giraffe']=None
        self.scaleValues['wildebeest']=None
        self.scaleValues['zebra']=None
        self.scaleValues['lion']=None
               
    def setPlantModels(self):
        self.plantModels['bigTree'] = "models/bigTree/bigTree"
        self.plantModels['boabab_L'] = "models/trees/with_leaves/baobabtree"
        self.plantModels['boabab_NL'] = "models/trees/without_leaves/baobabtree"
        
    def setAnimalModels(self):
        #list of modelnames, animations
        
        ############### Models with 2 kinds of animations
        self.modelAnimationsList['ralph'] = ("models/ralph/ralph",
                                               {"ralph-run":"models/ralph/ralph-run",
                                                "ralph-walk":"models/ralph/ralph-walk"})  
        
        ############### Birds goes here
        
        self.modelAnimationsList['sparrow'] = ("models/sparrow/sparrow",
                                               {"sparrow-walk":"models/sparrow/sparrow-walk",
                                                "sparrow-die":"models/sparrow/sparrow-die",
                                                "sparrow-peck":"models/sparrow/sparrow-peck",
                                                "sparrow-flap":"models/sparrow/sparrow-flap"})
        
        self.modelAnimationsList['vulture'] = ("models/vulture/vulture",
                                               {"vulture-walk":"models/vulture/vulture-walk",
                                                "vulture-die":"models/vulture/vulture-die",
                                                "vulture-peck":"models/vulture/vulture-peck",
                                                "vulture-flap":"models/vulture/vulture-flap"})
            
        ############### Animals with 3 kinds of animations
        self.modelAnimationsList['elephant'] = ("models/elephant/elephant",
                                               {"elephant-walk":"models/elephant/elephant-walk",
                                                "elephant-die":"models/elephant/elephant-die",
                                                "elephant-eat":"models/elephant/elephant-eat"})
        
        self.modelAnimationsList['giraffe'] = ("models/giraffe/giraffe",
                                               {"giraffe-walk":"models/giraffe/giraffe-walk",
                                                "giraffe-die":"models/giraffe/giraffe-die",
                                                "giraffe-eat":"models/giraffe/giraffe-eat"})
 
        self.modelAnimationsList['wildebeest'] = ("models/wildebeest/wildebeest",
                                               {"wildebeest-walk":"models/wildebeest/wildebeest-walk",
                                                "wildebeest-die":"models/wildebeest/wildebeest-die",
                                                "wildebeest-eat":"models/wildebeest/wildebeest-eat"})
        
        self.modelAnimationsList['zebra'] = ("models/zebra/zebra",
                                               {"zebra-walk":"models/zebra/zebra-walk",
                                                "zebra-die":"models/zebra/zebra-die",
                                                "zebra-eat":"models/zebra/zebra-eat"})               
        ############### Animal with 4 kinds of animations
        self.modelAnimationsList['caracal'] = ("models/caracal/caracal",
                                               {"caracal-walk":"models/caracal/caracal-walk",
                                                "caracal-die":"models/caracal/caracal-die",
                                                "caracal-eat":"models/caracal/caracal-eat",
                                                "caracal-attack":"models/caracal/caracal-attack"})
        
        self.modelAnimationsList['cheetah'] = ("models/cheetah/cheetah",
                                               {"cheetah-walk":"models/cheetah/cheetah-walk",
                                                "cheetah-die":"models/cheetah/cheetah-die",
                                                "cheetah-eat":"models/cheetah/cheetah-eat",
                                                "cheetah-attack":"models/cheetah/cheetah-attack"})
        
        self.modelAnimationsList['lion'] = ("models/lion/lion",
                                               {"lion-walk":"models/lion/lion-walk",
                                                "lion-die":"models/lion/lion-die",
                                                "lion-eat":"models/lion/lion-eat",
                                                "lion-attack":"models/lion/lion-attack"})
        
    def getModelAnimationsList(self):
        return self.modelAnimationsList
    
    def getModelNameAndAnimation(self,animal):
        return self.modelAnimationsList[animal] #returns the modelPath and animations
    
    def getModelName(self,animal):
        return self.modelAnimationsList[animal][0]
    
    def getModelAnimation(self,animal):
        return self.modelAnimationsList[animal][1]