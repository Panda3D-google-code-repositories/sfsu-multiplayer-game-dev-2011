# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 19, 2011 1:33:01 AM$"

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from direct.showbase.DirectObject import DirectObject

class ResponseUpdateAnimalCoors(ServerResponse):

    def execute(self, data):

        try:
            self.status     = data.getUint16()

            main.msgQ.putToMsgQ(CMSG_UPDATE_ANIMAL_COORS, self.status)

            self.log('Received [' + str(Constants.SMSG_UPDATE_ANIMAL_COORS) + '] Update Animal Coors Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_UPDATE_ANIMAL_COORS) + '] Update Animal Coors Response')
            print_exc()



