from common.Constants import Constants
from main.MainLobby.World.World3D.Zone3D import Zone3D
class Env3D():
    def __init__(self, xo, yo):
        if Constants.DEBUG:
            envId = (xo * 10) + (yo+1)  #where x0=column, y0=row
            print "Creating environment " +str(envId)
        self.envId = envId    
        self.zones = []
        self.terrainFiles = []
        self.terrainFiles.append('models/terrain/tropical01.png')
        self.terrainFiles.append('models/terrain/desert01.png')
        #szones[0].setup(random.sample(self.terrainFiles,1)[0])
        for x in range(2):
            for y in range(2):
                self.zoneId = y+(x*2)
                self.zones.append(Zone3D(self.zoneId))
                self.zones[y+x*2].xoff = xo
                self.zones[y+x*2].yoff = yo
                self.zones[y+x*2].setup(self.terrainFiles[(y+x*2)%2])
                self.zones[y+x*2].move(x,y)
                print x, y