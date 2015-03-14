# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 19, 2011 12:38:15 AM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from direct.showbase.DirectObject import DirectObject

class ResponseUpdatePlantNoLightCount(ServerResponse):

    def execute(self, data):

        try:
            self.info = { 'plantID'  : data.getUint16(),
                          'noLightCount' : data.getUint16() }

            main.msgQ.putToMsgQ(Constants.SMSG_UPDATE_PLANT_NO_LIGHT_COUNT, self.info)

            self.log('Received [' + str(Constants.SMSG_UPDATE_PLANT_NO_LIGHT_COUNT) + '] Update Plant No Light Count Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_UPDATE_PLANT_NO_LIGHT_COUNT) + '] Update Plant No Light Count Response')
            print_exc()
