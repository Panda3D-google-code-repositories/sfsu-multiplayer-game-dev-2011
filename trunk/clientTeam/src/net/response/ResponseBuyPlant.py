from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseBuyPlant(ServerResponse):

    def execute(self, data):

        try:
            args = {'status'        : data.getUint16(),
                    'plantTypeID'   : data.getUint32(),
                    'amount'        : data.getUint32()}

            main.msgQ.putToMsgQ(Constants.SMSG_BUY_PLANT, args)

            self.log('Received [' + str(Constants.SMSG_BUY_PLANT) + '] Buy Plant Response')
        except:
            self.log('Bad [' + str(Constants.SMSG_BUY_PLANT) + '] Buy Plant Response')
            print_exc()