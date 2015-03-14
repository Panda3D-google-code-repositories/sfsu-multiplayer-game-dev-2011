from direct.gui.OnscreenText import OnscreenText
from direct.interval.IntervalGlobal import LerpPosInterval
from direct.interval.IntervalGlobal import Parallel

from panda3d.core import Point2
from panda3d.core import Point3
from panda3d.core import TextNode

from common.Constants import Constants

class FloatingText:

    def __init__(self, align = TextNode.ACenter):

        self.align = align

        self.textList = []
        self.newTextList = []

        self.targetPosition = (0, 0, 0)

        taskMgr.doMethodLater(0.75, self.createTextTask, 'createTextTask')
        taskMgr.add(self.updateRoutine, 'updateRoutine-FloatingText', 35)

    def createPendingText(self, type, text):

        self.newTextList.append((type, text))

    def createText(self, type, text, target):

        textNode = aspect2d.attachNewNode('textNode', -2)

        floatingText = OnscreenText( text = text,
                                     scale = 0.1,
                                     fg = Constants.TEXT_COLOR,
                                     shadow = Constants.TEXT_SHADOW_COLOR,
                                     align = self.align,
                                     font = Constants.FONT_TYPE_02 )
        floatingText.reparentTo(textNode)

        if type == Constants.TEXT_TYPE_CRITICAL:
            floatingText['fg'] = Constants.TEXT_TYPE_CRITICAL
        elif type == Constants.TEXT_TYPE_DAMAGE:
            floatingText['fg'] = Constants.TEXT_TYPE_DAMAGE
        elif type == Constants.TEXT_TYPE_DEATH:
            floatingText['fg'] = Constants.TEXT_TYPE_DEATH
        elif type == Constants.TEXT_TYPE_EXPERIENCE:
            floatingText['fg'] = Constants.TEXT_TYPE_EXPERIENCE
        elif type == Constants.TEXT_TYPE_HEALTH:
            floatingText['fg'] = Constants.TEXT_TYPE_HEALTH
        elif type == Constants.TEXT_TYPE_LEVEL_UP:
            floatingText['fg'] = Constants.TEXT_TYPE_LEVEL_UP
        elif type == Constants.TEXT_TYPE_MONEY:
            floatingText['fg'] = Constants.TEXT_TYPE_MONEY
        elif type == Constants.TEXT_TYPE_BIRTH:
            floatingText['fg'] = Constants.TEXT_TYPE_BIRTH
        textSequence = Parallel( LerpPosInterval( floatingText, 3,
                                                  Point3(0, 0, floatingText.getZ() + 0.3),
                                                  other = textNode ),
                                 floatingText.colorScaleInterval(3, (1, 1, 1, 0)) )
        textSequence.start()

        if target:
            targetPosition = target.getPos()
            targetPosition.setZ(render.getRelativePoint(target, target.upperBound).getZ() + 0.75)
            static = False
        else:
            targetPosition = self.targetPosition
            static = True
            floatingText['scale'] = 0.065

        self.textList.append((targetPosition, textNode, floatingText, textSequence, static))

    def setPosition(self, x, y):
        self.targetPosition = (x, 0, y)

    def map3Dto2D(self, nodePath, position):
        pos2D = Point2()

        if base.camLens.project(base.cam.getRelativePoint(nodePath, position), pos2D):
            return aspect2d.getRelativePoint(render2d, (pos2D.getX(), 0, pos2D.getY()))

    def createTextTask(self, task):

        if len(self.newTextList) > 0:
            textInfo = self.newTextList.pop(0)
            self.createText(textInfo[0], textInfo[1], None)

        return task.again

    def updateRoutine(self, task):

        for i in reversed(range(len(self.textList))):
            floatingText = self.textList[i]

            if floatingText[3].isPlaying():
                if floatingText[4]:
                    position = floatingText[0]
                    floatingText[1].setPos(position)
                else:
                    position = self.map3Dto2D(render, floatingText[0])

                    if position != None:
                        if floatingText[1].getPos() != position:
                            floatingText[1].setPos(position)
                    else:
                        floatingText[1].setZ(10)
            else:
                floatingText[1].removeNode()
                floatingText[2].destroy()

                self.textList.pop(i)

        return task.cont

    def unload(self):

        taskMgr.remove('updateRoutine-FloatingText')

        del self.newTextList[:]

        for i in reversed(range(len(self.textList))):
            floatingText = self.textList.pop(i)

            floatingText[1].removeNode()
            floatingText[2].destroy()
            floatingText[3].clearToInitial()
