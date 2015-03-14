from common.Constants import Constants
from main.MainLobby.WorldLobby.PvPWorldLobby import WorldObj
from net.response.ServerResponse import ServerResponse
from traceback import print_exc

class ResponseCreateNewWorld(ServerResponse):

    def execute(self, data):

        try:
            status = data.getUint16()
            worldType = data.getUint16()                                #1 = PvE, 2 = PvP

            name = ''
            if status == 0:                                        #success
                world_id = data.getUint32()
                name  = data.getString()
                ecosystem  = data.getString()
                maxPlayerNumber = data.getUint16()
                charName    = data.getString()

                _object = WorldObj(name, ecosystem, maxPlayerNumber, charName)

                main.msgQ.addToPendingObj(Constants.PENDING_WORLD_LOBBY_OBJ, _object)

                args = {'status'    : status,
                        'world_id'  : world_id,
                        'name'      : name}
                main.msgQ.putToMsgQ(Constants.SMSG_CREATE_NEW_WORLD, args)

            if worldType == 1:
                messenger.send(Constants.LISTENER_CREATE_NEW_WORLD_RESPONSE, [status, name])
            else:
                messenger.send(Constants.LISTENER_CREATE_NEW_GAME_RESPONSE, [status])

            self.log('Received [' + str(Constants.SMSG_CREATE_NEW_WORLD) + '] Create New World Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_CREATE_NEW_WORLD) + '] Create New World Response')
            print_exc()
