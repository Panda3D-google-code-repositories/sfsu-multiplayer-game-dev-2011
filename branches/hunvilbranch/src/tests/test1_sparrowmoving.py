# Author: Shao Zhang and Phil Saltzman
# Models: Eddie Canaan
# Last Updated: 5/1/2005
#
# This tutorial shows how to determine what objects the mouse is pointing to
# We do this using a collision ray that extends from the mouse position
# and points straight into the scene, and see what it collides with. We pick
# the object with the closest collision
import math
from panda3d.core import GeoMipTerrain
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
import sys

#First we define some contants for the colors
BLACK = Vec4(0,0,0,0)
WHITE = Vec4(1,1,1,0)
HIGHLIGHT = Vec4(0,1,1,1)
PIECEBLACK = Vec4(.15, .15, .15, 1)

#Now we define some helper functions that we will need later

#This function, given a line (vector plus origin point) and a desired z value,
#will give us the point on the line where the desired z value is what we want.
#This is how we know where to position an object in 3D space based on a 2D mouse
#position. It also assumes that we are dragging in the XY plane.
#
#This is derived from the mathmatical of a plane, solved for a given point
def PointAtZ(z, point, vec):
  return point + vec * ((z-point.getZ()) / vec.getZ())

#A handy little function for getting the proper position for a given square
def SquarePos(i):
  return Point3((i%8) - 3.5, int(i/8) - 3.5, 0)

#Helper function for determining wheter a square should be white or black
#The modulo operations (%) generate the every-other pattern of a chess-board
def SquareColor(i):
  return WHITE
  if (i + ((i/8)%2))%2: return BLACK
  else: return WHITE

class World(DirectObject):
  def __init__(self):
    
    #This code puts the standard title and instruction text on screen
    self.title = OnscreenText(text="Beast Reality Map",
                              style=1, fg=(1,1,1,1),
                              pos=(0.8,-0.95), scale = .07)
    self.escapeEvent = OnscreenText( 
      text="ESC: Quit",
      style=1, fg=(1,1,1,1), pos=(-1.3, 0.95),
      align=TextNode.ALeft, scale = .05)
    self.mouse1Event = OnscreenText(
      text="",
      style=1, fg=(1,1,1,1), pos=(-1.3, 0.90),
      align=TextNode.ALeft, scale = .05)

    self.accept('escape', sys.exit)              #Escape quits
    base.disableMouse()                          #Disble mouse camera control
    camera.setPosHpr(0, -13.75, 10, 0, -25, 0)    #Set the camera
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
    self.squares = [None for i in range(64)]
    self.pieces = [None for i in range(64)]
    self.ralph = Actor('../models/sparrow', {
        'walk':'../models/sparrow-walk',
          'run':'../models/sparrow-flap',
    })
    self.ralph.reparentTo(self.squareRoot)
    self.ralph.setPos(Point3(0,0,1))
    self.ralph.setScale(0.2)
    terrain = GeoMipTerrain("myDynamicTerrain")
    terrain.setHeightfield("./models/YukonHeightField.png")
    terrain.setColorMap("../models/maps/desert.rgb")
    # Set terrain properties
    terrain.setBlockSize(32)
    terrain.setNear(40)
    terrain.setFar(100)
    terrain.setFocalPoint(camera)
    #terrain.setBruteforce(True) 
    # Store the root NodePath for convenience
    root = terrain.getRoot()
    root.reparentTo(self.squareRoot)
    root.setSz(10)
    
    # Generate it.
    terrain.generate()
    # Add a task to keep updating the terrain
    def updateTask(task):
        terrain.update()
        return task.cont
    taskMgr.add(updateTask, "update")
    for i in range(64):
      #Load, parent, color, and position the model (a single square polygon)
      self.squares[i] = loader.loadModel("../models/square")
      tex = loader.loadTexture('../models/maps/desert.rgb')
      self.squares[i].setTexture(tex)
      self.squares[i].reparentTo(self.squareRoot)
      self.squares[i].setPos(SquarePos(i))
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
      self.squares[self.hiSq].setColor(SquareColor(self.hiSq))
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
          PointAtZ(.5, nearPoint, nearVec))

      #Do the actual collision pass (Do it only on the squares for
      #efficiency purposes)
      self.picker.traverse(self.squareRoot)
      if self.pq.getNumEntries() > 0:
        #if we have hit something, sort the hits so that the closest
        #is first, and highlight that node
        self.pq.sortEntries()
        i = int(self.pq.getEntry(0).getIntoNode().getTag('square'))
        #Set the highlight on the picked square
        self.squares[i].setColor(HIGHLIGHT)
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
      xdiff = newpos.x - self.ralph.getPos().x
      ydiff = newpos.y - self.ralph.getPos().y
# JOHAN: need distance because normally a posInterval uses time as its first argument
#        we want it to be based on how far it is, not a certain amount of time
#        dist/2 works for this
      dist = math.sqrt(math.pow(xdiff,2)+math.pow(ydiff,2))
      deg = math.degrees(math.atan2(ydiff,xdiff))+90
# first I set up all the intervals, to displace x and y location
# rotate, run animation, and stand animation
      intervalPosition = self.ralph.posInterval(dist/2, newpos)
      intervalRotate = self.ralph.hprInterval(0.1, Vec3(deg,0,0))
      intervalRun = self.ralph.actorInterval("run",loop=1,duration=dist/2)
      intervalStand = self.ralph.actorInterval("walk",loop=0,startFrame=5,endFrame=5)
# then i make a sequence to rotate then move position gradually
      moveSequence = Sequence(intervalRotate,intervalPosition)
      moveSequence.start()
# that sequence will run concurrently with this sequence, which runs then stands
      animSequence = Sequence(intervalRun, intervalStand)
      animSequence.start()


#Classes for each type of chess piece
#Obviously, we could have done this by just passing a string to Piece's init.
#But if you watned to make rules for how the pieces move, a good place to start
#would be to make an isValidMove(toSquare) method for each piece type
#and then check if the destination square is acceptible during ReleasePiece

#Do the main initialization and start 3D rendering
w = World()
run()
