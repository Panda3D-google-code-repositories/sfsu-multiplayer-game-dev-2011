# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 20, 2011 2:18:02 PM$"

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from direct.showbase.DirectObject import DirectObject

class ResponseUpdatePlantCoors(ServerResponse):

    def execute(self, data):

        try:
            self.status     = data.getUint16()

            main.msgQ.putToMsgQ(Constants.CMSG_UPDATE_PLANT_COORS, self.status)

            self.log('Received [' + str(Constants.SMSG_UPDATE_PLANT_COORS) + '] Update Plant Coors Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_UPDATE_PLANT_COORS) + '] Update Plant Coors Response')
            print_exc()



