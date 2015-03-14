from common.Constants import Constants
from common.DirectBasicButton import DirectBasicButton
from common.DirectTextField import DirectTextField
from common.DirectWindow import DirectWindow
from direct.gui.DirectEntryScroll import DirectEntryScroll
from direct.gui.DirectFrame import DirectFrame
from direct.gui.DirectGui import DGG
from direct.gui.DirectLabel import DirectLabel
from direct.gui.DirectSlider import DirectSlider
from main.Chatcontrol.Chat import Chat
from panda3d.core import TextNode, TransparencyAttrib


class WorldChat:
    
    def __init__(self, parent):
        
        
        self.maxItemsVisible=4
        self.chatLines=[]
        self.chatButtons=[]
        self.parent = parent
        self.createMainFrame()
        self.createButtons()
        self.createLog()
        self.createEntry()
        self.chat = Chat(self.chatEntry, self.scrollBar, self.chatLines,
                         self.sendButton, self.maxItemsVisible, Constants.CMSG_PVEWORLD_CHAT, 23)
        self.setCommandForChat()
        
    def createMainFrame(self):
        
        self.mainFrame = DirectWindow(frameSize = (-0.6, 0.6, -0.2, 0.2),
                                      frameColor =(0,0,0,0),
                                      pos = (1,0,-0.81))
        self.mainFrame.reparentTo(self.parent)
        
    def createButtons(self):

        self.buttonFrame = DirectFrame( frameSize = (-0.25, 0.25, -0.05, 0.055),
                                        frameColor = Constants.BG_COLOR,
                                        pos = (0.35, 0, 0.24) )
        self.buttonFrame.reparentTo(self.mainFrame)

        self.pveWorldChatButton = DirectBasicButton( text = 'World',
                                            text_fg = Constants.TEXT_COLOR,
                                            text_font = Constants.FONT_TYPE_01,
                                            text_pos = (0, -0.015),
                                            text_scale = 0.045,
                                            text_shadow = Constants.TEXT_SHADOW_COLOR,
                                            frameSize = (-0.1, 0.1, -0.043, 0.043),
                                            frameColor = Constants.CHAT_BUTTON_FOCUS,
                                            pos = (-0.12, 0, 0),
                                            relief = DGG.FLAT)
#                                            command = self.setChatMode )
        self.pveWorldChatButton.setTransparency(TransparencyAttrib.MAlpha)
        self.pveWorldChatButton.reparentTo(self.buttonFrame)

        self.teamChatButton = DirectBasicButton( text = 'Team',
                                            text_fg = Constants.TEXT_COLOR,
                                            text_font = Constants.FONT_TYPE_01,
                                            text_pos = (0, -0.015),
                                            text_scale = 0.045,
                                            text_shadow = Constants.TEXT_SHADOW_COLOR,
                                            frameSize = (-0.1, 0.1, -0.043, 0.043),
                                            frameColor = Constants.CHAT_BUTTON_COLOR,
                                            pos = (0.12, 0, 0),
                                            relief = DGG.FLAT)
        self.teamChatButton.reparentTo(self.buttonFrame)
        self.teamChatButton.setTransparency(TransparencyAttrib.MAlpha)
        
    def createLog(self):

        self.chatLogFrame = DirectFrame( frameSize = (-0.6, 0.6, -0.085, 0.19),
                                         frameColor = Constants.BG_COLOR,
                                         pos = (0, 0, 0) )
        self.chatLogFrame.reparentTo(self.mainFrame)

        for i in range(self.maxItemsVisible):
            chatLine = DirectLabel( text = '',
                                    text_align = TextNode.ALeft,
                                    text_fg = Constants.TEXT_COLOR,
                                    text_pos = (-0.57, -0.01),
                                    text_scale = 0.05,
                                    text_shadow = Constants.TEXT_SHADOW_COLOR,
                                    frameSize = (-0.58, 0.55, -0.03, 0.03),
                                    frameColor = (0, 0, 0, 0),
                                    pos = (-0.02, 0, 0.14 - i * 0.06) )
            chatLine.reparentTo(self.chatLogFrame)
            self.chatLines.append(chatLine)

        self.scrollBar = DirectSlider( pos = (0.565, 0, 0.052),
                                       scale = 0.13,
                                       value = 1,
                                       range = (1, 0),
                                       scrollSize = 1,
                                       frameSize = (-0.03,0.03,-0.9,0.9),
                                       pageSize = 1,
                                       orientation = DGG.VERTICAL,
                                       thumb_frameSize = (-0.1, 0.1, -0.2, 0.2),
                                       thumb_relief = DGG.FLAT)
