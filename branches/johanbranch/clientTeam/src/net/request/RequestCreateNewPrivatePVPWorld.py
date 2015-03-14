# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"

from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestCreateNewPrivatePVPWorld(ServerRequest):

    def send(self, args):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_CREATE_NEW_PRIVATE_PVP_WORLD)
            pkg.addString(args['gameName'])
            pkg.addString(args['password'])
            pkg.addUint16(args['maxPlayersInGame'])
            pkg.addString(args['worldEcoSystem'])
            pkg.addString(args['typeOfAvatar'])

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_CREATE_NEW_PRIVATE_PVP_WORLD) + '] Create New Private PVP Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_CREATE_NEW_PRIVATE_PVP_WORLD) + '] Create New Private PVP Request')
            print_exc()
