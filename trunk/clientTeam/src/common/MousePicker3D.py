from math import floor
from math import sqrt
from random import choice

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
from common.DatabaseHelper import DatabaseHelper

class MousePicker3D(DirectObject):

    def __init__(self, world):

        if Constants.DEBUG:
            print 'Loading Mouse Picker...'

        self.gameState = world
        self.animalList =[]
        self.selectMarkerList = {}
        self.currentZone = None

        self.keyMap = {'mouse1' : [0, 0],
                       'mouse3' : [0, 0],
                       'control': [0, 0],
                       'shift'  : [0, 0]}

        self.lastTarget = None
        self.lastTargetPoint = (0, 0, 0)

        self.newObject = None
        self.lastEntry = None

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
        self.accept('shift-mouse1', self.setMultipleKey, [{'shift' : 1, 'mouse1' : 1}])
        self.accept('shift', self.setKey, ['shift', 1])
        self.accept('shift-up', self.setKey, ['shift', 0])
        self.accept('escape', self.removeObjectTask)

        self.EnvID = None
        self.zoneID = None
        self.targetPoint = None
        self.clickOnTerrain = None
        taskMgr.add(self.slowUpdateRoutine, 'slowUpdateRoutine-MousePicker', -10)
        taskMgr.doMethodLater(0.05, self.updateRoutine, 'updateRoutine-MousePicker')
        
        self.animalText = OnscreenText( text = '',
                              scale = 0.07,
                              pos = (0, -0.3),
                              fg = Constants.TEXT_COLOR,
                              shadow = Constants.TEXT_SHADOW_COLOR,
                              font = Constants.FONT_TYPE_01 )
        self.animalText.reparentTo(aspect2d)

    def setKey(self, key, value):

        self.keyMap[key][1] = self.keyMap[key][0]
        self.keyMap[key][0] = value

    def setMultipleKey(self, args):
        for key, value in args.items():
            self.setKey(key, value)

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
        self.zoneText.hide()

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
        self.mousePickerSphereNode.addSolid(CollisionSphere(0, 0, 0, 0.01))
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
        self.EnvID = object_id

        if type == 'Terrain':
            block = targetNodePath.getName().lstrip('gmm').split('x')
            self.zoneID = self.getClickedZoneId(surfacePoint.getX(), surfacePoint.getY())

            if status == 0 and self.animalList :
                self.setHighlight(targetNodePath, block, True)
                self.currentZone = object_id
                self.zoneText['text'] = 'User ' + str(object_id) + '\'s Zone ' + str(self.zoneID)
                self.showHoverInfo(surfacePoint)
            else:
                self.setHighlight(targetNodePath, block, False)
                
        elif type == 'Animal':
            if status == 0:
                targetNodePath.setColorScale(1, 0, 0, 0.5)

                zone = game.listOfZones[game.listOfAnimals[object_id]]
                animal = zone.getAnimal(object_id)
                self.animalText.setText(animal.getName() + ' [' + str(animal.getGroupSize()) + ' / ' + str(zone.totalAnimalList[animal.type]) + ']')
            elif status == 1:
                targetNodePath.setColorScale(1, 1, 1, 1)
                self.animalText.setText('')
 
        elif type == 'Plant':
            if status == 0:
                targetNodePath.setColorScale(1, 0, 0, 0.5)

                zone = game.listOfZones[game.listOfPlants[object_id]]
                plant = zone.getPlant(object_id)
                self.animalText.setText(plant.getName() + ' [' + str(plant.getGroupSize()) + ' / ' + str(zone.totalPlantList[plant.type]) +  ']')
            elif status == 1:
                targetNodePath.setColorScale(1, 1, 1, 1)
                self.animalText.setText('')               
    '''Method to highlight and remove highlighting the zones based
    on users cursor movement. The function assumes that the environment has 
    16x16 blocks and the row and column to highlight is decided based on this.
    There is overlap in highlighting the blocks which lie in the border of a zone.
    This is because blocks can be onli power of 2, whereas we have 9 zones'''
    def setHighlight(self, targetNodePath, block, setStatus):
        row = int(block[0])
        col = int(block[1])
        BLOCK_SIZE = 256
        NO_OF_BLOCKS = floor (sqrt (BLOCK_SIZE)/3)
        
        #Boundary conditions
        if row == NO_OF_BLOCKS * 3:
            row = row - 1
        if col == NO_OF_BLOCKS *3:
            col = col -1
            
        # Find the range of blocks to be highlighted
        startR = row - row % NO_OF_BLOCKS
        endR = startR + NO_OF_BLOCKS
        startC = col - col % NO_OF_BLOCKS
        endC = startC + NO_OF_BLOCKS
          
        if setStatus == True :
            for i in range(startR, endR+1):
                for j in range(startC, endC+1):
                    targetNodePath.getParent().find('**/gmm'+ str(i) + 'x' + str(j)).setColorScale(1, 0, 0, 0.5)
        elif setStatus == False :
            for i in range(startR, endR+1):
                for j in range(startC, endC+1):
                    targetNodePath.getParent().find('**/gmm'+ str(i) + 'x' + str(j)).setColorScale(1, 1, 1, 1)
     
    ''' This method is a helper method hich returns the zoneID that the user hovers 
    the mouse over while moving an animal from one zone to another'''            
    def getClickedZoneId(self,xCoor,yCoor):
        ENVIRONMENT_SIZE = 512 * 4
        ZONE_SIZE = (512 *4)/3
        zoneId = None
        
        j = int(xCoor/(ENVIRONMENT_SIZE))
        i = int(yCoor/(ENVIRONMENT_SIZE))
        
        zoneX_1 = j *(ENVIRONMENT_SIZE)               #top left corner x,y
        zoneY_1 = i *(ENVIRONMENT_SIZE)
        
        zoneX_2 = j *(ENVIRONMENT_SIZE) + (ENVIRONMENT_SIZE)    #top right corner x,y
        zoneY_2 = i *(ENVIRONMENT_SIZE)
        
        zoneX_3 = j *(ENVIRONMENT_SIZE)               #bottom left corner x,y
        zoneY_3 = i *(ENVIRONMENT_SIZE) + (ENVIRONMENT_SIZE)
        
        zoneX_4 = j *(ENVIRONMENT_SIZE)+ (ENVIRONMENT_SIZE)     #bottom right corner x,y
        zoneY_4 = i *(ENVIRONMENT_SIZE)+ (ENVIRONMENT_SIZE)
        
        
        for j in range(3):
            envXStart = zoneX_1
            envYStart = zoneY_1 + ((ZONE_SIZE)*j)
            for i in range(3):
                zone0_X1 = envXStart
                zone0_Y1 = envYStart
                
                zone0_X2 = envXStart + ZONE_SIZE
                zone0_Y2 = envYStart
                
                zone0_X3 = envXStart  
                zone0_Y3 = envYStart + ZONE_SIZE
                
                zone0_X4 = envXStart + ZONE_SIZE
                zone0_Y4 = envYStart + ZONE_SIZE
                
                #do the comparision here, if it falls within the four boundaries
                #then it belongs to the zone and break, else continue through all nine zones
                if(xCoor>zone0_X1 and xCoor<zone0_X2):
                    if(yCoor>zone0_Y1 and yCoor<zone0_Y3):
                        zoneId = i + j*3
                        break
                envXStart = zone0_X2
                envYStart = zone0_Y2
        return zoneId
        
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

    def createObject(self, species, type, model_id, image = None):

        if self.newObject:
            taskMgr.remove('createObjectTask')
            prevType = self.newObject.getNetTag('type')
            self.newObject.removeNode()

            if prevType == str(type):
                return

        if type:
            if species == 'animal':
                result = DatabaseHelper.dbSelectRowByID('animal', 'animal_id', model_id)
            elif species == 'plant':
                result = DatabaseHelper.dbSelectRowByID('plant', 'plant_id', model_id)

            if not result:
                result = DatabaseHelper.dbSelectRowByID('animal', 'animal_id', 999)

            model_dir = str(result['model_dir'])
            model_file = str(result['model_file'])
            scale = float(result['scale'])

            object = loader.loadModel('models/' + model_dir + '/' + model_file)
            object.setH(choice([-45, -90, 45]))
            object.setScale(scale / 50.0)
            object.setTag('species', species)
            object.setTag('type', str(type))

            if model_file == 'dummy':
                object.setTexture(loader.loadTexture(image), 1)
        else:
            object = loader.loadModel('models/sphere_white')
            object.setScale(0.25)

        object.reparentTo(render)

        self.newObject = object
        taskMgr.add(self.createObjectTask, 'createObjectTask')

        game.worldGui.msgLabel['text'] = 'Shift-Click to Purchase Multiple Organisms'

    def createObjectTask(self, task):

        if self.lastEntry:
            surfacePoint = self.lastEntry.getSurfacePoint(render)
            self.newObject.setPos(surfacePoint)

        if self.keyMap['mouse1'][1] == 0 and self.keyMap['mouse1'][0]:
            object = self.lastEntry.getIntoNodePath()

            type = object.getNetTag('type')

            if type == 'Zone':
                object_id = int(object.getNetTag('object_id'))
                env_id = int(object.getNetTag('env_id'))

                if self.newObject.getNetTag('species') == 'animal':
                    self.gameState.requestBuyAnimal(self.newObject.getNetTag('type'), object_id, surfacePoint)
                elif self.newObject.getNetTag('species') == 'plant':
                    self.gameState.requestBuyPlant(self.newObject.getNetTag('type'), object_id, surfacePoint)

                if self.keyMap['shift'][0] == 0:
                    self.removeObjectTask()
                    return task.done

        return task.cont

    def removeObjectTask(self):

        taskMgr.remove('createObjectTask')

        if self.newObject:
            self.newObject.removeNode()
            self.newObject = None

        game.worldGui.msgLabel['text'] = ''

    def handleLeftClick(self):

        self.setKey('mouse1', 1)

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

        self.setKey('mouse1', 1)

        collisionEntry = self.checkMousePicker()

        if collisionEntry != None:
            surfacePoint = collisionEntry.getSurfacePoint(render)
            object = collisionEntry.getIntoNodePath()

            type = object.getNetTag('type')
            object_id = int(object.getNetTag('object_id'))

            if type == 'Animal':
                #print object.getX(), "********"
                self.selectAnimal(object)

    def handleRightClick(self):

        self.setKey('mouse3', 1)

        collisionEntry = self.checkMousePicker()

        if collisionEntry != None:
            surfacePoint = collisionEntry.getSurfacePoint(render)
            targetNodePath = collisionEntry.getIntoNodePath()

            type = targetNodePath.getNetTag('type')
            object_id = int(targetNodePath.getNetTag('object_id'))

            if type == 'Terrain':
                self.handleTerrain(object_id, surfacePoint)

    def createSelectMarker(self):

        selectMarker = loader.loadModel('models/smiley')
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
            self.targetPoint  = targetPoint 
            first = 1
            self.getUniqueZoneID()
            for animal in self.animalList:                                        
