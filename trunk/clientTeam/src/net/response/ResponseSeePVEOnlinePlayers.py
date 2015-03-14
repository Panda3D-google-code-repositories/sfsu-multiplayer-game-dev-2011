from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from traceback import print_exc

class ResponseSeePVEOnlinePlayers(ServerResponse):

    def execute(self, data):

        try:
            self.numberOfPlayers = data.getUint16()

            self.onlinePlayers = []

            for player in range (self.numberOfPlayers):
                self.onlinePlayers.append(player)

            main.msgQ.putToMsgQ(Constants.CMSG_SEE_PVE_ONLINE_PLAYERS, self.onlinePlayers)

            self.log('Received [' + str(Constants.SMSG_SEE_PVE_ONLINE_PLAYERS) + '] See PVE Online Players Response')
        except:
            self.log('Bad [' + str(Constants.SMSG_SEE_PVE_ONLINE_PLAYERS) + '] See PVP Online Players Response')
            print_exc()
