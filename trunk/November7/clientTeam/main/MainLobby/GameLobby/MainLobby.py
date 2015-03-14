

from common.Constants import Constants
from common.DirectBasicButton import DirectBasicButton
from common.DirectTextField import DirectTextField
from direct.gui.DirectEntryScroll import DirectEntryScroll
from direct.gui.DirectFrame import DirectFrame
from direct.gui.DirectGui import DGG
from direct.gui.DirectLabel import DirectLabel
from direct.gui.DirectSlider import DirectSlider
from direct.gui.OnscreenImage import OnscreenImage
from direct.showbase.DirectObject import DirectObject
from main.Chatcontrol.Chat import Chat
from main.MainLobby.GameLobby.PlayerWindow import PlayerWindow
from panda3d.core import TextNode
from pandac.PandaModules import TransparencyAttrib

class MainLobbyControl(DirectObject):

    def __init__(self, parent=None):
        self.accept(Constants.UPDATE_MAIN_ONLINE_PLAYERS, parent.receiveMessage, [])

class MainLobby:
    '''
    classdocs
    '''

    def __init__(self, parent):
                
        self.mainFrame = parent
#        self.lobbyHeader = LobbyHeader(self.mainFrame)
        self.imageDir = 'models/2d/'
        base.disableMouse() 
        self.chatButtons=[]
        self.chatLines = []
        self.maxItemsVisible = 21
        

        self.createLog()
#        self.chatLogFrame.hide()
        self.createEntry()
#        self.createLabels()
        
        self.chat=Chat(self.chatEntry, self.scrollBar, self.chatLines, 
                       self.sendButton,self.maxItemsVisible, Constants.CMSG_UNIVERSAL_CHAT, 35)
        self.setCommandForChat()
        self.playerWindow = PlayerWindow((0.98, 0 ,-0.15), self.chatEntry, self.mainFrame)
        self.playerWindow.show()
        self.playerWindow.hideHideButton()
        self.control = MainLobbyControl(self)
        
        self.hide()
        
        
    def createLog(self):
        
        self.chatLogFrame = DirectFrame( frameSize = (-0.9,0.9, -0.78, 0.54),
                                         pos = (-0.55, 0, 0.06),
                                         frameColor=(0,0,0,0),
                                         image=self.imageDir+'chat_bg.jpg',
                                         image_pos=(0,0,-0.13),
                                         image_scale=(0.9,0,0.665))
        self.chatLogFrame.reparentTo(self.mainFrame)
        
#        self.universalChatHeader = OnscreenImage(image = self.imageDir+'universalChat_400x50.jpg',
#                                               scale=(0.9, 0, 0.08),
#                                               pos = (-0.55, 0, 0.68))
#        self.universalChatHeader.reparentTo(self.mainFrame)
#        self.universalChatHeader.setTransparency(TransparencyAttrib.MAlpha)
        
        for i in range(self.maxItemsVisible):
            chatLine = DirectLabel( text = '',
                                    text_align = TextNode.ALeft,
                                    text_fg = Constants.TEXT_COLOR,
                                    text_pos = (-0.86, -0.01),
                                    text_scale = 0.05,
                                    text_shadow = Constants.TEXT_SHADOW_COLOR,
                                    frameSize = (-0.87, 0.8, -0.03, 0.03),
                                    frameColor = (1, 0, 0, 0),
                                    pos = (-0.015, 0, 0.47 - i * 0.06) )
            chatLine.reparentTo(self.chatLogFrame)
            self.chatLines.append(chatLine)

        self.scrollBar = DirectSlider( pos = (0.85, 0, -0.13),
                                       scale = 0.13,
                                       value = 1,
                                       range = (1, 0),
                                       frameSize =(-0.05,0.05,-4.8,4.8),
                                       scrollSize = 1,
                                       pageSize = 1,
                                       orientation = DGG.VERTICAL,
                                       thumb_frameSize = (-0.1, 0.1, -3.0, 3.0),
                                       thumb_relief = DGG.FLAT )
        self.scrollBar.reparentTo(self.chatLogFrame)
        
    def createEntry(self):

        self.bottomFrame = DirectFrame( frameSize = (-0.9, 0.9, -0.1, 0.08),
                                        frameColor = (0,0,0,0),
                                        pos = (-0.55, 0, -0.8) )
        self.bottomFrame.reparentTo(self.mainFrame)
        
        self.bottomFrameBg = OnscreenImage(image = self.imageDir + "chat_bg.png",
                                           scale = (0.9, 0, 0.085),
                                           pos=(0,0,-0.02))
        self.bottomFrameBg.reparentTo(self.bottomFrame)
        self.bottomFrameBg.setTransparency(TransparencyAttrib.MAlpha)       
        
        self.chatEntry = DirectTextField( self.mainFrame,
                                          text = '',
                                          cursorKeys = 1,
                                          text_font = Constants.FONT_TYPE_01,
                                          frameColor = (0.8, 0.8, 0.8, 0.4),
                                          width = 90,
#                                          command = self.chat.sendMsg,
                                          focusInCommand = self.onChatEntryFocus,
                                          focusOutCommand = self.onChatEntryFocusOut )

        self.chatEntryScroll = DirectEntryScroll( self.chatEntry,
                                                  pos = (-0.86, 0, -0.03),
                                                  scale = 0.05,
                                                  clipSize = (0, 30, -1, 1) )
        self.chatEntryScroll.reparentTo(self.bottomFrame)

        sendImage=(self.imageDir+'bt_send_unpressed.jpg',
                   self.imageDir+'bt_send_pressed.png',
                   self.imageDir+'bt_send_pressed.png',
                   self.imageDir+'bt_send_pressed.png') 
        self.sendButton = DirectBasicButton( text = '',
                                             image = sendImage,
                                             image_scale=(0.1,0.08,0.04),
                                             image_pos=(0,0,0),
                                             frameSize = (-0.1, 0.1, -0.04, 0.04),
                                             frameColor = (0,0,0,0),
                                             pos = (0.77, 0, -0.015),
                                             relief = DGG.FLAT)
