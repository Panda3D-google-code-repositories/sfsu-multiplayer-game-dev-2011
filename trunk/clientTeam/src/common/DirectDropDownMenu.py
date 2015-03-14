from direct.gui.DirectFrame import DirectFrame
from direct.gui.DirectGui import DGG
from direct.gui.DirectSlider import DirectSlider
from direct.interval.IntervalGlobal import Sequence
from direct.interval.LerpInterval import LerpFunc

from panda3d.core import TextNode
from panda3d.core import TransparencyAttrib

from common.Constants import Constants
from common.DirectBasicButton import DirectBasicButton
from common.DirectBasicLabel import DirectBasicLabel

class DirectDropDownMenu:

    def __init__(self, frameColor = Constants.BG_COLOR, width = 1, max_items = 10, direction = 'down', command = None):

        self.itemList = []
        self.sequenceList = []

        self.frameColor = frameColor
        self.width = float(width)
        self.maxItemsVisible = max_items
        self.direction = direction
        self.command = command

        self.isHidden = True
        self.currentIndex = -1
        self.textNode = TextNode('textNode')

        self.createMainFrame()
        self.createMenu()
        self.createScrollBar()

    def createMainFrame(self):

        self.mainFrame = DirectFrame( frameSize = (-self.width / 2, self.width / 2, -0.046, 0.046),
                                      frameColor = self.frameColor,
                                      pos = (0, 0, 0),
                                      state = DGG.NORMAL )

        self.mainButton = DirectBasicButton( text = '',
                                             text_fg = Constants.TEXT_COLOR,
                                             text_font = Constants.FONT_TYPE_01,
                                             text_pos = (0, -0.015),
                                             text_scale = 0.045,
                                             text_shadow = Constants.TEXT_SHADOW_COLOR,
                                             image = 'models/arrow.png',
                                             image_scale = (0.025, 1, 0.025),
                                             frameSize = (-0.04, 0.04, -0.04, 0.04),
                                             frameColor = (0, 0, 0, 0.2),
                                             pos = (self.mainFrame['frameSize'][1] - 0.04 - 0.006, 0, 0),
                                             relief = DGG.FLAT,
                                             command = self.toggleMenu,
                                             rolloverSound = None,
                                             clickSound = None )
        self.mainButton.reparentTo(self.mainFrame)
        self.mainButton.setTransparency(TransparencyAttrib.MAlpha)

        if self.direction == 'up':
            self.mainButton.setR(180)
        else:
            self.mainButton.setR(0)

        width = self.width - 0.012 - self.mainButton['frameSize'][1] * 2 - 0.012

        self.mainButtonSeq = self.createGlowSequence(self.mainButton, (0, 0, 0, 0.2), (1, 1, 1, 0.2))

        self.mainLabel = DirectBasicLabel( text = 'None',
                                           text_align = TextNode.ALeft,
                                           text_fg = Constants.TEXT_COLOR,
                                           text_font = Constants.FONT_TYPE_01,
                                           text_pos = (-width / 2 + 0.025, -0.015),
                                           text_scale = 0.045,
                                           text_shadow = Constants.TEXT_SHADOW_COLOR,
                                           frameSize = (-width / 2, width / 2, -0.04, 0.04),
                                           frameColor = (0, 0, 0, 0.2),
                                           pos = (self.mainFrame['frameSize'][0] + width / 2 + 0.006, 0, 0) )
        self.mainLabel.reparentTo(self.mainFrame)

        self.mainLabelSeq = self.createGlowSequence(self.mainLabel, (0, 0, 0, 0.2), (1, 1, 1, 0.2))

    def setFrameColor(self, value, label, fromColor, toColor):

        r = (toColor[0] - fromColor[0]) * value
        g = (toColor[1] - fromColor[1]) * value
        b = (toColor[2] - fromColor[2]) * value
        a = (toColor[3] - fromColor[3]) * value

        label['frameColor'] = (fromColor[0] + r, fromColor[1] + g, fromColor[2] + b, fromColor[3] + a)

    def createGlowSequence(self, label, fromColor, toColor):

        return Sequence( LerpFunc( self.setFrameColor,
                                   duration = 1,
                                   extraArgs = [label, fromColor, toColor] ),
                         LerpFunc( self.setFrameColor,
                                   duration = 1,
                                   extraArgs = [label, toColor, fromColor] ) )

    def createMenu(self):

        self.menuFrame = DirectFrame( frameSize = (self.mainFrame['frameSize'][0], self.mainFrame['frameSize'][1], -0.045, 0),
                                      frameColor = self.frameColor,
                                      state = DGG.NORMAL )
        self.menuFrame.reparentTo(self.mainFrame)
        self.menuFrame.hide()

        self.menuBox = DirectFrame ( frameSize = (self.menuFrame['frameSize'][0] + 0.006, self.menuFrame['frameSize'][1] - 0.006, -0.045 + 0.012, 0),
                                     frameColor = (0, 0, 0, 0.2),
                                     pos = (0, 0, -0.006))
        self.menuBox.reparentTo(self.menuFrame)

        self.menuFrame.setZ(self.mainFrame['frameSize'][2])

    def setItems(self, items):

        for item in items:
            self.createItem(item)

    def setItem(self, item):

        self.createItem(item)

    def startMainButtonGlow(self):
        self.mainButtonSeq.loop()

    def stopMainButtonGlow(self):
        self.mainButtonSeq.finish()

    def startMainLabelGlow(self):
        self.mainLabelSeq.loop()

    def stopMainLabelGlow(self):
        self.mainLabelSeq.finish()

    def startOptionGlow(self, index):
        self.sequenceList[index].loop()

    def stopOptionGlow(self, index):
        self.sequenceList[index].finish()

    def setPos(self, x, y, z):
        self.mainFrame.setPos(x, y, z)

    def reparentTo(self, parent):
        self.mainFrame.reparentTo(parent)

    def createScrollBar(self):

        self.scrollBar = DirectSlider( pos = (self.mainButton.getX(), 0, self.menuBox.getZ()),
                                       range = (1, 0),
                                       scrollSize = 1,
                                       orientation = DGG.VERTICAL,
                                       frameSize = (-0.01, 0.01, -0.35, 0),
                                       thumb_frameSize = (-0.015, 0.015, -0.015, 0.015),
                                       thumb_relief = DGG.FLAT,
                                       command = self.scrollList,
                                       thumb_rolloverSound = None,
                                       thumb_clickSound = None )
        self.scrollBar.reparentTo(self.menuBox, 5)

    def scrollList(self):

        sliderValue = int(self.scrollBar['value'])

        for i in range(len(self.itemList)):
            item = self.itemList[i]
            item.setZ(-0.04 - (i - sliderValue) * 0.08)

            if i < sliderValue or i >= sliderValue + self.maxItemsVisible:
                item.hide()
            else:
                item.show()

    def updateScrollBar(self):

        if len(self.itemList) <= self.maxItemsVisible:
            length = 0.006 + len(self.itemList) * 0.08 + 0.006
            self.menuFrame['frameSize'] = (self.menuFrame['frameSize'][0], self.menuFrame['frameSize'][1], -length, 0)

            length = len(self.itemList) * 0.08
            self.menuBox['frameSize'] = (self.menuBox['frameSize'][0], self.menuBox['frameSize'][1], -length, 0)

            self.scrollBar['frameSize'] = (-0.01, 0.01, self.menuBox['frameSize'][2] + 0.012, 0)

            if self.direction == 'up':
                self.menuFrame.setZ(-self.mainFrame['frameSize'][2] + length + 0.012)

        if len(self.itemList) > self.maxItemsVisible:
            self.scrollBar.show()

            percent = min(1.0, float(self.maxItemsVisible) / len(self.itemList))
            self.scrollBar['thumb_frameSize'] = (self.scrollBar['thumb_frameSize'][0],
                                                 self.scrollBar['thumb_frameSize'][1],
                                                 self.scrollBar['frameSize'][2] * percent,
                                                 self.scrollBar['frameSize'][3] * percent)
        else:
            self.scrollBar.hide()

        self.scrollBar['range'] = (max(1, len(self.itemList) - self.maxItemsVisible), 0)

    def createItem(self, name):

        self.textNode.setText(name)
        width = self.mainLabel['frameSize'][1] * 35

        if self.textNode.getWidth() < width:
            text = name
        else:
            text = name[:int(width * 2)] + '...'

        itemLabel = DirectBasicButton( text = text,
                                       text_align = TextNode.ALeft,
                                       text_fg = Constants.TEXT_COLOR,
                                       text_font = Constants.FONT_TYPE_01,
                                       text_pos = (0, -0.015),
                                       text_scale = 0.045,
                                       text_shadow = Constants.TEXT_SHADOW_COLOR,
                                       frameSize = (self.menuBox['frameSize'][0], self.menuBox['frameSize'][1], -0.04, 0.04),
                                       frameColor = (0, 0, 0, 0),
                                       relief = DGG.FLAT,
                                       pos = (0, 0, -0.04 - len(self.itemList) * 0.08),
                                       command = self.selectOption,
                                       extraArgs = [name],
                                       rolloverSound = None,
                                       clickSound = None )
        itemLabel.reparentTo(self.menuBox)
        itemLabel['text_pos'] = (itemLabel['frameSize'][0] + 0.025, -0.015)

        itemLabel.setTag('name', name)

        self.itemList.append(itemLabel)

        itemLabelSeq = self.createGlowSequence(itemLabel, (0, 0, 0, 0), (1, 1, 1, 0.2))
        self.sequenceList.append(itemLabelSeq)

        self.updateScrollBar()

    def showMenu(self):

        if len(self.itemList) > 0:
            self.menuFrame.show()
        self.isHidden = False

        if self.direction == 'up':
            self.mainButton.setR(0)
        else:
            self.mainButton.setR(180)

    def hideMenu(self):

        if len(self.itemList) > 0:
            self.menuFrame.hide()
        self.isHidden = True

        if self.direction == 'up':
            self.mainButton.setR(180)
        else:
            self.mainButton.setR(0)

    def toggleMenu(self):

        if self.isHidden:
            self.showMenu()
        else:
            self.hideMenu()

    def setOption(self, label):

        self.mainLabel['text'] = label['text']
        self.hideMenu()

    def removeOption(self, index):

        label = self.itemList[index]
        label.destroy()

        del self.itemList[index]
        del self.sequenceList[index]

        if len(self.itemList) > 0:
            self.selectOptionByIndex(0)
            self.updateScrollBar()
        else:
            self.mainLabel['text'] = 'None'

    def selectOption(self, name):

        for i in range(len(self.itemList)):
            label = self.itemList[i]
            if label.getNetTag('name') == name:
                self.selectOptionByIndex(i)

    def selectOptionByIndex(self, index):

        self.setOption(self.itemList[index])

        if self.command:
            apply(self.command, [index])

        self.currentIndex = index

    def getCurrentIndex(self):
        return self.currentIndex

    def getOptionLabel(self, index):
        return self.itemList[index]
