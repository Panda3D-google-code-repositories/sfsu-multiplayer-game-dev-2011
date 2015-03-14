from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestRestart(ServerRequest):

    def send(self, args):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_RESTART)
            pkg.addBool(args['status'])

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_RESTART) + '] Restart Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_RESTART) + '] Restart Request')
            print_exc()
