# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseSearchPrivateGames(ServerResponse):

    def execute(self, data):

        try:
            if 'MainLobby' in self.main.envMap:
                status = data.getUint16()

                #code will be here


            self.log('Received [' + str(Constants.SMSG_SEARCH_PRIVATE_GAMES) + '] Search Private Games Response')
        except:
            self.log('Bad [' + str(Constants.SMSG_SEARCH_PRIVATE_GAMES) + '] Search Private Games Response')
            print_exc()
