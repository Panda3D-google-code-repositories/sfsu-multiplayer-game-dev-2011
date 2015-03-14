# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 5, 2011 5:24:24 PM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseStartToReadyWorld(ServerResponse):

    def execute(self, data):

        try:
            self.status = data.getUint16()      #0 = success

            main.msgQ.putToMsgQ(Constants.CMSG_START_TO_READY_GAME, self.status)

            self.log('Received [' + str(Constants.SMSG_START_TO_READY_GAME) + '] Authentication Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_START_TO_READY_GAME) + '] Authentication Response')
            print_exc()