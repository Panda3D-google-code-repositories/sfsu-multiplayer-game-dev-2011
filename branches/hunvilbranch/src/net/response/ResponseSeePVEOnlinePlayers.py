# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 6, 2011 11:40:46 PM$"

from common.Constants import Constants
#from direct.showbase.DirectObject import DirectObject
from net.response.ServerResponse import ServerResponse
from traceback import print_exc

class ResponseSeePVEOnlinePlayers(ServerResponse):

    def execute(self, data):

        try:
            self.numberOfPlayers = data.getUint16()

            self.onlinePlayers = []

            for i in range (self.numberOfPlayers):
                i = data.getString()
                self.onlinePlayers.append(i)

            main.msgQ.putToMsgQ(CMSG_SEE_PVE_ONLINE_PLAYERS, self.onlinePlayers)


            self.log('Received [' + str(Constants.SMSG_SEE_PVE_ONLINE_PLAYERS) + '] See PVE Online Players Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_SEE_PVE_ONLINE_PLAYERS) + '] See PVP Online Players Response')
            print_exc()

