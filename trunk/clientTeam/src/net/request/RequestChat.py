from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestChat(ServerRequest):

    def send(self, args):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_CHAT)
            pkg.addUint16(args['type'])
            pkg.addString(args['message'])

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_CHAT) + '] Chat Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_CHAT) + '] Chat Request')
            print_exc()
