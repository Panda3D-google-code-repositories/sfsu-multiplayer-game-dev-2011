# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 23, 2011 11:55:45 AM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseChooseAvatarTypePVE(ServerResponse):

    def execute(self, data):

        try:
            self.status = data.getUint16()      #0 = success
            print 'status: '+str(self.status)
            main.msgQ.putToMsgQ(Constants.CMSG_CHOOSE_AVATAR_TYPE, self.status)

            self.log('Received [' + str(Constants.SMSG_CHOOSE_AVATAR_TYPE) + '] Choose Avatar Type PVE Response')
        except:
            self.log('Bad [' + str(Constants.SMSG_CHOOSE_AVATAR_TYPE) + '] Choose Avatar Type PVE Response')
            print_exc()

