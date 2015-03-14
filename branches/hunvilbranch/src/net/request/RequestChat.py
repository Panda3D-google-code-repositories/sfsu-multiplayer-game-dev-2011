#@PydevCodeAnalysisIgnore
# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 12, 2011 8:46:07 PM$"

from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestChat(ServerRequest):

    def send(self, args):

        try:
            pkg = PyDatagram()

            type = args['chatType']
            
            if type == 68:              #pvp game chat
                chatType = 1
            elif type == 70:            #pve game chat
                chatType = 2
            elif type == 72:            #universal chat
                chatType = 3
            elif type == 74:            #pvp world chat
                chatType = 4
            elif type == 76:            #pve world chat
                chatType = 5     
            elif type == 78:            #team chat
                chatType = 6

            pkg.addUint16(Constants.CMSG_CHAT)
            pkg.addUint16(chatType)    
            pkg.addString(args['msg'])         




            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_CHAT) + '] Chat Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_CHAT) + '] Chat Request')
            print_exc()

