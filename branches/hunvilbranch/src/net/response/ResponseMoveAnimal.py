# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 16, 2011 6:22:10 PM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from direct.showbase.DirectObject import DirectObject

class ResponseMoveAnimal(ServerResponse):

    def execute(self, data):

        try:
            self.status = data.getUint16()

            if self.status == 1:
                self.info = { 'animalID' : data.getUint16(),
                              'xTarg'        : data.getUint16(),
                              'yTarg'        : data.getUint16() }

            main.msgQ.putToMsgQ(CMSG_MOVE_ANIMAL, self.info)

            self.log('Received [' + str(Constants.SMSG_MOVE_ANIMAL) + '] Move Animal Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_MOVE_ANIMAL) + '] Move Animal Response')
            print_exc()

