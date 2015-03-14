# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Oct 29, 2011 5:33:48 PM$"

from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestGetPvPWorlds(ServerRequest):

    def send(self, args = None):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_GETPVPWORLDS)

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_GETPVPWORLDS) + '] Get PVP Worlds Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_GETPVPWORLDS) + '] Get PVP Worlds Request')
            print_exc()
