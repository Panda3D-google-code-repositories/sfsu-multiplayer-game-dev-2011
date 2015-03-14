# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseSearchPrivateWorld(ServerResponse):

    def execute(self, data):

        try:
            self.status = data.getUint16()

            if self.status == 0:                                        #private game exists
                self.info = {'worldName'     : data.getString(),
                             'worldType'     : data.getUint16() }       #0 = PVE, 1 = PVP

                main.msgQ.addToPendingObj(Constants.PENDING_SEARCH_PRIVATE_WORLD, self.info)

            main.msgQ.putToMsgQ(Constants.CMSG_SEARCH_PRIVATE_WORLD, self.status)


            self.log('Received [' + str(Constants.SMSG_SEARCH_PRIVATE_WORLD) + '] Search Private World Response')
        except:
            self.log('Bad [' + str(Constants.SMSG_SEARCH_PRIVATE_WORLD) + '] Search Private World Response')
            print_exc()
