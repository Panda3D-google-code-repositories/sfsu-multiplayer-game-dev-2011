from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseBuyAnimal(ServerResponse):

    def execute(self, data):

        try:
            args = {'status'        : data.getUint16(),
                    'animalTypeID'  : data.getUint32(),
                    'amount'        : data.getUint32()}

            main.msgQ.putToMsgQ(Constants.SMSG_BUY_ANIMAL, args)

            self.log('Received [' + str(Constants.SMSG_BUY_ANIMAL) + '] Buy Animal Response')
        except:
            self.log('Bad [' + str(Constants.SMSG_BUY_ANIMAL) + '] Buy Animal Response')
            print_exc()
