from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseDrinkWater(ServerResponse):

    def execute(self, data):

        try:
            species_id = data.getUint32()

            self.log('Received [' + str(Constants.SMSG_DRINK_WATER) + '] Drink Water Response')   

        except:
            self.log('Bad [' + str(Constants.SMSG_DRINK_WATER) + '] Drink Water Response')
            print_exc()
