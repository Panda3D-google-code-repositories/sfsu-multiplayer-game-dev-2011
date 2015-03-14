from direct.gui.OnscreenText import OnscreenText
from direct.interval.IntervalGlobal import Func
from direct.interval.IntervalGlobal import Sequence
from direct.interval.IntervalGlobal import Wait
from direct.showbase.DirectObject import DirectObject

from panda3d.core import CollisionHandlerEvent
from panda3d.core import CollisionHandlerQueue
from panda3d.core import CollisionNode
from panda3d.core import CollisionRay
from panda3d.core import CollisionSphere
from panda3d.core import CollisionTraverser
from panda3d.core import Point2
from panda3d.core import TextNode
from panda3d.core import TransparencyAttrib

from common.Constants import Constants

class MousePicker(DirectObject):

    def __init__(self, world):

        if Constants.DEBUG:
            print 'Loading Mouse Picker...'

        self.worldGui = world
        self.animalList =[]
        self.selectMarkerList = {}
        self.currentZone = None

        self.keyMap = {'mouse1' : 0,
                       'mouse3' : 0,
                       'control' : 0}

        self.lastTarget = None
        self.lastTargetPoint = (0, 0, 0)

        self.setModels()
        self.createZoneInfo()
        self.setMousePicker()
        self.setMousePickerEvent()

        self.markerSequence = Sequence( Func(self.markerObject.show),
                                        Wait(1),
                                        Func(self.markerObject.hide) )

        self.accept('mouse1', self.handleLeftClick)
        self.accept('control-mouse1', self.handleControlLeftClick)
        self.accept('mouse1-up', self.setKey, ['mouse1', 0])
        self.accept('mouse3', self.handleRightClick)
        self.accept('mouse3-up', self.setKey, ['mouse3', 0])
        self.accept('control', self.setKey, ['control',1])
        self.accept('control-up', self.setKey, ['control',0])

        taskMgr.add(self.updateRoutine, 'updateRoutine-MousePicker')

    def setKey(self, key, value):
        self.keyMap[key] = value

    def setModels(self):
        """Load Mouse Picker model."""
        self.markerObject = loader.loadModel('models/sphere')
        self.markerObject.reparentTo(render)

        self.markerObject.hide()

        self.markerObject.setColor(0.76, 0.82, 0.82, 0.8)
