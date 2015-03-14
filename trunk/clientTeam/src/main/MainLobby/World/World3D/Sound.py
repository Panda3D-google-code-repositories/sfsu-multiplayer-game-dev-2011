'''
Created on Dec 2, 2011

@author: Spoorthi
'''

from direct.showbase import Audio3DManager
import direct.directbase.DirectStart
from direct.task import Task
import random

class Sound():
    def __init__(self):
        self.camera = base.camera
        self.AnimalSoundMap = {}
        self.soundMap = {}
        self.listOfSound = {}
        self.AnimalSoundMap['cheetah']= 'audio/animal/Cheetah.wav'
        self.AnimalSoundMap['elephant'] = 'audio/animal/Elephant.wav'
        self.AnimalSoundMap['frog'] ='audio/animal/Frog.mp3'
        self.soundMap['fire'] = 'audio/nature/Fire.mp3'
#        self.soundMap['lion'] = 'audio/animal/Lion.mp3'
        self.AnimalSoundMap['monkey'] = 'audio/animal/Monkey.wav'
        self.soundMap['nature'] = 'audio/nature/Nature.mp3'
        self.soundMap['rain'] = 'audio/nature/Rain.wav'
        self.soundMap['thunder'] = 'audio/nature/Thunder.mp3'
        self.AnimalSoundMap['snake'] = 'audio/animal/Snake.wav'
        self.AnimalSoundMap['sparrow'] = 'audio/animal/Sparrow.mp3'
        self.AnimalSoundMap['zebra'] = 'audio/animal/Zebra.mp3'
        self.AnimalSoundMap['wildbeast'] = 'audio/animal/Wildebeest.mp3'
        
        
    def playSoundTask(self,sound):
        sound.setLoopCount(1)
        sound.play()
        return Task.again
        
    def playSound(self,type,instanceID):
        camera = base.camera
        audio3d = Audio3DManager.Audio3DManager(base.sfxManagerList[0], camera)
        if type in self.AnimalSoundMap : 
            sound = audio3d.loadSfx(self.AnimalSoundMap[type]) #Calls the  sound  with positional audio effect
            self.listOfSound[type+str(instanceID)] = sound 
##            if type == "elephant" :
##                a = (random.randint(100,200)/10) # temporary work around since elephant sound is too lengthy
##                sound.setVolume(1)
#            else :
            a = random.randint(8,20) 
            taskMgr.doMethodLater(a, self.playSoundTask, "soundTask"+type+str(instanceID), extraArgs=[self.listOfSound[type+str(instanceID)]])
           
        elif type in self.soundMap :
            sound = audio3d.loadSfx(self.soundMap[type]) #Calls the  sound  with positional audio effect 
            sound.setLoopCount(0)# This function will play the sound 3 times,  0 = infinite loop. 
            self.listOfSound[type+str(instanceID)] = sound
            sound.play()
      
    # Called when you want to stop the sound  
    def stopSound(self,type, instanceID):
        if type+str(instanceID) in self.listOfSound :
            sound = self.listOfSound[type+str(instanceID)]
            if sound.status() == sound.PLAYING:
                sound.stop()
            
    # Call the below method when an animal dies
    def removeSound(self, type, instanceID):
        if type+instanceID in self.listOfSound:
            sound = self.listOfSound[type+str(instanceID)]
            sound.stop()
            del self.listOfSound[type+str(instanceID)]
        taskMgr.remove("soundTask" + type+str(instanceID))
        
    def unload(self):
        for sound in self.listOfSound:
            sound.stop()
            taskMrg.remove("soundTask"+str(sound))