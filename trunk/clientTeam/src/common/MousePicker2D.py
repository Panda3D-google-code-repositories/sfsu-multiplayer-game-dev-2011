#@PydevCodeAnalysisIgnore

from direct.gui.DirectGui import DGG
from direct.gui.DirectGui import DirectFrame
from direct.gui.DirectGui import DirectLabel
from direct.showbase.DirectObject import DirectObject

from panda3d.core import CollisionHandlerQueue
from panda3d.core import CollisionNode
from panda3d.core import CollisionRay
from panda3d.core import CollisionTraverser
from panda3d.core import TextNode

from common.Constants import Constants
from common.DirectBasicButton import DirectBasicButton

class MousePicker2D(DirectObject):

    def __init__(self):

        if Constants.DEBUG:
            print 'Loading Mouse Picker 2D...'

        self.lastFrame = None
        self.lastLine = None
        self.lastDropBox = None
        self.lastDropLineSlot = -1

        self.lastDropSlot = -1
        self.lastDropFrame = None

        self.lastDragSlot = -1
        self.lastDragSlotSource = None

        self.target = None

        self.charMenuButton = []

        self.maxWidth = 13

        self.createMouseNode()
        self.createDescriptionBox()
        self.createCharacterMenu()

        self.setCollision()

        self.accept('mouse1', self.handleLeftClick)
        self.accept('mouse1-up', self.handleLeftClickUp)
        self.accept('mouse3', self.handleRightClick)

        taskMgr.add(self.updateRoutine, 'updateRoutine-MousePicker2D')

    def setCollision(self):

        self.cTrav = CollisionTraverser('cTrav-mousePicker2D')

        self.mousePickerRay = CollisionRay()
        self.mousePickerColliderNode = CollisionNode('mousePickerNode2D')
        self.mousePickerColliderNode.addSolid(self.mousePickerRay)
        self.mousePickerColliderNode.setFromCollideMask(Constants.MOUSE_CLICK_MASK)
        self.mousePickerColliderNode.setIntoCollideMask(Constants.NO_MASK)
        self.mousePickerColliderNodePath = base.camera2d.attachNewNode(self.mousePickerColliderNode)

        self.mousePickerHandler = CollisionHandlerQueue()

        self.cTrav.addCollider(self.mousePickerColliderNodePath, self.mousePickerHandler)

