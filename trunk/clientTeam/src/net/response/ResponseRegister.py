# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseRegister(ServerResponse):

    def execute(self, data):

        try:
            self.status = data.getUint16()

            main.msgQ.putToMsgQ(Constants.CMSG_REGISTER, self.status)

            self.log('Received [' + str(Constants.SMSG_REGISTER) + '] Register Response')
        except:
            self.log('Bad [' + str(Constants.SMSG_REGISTER) + '] Register Response')
            print_exc()
