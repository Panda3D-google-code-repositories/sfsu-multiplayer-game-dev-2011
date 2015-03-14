from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestDeleteWorld(ServerRequest):

    def send(self, args):

        try:
            pkg = PyDatagram()

            pkg.addUint16(Constants.CMSG_DELETE_WORLD)
            pkg.addUint32(args['world_id'])
            
            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_DELETE_WORLD) + '] Delete World Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_DELETE_WORLD) + '] Delete World Request')
            print_exc()
