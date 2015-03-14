# This code contains all the frunctions usable for the sounds, camera control, 
# volume control, pan control  and loops. 

# Audio Manager.
from direct.showbase import Audio3DManager
import direct.directbase.DirectStart
 
#--------------------------------------- NON Positional Audio Manager  -------------------------------#
base = ShowBase() 
 
 #--------------------------       Camera Control for the sound         ---------------------------------#
 # This function allows tohe sounds to be positional,  the sounds is louder or lower 
 # as the camera gets closer  or far from the  objec                                       
audio3d = Audio3DManager.Audio3DManager(base.sfxManagerList[0], camera)



#-------------------------------------------------------------------- CHEETAH  CLASS -------------------------------------------------------------------#
#RAIN  WITH DIRECTIONAL SOUND EFFECT
cheetahSound = audio3d.loadSfx("cheetah.wav") #Calls the  cheetah  sound  with positional audio effect 
cheetahSound.setLoopCount(3)# This function will play the sound 3 times,  0 = infinite loop. 
cheetahSound.play()  # Plays the sound 
#---------------------------------------------------------------- END OF CHEETAH CLASS  ----------------------------------------------------------#


#-------------------------------------------------------------------- ELEPHANT   CLASS -----------------------------------------------------------------#
elephantSound = audio3d.loadSfx("Elephant.wav") #Calls the  elephant  sound  with positional audio effect 
elephantSound.setLoopCount(3)# This function will play the sound 3 times,  0 = infinite loop. 
elephantSound.play()  # Plays the sound 
#---------------------------------------------------------------- END OF ELEPHANT CLASS   --------------------------------------------------------#

#-------------------------------------------------------------------- FIRE    CLASS   ------------------------------------------------------------------------#
fireSound = audio3d.loadSfx("Fire.mp3") #Calls the  fire  sound  with positional audio effect 
fireSound.setLoopCount(3)# This function will play the sound 3 times,  0 = infinite loop. 
fireSound.play()  # Plays the sound 
#--------------------------------------------------------------------  END FIRE  CLASS   -------------------------------------------------------------------#

#-------------------------------------------------------------------- FROG   CLASS   -------------------------------------------------------------------------#
frogSound = audio3d.loadSfx("Frog.mp3") #Calls the  frog   sound  with positional audio effect 
frogSound.setLoopCount(3)# This function will play the sound 3 times,  0 = infinite loop. 
frogSound.play()  # Plays the sound 
#--------------------------------------------------------------------  END FROG CLASS   -------------------------------------------------------------------#

#-------------------------------------------------------------------- LION   CLASS   ----------------------------------------------------------------------------#
lionSound = audio3d.loadSfx("Lion.mp3") #Calls the  lion sound  with positional audio effect 
lionSound.setLoopCount(3)# This function will play the sound 3 times,  0 = infinite loop. 
lionSound.play()  # Plays the sound 
#--------------------------------------------------------------------  END LION CLASS   ----------------------------------------------------------------------#

#-------------------------------------------------------------------- MONKEY  CLASS   -----------------------------------------------------------------------#
monkeySound = audio3d.loadSfx("Monkey.wav") #Calls the  monkey  sound  with positional audio effect  
monkeySound.setLoopCount(3)# This function will play the sound 3 times,  0 = infinite loop. 
monkeySound.play()  # Plays the sound 
#--------------------------------------------------------------------  END  MONKEY CLASS   ----------------------------------------------------------------#

#-------------------------------------------------------------------- NATURE CLASS   ---------------------------------------------------------------------------#
natureSound =  base.loader.loadSfx("Nature.mp3") #Calls the  nature sound  with NON positional audio effect. 
natureSound.setLoop(True) # This loop is sent to infinite because the  anbience sound will be played continiously
natureSound.play()  # Plays the sound 
#--------------------------------------------------------------------  END  NATURE CLASS   ------------------------------------------------------------------#


#-------------------------------------------------------------------- RAIN & THUNDER CLASS   --------------------------------------------------------------#
rainSound = audio3d.loadSfx("Rain.wav") #Calls the  rain  sound  with positional audio effect  
rainSound.setBalance(-1.0) #PAN TO LEFT , this function splits the sounds for sorround effects left  & right speakers. 
rainSound.setLoopCount(3)# This function will play the sound 3 times,  0 = infinite loop.  
rainSound.play()  # Plays the sound 

#tTHUNDER
thunderSound = audio3d.loadSfx("Thunder.mp3") #Calls the  thunder  sound  with positional audio effect 
thunderSound.setBalance(1.0)#PAN TO RIGHT ,this function splits the sounds for sorround effects left  & right speakers.
thunderSound.setLoopCount(3)# This function will play the sound 3 times,  0 = infinite loop. 
thunderSound.play() # Plays the sound 
#-------------------------------------------------------------------- RAIN & THUNDER END  CLASS   -------------------------------------------------------#

#-------------------------------------------------------------------- SNAKE CLASS   -------------------------------------------------------------------------------#
snakeSound = audio3d.loadSfx("Snake.wav") #Calls the  snake  sound  with positional audio effect 
snakeSound.setLoopCount(3)# This function will play the sound 3 times,  0 = infinite loop.
snakeSound.play()  # Plays the sound 
#-------------------------------------------------------------------- SNAKE END  CLASS   ------------------------------------------------------------------------#

#-------------------------------------------------------------------- SPARROW  CLASS   --------------------------------------------------------------------------#
sparrowSound = audio3d.loadSfx("Sparrow.mp3") #Calls the  sparrow sound  with positional audio effect 
sparrowSound.setLoopCount(3)# This function will play the sound 3 times,  0 = infinite loop.
sparrowSound.play()  # Plays the sound 
#-------------------------------------------------------------------- SPARROW  END  CLASS   ------------------------------------------------------------------#

#-------------------------------------------------------------------- ZEBRA  CLASS   ---------------------------------------------------------------------------------#
zebraSound = audio3d.loadSfx("Zebra.mp3") #Calls the  zebra  sound  with positional audio effect 
zebraSound.setLoopCount(3)# This function will play the sound 3 times,  0 = infinite loop.
zebraSound.play()  # Plays the sound 
#-------------------------------------------------------------------- ZEBRA  END  CLASS   -------------------------------------------------------------------------#

#-------------------------------------------------------------------- WWILDEBEEST CLASS   -----------------------------------------------------------------------#
wildebeestSound = audio3d.loadSfx("Wildebeest.mp3") #Calls the  zebra  sound  with positional audio effect 
wildebeestSound.setLoopCount(3)# This function will play the sound 3 times,  0 = infinite loop.
wildebeestSound.play()  # Plays the sound 
#-------------------------------------------------------------------- WILDEBEEST  END  CLASS   --------------------------------------------------------------------#