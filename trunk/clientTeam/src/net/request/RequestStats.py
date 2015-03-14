'''
Created on Apr 14, 2012

@author: hunvil
'''
from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestStats(ServerRequest):

    def send(self, args):

        try:
            print 'Ten day Request Stats sent to server',args['activityStartDay'],args['activityEndDay']
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_STATISTICS)
            pkg.addUint16(args['activityStartDay'])
            pkg.addUint16(args['activityEndDay'])
            
            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_STATISTICS) + '] Ten Day Statistics Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_STATISTICS) + '] Ten Day Statistics Request')
            print_exc()