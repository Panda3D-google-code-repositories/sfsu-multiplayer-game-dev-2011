from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseShopListAnimal(ServerResponse):

    def execute(self, data):

        try:
            listAnimal = []

            for i in range (data.getUint16()):
                self.info = { 'animalTypeID'    : data.getUint16(),
                              'itemName'    : data.getString(),
                              'desc'        : data.getString(),
                              'category'        :data.getString(),
                              'priceOfItem' : str(data.getUint16()),
                              'predatorList': data.getString(),
                              'preyList'    : data.getString(),
                              'biomass'  : data.getUint16(),
                              'mass'        : data.getUint16(),
                              'movement_force' : data.getUint16(),
                              'max_force'   : data.getUint16(),
                              'model_id'    : data.getUint32(),
                              'animal_category' : data.getString()}
                listAnimal.append(self.info)

            main.msgQ.putToMsgQ(Constants.CMSG_SHOP_LIST_ANIMAL, {'items' : listAnimal, 'initial' : True})
            main.msgQ.putToMsgQ(Constants.CMSG_SHOP_LIST_ANIMAL_GAMESTATE, listAnimal)

            self.log('Received [' + str(Constants.SMSG_SHOP_LIST_ANIMAL) + '] Shop List Animal Response')
        except:
            self.log('Bad [' + str(Constants.SMSG_SHOP_LIST_ANIMAL) + '] Shop List Animal Response')
            print_exc()

