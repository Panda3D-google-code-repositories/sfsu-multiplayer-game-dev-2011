# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 19, 2011 1:00:33 AM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseUpdateAvgGameScale(ServerResponse):

    def execute(self, data):

        try:
            self.avgVote    = data.getUint16()

            main.msgQ.putToMsgQ(Constants.SMSG_UPDATE_AVG_GAME_SCALE, self.avgVote)

            self.log('Received [' + str(Constants.SMSG_UPDATE_AVG_GAME_SCALE) + '] Update Avg Game Scale Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_UPDATE_AVG_GAME_SCALE) + '] Update Avg Game Scale Response')
            print_exc()
