from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestGetFunctionalParameters(ServerRequest):

    def send(self, args):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_GET_FUNCTIONAL_PARAMETERS)
            pkg.addString(args['predator_name'])
            pkg.addUint16(args['parameter_type'])

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_GET_FUNCTIONAL_PARAMETERS) + '] Get Functional Parameters Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_GET_FUNCTIONAL_PARAMETERS) + '] Get Functional Parameters Request')
            print_exc()
