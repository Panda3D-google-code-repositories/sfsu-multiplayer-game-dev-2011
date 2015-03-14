# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 19, 2011 12:26:11 AM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from direct.showbase.DirectObject import DirectObject

class ResponseUpdateAnimalNoWaterCount(ServerResponse):

    def execute(self, data):

        try:
            self.info = {  'animalID'     : data.getUint16(),
                           'noWaterCOunt' : data.getUint16() }

            main.msgQ.putToMsgQ(Constants.SMSG_UPDATE_ANIMAL_NO_WATER_COUNT, self.info)

            self.log('Received [' + str(Constants.SMSG_UPDATE_ANIMAL_NO_WATER_COUNT) + '] Update Animal No Water Count Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_UPDATE_ANIMAL_NO_WATER_COUNT) + '] Update Animal No Water Count Response')
            print_exc()

