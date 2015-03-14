# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 19, 2011 12:33:25 AM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from direct.showbase.DirectObject import DirectObject

class ResponseRevealPlantDisease(ServerResponse):

    def execute(self, data):

        try:
            self.info = { 'plantTypeID'  : data.getUint16(),
                          'diseaseID'    : data.getUint16() }

            main.msgQ.putToMsgQ(SMSG_REVEAL_PLANT_DISEASE, self.info)

            self.log('Received [' + str(Constants.SMSG_REVEAL_PLANT_DISEASE) + '] Reveal Plant Disease Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_REVEAL_PLANT_DISEASE) + '] Reveal Plant Disease Response')
            print_exc()