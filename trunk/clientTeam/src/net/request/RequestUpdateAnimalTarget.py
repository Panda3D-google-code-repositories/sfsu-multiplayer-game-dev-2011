# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 19, 2011 1:19:31 AM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class RequestUpdateAnimalTarget(ServerResponse):

    def execute(self, args):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_UPDATE_ANIMAL_TARGET)
            pkg.addUint16(args['animalID'])
            pkg.addUint16(args['zoneID'])
            pkg.addUint16(args['xCoor'])
            pkg.addUint16(args['yCoor'])

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_UPDATE_ANIMAL_TARGET) + '] Update Animal Target Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_UPDATE_ANIMAL_TARGET) + '] Update Animal Target Request')
            print_exc()
