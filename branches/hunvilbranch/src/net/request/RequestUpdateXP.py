# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 17, 2011 8:46:08 AM$"

from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestUpdateXP(ServerRequest):

    def send(self, args):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_UPDATE_XP)
            pkg.addUint16(args['newXP'])

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_UPDATE_XP) + '] Update XP Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_UPDATE_XP) + '] Update XP Request')
            print_exc()