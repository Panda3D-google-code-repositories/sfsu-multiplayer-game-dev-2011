# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 19, 2011 12:03:35 AM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from direct.showbase.DirectObject import DirectObject

class ResponseUpdateAnimalOwner(ServerResponse):

    def execute(self, data):

        try:
            info = {  'animalID'     : data.getUint16(),
                      'newAvatarID'  : data.getUint16() }

            main.msgQ.putToMsgQ(SMSG_UPDATE_ANIMAL_OWNER, info)

            self.log('Received [' + str(Constants.SMSG_UPDATE_ANIMAL_OWNER) + '] Update Animal Owner Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_UPDATE_ANIMAL_OWNER) + '] Update Animal Owner Response')
            print_exc()

