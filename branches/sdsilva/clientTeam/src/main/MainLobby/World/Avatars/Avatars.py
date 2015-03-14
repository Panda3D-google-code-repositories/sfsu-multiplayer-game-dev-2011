

from common.Constants import Constants
from common.DirectBasicButton import DirectBasicButton
from common.DirectControls import DirectControls
from common.DirectWindow import DirectWindow
from direct.gui.DirectGui import DGG
from direct.gui.DirectSlider import DirectSlider
from direct.interval.FunctionInterval import Func, Wait
from direct.interval.MetaInterval import Sequence
from main.MainLobby.World.Avatars.Stats import Stats
from panda3d.core import TransparencyAttrib, TextNode
from threading import Timer

class AvatarControls(DirectControls):

    def __init__(self, parent):

        DirectControls.__init__(self, parent)

        self.accept('e', parent.applyEffect)
        self.accept('a', parent.toggleOtherAvatarVisibility)

class Avatars:
    
    """
    1). create own avatar and other avatar, and stat button
    2). Implement stat button click
    3). Implement otherAvatar click
    4). Implement the effect of click on own avatar
    5). Implement notification
    """
    def __init__(self, parent):
        """
        parent is the mainFrame from game world
        """
        self.parent = parent
#        self.otherAvatars = []
        self.alertBG = (1,0.2,0.2,0.8)
        self.notificationFrameColor = (0.31, 0.65, 0.76, 0.8)
        self.notificationPos=(-1.24,0,-0.26)
        self.statButtonPos=(-1.5, 0, -0.575)
        self.avatarPos=(-1.5, 0, -0.45)
        self.otherAvatarPos=(-1.31, 0, -0.53)
        self.numOfAvatars = 1
        self.createOwnAvatar()
        self.createStatButton()
        self.createOtherAvatars()
        self.stats = Stats(self.parent)
        self.stats.hide()
        self.createOtherAvatarsListFrame()
        self.msgBubbleSequence = Sequence()
        self.createMessageBubble()
        self.control = AvatarControls(self)
        
#        _t = Timer(6, self.notify, ['Avatar: this is sample message to test notification features', 
#                                    self.notificationFrameColor])
#        _t.start()
#        
#        _t = Timer(20, self.notify,['Test alert message', self.alertBG])
#        _t.start()
    def createOwnAvatar(self):
        """
        Avatar id is needed for this.
        """
        _avatar = 'models/avatar/1a.png'
        self.avatar = DirectBasicButton(image=_avatar,
                                        image_pos=(0, 0, 0),
                                        image_scale=(0.11, 0.11, 0.11),
                                        frameSize=(-0.12, 0.12, -0.1, 0.1),
                                        frameColor=(0, 0, 0, 0),
                                        pos=self.avatarPos)
        self.avatar.setTransparency(TransparencyAttrib.MAlpha)
        self.avatar.reparentTo(self.parent)
        
    def createStatButton(self):
        
        self.statButton = DirectBasicButton(text='Stat',
                                            text_fg=(0, 0, 0, 1),
                                            text_font=Constants.FONT_TYPE_01,
                                            text_pos=(0, -0.015),
                                            text_scale=0.04,
                                            text_shadow=Constants.TEXT_SHADOW_COLOR,
                                            frameSize=(-0.08, 0.08, -0.035, 0.035),
                                            frameColor=(0, 0, 0, 0.2),
                                            pos=self.statButtonPos,
                                            relief=DGG.FLAT,
                                            command=self.showStatFrame)
        self.statButton.setTransparency(TransparencyAttrib.MAlpha)
        self.statButton.reparentTo(self.parent)
        
    def createOtherAvatars(self):
        _avatar = 'models/avatar/1a.png'
        
