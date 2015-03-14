from direct.showbase.DirectObject import DirectObject

from panda3d.core import CollisionHandlerQueue
from panda3d.core import CollisionNode
from panda3d.core import CollisionRay
from panda3d.core import CollisionTraverser
from panda3d.core import Vec3

from common.Constants import Constants

class Camera(DirectObject):

    def __init__(self, parent):

        base.disableMouse()

        self.parent = parent

        self.bound = 2
        self.panFactor = 0.75
        self.maxZoom = -5
        self.minZoom = -30
        self.maxRotate = -20
        self.minRotate = -45
        self.scrollFactor = 2
        self.scrollRate = 0
        self.maxZoomCount = -5
        self.minZoomCount = -30
        self.count = -30

        self.camera = render.attachNewNode('CameraNode')
        base.camera.reparentTo(self.camera)
        base.camera.setY(self.minZoom)
        self.camera.setP(-45)
#        self.camera.setP(-25)
        self.camera.setX(10)
        self.camera.setY(10)
#        self.camera.setPos(10, 10, self.parent.listOfEnv[1].getElevation(10, 10))

        self.prevPos = self.camera.getPos()

        self.createCollision()

        self.keyList = {'arrow_up'      : 0,
                        'arrow_down'    : 0,
                        'arrow_left'    : 0,
                        'arrow_right'   : 0,
                        'mouse_up'      : 0,
                        'mouse_down'    : 0,
                        'mouse_left'    : 0,
                        'mouse_right'   : 0}

        self.accept('wheel_up', self.setScrollRate, [1])
        self.accept('wheel_down', self.setScrollRate, [-1])
        
#        self.accept('mouse1', self.setMouse1Pressed, [1])
#        self.accept('mouse1-up', self.setMouse1Pressed, [-1])
#        
#        self.accept('mouse2', self.setMouse2Pressed, [1])
#        self.accept('mouse2-up', self.setMouse2Pressed, [-1])

        self.accept('arrow_up', self.setKey, ['arrow_up', 1])
        self.accept('arrow_up-up', self.setKey, ['arrow_up', 0])
        self.accept('arrow_down', self.setKey, ['arrow_down', 1])
        self.accept('arrow_down-up', self.setKey, ['arrow_down', 0])
        self.accept('arrow_left', self.setKey, ['arrow_left', 1])
        self.accept('arrow_left-up', self.setKey, ['arrow_left', 0])
        self.accept('arrow_right', self.setKey, ['arrow_right', 1])
        self.accept('arrow_right-up', self.setKey, ['arrow_right', 0])

        self.accept('space', self.resetPosition)

        taskMgr.doMethodLater(1.0, self.updateTask, 'updateTask')

#    def setMouse1Pressed(self,value):
#        #print "Left",self.count
#        if(self.count > -5):
#            return
#        else:
#            self.count = self.count + 1
#            base.camera.setY(self.count)
#    
#    def setMouse2Pressed(self,value):
#        #print "Right",self.count
#        self.count = -30
#        base.camera.setY(self.count)

    def resetPosition(self):
        self.camera.setX(10)
        self.camera.setY(10)

    def setKey(self, key, value):
        self.keyList[key] = value

    def createCollision(self):

        self.cTrav = CollisionTraverser('cTrav-Camera')

        self.camGroundRayNode = CollisionNode('CameraRay')
        self.camGroundRayNode.addSolid(CollisionRay(0, 0, 3, 0, 0, -1))
        self.camGroundRayNode.setFromCollideMask(Constants.ZONE_MASK)
        self.camGroundRayNode.setIntoCollideMask(Constants.NO_MASK)
        self.camGroundRay = render.attachNewNode(self.camGroundRayNode)
        self.camGroundRay.setPos(self.camera.getPos())

        self.camGroundHandler = CollisionHandlerQueue()
        self.cTrav.addCollider(self.camGroundRay, self.camGroundHandler)

    def setScrollRate(self, value):
        self.scrollRate = self.scrollRate + value

    def checkMouse(self):

        if base.mouseWatcherNode.hasMouse():
            xPos = base.mouseWatcherNode.getMouseX()
            yPos = base.mouseWatcherNode.getMouseY()

            self.keyList['mouse_up'] = int(yPos > self.bound)
            self.keyList['mouse_down'] = int(yPos < -self.bound)
            self.keyList['mouse_left'] = int(xPos < -self.bound)
            self.keyList['mouse_right'] = int(xPos > self.bound)
        else:
            self.keyList['mouse_up'] = 0
            self.keyList['mouse_down'] = 0
            self.keyList['mouse_left'] = 0
            self.keyList['mouse_right'] = 0

    def checkGround(self):

        self.camGroundRay.setPos(self.camera.getPos())
        self.cTrav.traverse(render)

        if self.camGroundHandler.getNumEntries() > 0:
            self.camGroundHandler.sortEntries()
            collisionEntry = self.camGroundHandler.getEntry(0)

            if collisionEntry != None:
                return True

        return False

    def updateTask(self, task):

        self.checkMouse()

        vAxisK = self.keyList['arrow_up'] - self.keyList['arrow_down']
        hAxisK = self.keyList['arrow_right'] - self.keyList['arrow_left']

        vAxisM = self.keyList['mouse_up'] - self.keyList['mouse_down']
        hAxisM = self.keyList['mouse_right'] - self.keyList['mouse_left']

        vAxis = vAxisK + vAxisM
        hAxis = hAxisK + hAxisM

        deltaTime = globalClock.getDt() * 50
        moveDirection = Vec3(hAxis, vAxis, 0) * self.panFactor * max(abs((base.camera.getY() - self.maxZoom) / (self.maxZoom - self.minZoom)), 0.2) * deltaTime
        newPos = self.camera.getPos() + moveDirection
#        newPos.setZ(self.parent.listOfEnv[1].getElevation(newPos.getX(), newPos.getY()))
        self.camera.setPos(newPos)

        zoom = max(min(base.camera.getY() + self.scrollRate * self.scrollFactor, self.maxZoom), self.minZoom)
        base.camera.setY(zoom)

        rotate = max(min(self.camera.getP() + self.scrollRate * self.scrollFactor, self.maxRotate), self.minRotate)
        self.camera.setP(rotate)

        self.scrollRate = 0

        if self.checkGround():
            self.prevPos = self.camera.getPos()
        else:
            self.camera.setPos(self.prevPos)

        return task.cont
