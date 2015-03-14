from direct.gui.DirectGui import DGG
from direct.gui.DirectGui import DirectFrame
from direct.gui.DirectGui import DirectLabel
from direct.gui.OnscreenText import OnscreenText
import math
from direct.interval.ActorInterval import ActorInterval
import direct.directbase.DirectStart
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import *
from panda3d.core import CollisionTraverser,CollisionNode
from panda3d.core import CollisionHandlerQueue,CollisionRay
from panda3d.core import AmbientLight,DirectionalLight,LightAttrib
from panda3d.core import TextNode
from panda3d.core import Point3,Vec3,Vec4,BitMask32
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.DirectObject import DirectObject
from direct.task.Task import Task

from common.Constants import Constants
from common.DatabaseHelper import DatabaseHelper
from common.DirectBasicButton import DirectBasicButton
from common.DirectTextField import DirectTextField
from common.DirectWindow import DirectWindow

class World(DirectObject):

    def __init__(self):

        if Constants.DEBUG:
            print 'Loading World...'

        self.main = main
        base.disableMouse()
        self.createMainFrame()
        self.createBackground()
        self.displayGame()
         
    def PointAtZ(self, z, point, vec):
        return point + vec * ((z-point.getZ()) / vec.getZ())
    def SquarePos(self, i):
        return Point3((i%12) - 5, int(i/12) - 5, 0)
    
    def getControls(self):
        return self.controls
    
    def createMainFrame(self):
        """Create the main base frame."""

        
    def createBackground(self):
        """Create a background for the login screen."""
        
    def displayGame(self):
        camera.setPosHpr(0, -4, 11, 0, -70, 0)    #Set the camera
        self.setupLights()                           #Setup default lighting
        
        #Since we are using collision detection to do picking, we set it up like
        #any other collision detection system with a traverser and a handler
        self.picker = CollisionTraverser()            #Make a traverser
        self.pq     = CollisionHandlerQueue()         #Make a handler
        #Make a collision node for our picker ray
        self.pickerNode = CollisionNode('mouseRay')
        #Attach that node to the camera since the ray will need to be positioned
        #relative to it
        self.pickerNP = camera.attachNewNode(self.pickerNode)
        #Everything to be picked will use bit 1. This way if we were doing other
        #collision we could seperate it
        self.pickerNode.setFromCollideMask(BitMask32.bit(1))
        self.pickerRay = CollisionRay()               #Make our ray
        self.pickerNode.addSolid(self.pickerRay)      #Add it to the collision node
        #Register the ray as something that can cause collisions
        self.picker.addCollider(self.pickerNP, self.pq)
        #self.picker.showCollisions(render)
    
        #Now we create the chess board and its pieces
    
        #We will attach all of the squares to their own root. This way we can do the
        #collision pass just on the sqaures and save the time of checking the rest
        #of the scene
        self.squareRoot = render.attachNewNode("squareRoot")
        
        #For each square
        self.squares = [None for i in range(144)]
        self.sparrow = Actor('models/sparrow', {
            'walk':'models/sparrow-walk',
              'run':'models/sparrow-flap',
        })
        self.sparrow.reparentTo(self.squareRoot)
        self.sparrow.setPos(Point3(0,0,1))
        self.sparrow.setScale(0.1)
        for i in range(144):
            #Load, parent, color, and position the model (a single square polygon)
            self.squares[i] = loader.loadModel("models/square")
            tex = loader.loadTexture('models/maps/desert.rgb')
            self.squares[i].setTexture(tex)
            self.squares[i].reparentTo(self.squareRoot)
            self.squares[i].setPos(self.SquarePos(i))
            #self.squares[i].setColor(SquareColor(i))
            #self.squares[i].setTransparency(1)
            #Set the model itself to be collideable with the ray. If this model was
            #any more complex than a single polygon, you should set up a collision
            #sphere around it instead. But for single polygons this works fine.
            self.squares[i].find("**/polygon").node().setIntoCollideMask(
            BitMask32.bit(1))
            #Set a tag on the square's node so we can look up what square this is
            #later during the collision pass
            self.squares[i].find("**/polygon").node().setTag('square', str(i))
            #We will use this variable as a pointer to whatever piece is currently
            #in this square
    
        #The order of pieces on a chessboard from white's perspective. This list
        #contains the constructor functions for the piece classes defined below
        #This will represent the index of the currently highlited square
        self.hiSq = False
        #This wil represent the index of the square where currently dragged piece
        #was grabbed from
        self.dragging = False
        
        #Start the task that handles the picking
        self.mouseTask = taskMgr.add(self.mouseTask, 'mouseTask')
        self.accept("mouse1", self.clicked)
    
    def mouseTask(self, task):
        #This task deals with the highlighting and dragging based on the mouse
        
        #First, clear the current highlight
        if self.hiSq is not False:
            self.squares[self.hiSq].setColor(Constants.WHITE)
            self.hiSq = False
          
        #Check to see if we can access the mouse. We need it to do anything else
        if base.mouseWatcherNode.hasMouse():
            #get the mouse position
            mpos = base.mouseWatcherNode.getMouse()
        
            #Set the position of the ray based on the mouse position
            self.pickerRay.setFromLens(base.camNode, mpos.getX(), mpos.getY())
        
        #If we are dragging something, set the position of the object
        #to be at the appropriate point over the plane of the board
            if self.dragging is not False:
                #Gets the point described by pickerRay.getOrigin(), which is relative to
                #camera, relative instead to render
                nearPoint = render.getRelativePoint(camera, self.pickerRay.getOrigin())
                #Same thing with the direction of the ray
                nearVec = render.getRelativeVector(camera, self.pickerRay.getDirection())
                self.pieces[self.dragging].obj.setPos(
                    self.PointAtZ(.5, nearPoint, nearVec))
        
          #Do the actual collision pass (Do it only on the squares for
          #efficiency purposes)
            self.picker.traverse(self.squareRoot)
            if self.pq.getNumEntries() > 0:
                #if we have hit something, sort the hits so that the closest
                #is first, and highlight that node
                self.pq.sortEntries()
                i = int(self.pq.getEntry(0).getIntoNode().getTag('square'))
                #Set the highlight on the picked square
                self.squares[i].setColor(Constants.HIGHLIGHT)
                self.hiSq = i
              
        return Task.cont
    
    def setupLights(self):    #This function sets up some default lighting
        ambientLight = AmbientLight( "ambientLight" )
        ambientLight.setColor( Vec4(.8, .8, .8, 1) )
        directionalLight = DirectionalLight( "directionalLight" )
        directionalLight.setDirection( Vec3( 0, 45, -45 ) )
        directionalLight.setColor( Vec4( 0.2, 0.2, 0.2, 1 ) )
        render.setLight(render.attachNewNode( directionalLight ) )
        render.setLight(render.attachNewNode( ambientLight ) )
    def clicked(self):
        if (self.hiSq is not False):
            newpos = self.squares[self.hiSq].getPos()
            xdiff = newpos.x - self.sparrow.getPos().x
            ydiff = newpos.y - self.sparrow.getPos().y
            dist = math.sqrt(math.pow(xdiff,2)+math.pow(ydiff,2))
            deg = math.degrees(math.atan2(ydiff,xdiff))+90
            intervalPosition = self.sparrow.posInterval(dist/2, newpos)
            intervalRotate = self.sparrow.hprInterval(0.1, Vec3(deg,0,0))
            intervalRun = self.sparrow.actorInterval("run",loop=1,duration=dist/2)
            intervalStand = self.sparrow.actorInterval("walk",loop=0,startFrame=5,endFrame=5)
            moveSequence = Sequence(intervalRotate,intervalPosition)
            moveSequence.start()
            animSequence = Sequence(intervalRun, intervalStand)
            animSequence.start()
    def unload(self):
        """Unload this instance."""
        if Constants.DEBUG:
            print 'Unloading World...'
        main.removeGameControls()