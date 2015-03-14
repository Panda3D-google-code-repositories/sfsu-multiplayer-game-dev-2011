# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 18, 2011 11:24:45 PM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from direct.showbase.DirectObject import DirectObject

class ResponseUpdatePlantBiomass(ServerResponse):

    def execute(self, data):

        try:
            status = data.getUint16()

            if status == 1:
                animal = {  'plantID'      : data.getUint16(),
                            'biomass'      : data.getUint16(),
                            'targetBiomass': data.getUint16(),
                            'targetTime'   : data.getUint16() }

            main.msgQ.putToMsgQ(SMSG_UPDATE_PLANT_BIOMASS, animal)

            self.log('Received [' + str(Constants.SMSG_UPDATE_PLANT_BIOMASS) + '] Update Plant Biomass Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_UPDATE_PLANT_BIOMASS) + '] Update Plant Biomass Response')
            print_exc()
