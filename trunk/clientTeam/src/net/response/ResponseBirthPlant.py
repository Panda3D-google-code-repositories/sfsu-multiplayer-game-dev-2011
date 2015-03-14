from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseBirthPlant(ServerResponse):

    def execute(self, data):

        try:
            plant = {'status'       : data.getUint16(),
                     'plantID'      : data.getUint32(),
                     'name'         : data.getString(),
                     'modelID'      : data.getUint16(),
                     'plantTypeID'  : data.getUint16(),
                     'avatarID'     : data.getUint32(),
                     'zoneID'       : data.getUint32(),
                     'biomass'      : data.getUint16(),
                     'xCoor'        : data.getFloat32(),
                     'yCoor'        : data.getFloat32(),
                     'zCoor'        : data.getFloat32(),
                     'group_size'   : data.getUint16(),
                     'count'        : data.getUint16()}

            main.msgQ.putToMsgQ(Constants.SMSG_BIRTH_PLANT, plant)

            self.log('Received [' + str(Constants.SMSG_BIRTH_PLANT) + '] Birth Plant Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_BIRTH_PLANT) + '] Birth Plant Response')
            print_exc()

