# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 17, 2011 8:49:57 AM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from direct.showbase.DirectObject import DirectObject

class ResponseUpdateXP(ServerResponse):

    def execute(self, data):

        try:
            self.status = data.getUint16()

            if status == 1:
                self.xp        = data.getUint16()

            main.msgQ.putToMsgQ(CMSG_UPDATE_XP, self.xp)

            self.log('Received [' + str(Constants.SMSG_UPDATE_XP) + '] Update XP Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_UPDATE_XP) + '] Update XP Response')
            print_exc()
