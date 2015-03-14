# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 7, 2011 12:02:38 AM$"

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from traceback import print_exc

class ResponseReady(ServerResponse):

    def execute(self, data):

        try:
            status = data.getBool()
            username = data.getString()

            main.msgQ.putToMsgQ(Constants.CMSG_READY, [status, username])

            self.log('Received [' + str(Constants.SMSG_READY) + '] Ready Response')
        except:
            self.log('Bad [' + str(Constants.SMSG_READY) + '] Ready Response')
            print_exc()