#        self.markerObject.setP(-90)
        self.markerObject.setScale(1.5)
        self.markerObject.setTransparency(TransparencyAttrib.MAlpha)

        self.mouseOverText = TextNode('node name')
        self.mouseOverText.setAlign(TextNode.ACenter)
        self.mouseOverText.setText('Move Here')
        self.mouseOverText.setTextColor(0, 0, 0, 1)
        self.mouseOverText.setFrameColor(0, 0, 1, 1)
        self.mouseOverText.setFrameAsMargin(0.2, 0.2, 0.2, 0.2)
        self.mouseOverText.setCardColor(1, 1, 1, 1)
        self.mouseOverText.setCardAsMargin(0.2, 0.2, 0.2, 0.2)
        self.mouseOverText.setCardDecal(True)

        self.mouseOverTextNodePath = aspect2d.attachNewNode(self.mouseOverText)
        self.mouseOverTextNodePath.setScale(0.045)
        self.mouseOverTextNodePath.hide()

    def createZoneInfo(self):

        self.zoneText = OnscreenText( text = 'User\'s Zone',
                                      scale = 0.1,
                                      pos = (0, 0.75),
                                      fg = Constants.TEXT_COLOR,
                                      shadow = Constants.TEXT_SHADOW_COLOR,
                                      font = Constants.FONT_TYPE_02 )
        self.zoneText.reparentTo(aspect2d)

    def setMousePicker(self):

        self.cTrav = CollisionTraverser('cTrav-mousePicker')

        self.mousePickerRay = CollisionRay()
        self.mousePickerNode = CollisionNode('mousePicker')
        self.mousePickerNode.addSolid(self.mousePickerRay)
        self.mousePickerNode.setFromCollideMask(Constants.MOUSE_CLICK_MASK)
        self.mousePickerNode.setIntoCollideMask(Constants.NO_MASK)
        self.mousePicker = base.camera.attachNewNode(self.mousePickerNode)

        self.mousePickerHandler = CollisionHandlerQueue()
        self.cTrav.addCollider(self.mousePicker, self.mousePickerHandler)

    def setMousePickerEvent(self):

        self.mousePickerEventRay = CollisionRay()
        self.mousePickerEventNode = CollisionNode('mousePickerEvent')
        self.mousePickerEventNode.addSolid(self.mousePickerEventRay)
        self.mousePickerEventNode.setFromCollideMask(Constants.MOUSE_CLICK_MASK)
        self.mousePickerEventNode.setIntoCollideMask(Constants.NO_MASK)
        self.mousePickerEvent = base.camera.attachNewNode(self.mousePickerEventNode)

        self.mousePickerEventHandler = CollisionHandlerQueue()
        self.cTrav.addCollider(self.mousePickerEvent, self.mousePickerEventHandler)

        base.cTrav = CollisionTraverser('cTrav-mousePickerEvent')

        self.mousePickerSphereNode = CollisionNode('mousePickerSphere')
        self.mousePickerSphereNode.addSolid(CollisionSphere(0, 0, 0, 0.1))
        self.mousePickerSphereNode.setFromCollideMask(Constants.MOUSE_CLICK_MASK)
        self.mousePickerSphereNode.setIntoCollideMask(Constants.NO_MASK)
        self.mousePickerSphere = render.attachNewNode(self.mousePickerSphereNode)
        self.mousePickerSphere.show()

        self.mousePickerSphereHandler = CollisionHandlerEvent()
        self.mousePickerSphereHandler.addInPattern('mousePickerEvent-In')
        self.mousePickerSphereHandler.addOutPattern('mousePickerEvent-Out')

        self.accept('mousePickerEvent-In', self.handleMousePickerEvent, [0])
        self.accept('mousePickerEvent-Out', self.handleMousePickerEvent, [1])

        base.cTrav.addCollider(self.mousePickerSphere, self.mousePickerSphereHandler)

    def handleMousePickerEvent(self, status, entry):

        surfacePoint = entry.getSurfacePoint(render)
        targetNodePath = entry.getIntoNodePath()

        type = targetNodePath.getNetTag('type')
        object_id = int(targetNodePath.getNetTag('object_id'))

        if type == 'Terrain':
            print targetNodePath.getName().lstrip('gmm').split('x')

            if status == 0 and self.animalList :
                targetNodePath.getParent().setColorScale(1, 0, 0, 0.5)
                self.currentZone = object_id
                self.zoneText['text'] = 'User ' + str(object_id) + '\'s Zone'
                self.showHoverInfo(surfacePoint)
            else:
                targetNodePath.getParent().setColorScale(1, 1, 1, 1)
        elif type == 'Animal':
            if status == 0:
                targetNodePath.setColorScale(1, 0, 0, 0.5)
            elif status == 1:
                targetNodePath.setColorScale(1, 1, 1, 1)

    def showHoverInfo(self, position):

        pos2D = Point2()

        if base.camLens.project(base.cam.getRelativePoint(render, position), pos2D):
            position = aspect2d.getRelativePoint(render2d, (pos2D.getX(), 0, pos2D.getY()))
        
            self.mouseOverTextNodePath.setPos(position.getX(), 0, position.getZ() + 0.1)
            self.mouseOverTextNodePath.show()

    def showMarker(self, targetPoint):

        self.markerObject.setPos(targetPoint)
        self.markerSequence.start()

    def checkMousePicker(self):

        if base.mouseWatcherNode.hasMouse():
            xPos = base.mouseWatcherNode.getMouseX()
            yPos = base.mouseWatcherNode.getMouseY()

            self.mousePickerRay.setFromLens(base.camNode, xPos, yPos)
            self.cTrav.traverse(render)

            if self.mousePickerHandler.getNumEntries() > 0:
                self.mousePickerHandler.sortEntries()
                collisionEntry = self.mousePickerHandler.getEntry(0)

                return collisionEntry

    def handleLeftClick(self):

        self.keyMap['mouse1'] = 1

        collisionEntry = self.checkMousePicker()

        if collisionEntry != None:
            surfacePoint = collisionEntry.getSurfacePoint(render)
            object = collisionEntry.getIntoNodePath()
            
            type = object.getNetTag('type')
            object_id = int(object.getNetTag('object_id'))

            if type == 'Animal':
                self.selectOneAnimal(object)
            elif type == 'Terrain':
                self.handleTerrain(object_id, surfacePoint)

    def handleControlLeftClick(self):

        self.keyMap['mouse1'] = 1

        collisionEntry = self.checkMousePicker()

        if collisionEntry != None:
            surfacePoint = collisionEntry.getSurfacePoint(render)
            object = collisionEntry.getIntoNodePath()

            type = object.getNetTag('type')
            object_id = int(object.getNetTag('object_id'))

            if type == 'Animal':
                print object.getX(), "********"
                self.selectAnimal(object)

    def handleRightClick(self):

        self.keyMap['mouse3'] = 1

        collisionEntry = self.checkMousePicker()

        if collisionEntry != None:
            surfacePoint = collisionEntry.getSurfacePoint(render)
            targetNodePath = collisionEntry.getIntoNodePath()

            type = targetNodePath.getNetTag('type')
            object_id = int(targetNodePath.getNetTag('object_id'))

            if type == 'Terrain':
                self.handleTerrain(object_id, surfacePoint)

    def createSelectMarker(self):

        selectMarker = loader.loadModel('smiley')
        selectMarker.setColor(0, 1, 0, 1)
        selectMarker.setScale(0.5)
        selectMarker.setTransparency(TransparencyAttrib.MAlpha)

        return selectMarker

    def clearAnimalList(self):

        for animal in self.animalList:
            object_id = int(animal.getNetTag('object_id'))

            self.selectMarkerList[object_id].removeNode()
            del self.selectMarkerList[object_id]

        del self.animalList[:]

    def selectAnimal(self, animal):

        object_id = int(animal.getNetTag('object_id'))

        if animal not in self.animalList:
            self.animalList.append(animal)

            selectMarker = self.createSelectMarker()
            selectMarker.reparentTo(animal)

            newPos = animal.getRelativePoint(animal.getParent(), animal.getTightBounds()[1])
            selectMarker.setZ(newPos.getZ() + 1)

            self.selectMarkerList[object_id] = selectMarker
        else:
            self.animalList.remove(animal)

            self.selectMarkerList[object_id].removeNode()
            del self.selectMarkerList[object_id]

    def selectOneAnimal(self, animal):

        self.clearAnimalList()
        self.selectAnimal(animal)

    def handleTerrain(self, object_id, targetPoint):

        if len(self.animalList) > 0:
            self.showMarker(targetPoint)
