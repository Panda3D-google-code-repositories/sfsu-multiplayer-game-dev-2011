# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 12, 2011 5:24:43 PM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseChangeAvatarType(ServerResponse):

    def execute(self, data):

        try:
            worldType = data.getUint16()              #(0 = PVE, 1 = PVP)
            numberOfPlayers = data.getUint16()


            if worldType == 0:                        #PVE
                #for i in range (numberOfPlayers):
                self.info = { 'userName'     : data.getString(),
                              'position'     : data.getUint16(),
                              'avatar'       : data.getString() }


            else:                                     #PVP
                #for i in range (numberOfPlayers):
                self.info = { 'userName'     : data.getString(),
                              'teamNumber'   : data.getUint16(),
                              'position'     : data.getUint16(),
                              'avatar'       : data.getString() }


            main.msgQ.putToMsgQ(Constants.CMSG_CHANGE_AVATAR_TYPE, self.info)

            self.log('Received [' + str(Constants.SMSG_CHANGE_AVATAR_TYPE) + '] Change Avatar Type Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_CHANGE_AVATAR_TYPE) + '] Change Avatar Type Response')
            print_exc()