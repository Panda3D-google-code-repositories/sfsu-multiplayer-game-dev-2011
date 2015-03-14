'''
Created on Nov 11, 2011

@author: Wenhui
'''
from Queue import Queue
from direct.task.TaskManagerGlobal import taskMgr

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
        self.msgQ = Queue()
        self.eventName = "eventName"
        self.object = "object"
        # this is used to hold the object for later usage in client side
        self.pendingObj={}
        taskMgr.add(self.execute, "MessageQueue")
    
    def addToPendingObj(self,eventName, obj):
        self.pendingObj[eventName]=obj
    
    def getObjFromPendingObj(self, eventName):
        obj = self.pendingObj[eventName]
        del self.pendingObj[eventName]
        return obj
    
    def addToCommandList(self, eventName, command):
        """
        Add function to command list, those function will be used to execute response message.
        """
        self.commandList[eventName] = command
        
    def putToMsgQ(self, eventName, obj=None):
        """
        Enqueue all the passing message 
        """
        self.msgQ.put({self.eventName : eventName, self.object : obj})
    
    def execute(self, task):
        """
        Execute all the message in msgQ until it reach stop event.
        """
        
        self.msgQ.put({self.eventName: "stop", self.object: None})
        event = self.msgQ.get()
        while event[self.eventName] != "stop":
            if self.commandList.has_key(event[self.eventName]):
                try:
                    apply(self.commandList.get(event[self.eventName]), [event[self.object]])
                except:
                    pass
#            else:
#                ## if there is no event detect, push it back to msgQ 
#                self.msgQ.put(event)
                
            event = self.msgQ.get()
        return task.cont
    
    def removeEvent(self, eventName):
        if self.commandList.has_key(eventName):
            del self.commandList[eventName]
    
            
            
        
