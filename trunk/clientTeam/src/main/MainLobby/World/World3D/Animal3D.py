from random import uniform

from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Func
from direct.interval.IntervalGlobal import Sequence
from direct.interval.IntervalGlobal import Wait

from panda3d.core import FadeLODNode
from panda3d.core import Point3
from panda3d.core import TransparencyAttrib

from common.Constants import Constants

from main.MainLobby.World.World3D.Animal import Animal

class Animal3D(Animal, Actor):

    def __init__(self, animal_id, name, type, avatarID, zoneID, biomass,model_dir,model_file,animation,scale):

        Animal.__init__(self, animal_id, name, type, avatarID, zoneID, biomass)

        self.healthy = True
        self.model_dir = model_dir
        self.model_file = model_file
        self.animation = animation
        self.sound = None
        self.lastPosition = Point3.zero()
        self.isMoving = False
        self.scale = scale
        self.aiChar = None
        self.aiBehaviors = None
        self.isHunting = False

        self.createAnimal()

        tightBounds = self.getChild(0).getTightBounds()
        self.lowerBound = tightBounds[0]
        self.upperBound = tightBounds[1]

        self.setColorScale(1, 1, 1, 0)
        self.enterSequence = self.colorScaleInterval(1, (1, 1, 1, 1))
        self.exitSequence = self.colorScaleInterval(2, (0, 0, 0, 0.1))

        self.enterSequence.start()

        self.wanderSequence = Sequence(Func(self.stop), Wait(3), Func(self.wander))
        self.deathSequence = Sequence()

    def createAnimal(self):

        Actor.__init__(self)

        self.setLODNode(FadeLODNode('Animal'))
        self.addLOD('Animal', Constants.LOD_FAR, Constants.LOD_NEAR)
        self.loadModel('models/' + self.model_dir + '/' + self.model_file, lodName = 'Animal')

        for animation in self.animation:
            self.loadAnims({animation : 'models/' + self.model_dir + '/' + self.model_file + '-' + animation})

        self.setScale(self.scale / 50.0)

        self.setCollideMask(Constants.CLICKABLE_MASK)
        self.setTag('type', str('Animal'))
        self.setTag('object_id', str(self.animalID))
        self.setTransparency(TransparencyAttrib.MAlpha)

    def setAIChar(self, aiChar):
        self.aiChar = aiChar
        self.aiBehaviors = aiChar.getAiBehaviors()

#    def playSound(self, animalType, soundMgr):
#        camera = base.camera
#        audio3d = Audio3DManager.Audio3DManager(base.sfxManagerList[0], camera)
#        if animalType in soundMgr.soundMap : 
#            self.sound = audio3d.loadSfx(soundMgr.soundMap[animalType]) #Calls the  sound  with positional audio effect 
#            self.sound.setLoopCount(0)# This function will play the sound 3 times,  0 = infinite loop. 
#            self.sound.play()
#            
#    def stopSound(self,animalType):
#        self.sound.stop()

    def death(self):

        self.play('die')
        self.zone.AIworld.removeAiChar(self.animalInstance)
        taskMgr.add(self.deathTask, 'deathTask-' + str(self.animalID))
        game.worldGui.floatingText.createText(Constants.TEXT_TYPE_DEATH, '!', self)

        self.lifeStatus = Constants.LIFE_STATUS_DYING

    def deathTask(self, task):

        animControl = self.getAnimControl('die')

        if animControl == None or not animControl.isPlaying():
            self.deathSequence = Sequence(Wait(1.0), self.exitSequence, Func(self.setGroupSize, self.groupSize - self.numDead))
            self.deathSequence.start()
            return task.done

        return task.cont

    def setAttackAware(self, attacker):
        self.aiBehaviors.evade(attacker, 5, 5)
        self.aiChar.setMaxForce(1.5)

    def attack(self, target, count):

        taskMgr.remove('wanderTask-' + str(self.animalID))

        self.isHunting = True

        self.aiBehaviors.pursue(target)
        target.setAttackAware(self)

        self.aiChar.setMaxForce(1.5)
        taskMgr.add(self.chaseTask, 'chaseTask-' + str(self.animalID), extraArgs = [target, count], appendTask = True)

    def chaseTask(self, target, count, task):

        try:
            distance = (target.getPos() - self.getPos()).length()

            if distance < 6:
                self.aiChar.setMaxForce(2)
                taskMgr.add(self.attackTask, 'attackTask-' + str(self.animalID), extraArgs = [target, count], appendTask = True)
                return task.done

            return task.cont
        except:
            return task.done

    def attackTask(self, target, count, task):

        if self.aiBehaviors.behaviorStatus('pursue') == 'done':
            self.aiBehaviors.removeAi('pursue')
            self.play('eat')
            taskMgr.add(self.eatTask, 'eatTask-' + str(self.animalID), extraArgs = [target, count], appendTask = True)

            return task.done

        return task.cont

    def eatTask(self, target, count, task):

        animControl = self.getAnimControl('eat')

        if animControl == None or not animControl.isPlaying():
            target.reduceGroupSize(count)

            self.wanderSequence.start()
            self.aiChar.setMaxForce(1)

            self.isHunting = False

            return task.done

        return task.cont

    def reduceGroupSize(self, amount):

        self.numDead = min(amount, self.groupSize)

        if self.numDead < self.groupSize:
            self.setGroupSize(self.groupSize - self.numDead)
        else:
            self.death()

    def wander(self):
        #print "enter wander"
        xPos = self.startPos.getX()
        yPos = self.startPos.getY()

        radius = 10

        xMin = max(xPos - radius, 0)
        xMax = min(xPos + radius, self.zone.getSize())

        yMin = max(yPos - radius, 0)
        yMax = min(yPos + radius, self.zone.getSize())

        xRandom = uniform(xMin, xMax)
        yRandom = uniform(yMin, yMax)

        newPos = self.zone.getWorldPoint(xRandom, yRandom)
        self.aiBehaviors.seek((newPos[0], newPos[1], self.zone.getElevation(xRandom, yRandom)))
        self.loop('walk')

        taskMgr.add(self.wanderTask, 'wanderTask-' + str(self.animalID))

    def wanderTask(self, task):

        if not self.isMoving and not self.wanderSequence.isPlaying():
            self.wanderSequence.start()
            return task.done
