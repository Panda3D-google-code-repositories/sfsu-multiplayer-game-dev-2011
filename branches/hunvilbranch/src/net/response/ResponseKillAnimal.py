# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 19, 2011 12:30:31 AM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from direct.showbase.DirectObject import DirectObject

class ResponseKillAnimal(ServerResponse):

    def execute(self, data):

        try:
            self.animalID = data.getUint16()

            main.msgQ.putToMsgQ(Constants.SMSG_KILL_ANIMAL, self.animalID)

            self.log('Received [' + str(Constants.SMSG_KILL_ANIMAL) + '] Kill Animal Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_KILL_ANIMAL) + '] Kill Animal Response')
            print_exc()
