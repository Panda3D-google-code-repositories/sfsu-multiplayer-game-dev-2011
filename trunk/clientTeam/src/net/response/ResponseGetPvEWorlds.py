# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Oct 29, 2011 5:46:48 PM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from main.MainLobby.GameLobby.PvPGameLobby import GameObject

class ResponseGetPvEWorlds(ServerResponse):

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

            main.msgQ.putToMsgQ(Constants.CMSG_GETPVEWORLDS, worldList)

#            messenger.send(Constants.LISTENER_PVE_2D, [pveClosedWorlds, pveOpenedWorlds])

            self.log('Received [' + str(Constants.SMSG_GETPVEWORLDS) + '] Get PVE Worlds Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_GETPVEWORLDS) + '] Get PVE Worlds Response')
            print_exc()


