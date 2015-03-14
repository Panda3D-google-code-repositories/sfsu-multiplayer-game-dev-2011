from common.Constants import Constants
from main.MainLobby.World.World3D.Zone3D import Zone3D
class Env3D():
    def __init__(self, xo, yo):
        if Constants.DEBUG:
            print "Creating environment rowId=",xo," columnId=",yo
        self.numTerrains = 4
        self.zones = []
        self.setupMip(xo,yo)
        taskMgr.add(self.updateTask, "updateTerrain")
    def setupMip(self,xo,yo):
        for x in range(3):
            for y in range(3):
                self.zones.append(Zone3D(self,x,y))
                self.zones[y+x*3].xoff = xo
                self.zones[y+x*3].yoff = yo
                self.zones[y+x*3].setupMip()
                self.zones[y+x*3].move(x,y)
    def updateTask(self, task):
        for z in self.zones:
            z.terrain.update()
        return task.cont
