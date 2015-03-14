from direct.interval.IntervalGlobal import Func
from direct.interval.IntervalGlobal import Sequence
from direct.interval.IntervalGlobal import Wait
from direct.showbase.DirectObject import DirectObject

from panda3d.core import CollisionHandlerQueue
from panda3d.core import CollisionNode
from panda3d.core import CollisionRay
from panda3d.core import CollisionTraverser
from panda3d.core import TransparencyAttrib

from common.Constants import Constants

class MousePicker3D(DirectObject):

    def __init__(self, world):

        if Constants.DEBUG:
            print 'Loading Mouse Picker 3D...'

        self.worldGui = world
        self.a =[]

        self.keyMap = {'mouse1' : 0,
                       'mouse3' : 0,
                       'control' : 0}

        self.lastTarget = None
        self.lastTargetPoint = (0, 0, 0)

        self.setModels()
        self.setCollision()

        self.markerSequence = Sequence( Func(self.markerObject.show),
                                        Wait(1),
                                        Func(self.markerObject.hide) )

        self.accept('mouse1', self.setKey, ['mouse1', 1])
        self.accept('mouse1-up', self.setKey, ['mouse1', 0])
        self.accept('mouse3', self.setKey, ['mouse3', 1])
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
        self.markerObject.setP(-90)
        self.markerObject.setScale(0.5)
        self.markerObject.setTransparency(TransparencyAttrib.MAlpha)

    def setCollision(self):
        self.cTrav = CollisionTraverser('cTrav-mousePicker')

        self.mousePickerRay = CollisionRay()
        self.mousePickerColliderNode = CollisionNode('mousePickerNode')
        self.mousePickerColliderNode.addSolid(self.mousePickerRay)
        self.mousePickerColliderNode.setFromCollideMask(Constants.MOUSE_CLICK_MASK)
        self.mousePickerColliderNode.setIntoCollideMask(Constants.NO_MASK)
        self.mousePickerColliderNodePath = base.camera.attachNewNode(self.mousePickerColliderNode)

        self.mousePickerHandler = CollisionHandlerQueue()

        self.cTrav.addCollider(self.mousePickerColliderNodePath, self.mousePickerHandler)

        self.cTrav.showCollisions(render)
        self.mousePickerColliderNodePath.show()


    def showMarker(self, targetPoint):
        self.markerObject.setPos(targetPoint)
        self.markerSequence.start()

    def checkMousePicker(self):
        if base.mouseWatcherNode.hasMouse():
            xPos = base.mouseWatcherNode.getMouseX()
            yPos = base.mouseWatcherNode.getMouseY()

            if abs(xPos) <= 1 and abs(yPos) <= 1:
                 
                self.mousePickerRay.setFromLens(base.camNode, xPos, yPos)
                self.cTrav.traverse(render)
                if self.mousePickerHandler.getNumEntries() > 0:
                    self.mousePickerHandler.sortEntries()
                    collisionEntry = self.mousePickerHandler.getEntry(0)
                    targetNodePath = collisionEntry.getIntoNodePath()
                
                    #self.lastTargetPoint = collisionEntry.getSurfacePoint(self.worldGui.env[0].zones[2].getZoneRender())
                    self.lastTargetPoint = collisionEntry.getSurfacePoint(render)
                    # check for mouse click
                    if self.keyMap['mouse1']!=0:
#                        # check if animal was selected
#                        if targetNodePath.hasNetTag('eObject'):
#                            print "its elephant"
#                            object_id = int(targetNodePath.getNetTag('eObject'))
#                            self.keyMap['mouse1'] = 0
#                            self.handleLeftClick(object_id, self.lastTargetPoint)
#                            print targetNodePath.getColorScale(), "<<<<<<<<"
#
#                            targetNodePath.setTransparency(1)
#                            targetNodePath.setColorScale(0.5)
                
                        # check if terrain was selected
                        if targetNodePath.hasNetTag('sObject'):
                            print "its terrain"
                            object_id = int(targetNodePath.getNetTag('sObject'))
                            self.keyMap['mouse1'] = 0
                            self.handleLeftClick(object_id, self.lastTargetPoint)
                            
#                    if self.keyMap['control'] !=0:
#                        self.flag = 1
#                    else:
#                        self.flag = 0


    def handleLeftClick(self, object_id, targetPoint):
        """ IF terrain is selected then move the animals that were previously selected 
        to the new location """
        
        if object_id == 2:
            print "to location", targetPoint
            if self.a:
                print self.worldGui
                self.worldGui.moveAnimal(self.a, targetPoint) 
                self.a = []       # clear the list of animals that were selected
                
        else :
            """ If an animal was selected then keep adding it to the list 
                until the user clicks on the terrain""" 
            print "move animal", object_id
            self.a.append(object_id)


    def handleDestination(self, targetPoint):
        """Set point and click movement destination."""
        # Reveal a marker object as a visual representation of the destination.
        self.showMarker(targetPoint)


    def getTargetPoint(self):
        return self.lastTargetPoint

    def updateRoutine(self, task):
        """A once-per-frame task used to monitor mouse clicking."""
        self.checkMousePicker()

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
