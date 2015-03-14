#@PydevCodeAnalysisIgnore
class AudioManager:

    def __init__(self):

        self.music = None
        self.musicFile = None

        self.setMusicVolume(0.5)
        self.setSoundVolume(0.75)

    def getMusic(self):
        return self.music

    def setMusic(self, file):
        self.musicFile = file

        if self.music != None:
            self.music.stop()

        self.music = loader.loadMusic('audio/bgm/' + self.musicFile)
        self.music.setLoopCount(0)
        self.music.play()

    def removeMusic(self):
        if self.music != None:
            self.music.stop()

    def getMusicFile(self):
        return self.musicFile

    def getMusicVolume(self):
        return base.musicManager.getVolume()
    

    def setMusicVolume(self, value):
        base.musicManager.setVolume(value)

    def getSoundVolume(self):
        return base.sfxManagerList[0].getVolume()

    def setSoundVolume(self, value):
        base.sfxManagerList[0].setVolume(value)
