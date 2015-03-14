#@PydevCodeAnalysisIgnore
# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 23, 2011 12:07:18 AM$"

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from traceback import print_exc

class ResponseGetEnv(ServerResponse):

    def execute(self, data):

        try:
            status = data.getUint16()

            if status == 0:                        #success
                numberOfEnv = data.getUint16()
                self.env = []

                for i in range(numberOfEnv):
                    info = { 'envID' : data.getUint32(),
                              'rowID'       : data.getUint16(),
                              'columnID'    : data.getUint16(),
                              'avatarID'    : data.getUint32(),
                              'envScore'    : data.getUint32()
                           }

                    for i in range(9):
                        info['zone' + str(i) + 'Enable'] = data.getBool()
                        info['zone' + str(i) + 'ID'] = data.getUint16()
                        info['zone' + str(i) + 'Type'] = data.getUint16()

                        if data.getBool():
                            info['zone' + str(i) + '_water_id'] = data.getUint32()
                            info['zone' + str(i) + '_max_water'] = data.getUint32()
                            info['zone' + str(i) + '_water'] = data.getUint32()

                    self.env.append(info)

            #print self.env
            main.msgQ.putToMsgQ(Constants.SMSG_RESPONSE_GET_ENVIRONMENT, self.env)

            self.log('Received [' + str(Constants.SMSG_RESPONSE_GET_ENVIRONMENT) + '] Get Environment Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_RESPONSE_GET_ENVIRONMENT) + '] Get Environment Response')
            print_exc()
