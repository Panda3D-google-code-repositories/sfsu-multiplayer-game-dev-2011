#@PydevCodeAnalysisIgnore
'''
Created on Nov 11, 2011

@author: Wenhui
'''
from traceback import print_exc

class MessageQueue:
    """
    How this works:
        All the incoming message will add to msgQ, when the message task start to execute, an event name 
        called 'stop' will automatically add to msgQ to prevent continuously execute. All the rest of message 
        will be execute in next frame.
    
    Usage:
    ( For request )
        Call addToCommandList() to add a unique event name and the function that will execute the incomming 
        message.
    
    ( For response )
        Call putToMsgQ() to put the event name and the request object to message queue.
    
    ** Since Queue() in python is synchronized, so it is possible to put and get object from the queue at 
    the same time.
    """
    
    def __init__(self):
        
        self.commandList = {}
        self.msgQ = []
        # this is used to hold the object for later usage in client side
        self.pendingObj = {}
        taskMgr.add(self.execute, "MessageQueue")
    
    def addToPendingObj(self,eventName, obj):
        self.pendingObj[eventName] = obj
    
    def getObjFromPendingObj(self, eventName):
        try:
            obj = self.pendingObj[eventName]
            del self.pendingObj[eventName]
            return obj
        except:
            return None
        
    def addToCommandList(self, eventName, command):
        """
        Add function to command list, those function will be used to execute response message.
        """
        self.commandList[eventName] = command
        
    def putToMsgQ(self, eventName, obj = None):
        """
        Enqueue all the passing message 
        """
        self.msgQ.append([eventName, obj])
    
    def execute(self, task):
        """
        Execute all the message in msgQ until it reach stop event.
        """

        while len(self.msgQ) > 0:
            event = self.msgQ.pop(0)

            if event[0] in self.commandList:
                try:
                    apply(self.commandList.get(event[0]), [event[1]])
                except:
                    print 'Failed at Event No. ' + str(event[0]) + '...'
                    print_exc()
            else:
                print 'Missing Event No. ' + str(event[0]) + '...'

        return task.cont

    def removeEvent(self, eventName):
        if eventName in self.commandList:
            del self.commandList[eventName]
