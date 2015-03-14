from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseExitGame(ServerResponse):

    def execute(self, data):

        try:
            status = data.getUint16()

            main.msgQ.putToMsgQ(Constants.CMSG_SAVE_EXIT_GAME, status)

            self.log('Received [' + str(Constants.SMSG_SAVE_EXIT_GAME) + '] Exit Game Response')
        except:
            self.log('Bad [' + str(Constants.SMSG_SAVE_EXIT_GAME) + '] Exit Game Response')
            print_exc()
