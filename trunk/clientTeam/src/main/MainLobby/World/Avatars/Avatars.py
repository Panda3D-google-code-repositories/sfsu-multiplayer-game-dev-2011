from common.Constants import Constants
from common.DirectBasicButton import DirectBasicButton
from common.DirectControls import DirectControls
from common.DirectWindow import DirectWindow
from direct.gui.DirectGui import DGG
from direct.gui.DirectSlider import DirectSlider
from direct.interval.FunctionInterval import Func, Wait
from direct.interval.MetaInterval import Sequence
from main.MainLobby.World.Avatars.Stats import Stats
from main.MainLobby.World.Avatars.TenDayStats import TenDayStats
from main.MainLobby.World.Avatars.Params import Params
from panda3d.core import TransparencyAttrib, TextNode
from direct.gui.DirectFrame import DirectFrame
from direct.gui.DirectLabel import DirectLabel

class AvatarControls(DirectControls):

    def __init__(self, parent):

        DirectControls.__init__(self, parent)

#        self.accept('e', parent.applyEffect)
#        self.accept('a', parent.toggleOtherAvatarVisibility)

class Avatars:
    
    """
    1). create own avatar and other avatar, and stat button
    2). Implement stat button click
    3). Implement otherAvatar click
    4). Implement the effect of click on own avatar
    5). Implement notification
    """
    def __init__(self, world):
        """
        parent is the mainFrame from game world
        """
        self.world = world
        self.parent = self.world.mainFrame
        self.avatarShown = False
        self.avatarList = []
        self.avatars = []
        self.maxItemsVisible = 11
        self.topIndexOfList = 0
        self.count=0
        self.worldNameObj = {'worldName': self.world.gameState.worldName}
#        self.otherAvatars = []
        self.alertBG = (1, 0.2, 0.2, 0.8)
        self.notificationFrameColor = (0.31, 0.65, 0.76, 0.8)
        self.notificationPos = (-1.24, 0, -0.26)
        self.statButtonPos = (-1.445, 0, -0.44)
        self.paramButtonPos = (-1.375, 0, -0.83)
        self.tenDayStatButtonPos = (-1.475, 0, -0.72)
        self.avatarPos = (-1.375, 0, -0.52)
        self.otherAvatarPos = (-1.31, 0, -0.53)
        self.numOfAvatars = 1
        self.createOwnAvatar()
#        self.createStatButton()
        self.createTenDayStatButton()
        self.createParamButton()
#        self.createOtherAvatars()
        self.stats = Stats(self.world)
        self.tenDayStats = TenDayStats(self.world)
        self.params = Params(self.world)

        self.params.hide()
        self.msgBubbleSequence = Sequence()
        self.createMessageBubble()
        self.control = AvatarControls(self)
        self.createOtherAvatarsListFrame()
        main.msgQ.addToCommandList(Constants.CMSG_ALL_AVATAR_INFO, self.loadAvatarList)
#        _t = Timer(6, self.notify, ['Avatar: this is sample message to test notification features', 
#                                    self.notificationFrameColor])
#        _t.start()
#        
#        _t = Timer(20, self.notify,['Test alert message', self.alertBG])
#        _t.start()

    def loadAvatarList(self, avatars=[]):
        """
        Load list of other avatars from gameState
        """
#        self.count += 10
        self.avatars = avatars
