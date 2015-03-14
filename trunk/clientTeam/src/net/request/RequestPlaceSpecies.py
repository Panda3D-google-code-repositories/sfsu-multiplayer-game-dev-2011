# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 26, 2011 10:08:50 PM$"

from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestPlaceSpecies(ServerRequest):

    def send(self, args):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_PLACE_SPECIES)
            pkg.addUint16(args['speciesID'])
            pkg.addUint16(args['zoneID'])
            pkg.addUint16(args['xCoor'])
            pkg.addUint16(args['yCoor'])

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_PLACE_SPECIES) + '] Place Species Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_PLACE_SPECIES) + '] Place Species Request')
            print_exc()
