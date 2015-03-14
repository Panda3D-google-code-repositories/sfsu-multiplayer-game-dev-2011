# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"

from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestExitGame(ServerRequest):

    def send(self, args = None):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_SAVE_EXIT_GAME)

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_SAVE_EXIT_GAME) + '] Save Exit Game Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_SAVE_EXIT_GAME) + '] Save Exit Game Request')
            print_exc()
