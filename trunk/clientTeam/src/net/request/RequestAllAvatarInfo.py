# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 26, 2011 9:55:02 PM$"

from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestAllAvatarInfo(ServerRequest):

    def send(self, args):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_ALL_AVATAR_INFO)
            pkg.addString(args['worldName'])

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_ALL_AVATAR_INFO) + '] All Avatar Info Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_ALL_AVATAR_INFO) + '] All Avatar Info Request')
            print_exc()
