'''
Created on Nov 12, 2011

@author: lloyd
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
from main.MousePicker.MousePicker import MousePicker


from common.Constants import Constants
from common.DirectBasicButton import DirectBasicButton
from common.DirectBasicLabel import DirectBasicLabel
from common.DirectWindow import DirectWindow
from direct.gui.DirectGui import DGG
from direct.gui.DirectLabel import DirectLabel
from main.MainLobby.World.Avatars.Avatars import Avatars
from main.MainLobby.World.Chat.Chat import WorldChat
from main.MainLobby.World.GameShop.GameShop import GameShop
from main.MainLobby.World.Menu.Menu import Menu
from main.MainLobby.World.Weather.Weather import Weather
from panda3d.core import TextNode
from util.AudioManager import AudioManager
from direct.interval.IntervalGlobal import *
from math import *

from main.MainLobby.World.World3D.Env3D import Env3D
from main.MainLobby.World.World3D.Animal import Animal

class WorldGUI:
    
    def __init__(self):
        if Constants.DEBUG:
            print 'Loading World...'
            
        self.main = main
        base.disableMouse()
        self.env = []           #use #getZoneInEnvironment(self,envId,zoneId) to add animal or plant
        self.displayGame()

           
        self.info = []
        self.createMainFrame()
        self.audioManager = AudioManager()
        self.audioManager.setMusic('01.ogg')
        self.weatherFrame = Weather(self.mainFrame)
        self.chatFrame = WorldChat(self.mainFrame)
        self.gameShop = GameShop(self.mainFrame)
        self.avatar = Avatars(self.mainFrame)
        self.menu = Menu(self.mainFrame, self)
        self.mPicker = MousePicker(self)
        self.createInfoLabel()
        self.createTimeFrame()
        
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
        self.audioManager.removeMusic()

    def PointAtZ(self, z, point, vec):
        return point + vec * ((z-point.getZ()) / vec.getZ())
    def SquarePos(self, i):
        return Point3((i%12) - 5, int(i/12) - 5, 0)
    
    def getControls(self):
        return self.controls
       
    def displayGame(self):      
        self.scaleFactor = 0.5  

        self.env.append(Env3D(0,0))     #getZoneInEnvironment(self,envId,zoneId)
        self.env[0].zones[0].addTree()
        self.env.append(Env3D(0,1))
        
        self.doSky()
        base.enableParticles()
        self.pspawn = loader.loadModel("models/square")
        self.r = 0
        watertex = loader.loadTexture("models/bluesky/sky-material-24-cl.png")
        watertex.setWrapU(Texture.WMRepeat)
        watertex.setWrapV(Texture.WMRepeat)
        watertex.setWrapW(Texture.WMRepeat)
        self.root2 = render.attachNewNode("root2")
        self.setupLights()
        taskMgr.add(self.updateTask, "update")
        taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        camera.reparentTo(render)
        camera.setPosHpr(129,-129, 400, 12, -45, 0)
        #base.disableMouse()
        base.enableMouse()
        
        a1 = Animal(1, "elephant", 510, 600)
        self.env[0].zones[2].addAnimal(a1,self.skysphere)
        
        a2 = Animal(1, "elephant", 540, 640)
        self.env[0].zones[2].addAnimal(a2,self.skysphere)
        
        a3 = Animal(1, "elephant", 580, 680)
        self.env[0].zones[2].addAnimal(a3,self.skysphere)
        
        self._setup_camera()

    def _setup_camera(self):
        sa = ShaderAttrib.make( )
        sa = sa.setShader(loader.loadShader('shaders/splut3Normal.sha'))
        cam = base.cam.node()
        cam.getLens().setNear(1)
        cam.getLens().setFar(5000)
        cam.setTagStateKey('Normal')
        cam.setTagState('True', RenderState.make(sa)) 
                
    def animateTex(self, task):
        currentFrame = int(task.time * task.fps)
        task.obj.setTexture(task.textures[currentFrame % len(task.textures)],1)
        return task.cont
    def updateTask(self, task):
        return task.cont
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        return Task.cont
    def doSky(self):
        self.skysphere = loader.loadModel('models/bluesky/blue-sky-sphere')
        self.skysphere.setEffect(CompassEffect.make(render))
        self.skysphere.setScale(1)
        self.skysphere.reparentTo(camera)
        self.skyTask = taskMgr.add(self.animateTex, "skyTask")
        self.skyTask.fps = 0.2
        self.skyTask.obj = self.skysphere
        self.daytex = loader.loadTexture("models/bluesky/day.png")
        self.nighttex = loader.loadTexture("models/bluesky/night.png")
        self.skyTask.textures = [self.daytex, self.nighttex]
    def setupLights(self):
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor(Vec4(.4, .4, .35, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(Vec3( 0, 8, -2.5 ) )
        directionalLight.setColor(Vec4( 0.9, 0.8, 0.9, 1 ) )
        render.setLight(render.attachNewNode( directionalLight ) )
        render.setLight(render.attachNewNode( ambientLight ) )
        
    def loadParticleConfig(self, file):
        print('not yet implemented')
        
    def getZoneInEnvironment(self,envId,zoneId):
        return self.env[envId-1].zones[zoneId]

    def moveAnimal(self, list, target):
        first = 1
        for id in list:
            a = self.env[0].zones[2].getAnimalInstance(id)
            t = self.env[0].zones[2].getTerrain()
            if first: 
                refX = a.getX()
                refY = a.getY()
                refZ = a.getZ()
                
                a.setX(target.getX())
                a.setY(target.getY())
                a.setZ(t.getElevation(target.getX(),target.getX())*t.getRoot().getSz())
                
                a.clearTransparency()
                a.setColorScale(1,1,1,1) 
                
                first = 0
            else:
                diffX = refX - a.getX()
                diffY = refY - a.getY()
                diffZ = refZ - a.getZ()
                
                a.setX(target.getX()+ diffX)
                a.setY(target.getY()+ diffY)
                a.setZ(t.getElevation(target.getX(),target.getX())*t.getRoot().getSz())
            
                a.clearTransparency()
                a.setColorScale(1,1,1,1)
    