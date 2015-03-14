from common.Constants import Constants
from main.MainLobby.World.World3D.SpeciesType import SpeciesType

class PlantType:

    def __init__(self, plantTypeID, plantType, desc, cost, maxBiomass,predatorList,model_id):

        self.plantTypeID         = plantTypeID;
        self.plantType           = plantType
        self.description         = desc
        self.cost                = cost
        self.maxBiomass          = maxBiomass
        self.plantPredators = []
        self.model_id            = model_id
        
    def getPlantTypeID(self):
        return self.plantTypeID
    
    def getPlantType(self):
        return self.plantType
    
    def getDescription(self):
        return self.description
    
    def getCost(self):
        return self.cost
    
    def getMaxBiomass(self):
        return self.maxBiomass
    
    def getPlantPredatorList(self):
        return self.plantPredators

    def getModelID(self):
        return self.model_id
