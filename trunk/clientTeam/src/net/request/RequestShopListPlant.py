# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 26, 2011 9:47:56 PM$"

from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestShopListPlant(ServerRequest):

    def send(self, args):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_SHOP_LIST_PLANT)

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_SHOP_LIST_PLANT) + '] Shop List Plant Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_SHOP_LIST_PLANT) + '] Shop List Plant Request')
            print_exc()