#        else:
#            water = self.zone.getWater()
#            if (water.getPos(render) - self.getPos(render)).length() < water.getSize():
#                self.aiBehaviors.seek(self.getPos())
#                self.wanderSequence.start()
#                return task.done
        return task.cont

    def drinkWater(self):

        taskMgr.remove('wanderTask-' + str(self.animalID))

        self.aiBehaviors.seek(self.zone.getWater().getWaterSphere())
        self.loop('walk')

        taskMgr.add(self.drinkWaterTask, 'drinkWaterTask-' + str(self.animalID), extraArgs = [self.zone.getWater()], appendTask = True)

    def drinkWaterTask(self, water, task):

        if (water.getPos(render) - self.getPos(render)).length() < water.getSize():
            self.aiBehaviors.seek(self.getPos())
            Sequence(Func(self.play, 'eat'), Wait(2), Func(self.play, 'eat'), Wait(3), Func(self.wander)).start()

            return task.done

        return task.cont

    def updateTask(self, task):

        temp = self.zone.getElevation(self.getX(), self.getY())
        self.setZ(temp)

        self.isMoving = self.getPos() != self.lastPosition
        self.lastPosition = self.getPos()
        #print "lp-",self.lastPosition
        
        #check for boundaries of x and y, x should be within +ve (0,32) range 
        #and y should be between +ve (32,0) range since all positions are relative
        x = self.lastPosition.getX()
        y = self.lastPosition.getY()
        if(x<1 or x>31):
            if(x<1):
                #print "x<0"
                h = self.getH()
                self.setH(h+180)
                #print "oldh-",h," newh-",h+180
                self.setX(x+0.5)
                #print "oldx-",x," newx-",x+0.5
                self.aiBehaviors.seek((16, 16, self.zone.getElevation(16, 16)))
            if(x>31):
                #print "x<32"
                h = self.getH()
                self.setH(h+180)
                #print "oldh-",h," newh-",h+180
                self.setX(x-0.5)   
                #print "oldx-",x," newx-",x-0.5    
                self.aiBehaviors.seek((16, 16, self.zone.getElevation(16, 16)))         
        if(y<1 or y>31):  
            if(y<2):
                #print "y<0"
                h = self.getH()
                self.setH(h+180)
                #print "oldh-",h," newh-",h+180
                self.setY(y+0.5) 
                #print "oldy-",y," newy-",y+0.5    
                self.aiBehaviors.seek((16, 16, self.zone.getElevation(16, 16)))           
            if(y>31):
                #print "y>32"
                h = self.getH()
                self.setH(h+180)
                #print "oldh-",h," newh-",h+180
                self.setY(y-0.5) 
                #print "oldy-",y," newy-",y-0.5        
                self.aiBehaviors.seek((16, 16, self.zone.getElevation(16, 16)))
        if(x<1 and y<1):     
                #print "x<5 and y<5"
                h = self.getH()
                #override the rotation if it is prev set
                self.setH(h+180)
                #print "oldh-",h," newh-",h+180
                self.aiBehaviors.seek((16, 16, self.zone.getElevation(16, 16)))  
        if(x>31 and y>31):     
                #print "x>27 and y>27"
                h = self.getH()
                self.setH(h+180)
                #print "oldh-",h," newh-",h+180
                self.aiBehaviors.seek((16, 16, self.zone.getElevation(16, 16)))

    def unload(self):

        taskMgr.remove('deathTask-' + str(self.animalID))
        taskMgr.remove('wanderTask-' + str(self.animalID))
        taskMgr.remove('chaseTask-' + str(self.animalID))
        taskMgr.remove('attackTask-' + str(self.animalID))
        taskMgr.remove('eatTask-' + str(self.animalID))
        taskMgr.remove('drinkWaterTask-' + str(self.animalID))

        self.enterSequence.clearToInitial()
        self.exitSequence.clearToInitial()
        self.wanderSequence.clearToInitial()
        self.deathSequence.clearToInitial()

        self.cleanup()
        self.removeNode()
