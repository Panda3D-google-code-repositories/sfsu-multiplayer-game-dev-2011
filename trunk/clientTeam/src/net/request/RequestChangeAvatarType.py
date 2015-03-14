# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 12, 2011 5:41:42 PM$"

from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestChangeAvatarType(ServerRequest):

    def send(self, args):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_CHANGE_AVATAR_TYPE)
            pkg.addUint32(args['avatar_id'])

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_CHANGE_AVATAR_TYPE) + '] Change Avatar Type Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_CHANGE_AVATAR_TYPE) + '] Change Avatar Type Request')
            print_exc()

