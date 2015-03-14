# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 17, 2011 8:47:30 AM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from direct.showbase.DirectObject import DirectObject

class ResponseUpdateGold(ServerResponse):

    def execute(self, data):

        try:
            self.status = data.getUint16()

            if self.status == 1:
                self.gold        = data.getUint16()

            main.msgQ.putToMsgQ(CMSG_UPDATE_GOLD, self.gold)

            self.log('Received [' + str(Constants.SMSG_UPDATE_GOLD) + '] Update Gold Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_UPDATE_GOLD) + '] Update Gold Response')
            print_exc()

