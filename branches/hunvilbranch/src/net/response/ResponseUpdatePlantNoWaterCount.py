# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 18, 2011 11:29:05 PM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from direct.showbase.DirectObject import DirectObject

class ResponseUpdatePlantNoWaterCount(ServerResponse):

    def execute(self, data):

        try:
            status = data.getUint16()

            if status == 1:
                info = {  'plantID'      : data.getUint16(),
                          'noWaterCount' : data.getUint16() }

            main.msgQ.putToMsgQ(SMSG_UPDATE_PLANT_NO_WATER_COUNT, info)

            self.log('Received [' + str(Constants.SMSG_UPDATE_PLANT_NO_WATER_COUNT) + '] Update Plant No Water Count Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_UPDATE_PLANT_NO_WATER_COUNT) + '] Update Plant No Water Count Response')
            print_exc()

