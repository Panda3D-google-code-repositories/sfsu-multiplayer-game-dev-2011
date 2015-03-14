from common.Constants import Constants
class Plant3D():
    def __init__(self):
        if Constants.DEBUG:
            print 'creating plant'        
        self.models = []
        self.healthy = True
        self.x = 0
        self.y = 0
        self.zone = None
        
    def tree(self, myzone, x, y,modelPath,scaleValue):
        #self.models.append(loader.loadModel("models/bigTree/bigTree"))
        print "Plant Model Path is ",modelPath
        self.plantModel = loader.loadModel(modelPath)
        self.models.append(loader.loadModel(modelPath))
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
    
    def getPlantModel(self):
        return self.plantModel