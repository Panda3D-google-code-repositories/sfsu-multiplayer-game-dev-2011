# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 19, 2011 1:10:08 AM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseUpdateEnvScore(ServerResponse):

    def execute(self, data):

        try:
            info = { 'env_id'    : data.getUint32(),
                     'score'     : data.getUint32()}

            main.msgQ.putToMsgQ(Constants.SMSG_UPDATE_ENV_SCORE, info)

            self.log('Received [' + str(Constants.SMSG_UPDATE_ENV_SCORE) + '] Update Env. Score Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_UPDATE_ENV_SCORE) + '] Update Env. Score Response')
            print_exc()