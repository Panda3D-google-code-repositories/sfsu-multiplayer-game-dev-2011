# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 30, 2011 3:19:41 PM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseUpdateGameScaleTime(ServerResponse):

    def execute(self, data):

        try:
            self.scaleTime = data.getFloat64()      #new scale time

            main.msgQ.putToMsgQ(Constants.SMSG_UPDATE_GAME_SCALE_TIME, self.scaleTime)

            self.log('Received [' + str(Constants.SMSG_UPDATE_GAME_SCALE_TIME) + '] Update Game Scale Time Response')
        except:
            self.log('Bad [' + str(Constants.SMSG_UPDATE_GAME_SCALE_TIME) + '] update Game Scale Time Response')
            print_exc()
