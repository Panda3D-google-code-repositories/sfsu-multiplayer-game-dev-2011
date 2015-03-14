# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"

from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestAddPlant(ServerRequest):

    def send(self, args):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_ADD_PLANT)
            pkg.addString(args['plantType'])
            pkg.addUint16(args['zoneNumber'])
            pkg.addUint16(args['x'])
            pkg.addUint16(args['y'])
            pkg.addUint16(args['z'])

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_ADD_PLANT) + '] Add Plant Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_ADD_PLANT) + '] Add Plant Request')
            print_exc()
