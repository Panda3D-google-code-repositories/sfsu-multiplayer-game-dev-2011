#@PydevCodeAnalysisIgnore
from math import ceil
from math import sqrt

from panda3d.core import CollisionHandlerQueue
from panda3d.core import CollisionNode
from panda3d.core import CollisionRay
from panda3d.core import CollisionTraverser
from panda3d.core import NodePath
from panda3d.core import TextureStage
from panda3d.core import VBase3

from common.Constants import Constants

from main.MainLobby.World.World3D.Zone3D import Zone3D
from main.MainLobby.World.World3D.Sound import Sound

class Env3D(NodePath):

    def __init__(self, args):

        NodePath.__init__(self, 'envRoot')

        self.env_id = args['envID']
        self.avatarID = args['avatarID']
        self.envScore = args['envScore']
        self.cPos = (args['rowID'], args['columnID'])

        self.mapID = 0
        self.numZones = 9
        self.envScale = 4
        self.zOffset = 0

        self.zones = []

        self.createRay()
        self.listOfZones = []
        self.setupZones(args)
        

    def createRay(self):

        self.cTrav = CollisionTraverser('cTrav-mousePicker')

        self.mousePickerNode = CollisionNode('mousePicker')
        self.mousePickerNode.addSolid(CollisionRay(0, 0, 1000, 0, 0, -1))
        self.mousePickerNode.setFromCollideMask(Constants.ZONE_MASK)
        self.mousePickerNode.setIntoCollideMask(Constants.NO_MASK)
        self.mousePicker = render.attachNewNode(self.mousePickerNode)

        self.mousePickerHandler = CollisionHandlerQueue()
        self.cTrav.addCollider(self.mousePicker, self.mousePickerHandler)

    def setupZones(self, args):

        maxColumns = int(ceil(sqrt(self.numZones)))

        for i in range(self.numZones):
            zone = Zone3D(self, args['zone' + str(i) + 'ID'], args['zone' + str(i) + 'Type'])
            zone.setSoundMgr(Sound())
            zone.reparentTo(self)

            zone.setPos(i % maxColumns * zone.getSize(), i / maxColumns * zone.getSize(), 0)

            if not args['zone' + str(i) + 'Enable']:
                zone.terrain_c.setCollideMask(Constants.NO_MASK)
                zone.hide()

            self.zones.append(zone)
            self.setZoneIDs(zone.getID())

    def getElevation(self, x, y):

        self.mousePicker.setPos(x, y, 0)
        self.cTrav.traverse(render)

        if self.mousePickerHandler.getNumEntries() > 0:
            self.mousePickerHandler.sortEntries()
            collisionEntry = self.mousePickerHandler.getEntry(0)
            surfacePoint = collisionEntry.getSurfacePoint(render)

            return surfacePoint.getZ()

        return 0

    def sethighlight(self):
        for zone in self.zones:
            zone.sethighlight()
        return
    
    def getID(self):
        return self.env_id

    def getAvatarID(self):
        return self.avatarID
    
    def getEnvironmentScore(self):
        return self.envScore
    
    def setEnvrionmentScore(self,envScore):
        self.envScore =envScore
        
    def getZones(self):
        return self.zones

    def setZoneIDs(self,zoneID):
        self.listOfZones.append(zoneID)
    
    def getZoneIDs(self):   
        return self.listOfZones
     
    def getUniqueZoneID(self,zoneID):
        return self.listOfZones[zoneID]