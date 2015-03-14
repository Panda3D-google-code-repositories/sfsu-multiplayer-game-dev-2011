#__author__="kelvin"
#__date__ ="$Nov 5, 2011 1:13:44 PM$"

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from traceback import print_exc

class ResponseCreateNewWorld(ServerResponse):

    def execute(self, data):

        try:
            self.status = data.getUint16()
            worldType   = data.getUint()                                #1 = PvE, 2 = PvP

            if self.status == 0:                                        #success

                worldName  = data.getString()
                ecosystem  = data.getString()
                maxPlayerNumber = data.getUint16()
                charName    = data.getString()

                object = WorldObj(worldName, ecosystem, maxPlayerNumber, charName)

                main.msgQ.addToPendingObj(Constants.PENDING_WORLD_LOBBY_OBJ, object)

            if worldType == 1:
                messenger.send(Constants.LISTENER_CREATE_NEW_WORLD_RESPONSE, self.status)
            else:
                messenger.send(Constants.LISTENER_CREATE_NEW_GAME_RESPONSE, self.status)


            #main.msgQ.putToMsgQ(Constants.CMSG_CREATE_NEW_WORLD, self.info)

            self.log('Received [' + str(Constants.SMSG_CREATE_NEW_WORLD) + '] Get PVP Worlds Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_CREATE_NEW_WORLD) + '] Get PVP Worlds Response')
            print_exc()
