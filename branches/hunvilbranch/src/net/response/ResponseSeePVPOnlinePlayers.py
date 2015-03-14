# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 6, 2011 11:47:49 PM$"

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from traceback import print_exc

class ResponseSeePVPOnlinePlayers(ServerResponse):

    def execute(self, data):

        try:
            self.numberOfPlayers = data.getUint16()
            self.onlinePlayers = []

            for i in range (self.numberOfPlayers):
                i = data.getString()
                self.onlinePlayers.append(i)

            main.msgQ.putToMsgQ(CMSG_SEE_PVP_ONLINE_PLAYERS, self.onlinePlayers)

            self.log('Received [' + str(Constants.SMSG_SEE_PVP_ONLINE_PLAYERS) + '] See PVP Online Players Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_SEE_PVP_ONLINE_PLAYERS) + '] See PVP Online Players Response')
            print_exc()


