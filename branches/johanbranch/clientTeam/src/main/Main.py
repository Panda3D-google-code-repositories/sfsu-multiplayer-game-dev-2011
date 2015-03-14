from main.MainLobby.World.WorldGUI import WorldGUI
from common.Constants import Constants
from common.DirectControls import DirectControls
from common.DirectWindow import DirectWindow
from common.MessageBox import MessageBox
from common.MousePicker2D import MousePicker2D
from direct.directbase.DirectStart import *
from direct.showbase.DirectObject import DirectObject
from hashlib import md5
from main.Env.Env import Env
from main.Login.Login import Login
from main.MainLobby.GameLobby.LobbyHeader import LobbyHeader
from main.MainLobby.WorldLobby.PvEWorldLobby import PvEWorldLobby
from main.MainLobby.WorldLobby.PvPWorldLobby import PvPWorldLobby
from main.Register.Register import Register
from panda3d.core import WindowProperties, loadPrcFileData
from sys import exit
from util.AudioManager import AudioManager
import __builtin__


from net.ConnectionManager import ConnectionManager
from net.ServerRequestTable import ServerRequestTable
from net.ServerResponseTable import ServerResponseTable

#loadPrcFileData('', 'aspect-ratio 1.0')
#loadPrcFileData('', 'aspect-ratio 1.3333')
loadPrcFileData('', 'aspect-ratio 1.6')
#loadPrcFileData('', 'aspect-ratio 1.7778')
#loadPrcFileData('', 'direct-gui-edit 1')
loadPrcFileData('', 'icon-filename icon.ico')
#loadPrcFileData('', 'icon-filename icon.png')
loadPrcFileData('', 'max-dt 0.03')
loadPrcFileData('', 'show-frame-rate-meter #t')
#loadPrcFileData('', 'sync-video #f')
#loadPrcFileData('', 'want-pstats 1')
#loadPrcFileData('', 'win-size 800 450')
#loadPrcFileData('', 'win-size 800 500')
#loadPrcFileData('', 'win-size 800 600')
#loadPrcFileData('', 'win-size 640 640')
loadPrcFileData('', 'win-size 1024 640')
#loadPrcFileData('', 'win-size 1024 768')
#loadPrcFileData('', 'win-size 1280 720')
#loadPrcFileData('', 'win-size 1280 800')
#loadPrcFileData('', 'win-size 1280 1024')
loadPrcFileData('', 'window-title Beast Reality')
#loadPrcFileData('', 'window-type none')

#from main.World.World import World

#from main.World.World import World

class Main(DirectObject):

    def __init__(self):

        __builtin__.main = self

        globalClock.setMaxDt(0.03)
        
        win = WindowProperties()
        win.setSize(1024, 640)
        win.setTitle('Beast Reality')
        base.win.requestProperties(win)

        self.charData = {}
        self.envMap = {}

        self.windowList = []
        self.msgBoxList = []

        self.mainWindow = DirectWindow( frameSize = (0, 0, 0, 0) )
        self.mainWindow.setControls(DirectControls(self))
        self.setWindow(self.mainWindow)

        self.accept('mouse1', self.removeCurrentWindow)

        self.mPicker2D = MousePicker2D()

        self.controls = DirectControls(self)
        self.gameControls = None

        self.currentGameMode = None

        self.audioManager = AudioManager()

        self.cManager = ConnectionManager()
        ServerRequestTable.init()
        ServerResponseTable.init()

        self.switchEnvironment('Login')

    def switchEnvironment(self, name):
        """Switch between different environments.

        Whenever an environment such as Login, Register or World is required
        to switch between one another, it will call its unloading method
        to perform a complete removal of the instance and clears itself from
        the environment map table for another environment to take its place.

        """
        self.removeGameMode()
            
        if name in globals():
            for eObject in self.envMap.values():
                eObject.unload()
            self.envMap.clear()

            self.clearMessageBoxList()

            self.envMap[name] = globals()[name]()

    def getWindowList(self):
        return self.windowList

    def getMainWindow(self):
        return self.mainWindow

    def getWindow(self, index):

        if index < len(self.windowList):
            return self.windowList[index]

    def setWindow(self, window):
        self.windowList.append(window)

    def removeWindow(self, window):

        if window in self.windowList:
            self.windowList.remove(window)

            if len(self.windowList) > 0:
                self.windowList[0].onFocus()

    def getCurrentWindow(self):

        if len(self.windowList) > 0:
            return self.windowList[0]

    def setCurrentWindow(self, window):

        current_win = self.getCurrentWindow()

        if window != current_win:
            if current_win != None:
                current_win.onFocusOut()

            if window in self.windowList:
                self.windowList.remove(window)

            self.windowList.insert(0, window)

            window.onFocus()

    def removeCurrentWindow(self, window = None):

        current_win = self.getCurrentWindow()

        if current_win != None:
            if window == current_win:
                current_win.onFocusOut()

        self.setCurrentWindow(self.mainWindow)

    def createMessageBox(self, type, text, command = None, extraArgs = []):

        self.msgBoxList.append(MessageBox(type, text, command, extraArgs))

    def removeMessageBox(self, msgBox):

        msgBox.destroy()
        self.msgBoxList.remove(msgBox)

    def clearMessageBoxList(self):

        for msgBox in self.msgBoxList:
            msgBox.cancel()
        del self.msgBoxList[:]

    def getGlobalControls(self):
        return self.controls

    def getGameControls(self):
        return self.gameControls

    def setGameControls(self, controls):

        self.removeGameControls()

        self.gameControls = controls
        self.gameControls.enable()

    def removeGameControls(self):

        self.disableGameControls()
        self.gameControls = None

    def enableGameControls(self):

        if self.gameControls != None:
            self.gameControls.enable()

    def disableGameControls(self):

        if self.gameControls != None:
            self.gameControls.disable()

    def getGameMode(self):
        return self.currentGameMode

    def setGameMode(self, mode):

        self.removeGameMode()
        self.currentGameMode = mode

    def removeGameMode(self):

        if self.currentGameMode != None:
            self.currentGameMode.unload()

        self.currentGameMode = None

    def startConnection(self):
        """Create a connection to the remote host.

        If a connection cannot be created, it will ask the user to perform
        additional retries.

        """
        if self.cManager.connection == None:
            if not self.cManager.startConnection():
                return False

        return True

    def login(self, username, password):

        rContents = {'userName' : username,
                     'password' : md5(password).hexdigest()}
        self.cManager.sendRequest(Constants.CMSG_AUTH, rContents)

    def closeClient(self):
        """Terminates the client."""
        exit()

    def updateRoutine(self, task):
        """A once-per-frame task to keep the connection alive.

        The client must send a heartbeat to the server before any updates
        can be retrieved while maintaining an active connection.

        """
        self.cManager.sendRequest(Constants.CMSG_HEARTBEAT)

        return task.again
