# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 19, 2011 1:08:33 AM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from direct.showbase.DirectObject import DirectObject

class ResponseUpdateAvatarCash(ServerResponse):

    def execute(self, data):

        try:
            self.cash    = data.getUint16()

            main.msgQ.putToMsgQ(SMSG_UPDATE_AVATAR_CASH, self.cash)

            self.log('Received [' + str(Constants.SMSG_UPDATE_AVATAR_CASH) + '] Update Avatar Cash Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_UPDATE_AVATAR_CASH) + '] Update Avatar Cash Response')
            print_exc()