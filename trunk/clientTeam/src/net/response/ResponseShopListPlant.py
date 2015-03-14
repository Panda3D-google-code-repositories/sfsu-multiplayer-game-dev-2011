from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseShopListPlant(ServerResponse):

    def execute(self, data):

        try:
            listPlant = []

            for i in range (data.getUint16()):
                self.info = { 'plantTypeID' : data.getUint16(),
                              'itemName'   : data.getString(),
                              'desc'        : data.getString(),
                              'category'    : data.getString(),
                              'priceOfItem'   : str(data.getUint16()),
                              'predatorList'   : data.getString(),
                              'model_id'        : data.getUint32(),
                              'biomass'        : str(data.getUint32())
                               }

                listPlant.append(self.info)

            main.msgQ.putToMsgQ(Constants.CMSG_SHOP_LIST_PLANT, {'items' : listPlant, 'initial' : True})
            main.msgQ.putToMsgQ(Constants.CMSG_SHOP_LIST_PLANT_GAMESTATE, listPlant)
            self.log('Received [' + str(Constants.SMSG_SHOP_LIST_PLANT) + '] Shop List Plant Response')
        except:
            self.log('Bad [' + str(Constants.SMSG_SHOP_LIST_PLANT) + '] Shop List Plant Response')
            print_exc()

