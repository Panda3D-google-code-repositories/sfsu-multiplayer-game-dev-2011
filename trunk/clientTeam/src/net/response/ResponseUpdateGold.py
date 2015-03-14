# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 17, 2011 8:47:30 AM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from direct.showbase.DirectObject import DirectObject

class ResponseUpdateGold(ServerResponse):

    def execute(self, data):

        try:
            info = {'amount'    : data.getUint32(),
                    'gold'      : data.getUint32()}

            main.msgQ.putToMsgQ(Constants.SMSG_UPDATE_GOLD, info)

            self.log('Received [' + str(Constants.SMSG_UPDATE_GOLD) + '] Update Gold Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_UPDATE_GOLD) + '] Update Gold Response')
            print_exc()

