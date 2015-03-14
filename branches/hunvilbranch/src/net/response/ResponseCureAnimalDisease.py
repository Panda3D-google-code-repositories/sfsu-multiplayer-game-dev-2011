# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 19, 2011 12:16:44 AM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from direct.showbase.DirectObject import DirectObject

class ResponseCureAnimalDisease(ServerResponse):

    def execute(self, data):

        try:
            self.info = { 'animalID'     : data.getUint16(),
                          'diseaseID'    : data.getUint16() }

            main.msgQ.putToMsgQ(Constants.CMSG_CURE_ANIMAL, self.info)

            self.log('Received [' + str(Constants.SMSG_CURE_ANIMAL_DISEASE) + '] Cure Animal Disease Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_CURE_ANIMAL_DISEASE) + '] Cure Animal Disease Response')
            print_exc()