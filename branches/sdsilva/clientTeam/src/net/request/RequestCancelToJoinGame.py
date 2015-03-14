# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"

from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestCancelToJoinGame(ServerRequest):

    def send(self):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_CANCEL_TO_JOIN_GAME)
            pkg.addString(gameName)

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_CANCEL_TO_JOIN_GAME) + '] Cancel to Join Game Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_CANCEL_TO_JOIN_GAME) + '] Cancel to Join Game Request')
            print_exc()