#            self.worldGui.moveAnimal(self.animalList, targetPoint)
            first = 1
            for animal in self.animalList:
                if first: 
                    refX = animal.getX(render)
                    refY = animal.getY(render)
                                        
                    animal.setPos(render, targetPoint)
                    
                    first = 0
                else:
                    diffX = refX - animal.getX(render)
                    diffY = refY - animal.getY(render)
                    
                    animal.setX(render, targetPoint.getX()+ diffX)
                    animal.setY(render, targetPoint.getY()+ diffY)
                    animal.setZ(render, targetPoint.getZ())
            self.clearAnimalList()
            self.mouseOverTextNodePath.hide()
        else:
            del self.animalList[:]

    def updateRoutine(self, task):

        if base.mouseWatcherNode.hasMouse():
            xPos = base.mouseWatcherNode.getMouseX()
            yPos = base.mouseWatcherNode.getMouseY()

            self.mousePickerEventRay.setFromLens(base.camNode, xPos, yPos)
            self.cTrav.traverse(render)

            if self.mousePickerEventHandler.getNumEntries() > 0:
                self.mousePickerEventHandler.sortEntries()
                collisionEntry = self.mousePickerEventHandler.getEntry(0)
                surfacePoint = collisionEntry.getSurfacePoint(render)

                self.mousePickerSphere.setPos(surfacePoint)

        return task.cont

    def unload(self):
        """Unload this instance."""
        if Constants.DEBUG:
            print 'Unloading Mouse Picker...'

        self.ignoreAll()

        taskMgr.remove('updateRoutine-MousePicker')

        self.markerObject.removeNode()

        self.mousePickerColliderNodePath.removeNode()

        self.markerSequence.clearIntervals()
