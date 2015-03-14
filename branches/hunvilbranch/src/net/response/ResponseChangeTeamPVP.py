# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 12, 2011 10:44:26 PM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseChangeTeamPVP(ServerResponse):

    def execute(self, data):

        try:
            self.status = data.getUint16()

            if self.status == 0:
        
                self.numberOfPlayers = data.getUint16()
                self.players = []

                for i in range (self.numberOfPlayers):
                    self.info = { 'userName'     : data.getString(),
                                  'teamNumber'   : data.getUint16(),
                                  'position'     : data.getUint16(),
                                  'avatar'       : data.getString(),
                                  'isReady'      : data.getUint16() }
                self.players.append(self.info)

                main.msgQ.putToMsgQ(Constants.CMSG_CHANGE_TEAM_PVP, self.info)

            self.log('Received [' + str(Constants.SMSG_CHANGE_TEAM_PVP) + '] Change Team PVP Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_CHANGE_TEAM_PVP) + '] Change Team PVP Response')
            print_exc()