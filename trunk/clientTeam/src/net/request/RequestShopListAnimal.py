# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 26, 2011 9:33:40 PM$"

from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestShopListAnimal(ServerRequest):

    def send(self, args = None):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_SHOP_LIST_ANIMAL)

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_SHOP_LIST_ANIMAL) + '] Shop List Animal Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_SHOP_LIST_ANIMAL) + '] Shop List Animal Request')
            print_exc()
