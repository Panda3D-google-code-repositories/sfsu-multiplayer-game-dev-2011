from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from traceback import print_exc

class ResponseSeeOnlinePlayers(ServerResponse):
        
    def execute(self, data):

        try:
            size = data.getUint16()

            playerList = {}

            for i in range(size):
                player_id = data.getUint32()
                name = data.getString()

                playerList[player_id] = name

            main.msgQ.putToMsgQ(Constants.CMSG_SEEONLINEPLAYERS, playerList)

            self.log('Received [' + str(Constants.SMSG_SEEONLINEPLAYERS) + '] See Online Players Response')
        except:
            self.log('Bad [' + str(Constants.SMSG_SEEONLINEPLAYERS) + '] See Online Players Response')
            print_exc()
