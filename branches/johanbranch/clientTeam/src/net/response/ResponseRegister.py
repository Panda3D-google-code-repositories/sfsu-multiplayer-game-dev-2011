# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseRegister(ServerResponse):

    def execute(self, data):

        try:
            if 'Register' in self.main.envMap:
                status = data.getUint16()

                if status == 0:
                    self.main.envMap['Register'].showConfirm()      #success
                else:                                               #Fail
                    self.main.envMap['Register'].showAlert(status)

            self.log('Received [' + str(Constants.SMSG_REGISTER) + '] Register Response')
        except:
            self.log('Bad [' + str(Constants.SMSG_REGISTER) + '] Register Response')
            print_exc()
