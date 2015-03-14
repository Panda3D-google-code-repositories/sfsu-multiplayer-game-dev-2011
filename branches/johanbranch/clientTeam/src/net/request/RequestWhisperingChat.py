# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"

from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestWhisperingChat(ServerRequest):

    def send(self, args):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_WHISPERING_CHAT)
            pkg.addString(args['msg'])
            pkg.addString(args['userName'])

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_WHISPERING_CHAT) + '] Whispering Chat Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_WHISPERING_CHAT) + '] Whispering Chat Request')
            print_exc()
