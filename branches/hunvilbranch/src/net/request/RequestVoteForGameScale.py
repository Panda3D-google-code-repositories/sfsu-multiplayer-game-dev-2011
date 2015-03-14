# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"

from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestVoteForGameScale(ServerRequest):

    def send(self, args):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_VOTE_GAME)
            pkg.addString(args['worldName'])
            pkg.addUint16(args['gameScale'])

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_VOTE_GAME) + '] Vote For Game Scale Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_VOTE_GAME) + '] Vote For Game Scale Request')
            print_exc()
