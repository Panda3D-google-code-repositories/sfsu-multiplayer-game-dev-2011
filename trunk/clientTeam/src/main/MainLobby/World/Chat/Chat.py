from random import uniform

from direct.gui.DirectEntryScroll import DirectEntryScroll
from direct.gui.DirectFrame import DirectFrame
from direct.gui.DirectGui import DGG
from direct.gui.DirectSlider import DirectSlider

from panda3d.core import TextNode

from common.Constants import Constants
from common.DirectBasicButton import DirectBasicButton
from common.DirectBasicLabel import DirectBasicLabel
from common.DirectTextField import DirectTextField
from common.DirectWindow import DirectWindow

class Chat:
    
    def __init__(self, parent):

        self.parent = parent

        self.msgList = []
        self.colorList = {}

        self.itemList = []

        self.maxItemsVisible = 7

        self.textNode = TextNode('textNode')

        self.createMainFrame()
        self.createScrollBar()
        self.createEntry()

        main.getGlobalControls().accept('enter', self.enterKey)

    def createMainFrame(self):

        self.mainFrame = DirectWindow( frameSize = (-0.6, 0.6, -0.2, 0.2),
                                       frameColor = (0, 0, 0, 0),
                                       pos = (0.95, 0, -0.775) )
#        self.mainFrame.reparentTo(self.parent)

    def createScrollBar(self):
        
        self.scrollBar = DirectSlider( pos = (0.585, 0, 0.155),
                                       range = (1, 0),
                                       scrollSize = 1,
                                       orientation = DGG.VERTICAL,
                                       frameSize = (-0.01, 0.01, -0.245, 0.245),
                                       thumb_frameSize = (-0.015, 0.015, -0.015, 0.015),
                                       thumb_relief = DGG.FLAT,
                                       command = self.scrollList )
        self.scrollBar.reparentTo(self.mainFrame) 
        self.scrollBar.hide()

    def scrollList(self):

        sliderValue = int(self.scrollBar['value'])

        for i in range(len(self.itemList)):
            item = self.itemList[i]

            if len(self.itemList) <= self.maxItemsVisible:
                item.setZ(-0.056 + (len(self.itemList) - 1 - i) * 0.07)
            else:
                item.setZ(0.364 - (i - sliderValue) * 0.07)

            if i < sliderValue or i >= sliderValue + self.maxItemsVisible:
                item.hide()
            else:
                item.show()

    def updateScrollBar(self):

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

    def createItem(self, type, message, color):

        self.textNode.setWordwrap(23)
        self.textNode.setText(message)

        for partial in self.textNode.getWordwrappedText().split('\n'):
            itemLabel = DirectBasicLabel( text = partial,
                                          text_align = TextNode.ALeft,
                                          text_fg = color,
                                          text_font = Constants.FONT_TYPE_01,
                                          text_pos = (-0.57, -0.015),
                                          text_scale = 0.045,
                                          text_shadow = Constants.TEXT_SHADOW_COLOR,
                                          frameSize = (-0.6, 0.6, -0.035, 0.035),
                                          frameColor = (0, 0, 0, 0),
                                          pos = (0, 0, -0.056 - len(self.itemList) * 0.07) )
            itemLabel.reparentTo(self.mainFrame)
            itemLabel.setTag('type', str(type))
            itemLabel.hide()

            self.itemList.append(itemLabel)

        value = self.scrollBar['value']
        range = self.scrollBar['range'][0]
        self.updateScrollBar()

        if value == range or (value == 0 and len(self.itemList) > self.maxItemsVisible):
            self.scrollBar['value'] = self.scrollBar['range'][0]

    def setUserMessage(self, type, name, message):

        self.msgList.append((type, name, message))

        if name in self.colorList:
            color = self.colorList[name]
        else:
            color = (uniform(0.7, 1), uniform(0.7, 1), uniform(0.7, 1), 1)
            self.colorList[name] = color

        self.createItem(type, '[' + name + '] says: ' + message, color)

    def setSystemMessage(self, type, message):

        self.msgList.append((type, message))

        self.createItem(type, message, Constants.TEXT_COLOR)

    def createEntry(self):

        self.chatEntryFrame = DirectFrame( frameSize = (-0.6, 0.6, -0.05, 0.05),
                                           frameColor = Constants.BG_COLOR,
                                           pos = (0, 0, -0.16) )
        self.chatEntryFrame.reparentTo(self.mainFrame)

        self.chatEntry = DirectTextField( self.mainFrame,
                                          text = '',
                                          text_font = Constants.FONT_TYPE_01,
                                          frameColor = (0.8, 0.8, 0.8, 0.4),
                                          width = 90,
                                          command = self.sendEvent,
                                          focusInCommand = self.onFocus,
                                          focusOutCommand = self.onFocusOut )

        self.chatEntryScroll = DirectEntryScroll( self.chatEntry,
                                                  pos = (-0.58, 0, -0.0134),
                                                  scale = 0.05,
                                                  clipSize = (0, 19.5, -1, 1) )
        self.chatEntryScroll.reparentTo(self.chatEntryFrame)

        self.sendButton = DirectBasicButton( text = 'Send',
                                             text_fg = Constants.TEXT_COLOR,
                                             text_font = Constants.FONT_TYPE_01,
                                             text_pos = (0, -0.015),
                                             text_scale = 0.045,
                                             text_shadow = Constants.TEXT_SHADOW_COLOR,
                                             frameSize = (-0.08, 0.08, -0.037, 0.037),
                                             frameColor = (0, 0, 0, 0.2),
                                             pos = (0.5, 0, 0),
                                             relief = DGG.FLAT,
                                             command = self.sendEvent)
        self.sendButton.reparentTo(self.chatEntryFrame)

    def sendEvent(self, message = None):

        if message == None:
            message = self.chatEntry.get()

        message = message.strip(' ')

        self.chatEntry.enterText('')
        self.chatEntry['focus'] = 0

        if len(message) > 0:
            game.requestChat(0, message)

    def enterKey(self):

        if self.chatEntry['frameColor'][3] == 0.4:
            self.chatEntry['focus'] = 1

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
