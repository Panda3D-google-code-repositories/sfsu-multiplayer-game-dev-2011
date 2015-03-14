import __builtin__

from hashlib import md5
from sys import exit
from time import strftime

from panda3d.core import loadPrcFileData
#loadPrcFileData('', 'aspect-ratio 1.0')
#loadPrcFileData('', 'aspect-ratio 1.3333')
#loadPrcFileData('', 'aspect-ratio 1.6')
#loadPrcFileData('', 'aspect-ratio 1.7778')
#loadPrcFileData('', 'direct-gui-edit 1')
#loadPrcFileData('', 'icon-filename icon.ico')
#loadPrcFileData('', 'icon-filename icon.png')
loadPrcFileData('', 'max-dt 0.03')
#loadPrcFileData('', 'show-frame-rate-meter #t')
#loadPrcFileData('', 'sync-video #f')
#loadPrcFileData('', 'want-pstats 1')
#loadPrcFileData('', 'win-size 800 450')
#loadPrcFileData('', 'win-size 800 500')
#loadPrcFileData('', 'win-size 800 600')
#loadPrcFileData('', 'win-size 640 640')
#loadPrcFileData('', 'win-size 1024 640')
#loadPrcFileData('', 'win-size 1024 768')
#loadPrcFileData('', 'win-size 1280 720')
#loadPrcFileData('', 'win-size 1280 800')
#loadPrcFileData('', 'win-size 1280 1024')
loadPrcFileData('', 'window-title World of Balance')
#loadPrcFileData('', 'window-type none')

from direct.directbase.DirectStart import *
from direct.showbase.DirectObject import DirectObject

from panda3d.core import TextProperties
from panda3d.core import TextPropertiesManager
from panda3d.core import Texture
from panda3d.core import WindowProperties

from common.Constants import Constants
from common.DirectControls import DirectControls
from common.DirectWindow import DirectWindow
from common.DatabaseHelper import DatabaseHelper
from common.MessageBox import MessageBox
from common.MessageQueue import MessageQueue
from common.MousePicker2D import MousePicker2D

from net.ConnectionManager import ConnectionManager
from net.ServerRequestTable import ServerRequestTable
from net.ServerResponseTable import ServerResponseTable

from util.AudioManager import AudioManager

from main.Login.Login import Login
from main.MainLobby.GameLobby.LobbyHeader import LobbyHeader
from main.MainLobby.GameLobby.PvEGameLobby import PvEGameLobby
from main.MainLobby.World.World3D.WorldGUI import WorldGUI
from main.MainLobby.WorldLobby.PvEWorldLobby import PvEWorldLobby
from main.MainLobby.WorldLobby.PvPWorldLobby import PvPWorldLobby
from main.Register.Register import Register

