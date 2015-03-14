# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 5, 2011 5:16:00 PM$"

from traceback import print_exc
from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseJoinPVPWorld(ServerResponse):

    def execute(self, data):

        try:
            self.status = data.getUint16()

            if self.status == 0:                           #success
                self.numberOfPlayers = data.getUint16()
                self.players = []

                for i in range (self.numberOfPlayers):
                    self.info = { 'userName'    : data.getString(),
                                  'teamNumber'  : data.getUint16(),
                                  'position'    : data.getUint16(),
                                  'avatar'      : data.getString() }

                    self.players.append(self.info)

            main.msgQ.putToMsgQ(Constants.CMSG_JOIN_PVP_WORLD, self.players)

            self.log('Received [' + str(Constants.SMSG_JOIN_PVP_WORLD) + '] Join PVP World Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_JOIN_PVP_WORLD) + '] Join PVP World Response')
            print_exc()
