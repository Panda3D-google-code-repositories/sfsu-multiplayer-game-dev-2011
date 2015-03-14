'''
Created on Nov 12, 2011

@author: hunvil
'''
#@PydevCodeAnalysisIgnore
from pandac.PandaModules import CompassEffect
from panda3d.core import Texture, TextureStage
from panda3d.core import AmbientLight, DirectionalLight, LightAttrib
from pandac.PandaModules import NodePath
from panda3d.core import Point3, Vec3, Vec4
from direct.task.Task import Task
from pandac.PandaModules import ShaderAttrib
from pandac.PandaModules import RenderState
from pandac.PandaModules import Spotlight
#from direct.particles.ParticleEffect import ParticleEffect
from panda3d.core import Filename

from common.Constants import Constants
from common.DirectBasicButton import DirectBasicButton
from common.DirectBasicLabel import DirectBasicLabel
from common.DirectWindow import DirectWindow
from direct.gui.DirectGui import DGG
from direct.gui.DirectLabel import DirectLabel
from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.OnscreenText import OnscreenText
from direct.interval.IntervalGlobal import *
from direct.task.Task import Task
from main.MainLobby.World.Avatars.Avatars import Avatars
from main.MainLobby.World.Chat.Chat import WorldChat
from main.MainLobby.World.GameShop.GameShop import GameShop
from main.MainLobby.World.Menu.Menu import Menu
from main.MainLobby.World.Weather.Weather import Weather
from panda3d.core import TextNode
from direct.interval.IntervalGlobal import *
from math import *

from main.MainLobby.World.World3D.Env3D import Env3D
from main.MainLobby.World.World3D.GameState import GameState

class WorldGUI:
    
    def __init__(self):
        if Constants.DEBUG:
            print 'Loading World...'
# Create an event called 'window-close' whenever the user tries to
# close the window to perform additional procedures before closing.
#        base.win.setCloseRequestEvent('window-close')
#        self.main = main
        self.createLoadingImage()
#        self.loadingImage = OnscreenImage(image = 'models/' + 'Loading.png',
#                                          scale = (base.camLens.getAspectRatio(), 1, 1),
#                                          sort = 30)
        # render a frame, otehrwise the screen won't chnage
        base.graphicsEngine.renderFrame()
        base.graphicsEngine.renderFrame()
        
        ##Loading info into world, please put all the loading process in between
        base.disableMouse()
        self.gameState = GameState()
        self.displayGame()

           
        self.info = []
        self.createMainFrame()
        self.weatherFrame = Weather(self.mainFrame)
        self.chatFrame = WorldChat(self.mainFrame)
        self.gameShop = GameShop(self)
        self.avatar = Avatars(self)
        self.menu = Menu(self)
        self.createInfoLabel()
        self.createTimeFrame()
        
		#End of loading process
        self.loadSequence = Sequence(Wait(0.1), Func(self.loadingImage.hide))
        self.loadSequence.start()
        main.audioManager.setMusic('01.ogg')
        
    def createLoadingImage(self):
        self.loadingImage = OnscreenImage(image = 'models/' + 'Loading.png',
                                          scale = (base.camLens.getAspectRatio(), 1, 1),
                                          sort = 30)