class Main(DirectObject):

    def __init__(self):

        __builtin__.main = self

        globalClock.setMaxDt(0.03)
        win = WindowProperties()
        win.setSize(1024, 640)
        win.setFullscreen(0) 
        win.setTitle('World of Balance')
        base.win.requestProperties(win)
        self.accept('window-close', self.exitGameRequest)
        base.win.setCloseRequestEvent('window-close')

        tpWhite = TextProperties()
        tpWhite.setTextColor(1, 1, 1, 1)
        tpGray = TextProperties()
        tpGray.setTextColor(0.5, 0.5, 0.5, 1)
        tpRed = TextProperties()
        tpRed.setTextColor(1, 0, 0, 1)
        tpGreen = TextProperties()
        tpGreen.setTextColor(0, 1, 0, 1)
        tpBlue = TextProperties()
        tpBlue.setTextColor(0, 0, 1, 1)
        tpScale05 = TextProperties()
        tpScale05.setTextScale(0.5)
        tpItalic = TextProperties()
        tpItalic.setSlant(0.3)
        tpShadowOn = TextProperties()
        tpShadowOn.setShadowColor(Constants.TEXT_SHADOW_COLOR)
        tpShadowOff = TextProperties()
        tpShadowOff.setShadowColor(0, 0, 0, 0)

        tpMgr = TextPropertiesManager.getGlobalPtr()
        tpMgr.setProperties('white', tpWhite)
        tpMgr.setProperties('gray', tpGray)
        tpMgr.setProperties('red', tpRed)
        tpMgr.setProperties('blue', tpBlue)
        tpMgr.setProperties('green', tpGreen)
        tpMgr.setProperties('scale_05', tpScale05)
        tpMgr.setProperties('italic', tpItalic)
        tpMgr.setProperties('shadow_on', tpShadowOn)
        tpMgr.setProperties('shadow_off', tpShadowOff)

        self.exitGameMessageIsShown=False
        self.charData = {}
        self.envMap = {}
        self.charName = None
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

        self.msgQ = MessageQueue()
        self.audioManager = AudioManager()

        self.cManager = ConnectionManager()
        ServerRequestTable.init()
        ServerResponseTable.init()
        self.msgQ.addToCommandList(Constants.CMSG_SAVE_EXIT_GAME, self.exitGame);
        self.switchEnvironment('Login')

        self.accept('control-m', self.captureScreen, [2400, 1500])

    def captureScreen(self, width, height):

        buffer = base.win.makeTextureBuffer('buffer', width, height, Texture(), True)

        region = buffer.makeDisplayRegion()
        region.setCamera(base.cam)

        region2d = buffer.makeDisplayRegion()
        region2d.setCamera(base.cam2d)

        base.graphicsEngine.renderFrame()
        texture = buffer.getTexture()
        buffer.setActive(False)

        texture.write('screenshots/' + 'World of Balance ' + strftime('%Y-%m-%d at %I.%M.%S %p') + '.jpg')
        base.graphicsEngine.removeWindow(buffer)

    def setFullScreenMode(self):
        win = WindowProperties()
        
        win.setFullscreen(1) 
#        win.setSize(1366, 768)
        base.win.requestProperties(win)
        base.openMainWindow() 
        base.win.requestProperties(win) 
        base.graphicsEngine.openWindows()
    
    def exitFullScreenMode(self):
        
        win = WindowProperties()
        win.setFullscreen(0) 
        win.setSize(1024, 640)
        base.win.requestProperties(win)
        base.openMainWindow() 
        base.win.requestProperties(win) 
        base.graphicsEngine.openWindows()
           
    def switchEnvironment(self, name):
        """Switch between different environments.

        Whenever an environment such as Login, Register or World is required
        to switch between one another, it will call its unloading method
        to perform a complete removal of the instance and clears itself from
        the environment map table for another environment to take its place.

        """
#        self.removeGameMode()
            
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

        msgBox = MessageBox(type, text, command, extraArgs)
        self.msgBoxList.append(msgBox)

        return msgBox

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

    def exitGameRequest(self):
        
        if not self.exitGameMessageIsShown:
            self.exitGameMessageIsShown = True
            self.createMessageBox(1, "Are you sure you want to quit the game?", self.requestExitGame)
    
    
    def requestExitGame(self, _exit=None):
        
        if _exit:
            self.cManager.sendRequest(Constants.CMSG_SAVE_EXIT_GAME, None)
            self.exitGame(0)
        else:
            self.exitGameMessageIsShown = False        
    
    def exitGame(self, status):
        """
        May need to do some extra things right here
        """
        
        if status == 0:
            print 'Exit game now'
            self.exitGameMessageIsShown=False
            base.closeWindow(base.win)
            exit()

    def login(self, username, password):

        rContents = {'userName' : username,
                     'password' : md5(password).hexdigest()}
        self.cManager.sendRequest(Constants.CMSG_AUTH, rContents)

    def updateRoutine(self, task):
        """A once-per-frame task to keep the connection alive.

        The client must send a heartbeat to the server before any updates
        can be retrieved while maintaining an active connection.

        """
        self.cManager.sendRequest(Constants.CMSG_HEARTBEAT)

        return task.again
    def showAlert(self, status):
        """Create failed registration box."""
        result = DatabaseHelper.dbSelectRowByID('msg', 'msg_id', status)
        self.createMessageBox(0, result['msg_text'], '', [])
