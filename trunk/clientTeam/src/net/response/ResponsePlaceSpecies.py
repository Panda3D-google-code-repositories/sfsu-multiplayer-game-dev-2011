# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 26, 2011 10:11:46 PM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from direct.showbase.DirectObject import DirectObject

class ResponsePlaceSpecies(ServerResponse):

    def execute(self, data):

        try:
            self.status    = data.getUint16()

            main.msgQ.putToMsgQ(Constants.CMSG_PLACE_SPECIES, self.status)

            self.log('Received [' + str(Constants.SMSG_PLACE_SPECIES) + '] Place Species Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_PLACE_SPECIES) + '] Place Species Response')
            print_exc()