#        self.percentage = OnscreenText(text='0%', pos=(0,1,0), scale=0.1)
        
    def createMainFrame(self):
        
        self.mainFrame = DirectWindow(frameSize = (0,0,0,0),
                                      frameColor = Constants.BG_COLOR,
                                      pos = (0,0,0))
        self.mainFrame.reparentTo(aspect2d)
    def createInfoLabel(self):
        
        for i in range (4):
            self.info.append( DirectBasicButton(text = '',
                                            text_fg = Constants.TEXT_COLOR,
                                            text_font = Constants.FONT_TYPE_01,
                                            text_align=TextNode.ALeft,
                                            text_pos = (-0.18, -0.015),
                                            text_scale = 0.045,
                                            text_shadow = Constants.TEXT_SHADOW_COLOR,
                                            frameSize = (-0.2, 0.2, -0.046, 0.046),
                                            frameColor = Constants.BG_COLOR,
                                            pos = (1.38, 0, 0.94 - i*0.1),
                                            relief = DGG.FLAT,
                                            state=DGG.DISABLED))
            self.info[i].reparentTo(self.mainFrame)
        
        self.info[0]['text']='Level:'
        self.info[1]['text']='XP:'
        self.info[2]['text']='Gold:'
        self.info[3]['text']='Env Scr:'
        self.info[1]['state']=DGG.NORMAL
        self.info[1].setMouseText('34 xp needed to level up')
        
    
    def createTimeFrame(self):
        
        self.timeFrame = DirectLabel(text='Time',
                                     text_fg = Constants.TEXT_COLOR,
                                    text_font = Constants.FONT_TYPE_01,
                                    text_align=TextNode.ACenter,
                                    text_pos = (0, -0.015),
                                    text_scale = 0.06,
                                    text_shadow = Constants.TEXT_SHADOW_COLOR,
                                    frameSize = (-0.15, 0.15, -0.05, 0.05),
                                    frameColor = Constants.BG_COLOR,
                                    pos = (0, 0, 0.95),
                                    relief = DGG.FLAT)
        self.timeFrame.reparentTo(self.mainFrame) 
    
    def hideBottom(self):
          
        self.chatFrame.hide()
        self.weatherFrame.hide()
        self.gameShop.hide()
        self.avatar.reposition()
        
    def showBottom(self):
        self.avatar.restorePos()
        self.chatFrame.show()
        self.weatherFrame.show()
        self.gameShop.show()
    
    def unload(self):
        if Constants.DEBUG:
            print 'Unloading World...'
        main.removeGameControls()        
        self.avatar.unload()
        self.gameShop.unload()
        self.weatherFrame.unload()
        self.chatFrame.unload()
        self.menu.unload()
        self.mainFrame.destroy()
        main.audioManager.removeMusic()

    def PointAtZ(self, z, point, vec):
        return point + vec * ((z-point.getZ()) / vec.getZ())
    def SquarePos(self, i):
        return Point3((i%12) - 5, int(i/12) - 5, 0)
    
    def getControls(self):
        return self.controls
    
    def displayGame(self):      
        self.effectStatus = 'day'
        self.scaleFactor = 0.5  
        #self.env = []
        #self.env.append(Env3D(0,0))
        #zone1 = self.env[0].zones[0]
        #zone1.demo_addTree()
        #zone2 = self.env[0].zones[5]
        #zone2.demo_addTree()
        #zone3 = self.env[0].zones[4]
        #zone3.demo_addTree()
        #self.env.append(Env3D(0,1))
        
        self.gameState.createEnvironment(0, 0, 80, 81, 82, 83, 84, 85, 86, 87, 88,3,1)
        i = 0
        self.gameState.responseBirthPlant(i, "bigTree", 5, 80, 100)
        self.gameState.responseBirthPlant(i+1, "boabab_L", 5, 80, 100)

        self.gameState.responseBirthAnimal(i+2, "elephant", 5, 80, 100)
        self.gameState.responseBirthAnimal(i+3,"cheetah",5,80,100)        
#        while i<40:
#            self.gameState.responseBirthPlant(i, "bigTree", 5, 80, 100)
#            self.gameState.responseBirthPlant(i+1, "boabab_L", 5, 80, 100)
#    
#            self.gameState.responseBirthAnimal(i+2, "elephant", 5, 80, 100)
#            self.gameState.responseBirthAnimal(i+3,"cheetah",5,80,100)
#            i = i + 3 
#            
#        self.gameState.createEnvironment(0, 1, 70, 71, 72, 73, 74, 75, 76, 77, 78,3,1)
#        self.gameState.responseBirthPlant(0, "bigTree", 4, 70, 100)
#        self.gameState.responseBirthPlant(91, "boabab_L", 4, 70, 100)
#        
#        self.gameState.responseBirthAnimal(90, "elephant", 4, 70, 100)
#        self.gameState.responseBirthAnimal(91,"cheetah",4,70,100)            
    
        self.gameState.responseKillAnimal(3,2)   #4-cheetah3(attackerAnimalID) 3-elephant(preyAnimalID)
        #self.gameState.responseKillPlant(90)      #3-bigTree
               
        self.doSky()