#                                             command = self.chat.sendMsg )
        self.sendButton.setTransparency(TransparencyAttrib.MAlpha)
        self.sendButton.reparentTo(self.bottomFrame)

    def createLabels(self):
        
        self.universalLabel = DirectLabel(text = "Universal Chat",
                                          text_font = Constants.FONT_TYPE_02,
                                          text_shadow = Constants.TEXT_SHADOW_COLOR,
                                          text_align = TextNode.ALeft,
                                          pos = (-1.45, 0, 0.65), 
                                          scale = 0.11, 
                                          text_bg = (0,0,0,0),
                                          text_fg=(1,1,1,1),
                                          frameColor=(1,1,1,0))
        self.universalLabel.reparentTo(self.mainFrame)
        
        self.onlinePlayerLabel = DirectLabel(text = "Online Player",
                                          text_font = Constants.FONT_TYPE_02,
                                          text_shadow = Constants.TEXT_SHADOW_COLOR,
                                          text_align = TextNode.ALeft,
                                          pos = (0.48, 0, 0.65), 
                                          scale = 0.11, 
                                          text_bg = (0,0,0,0),
                                          text_fg=(1,1,1,1),
                                          frameColor=(1,1,1,0))
        self.onlinePlayerLabel.reparentTo(self.mainFrame)
        
    def receiveMessage(self, _list=[]):
        print "message for main!"
        self.playerWindow.updatePlayersFromServer(_list)
                   
    def setCommandForChat(self):
        
        self.scrollBar['command']=self.chat.scrollChatLog
        self.chatEntry['command']=self.chat.sendEvent
        self.sendButton['command']=self.chat.sendEvent

             
    def onChatEntryFocus(self):

        self.chatEntry['frameColor'] = (0.8, 0.8, 0.8, 0.9)
        self.mainFrame.getControls().enable()

    def onChatEntryFocusOut(self):

        self.chatEntry['frameColor'] = (0.8, 0.8, 0.8, 0.4)
        self.mainFrame.getControls().disable()

#        if self.lastType < 0:
#            self.world.charHero.chatBubble.clear()

    def clearChatEntry(self):
        self.chatEntry.enterText('')
        
    def hide(self):

        self.bottomFrameBg.hide()
        self.chatLogFrame.hide()
        self.bottomFrame.hide()
#        self.universalLabel.hide()
#        self.onlinePlayerLabel.hide()
        self.playerWindow.hide()
        
    def show(self):
        
        self.bottomFrameBg.show()
        self.chatLogFrame.show()
        self.bottomFrame.show()
#        self.universalLabel.show()
#        self.onlinePlayerLabel.show()
        self.playerWindow.show()
        
#    def unload(self):
#        """ remove chatLog, and label"""
#        self.chatLogFrame.destroy()
#        self.bottomFrame.destroy()
#        self.universalLabel.destroy()
#        self.onlinePlayerLabel.destroy()
#        self.playerWindow.unload()
        