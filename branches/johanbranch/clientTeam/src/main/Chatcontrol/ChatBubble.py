
from direct.interval.IntervalGlobal import Func
from direct.interval.IntervalGlobal import Sequence
from direct.interval.IntervalGlobal import Wait

from panda3d.core import TextNode

from common.Constants import Constants

#from util.MiscUtil import MiscUtil

class ChatBubble:

    def __init__(self, target):

        #self.target = target

        self.lastPosition = None

        self.chatBubbleSequence = Sequence()

        self.defaultBoxColor = (1, 1, 1, 0.3)
        self.globalBoxColor = (1, 0.75, 0.8, 0.3)
        self.universalBoxColor = (1, 0.7, 0, 0.3)
        self.worldBoxColor = (0, 0, 0, 0.3)
        self.pvpBoxColor = (0, 0.4, 1, 0.3)

        self.defaultBorderColor = (1, 1, 1, 0.2)
        self.globalBorderColor = (1, 0.75, 0.8, 0.2)
        self.universalBorderColor = (1, 0.7, 0, 0.2)
        self.worldBorderColor = (0, 0, 0, 0.2)
        self.pvpBorderColor = (0, 0.4, 1, 0.2)

        #self.chatBubble = TextNode('chatBubble-' + str(self.target.getID()))
        self.chatBubble = TextNode('chatBubble-')
        self.chatBubble.setFont(Constants.FONT_TYPE_01)
        self.chatBubble.setText('')
        self.chatBubble.setTextColor(Constants.TEXT_COLOR)

        self.chatBubble.setCardAsMargin(0.5, 0.5, 0.5, 0.5)
        self.chatBubble.setFrameAsMargin(0.45, 0.45, 0.45, 0.45)

        self.chatBubble.setCardDecal(True)

        self.chatBubble.setShadow(0.05, 0.05)
        self.chatBubble.setShadowColor(Constants.TEXT_SHADOW_COLOR)

        self.chatBubble.setAlign(TextNode.ACenter)

        self.chatBubble.setWordwrap(12)

        self.chatBubbleNodePath = aspect2d.attachNewNode(self.chatBubble, -1)
        self.chatBubbleNodePath.setScale(0.05)

        #taskMgr.add(self.updateRoutine, 'updateRoutine-ChatBubble-' + str(self.target.getID()), -30)

    def setText(self, type, msg, fade):

        #if type == Constants.CMSG_GLOBAL_CHAT:
        #    self.chatBubble.setCardColor(self.globalBoxColor)
        #    self.chatBubble.setFrameColor(self.globalBorderColor)
        if type == Constants.CMSG_UNIVERSAL_CHAT:
            self.chatBubble.setCardColor(self.universalBoxColor)
            self.chatBubble.setFrameColor(self.universalBorderColor)
        elif type == Constants.CMSG_PVPWORLD_CHAT:
            self.chatBubble.setCardColor(self.worldBoxColor)
            self.chatBubble.setFrameColor(self.worldBorderColor)
        elif type == Constants.CMSG_PVPGAME_CHAT:
            self.chatBubble.setCardColor(self.pvpBoxColor)
            self.chatBubble.setFrameColor(self.pvpBorderColor)
        else:
            self.chatBubble.setCardColor(self.defaultBoxColor)
            self.chatBubble.setFrameColor(self.defaultBorderColor)

        self.chatBubbleSequence.clearToInitial()

        self.chatBubbleNodePath.reparentTo(aspect2d, -1)
        self.chatBubbleNodePath.setColorScale(1, 1, 1, 1)

        if fade:
            print 'ChatBubble: fade: set text to chat log'
            self.chatBubbleSequence = Sequence( Func(self.chatBubble.setText, msg),
                                                Wait(5),
                                                self.chatBubbleNodePath.colorScaleInterval(2, (1, 1, 1, 0)),
                                                Func(self.chatBubble.setText, '') )
            self.chatBubbleSequence.start()
        else:
            print 'ChatBubble: set text to chat log'
            self.chatBubble.setText(msg)

    def getText(self):

        return self.chatBubble.getText()

    def clear(self):

        self.chatBubbleSequence.clearToInitial()
        self.chatBubble.setText('')

    def updateRoutine(self, task):

        targetPosition = self.target.getPos()
        targetPosition.setZ(render.getRelativePoint(self.target, self.target.upperBound).getZ() + 0.5)

        position = MiscUtil.map3Dto2D(render, targetPosition)

        if position != None:
            position.setZ(position.getZ() + 0.0575 * (len(self.chatBubble.getWordwrappedText().split('\n'))))

            if position != self.lastPosition:
                self.lastPosition = position
                self.chatBubbleNodePath.setPos(position)
        else:
            self.chatBubbleNodePath.setZ(10)

        return task.cont

    def unload(self):

        taskMgr.remove('updateRoutine-ChatBubble-' + str(self.target.getID()))

        self.chatBubbleNodePath.removeNode()

        self.chatBubbleSequence.clearToInitial()
