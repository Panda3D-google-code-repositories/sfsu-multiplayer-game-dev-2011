# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"

from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestBuyPlant(ServerRequest):

    def send(self, args):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_BUY_PLANT)
            pkg.addString(args['avatarID'])
            #pkg.addString(args['useAbilityPoint'])
            pkg.addString(args['plantType'])
        
            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_BUY_PLANT) + '] Buy Plant Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_BUY_PLANT) + '] Buy Plant Request')
            print_exc()
