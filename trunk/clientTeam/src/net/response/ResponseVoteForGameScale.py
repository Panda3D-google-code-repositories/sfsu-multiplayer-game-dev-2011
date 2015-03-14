# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 16, 2011 9:46:37 PM$"

from src.common.Constants import Constants
from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseVoteForGameScale(ServerResponse):

    def execute(self, data):

        try:

            self.status = data.getUint16()

            if self.status == 0:
                self.gameScale = data.getUint16()

            main.msgQ.putToMsgQ(Constants.CMSG_VOTE_GAME_SCALE, self.gameScale)

            self.log('Received [' + str(Constants.SMSG_VOTE_GAME_SCALE) + '] Vote Game Scale Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_VOTE_GAME_SCALE) + '] Vote Game Scale Response')
            print_exc()