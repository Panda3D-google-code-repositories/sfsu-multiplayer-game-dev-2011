# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Oct 29, 2011 5:30:32 PM$"

from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestGetPvEWorlds(ServerRequest):

    def send(self, args):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_GETPVEWORLDS)

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_GETPVEWORLDS) + '] Get PVE Worlds Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_GETPVEWORLDS) + '] Get PVE Worlds Request')
            print_exc()
