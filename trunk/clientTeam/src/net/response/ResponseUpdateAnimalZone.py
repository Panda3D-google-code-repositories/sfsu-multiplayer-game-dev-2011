# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 18, 2011 11:34:36 PM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from direct.showbase.DirectObject import DirectObject

class ResponseUpdateAnimalZone(ServerResponse):

    def execute(self, data):

        try:
            info = {  'animalID'   : data.getUint16(),
                      'newZoneID'  : data.getUint16() }

            main.msgQ.putToMsgQ(Constants.SMSG_UPDATE_ANIMAL_ZONE, info)

            self.log('Received [' + str(Constants.SMSG_UPDATE_ANIMAL_ZONE) + '] Update Animal Zone Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_UPDATE_ANIMAL_ZONE) + '] Update Animal Zone Response')
            print_exc()


