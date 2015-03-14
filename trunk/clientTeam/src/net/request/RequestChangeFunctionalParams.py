from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestChangeFunctionalParams(ServerRequest):

    def send(self, args):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_CHANGE_FUNCTIONAL_PARAMETERS)
            pkg.addUint16(args['parameterType'])
            pkg.addString(args['predator'])
            pkg.addUint16(args['preyListSize'])

            for i in range(args['preyListSize']):
                item = args['animalType' +str(i)]
                pkg.addString(item)
                item = args['percentValue' +str(i)]
                pkg.addFloat32(item)
            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_CHANGE_FUNCTIONAL_PARAMETERS) + '] Change Functional Parameters Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_CHANGE_FUNCTIONAL_PARAMETERS) + '] Change Functional Parameters Request')
            print_exc()
