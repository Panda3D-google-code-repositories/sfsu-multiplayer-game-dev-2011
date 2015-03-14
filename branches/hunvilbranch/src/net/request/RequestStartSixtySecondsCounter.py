# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 21, 2011 2:47:24 PM$"

from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestStartSixtySecondsCounter(ServerRequest):

    def send(self, args):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_START_SIXTY_SECONDS_COUNTER)
            pkg.addString(args['worldName'])

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_SIXTY_SECONDS_COUNTER) + '] Sixty Seconds Counter Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_SIXTY_SECONDS_COUNTER) + '] Sixty Seconds Counter Request')
            print_exc()
