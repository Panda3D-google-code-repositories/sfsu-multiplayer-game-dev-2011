# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 19, 2011 12:35:43 AM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from direct.showbase.DirectObject import DirectObject

class ResponseCurePlantDisease(ServerResponse):

    def execute(self, data):

        try:
            self.info = { 'plantID'      : data.getUint16(),
                          'diseaseID'    : data.getUint16() }

            main.msgQ.putToMsgQ(Constants.SMSG_CURE_PLANT_DISEASE, self.info)

            self.log('Received [' + str(Constants.SMSG_CURE_PLANT_DISEASE) + '] Reveal Cure Disease Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_CURE_PLANT_DISEASE) + '] Reveal Cure Disease Response')
            print_exc()
