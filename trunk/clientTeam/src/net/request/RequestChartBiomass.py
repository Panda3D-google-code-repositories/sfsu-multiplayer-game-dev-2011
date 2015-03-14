from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestChartBiomass(ServerRequest):

    def send(self, args):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_CHART_BIOMASS)
            pkg.addUint16(args['type'])

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_CHART_BIOMASS) + '] Chart Biomass Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_CHART_BIOMASS) + '] Chart Biomass Request')
            print_exc()
