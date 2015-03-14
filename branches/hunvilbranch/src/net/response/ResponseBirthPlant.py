# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 17, 2011 8:16:46 AM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from direct.showbase.DirectObject import DirectObject

class ResponseBirthPlant(ServerResponse):

    def execute(self, data):

        try:
            if status == 1:
                plant = {   'plantID'     : data.getUint16(),
                            'plantType'   : data.getString(),
                            'avatarID'    : data.getUint16(),
                            'zoneID'      : data.getUint16(),
                            'biomass'     : data.getUint16(),
                            'xCoor'       : data.getUint16(),
                            'yCoor'       : data.getUint16()
                            #'desc'        : data.getString(),
                            #'cost'        : data.getUint16(),
                            #'maxBiomass'  : data.getUint16(),
                            #'waterNeedFreq' : data.getUint16(),
                            #'waterBiomassLoss' : data.getUint16(),
                            #'healChance'  : data.getUint16(),
                            #'growthRate'  : data.getUint16(),
                            #'growRadius'  : data.getUint16(),
                            #'lightNeedFreq' : data.getUint16()
                            }

            main.msgQ.putToMsgQ(Constants.SMSG_BIRTH_PLANT, plant)

            self.log('Received [' + str(Constants.SMSG_BIRTH_PLANT) + '] Birth Plnat Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_BIRTH_PLANT) + '] Birth Plant Response')
            print_exc()