#                    animal.setPos(render, targetPoint)
                    zone = self.getZoneID()
                    print zone
                    self.gameState.moveAnimal(animal.getNetTag('object_id'), targetPoint, zone) 
                    
            self.clearAnimalList()
            self.mouseOverTextNodePath.hide()
        else:
            del self.animalList[:]

    def slowUpdateRoutine(self, task):
        if self.keyMap['mouse1'][0]:
            self.setKey('mouse1', 1)

        return task.cont

    def updateRoutine(self, task):

        if base.mouseWatcherNode.hasMouse():
            xPos = base.mouseWatcherNode.getMouseX()
            yPos = base.mouseWatcherNode.getMouseY()

            self.mousePickerEventRay.setFromLens(base.camNode, xPos, yPos)
            self.cTrav.traverse(render)

            if self.mousePickerEventHandler.getNumEntries() > 0:
                self.mousePickerEventHandler.sortEntries()
                self.lastEntry = self.mousePickerEventHandler.getEntry(0)
                surfacePoint = self.lastEntry.getSurfacePoint(render)

                self.mousePickerSphere.setPos(surfacePoint)

        return task.again
    
    def getTargetPoint(self):
        return self.targetPoint
    
    def getZoneID(self):
        return self.zoneID

    def unload(self):
        """Unload this instance."""
        if Constants.DEBUG:
            print 'Unloading Mouse Picker...'

        self.ignoreAll()

        taskMgr.remove('updateRoutine-MousePicker')

        self.markerObject.removeNode()

        self.mousePickerColliderNodePath.removeNode()

        self.markerSequence.clearIntervals()
        self.animalText.destroy()
    
    def getUniqueZoneID(self):
        self.gameState.getUniqueZoneID(self.EnvID,self.zoneID)
