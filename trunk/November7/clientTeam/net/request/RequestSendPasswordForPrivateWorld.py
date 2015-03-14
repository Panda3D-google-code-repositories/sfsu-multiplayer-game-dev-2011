# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"

from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestSendPasswordForPrivateWorld(ServerRequest):

    def send(self, args):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_PASSWORD_PRIVATE_WORLD)
            pkg.addString(args['password'])

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_PASSWORD_PRIVATE_WORLD) + '] Password Private World')
        except:
            self.log('Bad [' + str(Constants.CMSG_PASSWORD_PRIVATE_WORLD) + '] Password Private World')
            print_exc()
