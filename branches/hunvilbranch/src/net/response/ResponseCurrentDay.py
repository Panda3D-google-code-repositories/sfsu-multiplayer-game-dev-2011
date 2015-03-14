# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 19, 2011 12:51:54 AM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from direct.showbase.DirectObject import DirectObject

class ResponseCurrentDay(ServerResponse):

    def execute(self, data):

        try:
            self.currentDay  = data.getUint16()

            main.msgQ.putToMsgQ(Constants.SMSG_CURRENT_DAY, self.currentDay)

            self.log('Received [' + str(Constants.SMSG_CURRENT_DAY) + '] Current Day Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_CURRENT_DAY) + '] Current Day Response')
            print_exc()
