

from main.MainLobby.World.Avatars.Avatars import Avatars
from main.MainLobby.World.Chat.Chat import WorldChat
from main.MainLobby.World.Menu.Menu import Menu
from common.Constants import Constants
from common.DirectWindow import DirectWindow
from direct.gui.DirectGui import DGG
from direct.gui.DirectLabel import DirectLabel
from main.MainLobby.World.GameShop.GameShop import GameShop
from main.MainLobby.World.Weather.Weather import Weather
from panda3d.core import TextNode


class WorldGUI:
    
    def __init__(self):
    
        self.info = []
        self.createMainFrame()
        self.weatherFrame = Weather(self.mainFrame)
        self.chatFrame = WorldChat(self.mainFrame)
        self.gameShop = GameShop(self.mainFrame)
        self.avatar = Avatars(self.mainFrame)
        self.menu = Menu(self.mainFrame, self)
        self.createInfoLabel()
        self.createTimeFrame()
        
    def createMainFrame(self):
        
        self.mainFrame = DirectWindow(frameSize = (0,0,0,0),
                                      frameColor = Constants.BG_COLOR,
                                      pos = (0,0,0))
        self.mainFrame.reparentTo(aspect2d)
    def createInfoLabel(self):
        
        
        for i in range (3):
            self.info.append( DirectLabel(text = '',
                                            text_fg = Constants.TEXT_COLOR,
                                            text_font = Constants.FONT_TYPE_01,
                                            text_align=TextNode.ARight,
                                            text_pos = (-0.05, -0.015),
                                            text_scale = 0.045,
                                            text_shadow = Constants.TEXT_SHADOW_COLOR,
                                            frameSize = (-0.2, 0.2, -0.046, 0.046),
                                            frameColor = Constants.BG_COLOR,
                                            pos = (1.38, 0, 0.94 - i*0.1),
                                            relief = DGG.FLAT))
            self.info[i].reparentTo(self.mainFrame)
        
        self.info[0]['text']='Level:'
        self.info[1]['text']='   XP:'
        self.info[2]['text']=' Gold:'
        
    
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
        self.avatar.unload()
        self.gameShop.unload()
        self.weatherFrame.unload()
        self.chatFrame.unload()
        self.menu.unload()
        self.mainFrame.destroy()

        