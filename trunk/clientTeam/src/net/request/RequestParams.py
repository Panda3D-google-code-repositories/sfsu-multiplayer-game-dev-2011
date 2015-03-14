'''
Created on Apr 14, 2012

@author: hunvil
'''
from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestParams(ServerRequest):

    def send(self, args):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_PARAMS)

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_PARAMS) + '] Parameters Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_PARAMS) + '] Parameters Request')
            print_exc()
