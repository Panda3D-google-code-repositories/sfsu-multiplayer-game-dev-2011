# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"

from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestSearchPrivateGames(ServerRequest):

    def send(self, args):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_SEARCH_PRIVATE_GAMES)
            pkg.addString(args['gameName'])
            pkg.addString(args['password'])

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_SEARCH_PRIVATE_GAMES) + '] Search Private Games Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_SEARCH_PRIVATE_GAMES) + '] Search Private Games Request')
            print_exc()
