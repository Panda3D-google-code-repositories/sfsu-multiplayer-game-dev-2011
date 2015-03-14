from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from traceback import print_exc

class ResponseCreateEnv(ServerResponse):

    def execute(self, data):

        try:
            info = { 'envID' : data.getUint32(),
                      'rowID'       : data.getUint16(),
                      'columnID'    : data.getUint16(),
                      'avatarID'    : data.getUint32(),
                      'envScore'    : data.getUint32()
                   }

            for i in range(9):
                info['zone' + str(i) + 'ID'] = data.getUint16()
                info['zone' + str(i) + 'Type'] = data.getUint16()

                if data.getBool():
                    info['zone' + str(i) + '_water_id'] = data.getUint32()
                    info['zone' + str(i) + '_max_water'] = data.getUint32()
                    info['zone' + str(i) + '_water'] = data.getUint32()
            #print info
            main.msgQ.putToMsgQ(Constants.SMSG_CREATE_ENV, info)

            self.log('Received [' + str(Constants.SMSG_CREATE_ENV) + '] Create Environment Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_CREATE_ENV) + '] Create Environment Response')
            print_exc()
