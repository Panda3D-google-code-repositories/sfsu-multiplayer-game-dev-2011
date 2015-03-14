from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseTargetReward(ServerResponse):

    def execute(self, data):

        try:
            info = {'target_id'     : data.getUint32(),
                    'type'          : data.getUint16(),
                    'amount'        : data.getUint32()}

            main.msgQ.putToMsgQ(Constants.SMSG_TARGET_REWARD, info)

            self.log('Received [' + str(Constants.SMSG_TARGET_REWARD) + '] Target Reward Response')
        except:
            self.log('Bad [' + str(Constants.SMSG_TARGET_REWARD) + '] Target Reward Response')
            print_exc()
