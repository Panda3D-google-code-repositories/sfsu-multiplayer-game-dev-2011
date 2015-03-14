# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 22, 2011 11:52:07 AM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from direct.showbase.DirectObject import DirectObject

class ResponseWaterSources(ServerResponse):

    def execute(self, data):

        try:
            self.status = data.getUint16()

            main.msgQ.putToMsgQ(CMSG_REQUESTWATERSOURCES, self.status)

            self.log('Received [' + str(Constants.SMSG_REQUESTWATERSOURCES) + '] Water sources Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_REQUESTWATERSOURCES) + '] Water sources Response')
            print_exc()

