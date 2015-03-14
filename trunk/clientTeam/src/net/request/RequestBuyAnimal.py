# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"

from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestBuyAnimal(ServerRequest):

    def send(self, args):
        #print args
        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_BUY_ANIMAL)
            pkg.addUint16(args['animalTypeID'])
            pkg.addUint16(args['zoneID'])
            pkg.addFloat32(args['xCoor'])
            pkg.addFloat32(args['yCoor'])

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_BUY_ANIMAL) + '] Buy Animal Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_BUY_ANIMAL) + '] Buy Animal Request')
            print_exc()
