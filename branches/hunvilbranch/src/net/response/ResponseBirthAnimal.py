# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 16, 2011 10:10:46 PM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from direct.showbase.DirectObject import DirectObject

class ResponseBirthAnimal(ServerResponse):

    def execute(self, data):

        try:
            animal = {  'animalID'     : data.getUint16(),
                        'animalType'   : data.getString(),
                        'avatarID'     : data.getUint16(),
                        #'desc'         : data.getString(),
                        #'cost'         : data.getUint16(),
                        #'maxBiomass'   : data.getUint16(),
                        'zoneID'       : data.getUint16(),
                        'biomass'      : data.getUint16(),
                        #'envIDcol'     : data.getUint16(),
                        #'envIDrow'     : data.getUint16(),
                        'xCoor'        : data.getUint16(),
                        'yCoor'        : data.getUint16(),
                        #'waterNeedFreq': data.getUint16(),
                        #'waterBiomassLoss' : data.getUint16(),
                        #'healChance'   : data.getUint16(),
                        #'growthRate'   : data.getUint16(),
                        #'loyalty'      : data.geUint16(),
                        #'maxTravelPerSec' : data.getUint16()
                            }
            
            main.msgQ.putToMsgQ(Constants.SMSG_BIRTH_ANIMAL, animal)

            self.log('Received [' + str(Constants.SMSG_BIRTH_ANIMAL) + '] Birth Animal Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_BIRTH_ANIMAL) + '] Birth Animal Response')
            print_exc()
