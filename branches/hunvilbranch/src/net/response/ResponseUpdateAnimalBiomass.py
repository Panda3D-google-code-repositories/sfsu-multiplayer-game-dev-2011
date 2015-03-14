# To change this template, choose Tools | Templates
# and open the template in the editor.

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from direct.showbase.DirectObject import DirectObject

class ResponseUpdateAnimalBiomass(ServerResponse):

    def execute(self, data):

        try:
            animal = {  'animalID'     : data.getUint16(),
                        'biomass'      : data.getUint16(),
                        'targetBiomass': data.getUint16(),
                        'targetTime'   : data.getUint16() }

            main.msgQ.putToMsgQ(SMSG_UPDATE_ANIMAL_BIOMASS, animal)

            self.log('Received [' + str(Constants.SMSG_UPDATE_ANIMAL_BIOMASS) + '] Update Animal Biomass Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_UPDATE_ANIMAL_BIOMASS) + '] Update Animal Biomass Response')
            print_exc()
