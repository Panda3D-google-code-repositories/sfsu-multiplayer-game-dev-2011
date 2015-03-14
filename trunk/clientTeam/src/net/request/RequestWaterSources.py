# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 22, 2011 11:45:10 AM$"

from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestWaterSources(ServerRequest):

    def send(self, args):

        try:
            
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_REQUESTWATERSOURCES)

            for i in args:                            #6 zone with water resources

                pkg.addUint32(i['x'])
                pkg.addUint32(i['y'])
                pkg.addUint32(i['z'])
                pkg.addUint16(i['zoneID'])
                
            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_REQUESTWATERSOURCES) + '] Water sources Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_REQUESTWATERSOURCES) + '] Water sources Request')
            print_exc()
