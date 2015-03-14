# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 19, 2011 12:43:06 AM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseKillPlant(ServerResponse):

    def execute(self, data):

        try:
            info = {'plantID'   : data.getUint32(),
                    'predatorID': data.getUint32(),
                    'count'     : data.getUint16()}

            main.msgQ.putToMsgQ(Constants.SMSG_KILL_PLANT, info)

            self.log('Received [' + str(Constants.SMSG_KILL_PLANT) + '] Kill Plant Response')
        except:
            self.log('Bad [' + str(Constants.SMSG_KILL_PLANT) + '] Kill Plant Response')
            print_exc()

