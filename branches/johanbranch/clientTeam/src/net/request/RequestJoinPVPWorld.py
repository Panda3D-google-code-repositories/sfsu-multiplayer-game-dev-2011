# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"

from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestJoinPVPWorld(ServerRequest):

    def send(self, args):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_JOIN_PVP_WORLD)
            pkg.addString(args['gameName'])
            pkg.addString(args['typeOfAvatar'])
            pkg.addUint16(args['team'])
            pkg.addUint16(args['locationInWorld'])

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_JOIN_PVP_WORLD) + '] Join PVP Game Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_JOIN_PVP_WORLD) + '] Join PVP Game Request')
            print_exc()
