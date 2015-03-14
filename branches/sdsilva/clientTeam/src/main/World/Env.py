#@PydevCodeAnalysisIgnore
'''
Created on Oct 22, 2011

@author: hunvil
'''
from common.Constants import Constants
from main.World.Zone import Zone
class Env():
    def __init__(self, xo, yo):
        if Constants.DEBUG:
            print "Creating Environment No." + str(envId)
        self.zones = []
        self.terrainFiles = []
        self.terrainFiles.append('models/terrain/tropical01.png614.bam')
        self.terrainFiles.append('models/terrain/desert01.png614.bam')
        #szones[0].setup(random.sample(self.terrainFiles,1)[0])
        for x in range(3):
            for y in range(3):
                self.zones.append(Zone())
                self.zones[y+x*3].xoff = xo
                self.zones[y+x*3].yoff = yo
                self.zones[y+x*3].setup(self.terrainFiles[(y+x*3)%2])
                self.zones[y+x*3].move(x,y)

    def getAnimalCountEnv(self):
        animalCount = 0
        for x in range(3):
            for y in range(3):
                self.zoneId = y+x*3
                animalCount = self.zones[self.zoneId].getAnimalCountZone()
                
    def getPlantCountEnv(self):
        plantCount = 0
        for x in range(3):
            for y in range(3):
                self.zoneId = y+x*3
                plantCount = self.zones[self.zoneId].getPlantCountZone()  