#        for i in range(self.numOfAvatars):
        self.otherAvatars = DirectBasicButton(image=_avatar,
                                    image_pos=(0, 0, 0),
                                    image_scale=(0.09, 0.09, 0.09),
                                    frameSize=(-0.09, 0.09, -0.08, 0.08),
                                    frameColor=(0, 0, 0, 0),
                                    pos=self.otherAvatarPos,
                                    command=self.showOtherAvatarFrame)
        self.otherAvatars.setTransparency(TransparencyAttrib.MAlpha)
        self.otherAvatars.reparentTo(self.parent)
    
    def showStatFrame(self):
        self.stats.show()  
        
    def createOtherAvatarsListFrame(self):
        
        self.otherAvatarFrame = DirectWindow(frameSize=(-0.5, 0.5, -0.6, 0.6),
                                      frameColor=Constants.BG_COLOR,
                                      pos=(0, 0, 0.15))
        self.otherAvatarFrame.reparentTo(self.parent)
        self.otherAvatarFrame.hide()
    
        self.hideButton = DirectBasicButton(text=" - ",
                                       text_fg=(1, 1, 1, 1),
                                       text_pos=(-0.007, -0.015),
                                       text_scale=0.05,
                                       frameColor=(0, 0, 0, 0.2),
                                       frameSize=(-0.04, 0.04, -0.025, 0.025),
                                       pos=(0.44, 0, 0.56),
                                       relief=DGG.FLAT,
                                       command=self.hideOtherAvatarFrame)
        self.hideButton.setTransparency(TransparencyAttrib.MAlpha)
        self.hideButton.reparentTo(self.otherAvatarFrame)
        
        self.scrollBar = DirectSlider(pos=(0.47, 0, -0.04),
                                       scale=0.13,
                                       value=1,
                                       range=(1, 0),
                                       scrollSize=1,
                                       frameSize=(-0.05, 0.05, -3.8, 3.8),
                                       pageSize=1,
                                       orientation=DGG.VERTICAL,
                                       thumb_frameSize=(-0.1, 0.1, -0.2, 0.2),
                                       thumb_relief=DGG.FLAT)
#                                       command = self.scrollChatLog )
        self.scrollBar.reparentTo(self.otherAvatarFrame)   
        
    def hideOtherAvatarFrame(self): 
        self.otherAvatarFrame.hide()
    
    def showOtherAvatarFrame(self):
        self.otherAvatarFrame.show()
    
    def toggleOtherAvatarVisibility(self):
        
        if self.otherAvatarFrame.isHidden():
            self.otherAvatarFrame.show()
        else:
            self.otherAvatarFrame.hide()
            
        
    def applyEffect(self):
        """
        apply avatar effect
        """
        print 'apply effect'  
    
    def notify(self, message, frameColor):
        """
        Message should limit to 40 characters
        """

        self.defaultBorderColor = (1, 1, 1, 0.2)
        self.msgBubble.setCardColor(self.notificationFrameColor)
        self.msgBubble.setFrameColor(self.defaultBorderColor)

        self.msgBubbleSequence.clearToInitial()

        self.msgBubbleNodePath.reparentTo(aspect2d, -1)
        self.msgBubbleNodePath.setColorScale(1, 1, 1, 1)
        self.msgBubbleNodePath.setPos(self.notificationPos)
        self.msgBubbleSequence = Sequence( Func(self.msgBubble.setText, message),
                                                Wait(5),
                                                self.msgBubbleNodePath.colorScaleInterval(2, (1, 1, 1, 0)),
                                                Func(self.msgBubble.setText, '') )
        self.msgBubbleSequence.start()
        
    def createMessageBubble(self):
        
        self.msgBubble = TextNode('msgBubble-')
        self.msgBubble.setFont(Constants.FONT_TYPE_01)
        self.msgBubble.setText('')
        self.msgBubble.setTextColor(0,0,0,1)
        
        self.msgBubble.setCardAsMargin(0.5, 0.5, 0.5, 0.5)
        self.msgBubble.setFrameAsMargin(0.45, 0.45, 0.45, 0.45)

        self.msgBubble.setCardDecal(True)

        self.msgBubble.setShadow(0.02, 0.02)
        self.msgBubble.setShadowColor(0,0,0,0.3)

        self.msgBubble.setAlign(TextNode.ACenter)

        self.msgBubble.setWordwrap(10)

        self.msgBubbleNodePath = aspect2d.attachNewNode(self.msgBubble, -1)
        self.msgBubbleNodePath.setScale(0.04)
       
    def reposition(self):
        _z1 = self.statButtonPos[2]-0.37
        _z2 = self.avatarPos[2]-0.37
        _z3 = self.otherAvatarPos[2]-0.37
        _z4 = self.notificationPos[2]-0.37
        self.statButton.setPos((self.statButtonPos[0], 0, _z1))
        self.avatar.setPos((self.avatarPos[0], 0, _z2))
        self.otherAvatars.setPos((self.otherAvatarPos[0],0, _z3))  
        self.notificationPos=(self.notificationPos[0], 0, _z4)
        
    def restorePos(self):
        _z4 = self.notificationPos[2]+0.37
        self.statButton.setPos(self.statButtonPos)
        self.avatar.setPos(self.avatarPos)
        self.otherAvatars.setPos(self.otherAvatarPos)  
        self.notificationPos=(self.notificationPos[0], 0, _z4)
        
    def unload(self):
        self.msgBubbleNodePath.removeNode()
        self.msgBubbleSequence.clearToInitial()