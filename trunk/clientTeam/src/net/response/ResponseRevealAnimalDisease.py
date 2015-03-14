# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 16, 2011 10:18:33 PM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from direct.showbase.DirectObject import DirectObject

class ResponseRevealAnimalDisease(ServerResponse):

    def execute(self, data):

        try:
            self.info = { 'animalID' : data.getUint16(),
                          'diseaseID'    : data.getUint16() }

            main.msgQ.putToMsgQ(Constants.SMSG_REVEAL_ANIMAL_DISEASE, self.info)

            self.log('Received [' + str(Constants.SMSG_REVEAL_ANIMAL_DISEASE) + '] Reveal Animal Disease Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_REVEAL_ANIMAL_DISEASE) + '] Reveal Animal Disease Response')
            print_exc()