#                                       command = self.scrollChatLog )
        self.scrollBar.reparentTo(self.chatLogFrame) 
           
    def createEntry(self):

        self.bottomFrame = DirectFrame( frameSize = (-0.6, 0.6, -0.055, 0.05),
                                        frameColor = Constants.BG_COLOR,
                                        pos = (0, 0, -0.135) )
        self.bottomFrame.reparentTo(self.mainFrame)

        self.chatEntry = DirectTextField( self.mainFrame,
                                          text = '',
                                          text_font = Constants.FONT_TYPE_01,
                                          frameColor = (0.8, 0.8, 0.8, 0.4),
                                          width = 90,
                                          focusInCommand = self.onFocus,
                                          focusOutCommand = self.onFocusOut )

        self.chatEntryScroll = DirectEntryScroll( self.chatEntry,
                                                  pos = (-0.58, 0, -0.01),
                                                  scale = 0.05,
                                                  clipSize = (0, 19.5, -1, 1) )
        self.chatEntryScroll.reparentTo(self.bottomFrame)

        self.sendButton = DirectBasicButton( text = 'Send',
                                             text_fg = Constants.TEXT_COLOR,
                                             text_font = Constants.FONT_TYPE_01,
                                             text_pos = (0, -0.015),
                                             text_scale = 0.045,
                                             text_shadow = Constants.TEXT_SHADOW_COLOR,
                                             frameSize = (-0.08, 0.08, -0.04, 0.04),
                                             frameColor = (0, 0, 0, 0.2),
                                             pos = (0.5, 0, 0),
                                             relief = DGG.FLAT)
        self.sendButton.reparentTo(self.bottomFrame)
    def setCommandForChat(self):
        
        self.scrollBar['command']=self.chat.scrollChatLog
        self.chatEntry['command']=self.chat.sendEvent
        self.sendButton['command']=self.chat.sendEvent
        self.pveWorldChatButton['command']=self.setChatMode
        self.pveWorldChatButton['extraArgs']=[Constants.CMSG_PVEWORLD_CHAT,0]
        self.teamChatButton['command']=self.setChatMode
        self.teamChatButton['extraArgs']=[Constants.CMSG_TEAM_CHAT,1]
        
    def setChatMode(self, mode, modeIndex):
        
        if modeIndex == 0:
            self.teamChatButton['frameColor']=Constants.CHAT_BUTTON_COLOR
            self.pveWorldChatButton['frameColor'] = Constants.CHAT_BUTTON_FOCUS
        else:
            self.teamChatButton['frameColor']=Constants.CHAT_BUTTON_FOCUS
            self.pveWorldChatButton['frameColor'] = Constants.CHAT_BUTTON_COLOR
            
        self.chat.setChatMode(mode, modeIndex)
    def onFocus(self):
        self.chatEntry['frameColor'] = (0.8, 0.8, 0.8, 0.9)
        self.mainFrame.getControls().enable()

    def onFocusOut(self):

        self.chatEntry['frameColor'] = (0.8, 0.8, 0.8, 0.4)
        self.mainFrame.getControls().disable()
    
    def hide(self):
        self.mainFrame.hide()

    def show(self):
        self.mainFrame.show()
        
    def unload(self):
        self.mainFrame.destroy()
        