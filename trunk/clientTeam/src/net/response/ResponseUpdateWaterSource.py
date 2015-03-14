# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 19, 2011 12:47:56 AM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseUpdateWaterSource(ServerResponse):

    def execute(self, data):

        try:
            self.info = { 'waterSourceID'       : data.getUint16(),
                          'zoneID'              : data.getUint16(),
                          'waterAmount'         : data.getUint16(),
                          'targetWaterAmount'   : data.getUint16(),
                          'targetTime'          : data.getUint16() }

            main.msgQ.putToMsgQ(Constants.SMSG_UPDATE_WATER_SOURCE, self.info)

            self.log('Received [' + str(Constants.SMSG_UPDATE_WATER_SOURCE) + '] Update Water Source Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_UPDATE_WATER_SOURCE) + '] Update Water Source Response')
            print_exc()