#        base.enableParticles()
#        self.rainParticles = ParticleEffect()
#        self.loadRain(self.rainParticles, zone3, 'models/rain/rain.ptf')
        self.pspawn = loader.loadModel("models/square")
        self.r = 0
        watertex = loader.loadTexture("models/bluesky/sky-material-24-cl.png")
        watertex.setWrapU(Texture.WMRepeat)
        watertex.setWrapV(Texture.WMRepeat)
        watertex.setWrapW(Texture.WMRepeat)
        self.root2 = render.attachNewNode("root2")
        self.setupLights()
        taskMgr.add(self.updateTask, "update")
        #taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        camera.setPosHpr(256*3,256*3, 100, 80, -80, 0)
        camera.reparentTo(render)
        #base.disableMouse()
        base.enableMouse()
    def animateTex(self, task):
        currentFrame = int(task.time * task.fps)
        task.obj.setTexture(task.textures[currentFrame % len(task.textures)],1)
        return task.cont
    def tempTask(self, task):
        currentFrame = int(task.time * task.fps)
        if currentFrame % 2 == 0 and self.effectStatus != 'day':
            self.globalEffects('day')
            self.effectStatus = 'day'
        if currentFrame % 2 == 1 and self.effectStatus != 'night':
            self.globalEffects('night')
            self.effectStatus = 'night'
        return task.cont
    def updateTask(self, task):
        return task.cont
    def spinCameraTask(self, task):
        angleDegrees = task.time * 12.0
        angleRadians = angleDegrees * (pi / 180.0)
        camera.setHpr(angleDegrees, -10, 0)
        return Task.cont
    def loadRain(self, p, zone, file):
        p.cleanup()
        p = ParticleEffect()
        p.loadConfig(Filename(file))        
        p.start(zone.root)
        off = 256
        offz = 100
        r = zone
        p.setPos(r.getX(off), r.getY(off), offz)
        print r.getX(off), r.getY(off), offz
    def doSky(self):
        self.skysphere = loader.loadModel('models/bluesky/blue-sky-sphere')
        self.skysphere.setEffect(CompassEffect.make(render))
        self.skysphere.setScale(1)
        self.skysphere.reparentTo(camera)
        self.skyTask = taskMgr.add(self.animateTex, "skyTask")
        self.tempTask1 = taskMgr.add(self.tempTask, "tempTask")
        self.skyTask.fps = 0.2
        self.tempTask1.fps = 0.2
        self.skyTask.obj = self.skysphere
        self.daytex = loader.loadTexture("models/bluesky/day.png")
        self.nighttex = loader.loadTexture("models/bluesky/night.png")
        self.skyTask.textures = [self.daytex, self.nighttex]
    def setupLights(self):
        self.ambientLight = AmbientLight("ambientLight")
        self.ambientLight.setColor(Vec4(.4, .4, .35, 1))
        self.directionalLight = DirectionalLight("directionalLight")
        self.directionalLight.setDirection(Vec3( 0, 8, -2.5 ) )
        self.directionalLight.setColor(Vec4( 0.9, 0.8, 0.9, 1 ) )
        render.setLight(render.attachNewNode( self.directionalLight ) )
        render.setLight(render.attachNewNode( self.ambientLight ) )
    def globalEffects(self, effect):
        if effect == 'day':
            self.directionalLight.setColor(Vec4( 0.9, 0.8, 0.9, 1 ) )
            self.ambientLight.setColor(Vec4(.4, .4, .35, 1))
            #print 'Day lights'
        if effect == 'night':
            self.directionalLight.setColor(Vec4( 0.4, 0.3, 0.5, 1 ) )
            self.ambientLight.setColor(Vec4(.2, .2, .2, 1))
            #print 'Night lights'
        if effect == 'rain':
            self.directionalLight.setColor(Vec4( 0.6, 0.5, 0.9, 1 ) )
            self.ambientLight.setColor(Vec4(.3, .3, .5, 1))
            print 'Rain lights'
        #render.setLight(render.attachNewNode( self.directionalLight ) )
    def loadParticleConfig(self, file):
        print('not yet implemented')

    def unload(self):
        """Unload this instance."""
        if Constants.DEBUG:
            print 'Unloading World...'
        main.removeGameControls()