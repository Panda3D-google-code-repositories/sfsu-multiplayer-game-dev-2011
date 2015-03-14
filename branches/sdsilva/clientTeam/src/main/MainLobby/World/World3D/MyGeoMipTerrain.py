from pandac.PandaModules import GeoMipTerrain
from pandac.PandaModules import TextureStage
from pandac.PandaModules import Texture
from pandac.PandaModules import Vec4

class MyGeoMipTerrain(GeoMipTerrain):
    def __init__(self, name):
        GeoMipTerrain.__init__(self, name)

    def update(self, dummy):
        GeoMipTerrain.update(self)

    def setMonoTexture(self):
        root = self.getRoot()
        ts = TextureStage('ts')
        tex = loader.loadTexture('textures/mountainoustexture.jpg')#textures/land01_tx_512.png
        root.setTexture(ts, tex)

    def setMultiTexture(self):
        root = self.getRoot()
            #root.setShader(loader.loadShader('shaders/splut3Normal.sha'))
        root.setShaderInput('tscale', Vec4(100.0, 100.0, 100.0, 1.0))    # texture scaling

        tex1 = loader.loadTexture('textures/SandPebbles0072_3_L.jpg')
        #tex1.setMinfilter(Texture.FTLinearMipmapLinear)
        tex1.setMinfilter(Texture.FTNearestMipmapLinear)
        tex1.setMagfilter(Texture.FTLinear)
        tex2 = loader.loadTexture('textures/rock_02.jpg')
        tex2.setMinfilter(Texture.FTNearestMipmapLinear)
        tex2.setMagfilter(Texture.FTLinear)
        tex3 = loader.loadTexture('textures/sable_et_gravier.jpg')
        tex3.setMinfilter(Texture.FTNearestMipmapLinear)
        tex3.setMagfilter(Texture.FTLinear)

        alp1 = loader.loadTexture('textures/testalpha.png')#alpha1
        alp2 = loader.loadTexture('textures/testalpha2.png')#alpha2
        alp3 = loader.loadTexture('textures/alpha3.png')#alpha3

        ts = TextureStage('tex1')    # stage 0
        root.setTexture(ts, tex1)
        ts = TextureStage('tex2')    # stage 1
        root.setTexture(ts, tex2)
        ts = TextureStage('tex3')    # stage 2
        root.setTexture(ts, tex3)
        ts = TextureStage('alp1')    # stage 3
        root.setTexture(ts, alp1)
        ts = TextureStage('alp2')    # stage 4
        root.setTexture(ts, alp2)
        ts = TextureStage('alp3')    # stage 5
        root.setTexture(ts, alp3)

        # enable use of the two separate tagged render states for our two cameras
        root.setTag( 'Normal', 'True' )
        root.setTag( 'Clipped', 'True' )