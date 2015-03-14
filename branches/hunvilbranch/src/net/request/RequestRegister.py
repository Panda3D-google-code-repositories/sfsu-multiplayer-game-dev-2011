from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestRegister(ServerRequest):

    def send(self, args):
            
        try:
        
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_REGISTER)
            pkg.addString(args['userName'])
            pkg.addString(args['password'])
            pkg.addString(args['confirm'])
            pkg.addString(args['email'])
            pkg.addString(args['charName'])

            self.cWriter.send(pkg, self.connection)
          
            self.log('Sent [' + str(Constants.CMSG_REGISTER) + '] Register Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_REGISTER) + '] Register Request')
            print_exc()
