# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseLogin(ServerResponse):

    def execute(self, data):

        try:
            if 'Login' in self.main.envMap:
                status = data.getUint16()

                if status == 0:                 #Success
                    self.main.switchEnvironment('LobbyHeader')
                    taskMgr.doMethodLater(0, self.main.updateRoutine, 'updateRoutine-Main')
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

