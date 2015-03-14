# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 20, 2011 2:14:59 PM$"

from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestUpdatePlantCoors(ServerRequest):

    def send(self, args):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_UPDATE_PLANT_COORS)
            pkg.addUint16(args['plantID'])
            pkg.addUint16(args['xCoor'])
            pkg.addUint16(args['yCoor'])
            pkg.addUint16(args['zCoor'])

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_UPDATE_PLANT_COORS) + '] Update Plant Coordinate Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_UPDATE_PLANT_COORS) + '] Update Plant Coordinate Request')
            print_exc()

