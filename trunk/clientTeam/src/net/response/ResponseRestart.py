from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseRestart(ServerResponse):

    def execute(self, data):

        try:
            status = data.getBool()

            main.msgQ.putToMsgQ(Constants.SMSG_RESTART, status)
            self.log('Received [' + str(Constants.SMSG_RESTART) + '] Restart Response')
        except:
            self.log('Bad [' + str(Constants.SMSG_RESTART) + '] Restart Response')
            print_exc()