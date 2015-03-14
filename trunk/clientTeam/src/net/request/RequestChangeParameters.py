from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestChangeParameters(ServerRequest):

    def send(self, args):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_CHANGE_PARAMETERS)
            pkg.addFloat32(args['carry_capacity'])
            pkg.addFloat32(args['growth_rate'])
            pkg.addFloat32(args['meta_rate'])
            pkg.addFloat32(args['meta_rate_a'])
            pkg.addFloat32(args['assim_scale'])
            pkg.addFloat32(args['funcr_scale'])
            pkg.addFloat32(args['sat_scale'])
            pkg.addFloat32(args['pred_scale'])

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_CHANGE_PARAMETERS) + '] Change Parameters Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_CHANGE_PARAMETERS) + '] Change Parameters Request')
            print_exc()
