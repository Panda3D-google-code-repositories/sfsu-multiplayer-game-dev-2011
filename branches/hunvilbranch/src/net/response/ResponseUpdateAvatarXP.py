# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 19, 2011 1:02:20 AM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from direct.showbase.DirectObject import DirectObject

class ResponseUpdateAvatarXP(ServerResponse):

    def execute(self, data):

        try:
            self.xp    = data.getUint16()

            main.msgQ.putToMsgQ(SMSG_UPDATE_AVATAR_XP, self.xp)

            self.log('Received [' + str(Constants.SMSG_UPDATE_AVATAR_XP) + '] Update Avatar XP Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_UPDATE_AVATAR_XP) + '] Update Avatar XP Response')
            print_exc()
