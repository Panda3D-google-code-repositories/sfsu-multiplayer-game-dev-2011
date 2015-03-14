# To change this template, choose Tools | Templates
# and open the template in the editor.
from common.Constants import Constants
from direct.showbase.DirectObject import DirectObject
from net.response.ServerResponse import ServerResponse
from traceback import print_exc

__author__="kelvin"
__date__ ="$Oct 29, 2011 6:11:52 PM$"


class ResponseSeeOnlinePlayers(ServerResponse):
        
    def execute(self, data):

        try:
            self.numberOfPlayers = data.getUint16()
            self.onlinePlayers = []

            for i in range (self.numberOfPlayers):
                i = data.getString()
                self.onlinePlayers.append(i)

            main.msgQ.putToMsgQ(Constants.CMSG_SEEONLINEPLAYERS, self.onlinePlayers)

            self.log('Received [' + str(Constants.SMSG_SEEONLINEPLAYERS) + '] See Online Players Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_SEEONLINEPLAYERS) + '] See Online Players Response')
            print_exc()

