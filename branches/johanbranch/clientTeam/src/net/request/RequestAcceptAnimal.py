# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"

from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestAcceptAnimal(ServerRequest):

    def send(self, args):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_ACCEPT_ANIMAL)
            pkg.addUint16(args['animalID'])
            pkg.addUint16(args['qty'])
            pkg.addString(args['userName'])

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_ACCEPT_ANIMAL) + '] Accept Animal Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_ACCEPT_ANIMAL) + '] Accept Animal Request')
            print_exc()
