# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"

from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestCreateNewPublicPVPWorld(ServerRequest):

    def send(self, args):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_CREATE_NEW_PUBLIC_PVP_WORLD)
            pkg.addString(args['gameName'])
            pkg.addUint16(args['maxPlayersInGame'])
            pkg.addString(args['worldEcoSystem'])
            pkg.addString(args['typeOfAvatar'])

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_CREATE_NEW_PUBLIC_PVP_WORLD) + '] Create New Public PVP Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_CREATE_NEW_PUBLIC_PVP_WORLD) + '] Create New Public PVP Request')
            print_exc()
