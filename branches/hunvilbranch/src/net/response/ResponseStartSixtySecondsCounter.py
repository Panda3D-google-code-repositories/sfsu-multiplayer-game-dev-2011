# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 21, 2011 2:50:06 PM$"


from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from traceback import print_exc

class ResponseStartSixtySecondsCounter(ServerResponse):

    def execute(self, data):

        try:
            self.status = data.getUint16()

            main.msgQ.putToMsgQ(Constants.CMSG_START_SIXTY_SECONDS_COUNTER, self.status)

            self.log('Received [' + str(Constants.SMSG_START_SIXTY_SECONDS_COUNTER) + '] Start Sixty Seconds Counter Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_START_SIXTY_SECONDS_COUNTER) + '] Start Sixty Seconds Counter Response')
            print_exc()
