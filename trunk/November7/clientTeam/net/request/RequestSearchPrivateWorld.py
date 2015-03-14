# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"

from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestSearchPrivateWorld(ServerRequest):

    def send(self, args):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_SEARCH_PRIVATE_WORLD)
            pkg.addString(args['worldName'])
            pkg.addString(args['password'])

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_SEARCH_PRIVATE_WORLD) + '] Search Private World Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_SEARCH_PRIVATE_WORLD) + '] Search Private World Request')
            print_exc()
