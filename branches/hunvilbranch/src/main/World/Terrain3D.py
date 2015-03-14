from PIL import Image
from random import *

class TerrainModel():
    def __init__(self, env, width):
        w2 = width+1
        t = []
        h = []
        g = []
        r = []
        wt = Image.open("models/terrain/waterzone_texture.png").resize((2*w2/3,2*w2/3))
        wh = Image.open("models/terrain/waterzone_height.png").resize((w2/3,w2/3))
        for i in range(5):
            t.append(Image.open("models/terrain/mip0"+str(i+1)+"_texture.png").resize((2*w2/3,2*w2/3)))
            h.append(Image.open("models/terrain/mip0"+str(i+1)+"_height.png").resize((w2/3,w2/3)))
            g.append(Image.open("models/terrain/grass"+str(i+1)+".png").convert('RGBA').resize((2*w2/3,2*w2/3)))
        self.heightmap = Image.new("L", (w2,w2))
        self.texture = Image.new("RGB", (w2*2,w2*2)) 
        for x in [0, w2/3, 2*w2/3]:
            for y in [0, w2/3, 2*w2/3]:
                ix = x/(w2/3)
                iy = y/(w2/3)
                if env.zoneDict[(ix,iy)].water:
                    self.heightmap.paste(wh,(x,y))
                    self.texture.paste(wt,(x*2,y*2))
                else:
                    i = env.zoneDict[(ix,iy)].zonetype
                    self.heightmap.paste(h[i],(x,y))
                    self.texture.paste(t[i],(x*2,y*2))
                grass = env.zoneDict[(ix,iy)].grass - 1
                if grass >= 0:
                    self.texture.paste(g[grass],(x*2,y*2),mask=g[grass])
        self.heightmap = self.heightmap.resize((w2,w2)).transpose(Image.FLIP_TOP_BOTTOM)
        self.texture = self.texture.resize((w2*2,w2*2)).transpose(Image.FLIP_TOP_BOTTOM)
        self.heightmap.save("models/terrain/current_height.png")
        self.texture.save("models/terrain/current_texture.png")
    def craftTexture(self):
        w2 = 513
    
