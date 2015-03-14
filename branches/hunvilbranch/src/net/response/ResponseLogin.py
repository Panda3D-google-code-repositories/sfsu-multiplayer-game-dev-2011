# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"


from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from direct.showbase.DirectObject import DirectObject

class ResponseLogin(ServerResponse):

    def execute(self, data):

        try:

            self.status = data.getUint16()

            if self.status == 0:
                main.charName = data.getString()
            
            main.msgQ.putToMsgQ(CMSG_AUTH, self.status)     #1 = wrong userName or password
                                                            #2 = account is being used
                                                            #3 = other error

            self.log('Received [' + str(Constants.SMSG_AUTH) + '] Authentication Response')
            
            taskMgr.doMethodLater(0, self.main.updateRoutine, 'updateRoutine-Main')
        except:
            self.log('Bad [' + str(Constants.SMSG_AUTH) + '] Authentication Response')
            print_exc()

