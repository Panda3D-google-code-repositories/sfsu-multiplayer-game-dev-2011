from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from main.MainLobby.GameLobby.PvPGameLobby import GameObject

class ResponseGetPlayerWorlds(ServerResponse):

    def execute(self, data):

        try:
            worldList = []
            numberOfWorlds = data.getUint16()

            for i in range(numberOfWorlds):
                isPublic = data.getUint16()
                playedByUser = data.getUint16()
                worldName = data.getString()
                currentPlayerNumber = data.getUint16()
                maxPlayerNumber = data.getUint16()
                ecosystem = data.getString()
                gameObj = GameObject(worldName, currentPlayerNumber, maxPlayerNumber, ecosystem, playedByUser)

                worldList.append(gameObj)

            main.msgQ.putToMsgQ(Constants.CMSG_GET_PLAYER_WORLDS, worldList)

            self.log('Received [' + str(Constants.CMSG_GET_PLAYER_WORLDS) + '] Get Player Worlds Response')

        except:
            self.log('Bad [' + str(Constants.CMSG_GET_PLAYER_WORLDS) + '] Get Player Worlds Response')
            print_exc()


