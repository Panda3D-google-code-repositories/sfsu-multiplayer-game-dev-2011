# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 16, 2011 10:24:49 PM$"

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from direct.showbase.DirectObject import DirectObject

class ResponseUpdateAnimalTarget(ServerResponse):

    def execute(self, data):

        try:
            self.status     = data.getUint16()
            
#            self.info = { 'animalTypeID' : data.getUint16(),
#                          'zoneID'       : data.getUint16(),
#                          'xTarget'      : data.getUint16(),
#                          'yTarget'      : data.getUint16() }

            main.msgQ.putToMsgQ(SMSG_UPDATE_ANIMAL_TARGET, self.status)

            self.log('Received [' + str(Constants.SMSG_UPDATE_ANIMAL_TARGET) + '] Update Animal Target Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_UPDATE_ANIMAL_TARGET) + '] Update Animal Target Response')
            print_exc()