#        for i in range(self.count):
#            self.avatars.append({"charName": "fancy green"+str(i), "avatarType": "weather man", "envScore": str(i)})
        
        if self.maxItemsVisible <= len(self.avatars):
            maxItems = self.maxItemsVisible
        else:
            maxItems = len(self.avatars)
            
        for i in range(maxItems):
            self.avatarList[i][0]['text'] = self.avatars[i]['charName']
            self.avatarList[i][1]['text'] = self.avatars[i]['avatarType']
            self.avatarList[i][2]['text'] = self.avatars[i]['envScore']
   
        self.updateScrollBar()  
        self.avatarShown=True
        self.headerFrame.show()
        
    def createOwnAvatar(self):
        """
        Avatar id is needed for this.
        """
        self.avatarFrame = DirectFrame( frameSize = (-0.126, 0.126, -0.126, 0.126),
                                        frameColor = Constants.BG_COLOR,
                                        pos = self.avatarPos )
        self.avatarFrame.reparentTo(self.parent)

        _avatar = 'models/avatar/1a.png'
        self.avatar = DirectBasicButton( image = _avatar,
                                         image_pos = (0, 0, 0),
                                         image_scale = (0.1, 0.1, 0.1),
                                         frameSize = (-0.12, 0.12, -0.12, 0.12),
                                         frameColor = (0, 0, 0, 0.2),
                                         pos = (0, 0, 0),
                                         rolloverSound = None,
                                         clickSound = None )
        self.avatar.setTransparency(TransparencyAttrib.MAlpha)
        self.avatar.reparentTo(self.avatarFrame)
        
    def createStatButton(self):
        
        self.statButton = DirectBasicButton(text='Stats',
                                            text_fg=(1, 1, 1, 1),
                                            text_font=Constants.FONT_TYPE_01,
                                            text_pos=(0, -0.015),
                                            text_scale=0.04,
                                            text_shadow=Constants.TEXT_SHADOW_COLOR,
                                            frameSize=(-0.08, 0.08, -0.035, 0.035),
                                            frameColor=Constants.BG_COLOR,
                                            pos=self.statButtonPos,
                                            relief=DGG.FLAT,
                                            command=self.showStatFrame)
        self.statButton.setTransparency(TransparencyAttrib.MAlpha)
        self.statButton.reparentTo(self.parent)
        
    def createTenDayStatButton(self):

        self.tenDayStatButtonFrame = DirectFrame( frameSize = (-0.086, 0.086, -0.041, 0.041),
                                                  frameColor = Constants.BG_COLOR,
                                                  pos = self.tenDayStatButtonPos )
        self.tenDayStatButtonFrame.reparentTo(self.parent)

        self.tenDayStatButton = DirectBasicButton(text='Stats',
                                            text_fg=(1, 1, 1, 1),
                                            text_font=Constants.FONT_TYPE_01,
                                            text_pos=(0, -0.015),
                                            text_scale=0.04,
                                            text_shadow=Constants.TEXT_SHADOW_COLOR,
                                            frameSize=(-0.08, 0.08, -0.035, 0.035),
                                            frameColor=(0, 0, 0, 0.2),
                                            pos= (0, 0, 0),
                                            relief=DGG.FLAT,
                                            command=self.showTenDayStatFrame)
        self.tenDayStatButton.reparentTo(self.tenDayStatButtonFrame)
        
    def createParamButton(self):

        self.paramButtonFrame = DirectFrame( frameSize = (-0.106, 0.106, -0.041, 0.041),
                                             frameColor = Constants.BG_COLOR,
                                             pos = self.paramButtonPos )
        self.paramButtonFrame.reparentTo(self.parent)
        
        self.paramButton = DirectBasicButton(text='Params',
                                            text_fg=(1, 1, 1, 1),
                                            text_font=Constants.FONT_TYPE_01,
                                            text_pos=(0, -0.015),
                                            text_scale=0.04,
                                            text_shadow=Constants.TEXT_SHADOW_COLOR,
                                            frameSize=(-0.1, 0.1, -0.035, 0.035),
                                            frameColor=(0, 0, 0, 0.2),
                                            pos= (0, 0, 0),
                                            relief=DGG.FLAT,
                                            command=self.showParamFrame)
        self.paramButton.reparentTo(self.paramButtonFrame)

    def createOtherAvatars(self):
        _avatar = 'models/avatar/1a.png'
        
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
        self.stats.toggleVisibility() 
        
    def showTenDayStatFrame(self):
        self.tenDayStats.toggleVisibility()    
        
    def showParamFrame(self):
        self.params.toggleVisibility()     

    def createOtherAvatarsListFrame(self):

        self.headerFrame = DirectWindow(frameSize=(-0.6, 0.6, -0.04, 0.04),
                                      frameColor=(0.3, 0.3, 0.3, 0.3),
                                      pos=(0, 0, 0.7),
                                      state=DGG.NORMAL)
        self.headerFrame.reparentTo(self.parent)
        self.headerFrame.hide()
        
        self.otherAvatarFrame = DirectFrame(frameSize=(-0.6, 0.6, -0.55, 0.55),
                                      frameColor=Constants.BG_COLOR,
                                      pos=(0, 0, -0.59))
        self.otherAvatarFrame.reparentTo(self.headerFrame)
        
        self.avatarShown = False
        
        self.hideButton = DirectBasicButton(text=" - ",
                                       text_fg=(1, 1, 1, 1),
                                       text_pos=(-0.007, -0.015),
                                       text_scale=0.05,
                                       frameColor=(0, 0, 0, 0.2),
                                       frameSize=(-0.04, 0.04, -0.025, 0.025),
                                       pos=(0.54, 0, 0),
                                       relief=DGG.FLAT,
                                       command=self.hideOtherAvatarFrame)
        self.hideButton.setTransparency(TransparencyAttrib.MAlpha)
        self.hideButton.reparentTo(self.headerFrame)
        self.hideButton.hide()

        self.createInfoHeader()
        self.createListFrame()
        
    def createInfoHeader(self):
        
        self.infoHeader = DirectFrame(frameSize=(-0.59, 0.59, -0.05, 0.05),
                                      pos=(0, 0, 0.49),
                                      frameColor=(0, 0, 0, 0.3))
        self.infoHeader.reparentTo(self.otherAvatarFrame)
        
        labels = []
        for i in range(3):
            labels.append(DirectLabel(text="",
                                       text_fg=(1, 1, 1, 1),
                                        text_font=Constants.FONT_TYPE_01,
                                        text_pos=(0, -0.015),
                                        text_scale=0.05,
                                        text_align=TextNode.ALeft,
                                        text_shadow=Constants.TEXT_SHADOW_COLOR,
                                        frameColor=(0, 0, 0, 0),
                                        pos=(-0.56 + i * 0.4, 0, 0)))
            labels[i].reparentTo(self.infoHeader)
        
        labels[0]['text'] = "CharName"
        labels[1]['text'] = 'Avatar'
        labels[2]['text'] = 'EnvScore' 
    
    def createListFrame(self):
        
        self.listFrame = DirectFrame(frameSize=(-0.59, 0.59, -0.485, 0.485),
                                      pos=(0, 0, -0.055),
                                      frameColor=(0, 0, 0, 0.3))
        self.listFrame.reparentTo(self.otherAvatarFrame)
        
        
        for j in range(self.maxItemsVisible):
            labels = []
            for i in range(3):
                labels.append(DirectLabel(text="",
                                       text_fg=(1, 1, 1, 1),
                                        text_font=Constants.FONT_TYPE_01,
                                        text_pos=(0, -0.015),
                                        text_scale=0.05,
                                        text_align=TextNode.ALeft,
                                        text_shadow=Constants.TEXT_SHADOW_COLOR,
                                        frameColor=(0, 0, 0, 0),
                                        pos=(-0.56 + i * 0.4, 0, 0.43 - j * 0.085)))
                labels[i].reparentTo(self.listFrame)
            self.avatarList.append(labels)
        
        self.scrollBar = DirectSlider(pos=(0.545, 0, 0),
                                       scale=0.13,
                                       value=1,
                                       range=(1, 0),
                                       scrollSize=1,
                                       frameSize=(-0.05, 0.05, -3.5, 3.5),
                                       pageSize=1,
                                       orientation=DGG.VERTICAL,
                                       thumb_frameSize=(-0.1, 0.1, -0.2, 0.2),
                                       thumb_relief=DGG.FLAT,
                                       command = self.scrollAvatarList)
        self.scrollBar.reparentTo(self.listFrame)   
        
    def hideOtherAvatarFrame(self):
         
        self.headerFrame.hide()
        self.avatarShown = False
        del self.avatars[0:]
        
    def showOtherAvatarFrame(self):
        
        if not self.avatarShown :
            main.cManager.sendRequest(Constants.CMSG_ALL_AVATAR_INFO, self.worldNameObj)

    
    def toggleOtherAvatarVisibility(self):
        
        if self.avatarShown == False:
            self.showOtherAvatarFrame()
        else:
            self.hideOtherAvatarFrame()       
        
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
        self.msgBubbleSequence = Sequence(Func(self.msgBubble.setText, message),
                                                Wait(5),
                                                self.msgBubbleNodePath.colorScaleInterval(2, (1, 1, 1, 0)),
                                                Func(self.msgBubble.setText, ''))
        self.msgBubbleSequence.start()
        
    def createMessageBubble(self):
        
        self.msgBubble = TextNode('msgBubble-')
        self.msgBubble.setFont(Constants.FONT_TYPE_01)
        self.msgBubble.setText('')
        self.msgBubble.setTextColor(0, 0, 0, 1)
        
        self.msgBubble.setCardAsMargin(0.5, 0.5, 0.5, 0.5)
        self.msgBubble.setFrameAsMargin(0.45, 0.45, 0.45, 0.45)

        self.msgBubble.setCardDecal(True)

        self.msgBubble.setShadow(0.02, 0.02)
        self.msgBubble.setShadowColor(0, 0, 0, 0.3)

        self.msgBubble.setAlign(TextNode.ACenter)

        self.msgBubble.setWordwrap(10)

        self.msgBubbleNodePath = aspect2d.attachNewNode(self.msgBubble, -1)
        self.msgBubbleNodePath.setScale(0.04)
       
    def reposition(self):
        _z1 = self.statButtonPos[2] - 0.37
        _z2 = self.avatarPos[2] - 0.37
        _z3 = self.otherAvatarPos[2] - 0.37
        _z4 = self.notificationPos[2] - 0.37
        _z5 = self.paramButtonPos[2] - 0.37
        _z6 = self.tenDayStatButtonPos[2] - 0.37
        self.statButton.setPos((self.statButtonPos[0], 0, _z1))
        self.avatar.setPos((self.avatarPos[0], 0, _z2))
        self.otherAvatars.setPos((self.otherAvatarPos[0], 0, _z3))  
        self.notificationPos = (self.notificationPos[0], 0, _z4)
        self.paramButton.setPos((self.paramButtonPos[0],0,_z5))
        self.tenDayStatButton.setPos((self.tenDayStatButtonPos[0],0,_z6))
        
    def restorePos(self):
        _z4 = self.notificationPos[2] + 0.37
        self.statButton.setPos(self.statButtonPos)
        self.avatar.setPos(self.avatarPos)
        self.otherAvatars.setPos(self.otherAvatarPos)  
        self.notificationPos = (self.notificationPos[0], 0, _z4)
        self.paramButton.setPos(self.paramButtonPos)
        self.tenDayStatButton.setPos(self.tenDayStatButtonPos)
        
    def scrollAvatarList(self):
        
        sliderValue = int(round(self.scrollBar['value']))
        self.topIndexOfList = sliderValue
        
        if len(self.avatars) < self.maxItemsVisible:
            maxItems = len(self.avatars)
        else:
            maxItems = self.maxItemsVisible
        
        for i in range(maxItems):
            if len(self.avatars) > self.maxItemsVisible:
                index = sliderValue + i
                self.avatarList[i][0]['text'] = self.avatars[index]['charName']
                self.avatarList[i][1]['text'] = self.avatars[index]['avatarType']
                self.avatarList[i][2]['text'] = self.avatars[index]['envScore']
            else:
                self.avatarList[i][0]['text'] = self.avatars[i]['charName']
                self.avatarList[i][1]['text'] = self.avatars[i]['avatarType']
                self.avatarList[i][2]['text'] = self.avatars[i]['envScore'] 
                       
    def updateScrollBar(self):

        if len(self.avatars) > self.maxItemsVisible:
            if self.scrollBar.isHidden():
                self.scrollBar.show()
                
            scrollRange = len(self.avatars) - self.maxItemsVisible
            
            currentSize = self.scrollBar['thumb_frameSize'][3] - self.scrollBar['thumb_frameSize'][2]
            if currentSize > 0.2:
                scrollRatio = float(self.maxItemsVisible) / len(self.avatars)
                if (scrollRatio * currentSize) > 0.2:
                    self.scrollBar['thumb_frameSize'] = (self.scrollBar['thumb_frameSize'][0],
                                                         self.scrollBar['thumb_frameSize'][1],
                                                         self.scrollBar['frameSize'][2]*scrollRatio,
                                                         self.scrollBar['frameSize'][3]*scrollRatio)
                else:
                    self.scrollBar['thumb_frameSize'] = (self.scrollBar['thumb_frameSize'][0],
                                                         self.scrollBar['thumb_frameSize'][1],
                                                         - 0.1, 0.1)
        else:
            self.scrollBar.hide()
            scrollRange = 1

        self.scrollBar['range'] = (scrollRange, 0) 
              
    def unload(self):
        self.msgBubbleNodePath.removeNode()
        self.msgBubbleSequence.clearToInitial()
        