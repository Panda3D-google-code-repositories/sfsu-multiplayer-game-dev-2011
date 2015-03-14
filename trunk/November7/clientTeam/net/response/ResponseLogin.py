# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"


from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from direct.showbase.DirectObject import DirectObject

class LoginListener(DirectObject):

    def __init__(self, parent):

        self.accept(Constants.LISTENER_LOGIN_2D, parent.send, [])

class ResponseLogin(ServerResponse):

    def __init__(self):
        
        self.listener = LoginListener(self)
        
    def send(self):
        print 'receive message from lobby header'
        messenger.send(Constants.UPDATE_MAIN_ONLINE_PLAYERS, [self.onlinePlayers])

    def execute(self, data):

        try:
            if 'Login' in self.main.envMap:
                status = data.getUint16()
                print "status ", status

                if status == 0:
                    self.userID = data.getUint16()
                    self.playerUserName = data.getString()
                    self.numberOfOnlinePlayers = data.getUint16()
                    
                    self.onlinePlayers = []

                    for i in (0, self.numberOfOnlinePlayers, 1):

                        i = data.getString()
                        self.onlinePlayers.append(i)
                        #source code will be here
                        print i
                        print "\n"
        
                    self.main.switchEnvironment('LobbyHeader')          #Success


                    #taskMgr.doMethodLater(0, self.main.updateRoutine, 'updateRoutine-Main')
                elif status == 1:               #Fail: wrong username or password
                    self.main.envMap['Login'].showAlert(status)
                elif status == 2:               #Fail: account is being used.
                    self.main.envMap['Login'].showAlert(status)
                elif status == 3:               #Fail: other
                    self.main.envMap['Login'].showAlert(status)

            self.log('Received [' + str(Constants.SMSG_AUTH) + '] Authentication Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_AUTH) + '] Authentication Response')
            print_exc()

