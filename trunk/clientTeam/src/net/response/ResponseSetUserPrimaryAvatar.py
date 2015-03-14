# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 19, 2011 1:15:38 AM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from direct.showbase.DirectObject import DirectObject

class ResponseSetUserPrimaryAvatar(ServerResponse):

    def execute(self, data):

        try:
            self.isUserPrimaryAvatar = data.getUint16()

            main.msgQ.putToMsgQ(Constants.SMSG_UPDATE_ENV_SCORE, self.isUserPrimaryAvatar)

            self.log('Received [' + str(Constants.SMSG_SET_USER_PRIMARY_AVATAR) + '] Set User Primary Avatar Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_SET_USER_PRIMARY_AVATAR) + '] Set User Primary Avatar Response')
            print_exc()
