# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 26, 2011 10:27:20 PM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseKickPlayerPVPLobby(ServerResponse):

    def execute(self, data):

        try:
            self.status = data.getUint16()

            if self.status == 0:

                self.info = { 'userName' : data.getString(),    #player that is kicked out
                              'message'  : data.getString() }

                main.msgQ.addToPendingObj(Constants.PENDING_KICK_PLAYER_PVP_LOBBY, self.info)

            main.msgQ.putToMsgQ(Constants.CMSG_KICK_PLAYER_PVP_LOBBY, self.status)

            self.log('Received [' + str(Constants.SMSG_KICK_PLAYER_PVP_LOBBY) + '] Kick Player PVP Lobby Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_KICK_PLAYER_PVP_LOBBY) + '] Kick Player PVP Lobby Response')
            print_exc()