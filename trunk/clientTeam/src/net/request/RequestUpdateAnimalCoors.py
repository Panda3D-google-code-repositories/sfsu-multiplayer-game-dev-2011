# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 17, 2011 8:51:44 AM$"

from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestUpdateAnimalCoors(ServerRequest):

    def send(self, args):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_UPDATE_ANIMAL_COORS)
            pkg.addUint16(args['animalID'])
            pkg.addUint16(args['xCoor'])
            pkg.addUint16(args['yCoor'])
            pkg.addUint16(args['zCoor'])

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_UPDATE_ANIMAL_COORS) + '] Update Animal Coordinate Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_UPDATE_ANIMAL_COORS) + '] Update Animal Coordinate Request')
            print_exc()
