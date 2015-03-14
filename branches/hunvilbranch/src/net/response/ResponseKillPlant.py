# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 19, 2011 12:43:06 AM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from direct.showbase.DirectObject import DirectObject

class ResponseKillPlant(ServerResponse):

    def execute(self, data):

        try:
            self.plantID  = data.getUint16()

            main.msgQ.putToMsgQ(Constants.SMSG_KILL_PLANT, self.plantID)

            self.log('Received [' + str(Constants.SMSG_KILL_PLANT) + '] Kill Plant Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_KILL_PLANT) + '] Kill Plant Response')
            print_exc()