#        self.cTrav.showCollisions(render2d)
#        self.mousePickerColliderNodePath.show()

    def createMouseNode(self):

        self.mouseNode = aspect2d.attachNewNode('mouseNode', 10)

        self.textNode = TextNode('textNode')
        self.textNode.setWordwrap(self.maxWidth)

    def createDescriptionBox(self):

        self.descriptionBox = DirectFrame( frameSize = (0, 0.6, -0.1, 0),
                                           frameColor = Constants.BG_COLOR,
                                           pos = (0, 0, 0) )
        self.descriptionBox.reparentTo(self.mouseNode)
        self.descriptionBox.hide()

        self.textBox = DirectLabel( text = '',
                                    text_align = TextNode.ALeft,
                                    text_fg = Constants.TEXT_COLOR,
                                    text_pos = (0.03, -0.06),
                                    text_scale = 0.05,
                                    text_wordwrap = self.maxWidth,
                                    frameSize = (0, 0.58, -0.08, 0),
                                    frameColor = (0, 0, 0, 0.3),
                                    pos = (0.01, 0, -0.01) )
        self.textBox.reparentTo(self.descriptionBox)

    def createCharacterMenu(self):

        self.charMenuBox = DirectFrame( frameSize = (0, 0.4, -0.1, 0),
                                        frameColor = Constants.BG_COLOR,
                                        pos = (0, 0, 0.05) )
        self.charMenuBox.hide()

        charMenuList = ['Trade', 'Add Friend', 'Add Party', 'Follow', 'Duel']

        for i in range(len(charMenuList)):
            charMenuButton = DirectBasicButton( text = charMenuList[i],
                                                text_align = TextNode.ALeft,
                                                text_fg = Constants.TEXT_COLOR,
                                                text_font = Constants.FONT_TYPE_01,
                                                text_pos = (0.03, -0.06),
                                                text_scale = 0.045,
                                                text_shadow = Constants.TEXT_SHADOW_COLOR,
                                                frameSize = (0, 0, 0, 0),
                                                frameColor = (0, 0, 0, 0.3),
                                                pos = (0.01, 0, -0.01 - i * 0.085),
                                                relief = DGG.FLAT,
                                                command = self.selectCharacterMenu,
                                                extraArgs = [i] )
            charMenuButton.reparentTo(self.charMenuBox)

            self.charMenuButton.append(charMenuButton)

    def mouseNodeTask(self):
        """Attaches a node at the mouse cursor by repositioning.

        If the mouse cursor is within the window, reposition the node at the
        current location of the mouse cursor. This node will be used for
        dragging GUI elements that are present in the game.

        """
        if base.mouseWatcherNode.hasMouse():
            xPos = base.mouseWatcherNode.getMouseX()
            yPos = base.mouseWatcherNode.getMouseY()

            if abs(xPos) <= 1 and abs(yPos) <= 1:
                self.mouseNode.setPos(render2d, xPos, 0, yPos)

    def checkMousePicker(self):

        if base.mouseWatcherNode.hasMouse():
            xPos = base.mouseWatcherNode.getMouseX()
            yPos = base.mouseWatcherNode.getMouseY()

            if abs(xPos) <= 1 and abs(yPos) <= 1:
                self.mousePickerRay.setFromLens(base.cam2d.node(), xPos, yPos)

                self.cTrav.traverse(render2d)

                if self.mousePickerHandler.getNumEntries() > 0:
                    self.mousePickerHandler.sortEntries()
                    collisionEntry = self.mousePickerHandler.getEntry(0)

                    targetNodePath = collisionEntry.getIntoNodePath()

                    if targetNodePath.hasNetTag('itemSlotObject'):
                        frame_type = int(targetNodePath.getNetTag('itemSlotObject').split(':')[0])
                        item_slot = int(targetNodePath.getNetTag('itemSlotObject').split(':')[1])
                        self.handleItemSlot(frame_type, item_slot)
                    elif targetNodePath.hasNetTag('itemBoxCard'):
                        frame_type = int(targetNodePath.getNetTag('itemBoxCard'))
                        self.handleBoxCard(frame_type)
                    elif targetNodePath.hasNetTag('lineSlotObject'):
                        box_type = targetNodePath.getNetTag('lineSlotObject').split(':')[0]
                        item_slot = int(targetNodePath.getNetTag('lineSlotObject').split(':')[1])
                        self.handleLineSlot(box_type, item_slot)
                else:
                    self.handleItemSlot(self.lastDropFrame, -1)

    def handleLineSlot(self, box_type, item_slot):

        self.lastDropBox = box_type
        self.lastDropLineSlot = item_slot

    def handleBoxCard(self, frame_type):

        self.lastDropFrame = frame_type
        self.lastDropSlot = 0

    def handleItemSlot(self, frame_type, item_slot):

        self.lastDropFrame = frame_type
        self.lastDropSlot = item_slot

        if self.lastDragSlot != -1:
            if self.lastDropFrame == Constants.MISC_INVENTORY:
                if self.lastDragSlotSource in [Constants.MISC_INVENTORY]:
                    main.envMap['World'].gui.inventory.selectItemSlot(item_slot)
            elif self.lastDropFrame == Constants.MISC_EQUIPMENT:
                if self.lastDragSlotSource in [Constants.MISC_INVENTORY]:
                    main.envMap['World'].gui.equipment.selectItemSlot(item_slot)
            elif self.lastDropFrame == Constants.MISC_HOTKEY:
                if self.lastDragSlotSource in [Constants.MISC_INVENTORY, Constants.MISC_HOTKEY]:
                    main.envMap['World'].gui.hotkeyBar.selectItemSlot(item_slot)
            elif self.lastDropFrame == Constants.MISC_TRADE:
                if self.lastDragSlotSource not in [Constants.MISC_HOTKEY]:
                    main.envMap['World'].gui.trade.selectItemSlot(item_slot)

    def startLineDrag(self, line, param = None):

        self.lastDragSlotSource = line.getParent()
        self.lastLine = line
        self.lastLine.wrtReparentTo(self.mouseNode)

    def stopLineDrag(self):

        currentGameMode = main.getGameMode()

        if currentGameMode != None and self.lastLine != None:
            itemSlot = None

            prevSlot = self.lastDragSlotSource.getNetTag('lineSlotObject').split(':')

            if prevSlot[0] == 'Left':
                if self.lastDropBox == 'Left':
                    itemSlot = currentGameMode.leftCodeLineSlot[self.lastDropLineSlot]
                elif self.lastDropBox == 'Right':
                    itemSlot = currentGameMode.rightCodeLineSlot[self.lastDropLineSlot]

                if itemSlot.getNumChildren() > 0:
                    lineLabel = itemSlot.getChild(0)

                    if currentGameMode.itemList[int(lineLabel.getNetTag('lineLabel'))]['state'] == DGG.NORMAL:
                        if self.lastDropBox == 'Right':
                            currentGameMode.setResultLine(int(self.lastLine.getNetTag('lineLabel')), self.lastDropLineSlot)

                        lineLabel.reparentTo(currentGameMode.leftCodeLineSlot[int(prevSlot[1])])
                    else:
                        itemSlot = self.lastDragSlotSource
                else:
                    if self.lastDropBox == 'Right':
                        currentGameMode.setResultLine(int(self.lastLine.getNetTag('lineLabel')), self.lastDropLineSlot)
            elif prevSlot[0] == 'Right':
                if self.lastDropBox == 'Left':
                    itemSlot = currentGameMode.leftCodeLineSlot[self.lastDropLineSlot]
                elif self.lastDropBox == 'Right':
                    itemSlot = currentGameMode.rightCodeLineSlot[self.lastDropLineSlot]

                if itemSlot.getNumChildren() > 0:
                    lineLabel = itemSlot.getChild(0)

                    if currentGameMode.itemList[int(lineLabel.getNetTag('lineLabel'))]['state'] == DGG.NORMAL:
                        currentGameMode.setResultLine(int(lineLabel.getNetTag('lineLabel')), int(prevSlot[1]))

                        if self.lastDropBox == 'Right':
                            currentGameMode.setResultLine(int(self.lastLine.getNetTag('lineLabel')), self.lastDropLineSlot)

                        lineLabel.reparentTo(currentGameMode.rightCodeLineSlot[int(prevSlot[1])])
                    else:
                        itemSlot = self.lastDragSlotSource
                else:
                    currentGameMode.setResultLine(-1, int(prevSlot[1]))

                    if self.lastDropBox == 'Right':
                        currentGameMode.setResultLine(int(self.lastLine.getNetTag('lineLabel')), self.lastDropLineSlot)

            self.lastLine.reparentTo(itemSlot)
            self.lastLine.setPos(0, 0, 0)
            self.lastLine = None

    def startFrameDrag(self, frame, param = None):

        self.lastFrame = frame
        self.lastFrame.wrtReparentTo(self.mouseNode)

    def stopFrameDrag(self):

        if self.lastFrame != None:
            self.lastFrame.wrtReparentTo(aspect2d)
            self.lastFrame = None

    def startItemDrag(self, source, item, param = None):

        if item.getItemState():
            self.handleHoverExit()
            self.lastDragSlotSource = source
            self.lastDragSlot = item.getSlot()

            item.wrtReparentTo(self.mouseNode)
            item.setState(DGG.DISABLED)

    def stopItemDrag(self):

        if self.lastDragSlot != -1:
            if self.lastDragSlotSource == Constants.MISC_INVENTORY:
                self.handleInventory()
            elif self.lastDragSlotSource == Constants.MISC_HOTKEY:
                self.handleHotkeyBar()
            elif self.lastDragSlotSource == Constants.MISC_TRADE:
                self.handleTrade()

            self.lastDragSlot = -1

        if self.lastDropFrame == Constants.MISC_INVENTORY:
            main.envMap['World'].gui.inventory.selectItemSlot(self.lastDragSlot)
        elif self.lastDropFrame == Constants.MISC_EQUIPMENT:
            main.envMap['World'].gui.equipment.selectItemSlot(self.lastDragSlot)
        elif self.lastDropFrame == Constants.MISC_HOTKEY:
            main.envMap['World'].gui.hotkeyBar.selectItemSlot(self.lastDragSlot)
        elif self.lastDropFrame == Constants.MISC_TRADE:
            main.envMap['World'].gui.trade.selectItemSlot(self.lastDragSlot)

    def isOverRegion(self):
        return base.mouseWatcherNode.isOverRegion(base.mouseWatcherNode.getMouseX(), base.mouseWatcherNode.getMouseY())

    def handleLeftClick(self):

        self.charMenuBox.hide()

    def handleLeftClickUp(self):

        self.stopFrameDrag()

        if 'World' in main.envMap:
            self.stopItemDrag()
            self.stopLineDrag()

    def handleRightClick(self):

        self.charMenuBox.hide()

    def handleInventory(self):

        item = main.envMap['World'].gui.inventory.getItem(self.lastDragSlot)

        if item != None:
            itemSlot = main.envMap['World'].gui.inventory.getItemSlot(self.lastDragSlot)

            item.reparentTo(itemSlot.getParent())
            item.setPos(itemSlot.getPos())
            item.setState(DGG.NORMAL)

            if not self.isOverRegion():
                main.envMap['World'].gui.inventory.throwItem(item.getInventoryID())
            elif self.lastDropSlot != -1:
                if self.lastDropFrame == Constants.MISC_INVENTORY:
                    if self.lastDropSlot != self.lastDragSlot:
                        main.envMap['World'].gui.inventory.moveItem(item.getInventoryID(), self.lastDropSlot)
                elif self.lastDropFrame == Constants.MISC_EQUIPMENT:
                    main.envMap['World'].gui.equipment.setEquipment(self.lastDropSlot, item.getInventoryID())
                elif self.lastDropFrame == Constants.MISC_HOTKEY:
                    main.envMap['World'].gui.hotkeyBar.checkItem(self.lastDropSlot, item)
                elif self.lastDropFrame == Constants.MISC_SHOP:
                    main.envMap['World'].npcShop.handleSell(item.getInventoryID())
                elif self.lastDropFrame == Constants.MISC_TRADE:
                    main.envMap['World'].gui.trade.setTradeItem(item, self.lastDropSlot)

    def handleHotkeyBar(self):

        item = main.envMap['World'].gui.hotkeyBar.getItem(self.lastDragSlot)

        if item != None:
            itemSlot = main.envMap['World'].gui.hotkeyBar.getItemSlot(self.lastDragSlot)

            item.reparentTo(itemSlot.getParent())
            item.setPos(itemSlot.getPos())
            item.setState(DGG.NORMAL)

            if not self.isOverRegion():
                main.envMap['World'].gui.hotkeyBar.removeItem(self.lastDragSlot)
            elif self.lastDropSlot != -1:
                if self.lastDropSlot != self.lastDragSlot:
                    if self.lastDropFrame == Constants.MISC_HOTKEY:
                        main.envMap['World'].gui.hotkeyBar.moveItem(self.lastDragSlot, self.lastDropSlot)

    def handleTrade(self):

        item = main.envMap['World'].gui.trade.getItem(self.lastDragSlot)

        if item != None:
            itemSlot = main.envMap['World'].gui.trade.getItemSlot(self.lastDragSlot)

            item.reparentTo(itemSlot.getParent())
            item.setPos(itemSlot.getPos())
            item.setState(DGG.NORMAL)

            if not self.isOverRegion():
                main.envMap['World'].gui.trade.throwItem(item.getInventoryID())

    def handleTextHoverEnter(self, itemLabel, text, param = None):

        if text != '':
            self.textNode.setText(text)

            lineWidth = self.textNode.getWidth()
            numLines = len(self.textNode.getWordwrappedText().split('\n'))

            self.descriptionBox['frameSize'] = (0, 0.05 * lineWidth + 0.08, -0.05 * numLines - 0.06, 0)

            self.textBox['text'] = text
            self.textBox['frameSize'] = (0, 0.05 * lineWidth + 0.06, -0.05 * numLines - 0.04, 0)

            if itemLabel.getParent() != self.mouseNode:
                self.descriptionBox.show()

    def handleHoverExit(self):

        self.descriptionBox.hide()

    def checkMousePosition(self):

        width = abs(self.descriptionBox['frameSize'][1])
        height = abs(self.descriptionBox['frameSize'][2])

        xPos = yPos = 0

        xMaxBound = base.camLens.getAspectRatio()
        yMaxBound = -1

        if self.mouseNode.getX() > xMaxBound - width:
            xPos = xMaxBound - self.mouseNode.getX() - width

        if self.mouseNode.getZ() < yMaxBound + height:
            yPos = yMaxBound - self.mouseNode.getZ() + height

        self.descriptionBox.setPos(xPos, 0, yPos)

    def showCharacterMenu(self, char_id):

        if not base.mouseWatcherNode.isOverRegion():
            self.target = main.envMap['World'].getCharacter(char_id)

            if self.target != None:
                if self.target.getName() in main.envMap['World'].gui.friends.friendsList:
                    self.charMenuButton[1]['text'] = 'Remove Friend'
                else:
                    self.charMenuButton[1]['text'] = 'Add Friend'

                if self.target.getID() in main.envMap['World'].gui.party.partyList:
                    self.charMenuButton[2]['text'] = 'Remove Party'
                else:
                    self.charMenuButton[2]['text'] = 'Add Party'

                textList = ''
                for charMenuButton in self.charMenuButton:
                    textList += charMenuButton['text'] + '\n'

                self.textNode.setText(textList)

                lineWidth = self.textNode.getWidth()
                numLines = len(self.charMenuButton)

                self.charMenuBox['frameSize'] = (0, 0.065 * lineWidth + 0.04, -0.085 * numLines - 0.02, 0)

                for charMenuButton in self.charMenuButton:
                    charMenuButton['frameSize'] = (0, 0.065 * lineWidth + 0.02, -0.085, 0)

                self.charMenuBox.show()

                self.charMenuBox.wrtReparentTo(self.mouseNode)
                self.charMenuBox.wrtReparentTo(aspect2d)

                width = abs(self.charMenuBox['frameSize'][1])
                height = abs(self.charMenuBox['frameSize'][2])

                xPos = self.mouseNode.getX()
                yPos = self.mouseNode.getZ()

                xMaxBound = base.camLens.getAspectRatio()
                yMaxBound = -1

                if self.mouseNode.getX() > xMaxBound - width:
                    xPos = xMaxBound - width

                if self.mouseNode.getZ() < yMaxBound + height:
                    yPos = yMaxBound + height

                self.charMenuBox.setPos(xPos, 0, yPos)

    def selectCharacterMenu(self, option):

        rContents = {'name' : self.target.getName()}

        if self.charMenuButton[option]['text'] == 'Trade':
            main.cManager.sendRequest(Constants.CMSG_TRADE, rContents)
        elif self.charMenuButton[option]['text'] == 'Add Friend':
            main.cManager.sendRequest(Constants.CMSG_BUDDY_ADD, rContents)
        elif self.charMenuButton[option]['text'] == 'Remove Friend':
            main.cManager.sendRequest(Constants.CMSG_BUDDY_REMOVE, rContents)
        elif self.charMenuButton[option]['text'] == 'Add Party':
            main.cManager.sendRequest(Constants.CMSG_PARTY_ADD, rContents)
        elif self.charMenuButton[option]['text'] == 'Remove Party':
            main.cManager.sendRequest(Constants.CMSG_PARTY_REMOVE, rContents)
        elif self.charMenuButton[option]['text'] == 'Follow':
            main.envMap['World'].charHero.isFollow = True
            main.envMap['World'].charHero.chaseTarget = True
            main.envMap['World'].charHero.setTarget(self.target)
        elif self.charMenuButton[option]['text'] == 'Duel':
            main.cManager.sendRequest(Constants.CMSG_DUEL_TOPICS, rContents)

        self.charMenuBox.hide()

    def updateRoutine(self, task):
        """A once-per-frame task used to monitor mouse clicking."""
        self.checkMousePicker()
        self.mouseNodeTask()
        self.checkMousePosition()

        return task.cont

    def unload(self):
        """Unload this instance."""
        if Constants.DEBUG:
            print 'Unloading Mouse Picker 2D...'

        self.ignoreAll()

        taskMgr.remove('updateRoutine-MousePicker2D')

        self.mousePickerColliderNodePath.removeNode()
        self.charMenuBox.destroy()
        self.descriptionBox.destroy()
        self.mouseNode.removeNode()
