from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseShopUnlock(ServerResponse):

    def execute(self, data):

        try:
            unlockList = []
            size = data.getUint16()

            for i in range(size):
                organism_type = data.getUint16()

                if organism_type == 1:
                    self.info = { 'organism_type'   : organism_type,
                                  'plantTypeID' : data.getUint16(),
                                  'itemName'   : data.getString(),
                                  'desc'        : data.getString(),
                                  'category'        : data.getString(),
                                  'priceOfItem'   : str(data.getUint16()),
                                  'predatorList'   : data.getString(),
                                  'model_id'        : data.getUint32(),
                                  'biomass'        : str(data.getUint32())
                                   }

                    unlockList.append(self.info)
                elif organism_type == 0:
                    self.info = { 'organism_type'   : organism_type,
                                  'animalTypeID'    : data.getUint16(),
                                  'itemName'    : data.getString(),
                                  'desc'        : data.getString(),
                                  'category'        : data.getString(),
                                  'priceOfItem' : str(data.getUint16()),
                                  'predatorList': data.getString(),
                                  'preyList'    : data.getString(),
                                  'biomass'  : data.getUint16(),
                                  'mass'        : data.getUint16(),
                                  'movement_force' : data.getUint16(),
                                  'max_force'   : data.getUint16(),
                                  'model_id'    : data.getUint32(),
                                  'animal_category' : data.getString()}

                    unlockList.append(self.info)

            main.msgQ.putToMsgQ(Constants.SMSG_SHOP_UNLOCK, unlockList)

            self.log('Received [' + str(Constants.SMSG_SHOP_UNLOCK) + '] Shop Unlock Response')
        except:
            self.log('Bad [' + str(Constants.SMSG_SHOP_UNLOCK) + '] Shop Unlock Response')
            print_exc()

