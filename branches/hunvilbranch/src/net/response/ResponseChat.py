# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 12, 2011 8:57:19 PM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseChat(ServerResponse):

    def execute(self, data):

        try:

            self.chat = { 'senderName' : data.getString(),
                          'message'    : data.getString() }

            main.msgQ.putToMsgQ(Constants.CMSG_CHAT, self.chat)

            self.log('Received [' + str(Constants.SMSG_CHAT) + '] Chat Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_CHAT) + '] Chat Response')
            print_exc()
