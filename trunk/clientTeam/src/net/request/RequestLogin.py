from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestLogin(ServerRequest):

    def send(self, args):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_AUTH)
            pkg.addString(Constants.CLIENT_VERSION)
            pkg.addString(args['userName'])
            pkg.addString(args['password'])

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_AUTH) + '] Login Request')
            print 'Login Request Sent'
        except:
            self.log('Bad [' + str(Constants.CMSG_AUTH) + '] Login Request')
            print_exc()
