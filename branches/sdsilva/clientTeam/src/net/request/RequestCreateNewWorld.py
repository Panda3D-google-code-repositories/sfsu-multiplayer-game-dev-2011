# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 5, 2011 1:02:03 PM$"

from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestCreateNewWorld(ServerRequest):

    def send(self, args):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_CREATE_NEW_WORLD)
            pkg.addUint16(args['worldType'])
            pkg.addString(args['worldName'])
            pkg.addUint16(args['maxPlayerNumber'])
            pkg.addString(args['ecosystem'])
            pkg.addUint16(args['privacyType'])

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_CREATE_NEW_WORLD) + '] Get PVE Worlds Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_CREATE_NEW_WORLD) + '] Get PVE Worlds Request')
            print_exc()