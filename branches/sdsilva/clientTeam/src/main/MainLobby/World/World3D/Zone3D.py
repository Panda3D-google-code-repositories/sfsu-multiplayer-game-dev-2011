#@PydevCodeAnalysisIgnore
from panda3d.core import Texture, TextureStage
from pandac.PandaModules import PandaNode,NodePath
from pandac.PandaModules import Filename
from pandac.PandaModules import GeoMipTerrain
from direct.showbase.DirectObject import DirectObject
from panda3d.core import Vec4

from common.Constants import Constants
from main.MainLobby.World.World3D.Plant3D import Plant3D
from main.MainLobby.World.World3D.Animal3D import Animal3D
from main.MainLobby.World.World3D.MyGeoMipTerrain import MyGeoMipTerrain
from pandac.PandaModules import CollisionTraverser
from pandac.PandaModules import CollisionHandlerQueue, CollisionNode, BitMask32
from pandac.PandaModules import CollisionPlane, CollisionSphere, CollisionRay

class Zone3D():
    def __init__(self,zoneId):
        if Constants.DEBUG:
            print 'creating zone ' + str(zoneId)
        self.zoneId = zoneId
        self.xoff = 0
        self.yoff = 0
        self.size = 513
        self.playerBuffer = 5
        self.plants = []
        self.grasses = []
        self.animals = []
        self.root = render.attachNewNode('root')
        self.object_id = "2"
        
        self.zoneRender = NodePath(PandaNode("zoneRender"))
        self.zoneRender.setPos(-200,50,-150)
        self.zoneRender.reparentTo(render)   
        
    def getZoneRender(self):
        return self.zoneRender
                
    def addTree(self):
        p = Plant3D()
        self.plants.append(p.tree(self, 100, 356))
    def moveDown(self):
        self.terrain.setY(self.y-self.size)
        self.y-= self.size
    def moveRight(self):
        self.terrain.setX(self.x+self.size)
        self.x+= self.size
    def getX(self,x):
        return (x*self.size)+(self.size*3*self.xoff)+(self.xoff*self.playerBuffer)
    def getY(self,y):
        return (y*self.size)+(self.size*3*self.yoff)+(self.yoff*self.playerBuffer)
    def move(self,x,y):
        self.x = self.getX(x)
        self.y = self.getY(y)
        self.terrain.getRoot().setX(self.x)
        self.terrain.getRoot().setY(self.y)
#    def setup(self, model):
#        self.modelName = model
#        self.terrain = loader.loadModel(self.modelName)
#        self.root = self.terrain
#        self.root.setTexScale(TextureStage.getDefault(), 1)
#        self.root.reparentTo(self.zoneRender)
#        self.x = self.terrain.getX()
#        self.y = self.terrain.getY()
        
    def setup(self,model):
        self.terrain = MyGeoMipTerrain('terrain')
        self.terrain.setHeightfield(Filename(model)) #models/land01-map.png
        self.terrain.setBlockSize(32)#128
        self.terrain.setFactor(100)
        self.terrain.setFocalPoint(base.camera)
        self.root = self.terrain.getRoot()
        self.root.reparentTo(self.zoneRender)
        self.root.setSz(100)    # z (up) scale original = 30
        self.terrain.generate()
     #   self.terrain.setMultiTexture()
        self.environ = self.terrain    # make available for original Ralph code below  
        self.root.setCollideMask(Constants.CLICKABLE_MASK)
        self.root.setTag('type', 'Terrain')
        self.root.setTag('object_id', str(self.zoneId))

        ambient = Vec4(0.34, 0.3, 0.3, 1)
        direct = Vec4(0.74, 0.7, 0.7, 1)        
        self.root.setShaderInput('lightvec', Vec4(0.7, 0.2, -0.2, 1))
        self.root.setShaderInput('lightcolor', direct)
        self.root.setShaderInput('ambientlight', ambient)        

    def addAnimal(self,animalObj,skybox):
        #animalObj is a instance of Animal Class
        type = animalObj.getSpeciesType()
        xCoor = animalObj.getXCoor()
        yCoor = animalObj.getYCoor()
        a = Animal3D(type,self.root,self.terrain,self.zoneRender,skybox,xCoor,yCoor,animalObj)
        self.animals.append(a)
        return None
    
    def getAnimalInstance(self, id):
        print id
        for instance in self.animals:
            print instance, "instance"
            if (int)(instance.object_id) == (int)(id):
                return instance.getActorModel()
        return None