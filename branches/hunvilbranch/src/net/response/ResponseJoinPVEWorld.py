# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 5, 2011 4:54:52 PM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseJoinPVEWorld(ServerResponse):

    def execute(self, data):

        try:
            self.status = data.getUint16()

            if self.status == 0:                  #success
                self.numberOfPlayers = data.getUint16()
                self.players = []

                for i in range (self.numberOfPlayers):
                    self.info   = { 'userName'  : data.getString(),
                                    'position'  : data.getUint16(),
                                    'avatar'    : data.getString() }

                    self.players.append(self.info)

            else:
                main.showAlert(self.status)

            main.msgQ.putToMsgQ(Constants.CMSG_JOIN_PVE_WORLD, self.players)

            self.log('Received [' + str(Constants.SMSG_JOIN_PVE_WORLD) + '] Join PVE Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_JOIN_PVE_WORLD) + '] Join PVE Response')
            print_exc()
