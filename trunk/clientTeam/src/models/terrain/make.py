from PIL import Image
from random import *

t = []
h = []
for i in range(4):
    t.append(Image.open("mip0"+str(i+1)+"_texture.png"))
    h.append(Image.open("mip0"+str(i+1)+"_height.png"))
h2 = Image.new("L", (513*3,513*3))
t2 = Image.new("RGB", (513*3,513*3))
for x in [0, 513, 1026]:
    for y in [0, 513, 1026]:
        i = randint(0,3)
        h2.paste(h[i],(x,y))
        t2.paste(t[i],(x,y))
h2.show()
t2.show()
h2.save("allmip_height.png")
t2.save("allmip_texture.png")
