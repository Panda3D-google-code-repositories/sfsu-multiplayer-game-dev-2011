# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 17, 2011 8:21:02 AM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from direct.showbase.DirectObject import DirectObject

class ResponseBuyPlant(ServerResponse):

    def execute(self, data):

        try:
            self.status = data.getUint16()

#        try:
#            if self.status == 1:
#                self.plant = {  'plantID'     : data.getUint16(),
#                                'plantType'   : data.getString(),
#                                'desc'        : data.getString(),
#                                'cost'        : data.getUint16(),
#                                'maxBiomass'  : data.getUint16(),
#                                'waterNeedFreq' : data.getUint16(),
#                                'waterBiomassLoss' : data.getUint16(),
#                                'healChance'  : data.getUint16(),
#                                'growthRate'  : data.getUint16(),
#                                'growRadius'  : data.getUint16(),
#                                'lightNeedFreq' : data.getUint16() }

            main.msgQ.putToMsgQ(Constants.CMSG_BUY_PLANT, self.status)

            self.log('Received [' + str(Constants.SMSG_BUY_PLANT) + '] Buy Plant Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_BUY_PLANT) + '] Buy Plant Response')
            print_exc()