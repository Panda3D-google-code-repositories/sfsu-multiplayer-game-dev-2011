from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseStartGame(ServerResponse):

    def execute(self, data):

        try:
            info = {'status' : data.getBool()}

            main.msgQ.putToMsgQ(Constants.CMSG_START_GAME, info)

            self.log('Received [' + str(Constants.SMSG_START_GAME) + '] Start Game Response')
        except:
            self.log('Bad [' + str(Constants.SMSG_START_GAME) + '] Start Game Response')
            print_exc()
