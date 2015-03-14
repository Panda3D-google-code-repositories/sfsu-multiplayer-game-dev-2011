# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 6, 2011 1:38:06 AM$"

from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestSeePVEOnlinePlayers(ServerRequest):

    def send(self, args = None):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_SEE_PVE_ONLINE_PLAYERS)

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_SEE_PVE_ONLINE_PLAYERS) + '] See PVE Online Players Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_SEE_PVE_ONLINE_PLAYERS) + '] See PVE Online Players Request')
            print_exc()

