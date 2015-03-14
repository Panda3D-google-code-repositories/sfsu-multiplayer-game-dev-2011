from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseChartBiomass(ServerResponse):

    def execute(self, data):

        try:
            args = {'type'  : data.getUint16(),
                    'csv'   : data.getString()}

            main.msgQ.putToMsgQ(Constants.SMSG_CHART_BIOMASS, args)

            self.log('Received [' + str(Constants.SMSG_CHART_BIOMASS) + '] Chart Biomass Response')
        except:
            self.log('Bad [' + str(Constants.SMSG_CHART_BIOMASS) + '] Chart Biomass Response')
            print_exc()
