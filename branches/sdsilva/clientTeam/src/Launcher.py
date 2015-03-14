#import sys

#from common.Constants import Constants
from main.Main import Main

#for i in range(len(sys.argv)):
#    if sys.argv[i] == '-d':
#        Constants.DEBUG = True
#    elif sys.argv[i] == '-ip':
#        if i + 1 < len(sys.argv):
#            Constants.SERVER_IP = sys.argv[i + 1]
#    elif sys.argv[i] == '-port':
#        if i + 1 < len(sys.argv):
#            Constants.SERVER_PORT = sys.argv[i + 1]
            

m = Main()
run()
