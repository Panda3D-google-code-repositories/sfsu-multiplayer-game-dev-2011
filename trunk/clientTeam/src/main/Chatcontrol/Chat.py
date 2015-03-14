
from common.Constants import Constants
from main.Chatcontrol.ChatBubble import ChatBubble
from main.Chatcontrol.ChatControls import ChatControls
from panda3d.core import Point3, TextNode, TransparencyAttrib, WindowProperties


class Chat:
    
    """
    main methods:
    setChatMode()
    sendEvent()
    scrollChatLog()
    """
    def __init__(self, chatEntry, scrollBar, chatLines,sendButton, maxItemsVisible,
                 defaultChatMode, wordWrap=30):
#    def __init__(self):    
#        self.chatBubble = ChatBubble(self)
        self.chatLog = []
        self.filterLog = []
        self.universalColor = (1, 1, 1, 1)
        self.pvpWorldColor = (1, 0.7, 0, 1)
        self.systemColor = (1, 1, 0, 1)
        self.pvpGameColor = (0, 0.4, 1, 1)
        self.pveWorldColor = (0, 0.7, 1, 1)
        self.pveGameColor = (0.5, 0.4, 1, 1)
        self.teamColor = (1, 0.5, 0.5, 1)
        
        # '/' kept reseved for whisper chat
        self.universalOp = ''
        self.pvpWorldOp = '%'
        self.pvpGameOp = '!'
        self.newpvpOp = self.pvpGameOp
        self.pveGameOp = '#'
        self.pveWorldOp = '&'
        self.teamOp = '$'
        self.whisper='/w'
        self.mapResponseChatType()
        self.chatOp = (self.pvpWorldOp,
                       self.universalOp,
                       self.pvpGameOp,
                       self.pveGameOp,
                       self.pveWorldOp,
                       self.teamOp)        

        self.chatMode = -1
        self.lastFilterSize = 0
        self.lastType = -1
        self.maxItems = 100
#        self.maxItemsVisible=6
        self.maxItemsVisible = maxItemsVisible
        self.modeIndex = -1        
        self.wordWrap=wordWrap
        self.scrollBar = scrollBar
#        self.scrollBar.hide()
        self.chatLines = chatLines
        self.chatEntry = chatEntry
        self.sendButton=sendButton
        self.setChatMode(defaultChatMode,0,False)
#        main.msgQ.addToCommandList(Constants.CMSG_CHAT, self.sendReceivedMsg)
        
#        self.controls.accept('enter', self.showTextField)
#        self.controls.accept('control-c', self.handleHideButton)        

#        self.chatMainFrame.setControls(ChatControls(self))


#    def toggleChatMode(self, direction):
#
#        self.modeIndex = (self.modeIndex + direction + len(self.chatButtons)) % len(self.chatButtons)
#        button = self.chatButtons[self.modeIndex]
#
#        if button is self.universalButton:
#            self.setChatMode(Constants.CMSG_UNIVERSAL_CHAT)
#        elif button is self.worldButton:
#            self.setChatMode(Constants.CMSG_PVPWORLD_CHAT)
#        elif button is self.pvpButton:
#            self.setChatMode(Constants.CMSG_PVPGAME_CHAT)



    def setChatMode(self, mode, modeIndex, focus = True):

        if focus:
            self.setChatFocus(True)

        oldChatMode = self.chatMode
        self.chatMode = mode
        self.modeIndex = modeIndex
        
        if mode != oldChatMode:
            self.clearChatBox()
            self.lastFilterSize = 0

            self.filterChat()

            self.scrollBar['range'] = (1, 0)
            self.scrollBar['value'] = 1

            self.updateScrollBar()
            self.scrollChatLog()

            chatOp = ''

            if mode == Constants.CMSG_UNIVERSAL_CHAT:
                
                chatOp = self.universalOp
            elif mode == Constants.CMSG_PVPWORLD_CHAT:
                chatOp = self.pvpWorldOp
            elif mode == Constants.CMSG_PVPGAME_CHAT:
                chatOp = self.pvpGameOp
            elif mode == Constants.CMSG_PVEGAME_CHAT:
                chatOp = self.pveGameOp
            elif mode == Constants.CMSG_PVEWORLD_CHAT:
                chatOp = self.pveWorldOp
            else:
                chatOp = self.teamOp

            currentText = self.chatEntry.get()

            if len(currentText) > 0:
                self.chatEntry.enterText(chatOp + currentText[1 : len(currentText)])
            else:
                self.chatEntry.enterText(chatOp)
        

    def scrollChatLog(self):

        sliderValue = int(round(self.scrollBar['value']))

        chatLog = self.filterLog

        if len(chatLog) < self.maxItemsVisible:
            maxItems = len(chatLog)
        else:
            maxItems = self.maxItemsVisible

        for i in range(maxItems):
            chatType = None

            if len(chatLog) > self.maxItemsVisible:
                self.chatLines[i]['text'] = chatLog[sliderValue + i].msg
                chatType = chatLog[sliderValue + i].type
            else:
                self.chatLines[i]['text'] = chatLog[i].msg
                chatType = chatLog[i].type

            if chatType == Constants.CMSG_UNIVERSAL_CHAT:
                self.chatLines[i]['text_fg'] = self.universalColor
            elif chatType == Constants.CMSG_PVPWORLD_CHAT:
                self.chatLines[i]['text_fg'] = self.pvpWorldColor
            elif chatType == Constants.CMSG_PVPGAME_CHAT:
                self.chatLines[i]['text_fg'] = self.pvpGameColor
            elif chatType == Constants.CMSG_PVEGAME_CHAT:
                self.chatLines[i]['text_fg'] = self.pveGameColor
            elif chatType == Constants.CMSG_PVEWORLD_CHAT:
                self.chatLines[i]['text_fg'] = self.pveWorldColor
            elif chatType == Constants.CMSG_TEAM_CHAT:
                self.chatLines[i]['text_fg'] = self.teamColor
            else:
                self.chatLines[i]['text_fg'] = self.systemColor

    def sendEvent(self, text = None):
        self.sendMsg()

    def sendMsg(self):

        msg = self.chatEntry.get()
        result = self.parseMsg(self.chatMode, msg)

        self.clearChatEntry()
 
        if result != None:
            chatMsg = {"chatType": result[0], "msg": result[1], 'charName': result[2], 'worldName': ""}
            print "chatType: "+str(result[0])
            print "msg:"+result[1]
            print 'charName'+result[2]
            main.cManager.sendRequest(Constants.CMSG_CHAT, chatMsg)
            self.setChatFocus(True)
        elif not self.chatEntry.getFocus():
            self.setChatFocus(True)
        else:
            self.setChatFocus(False)
#            self.chatBubble.clear()
        
    def setChatFocus(self, state):

        self.chatEntry['focus'] = state

    def parseMsg(self, _type, msg, send = True):

        msg = msg.strip()
        charName=''
        if len(msg) > 0:
            if msg[:2] == self.whisper:
                print 'pasrseMsg: whisper'
                list1 = msg.split('[', 1)
                list2 = list1[1].split(']', 1)
                charName = list2[0]
                msg = list2[1]
                _type = Constants.CMSG_WHISPER_CHAT
                print 'charName: '+charName
            elif msg[0] in self.chatOp:
                if _type == Constants.CMSG_UNIVERSAL_CHAT:
                    print 'parseMsg: universal chat'
                elif _type == Constants.CMSG_PVPWORLD_CHAT and len(msg) > 1:
                    print 'parseMsg: pvp world chat'
                    msg = msg[1 : len(msg)].strip()
                elif _type == Constants.CMSG_PVEWORLD_CHAT and len(msg) > 1:
                    print 'parseMsg: pve world chat'
                    msg = msg[1 : len(msg)].strip()
                elif _type == Constants.CMSG_PVEGAME_CHAT and len(msg) > 1:
                    print 'parseMsg: pve game chat'
                    msg = msg[1: len(msg)].strip()
                elif _type == Constants.CMSG_PVPGAME_CHAT and len(msg)>1:
                    print 'parseMsg: pvp game chat'
                    msg = msg[1 : len(msg)].strip()

                elif _type == Constants.CMSG_TEAM_CHAT and len(msg)>1:
                    msg = msg[1 : len(msg)].strip()
                else:
                    return None
            else:
                _type = Constants.CMSG_UNIVERSAL_CHAT

            return (_type, msg, charName)

    def clearChatEntry(self):

        if self.chatMode == Constants.CMSG_UNIVERSAL_CHAT:
            print 'clearChatEntry: clear universal chat entry'
            self.chatEntry.enterText(self.universalOp)
        elif self.chatMode == Constants.CMSG_PVPWORLD_CHAT:
            print 'clearChatEntry: clear pvpworld chat entry'
            self.chatEntry.enterText(self.pvpWorldOp)
        elif self.chatMode == Constants.CMSG_PVPGAME_CHAT:
            print 'clearChatEntry: clear pvpgame chat entry'
            self.chatEntry.enterText(self.pvpGameOp)
        elif self.chatMode == Constants.CMSG_PVEGAME_CHAT:
            print 'clearChatEntry: clear pvegame chat entry'
            self.chatEntry.enterText(self.pveGameOp)
        elif self.chatMode == Constants.CMSG_PVEWORLD_CHAT:
            self.chatEntry.enterText(self.pveWorldOp)
        elif self.chatMode == Constants.CMSG_TEAM_CHAT:
            self.chatEntry.enterText(self.teamOp)
            
    def clearChatBox(self):

        for chatLine in self.chatLines:
            chatLine['text'] = ''       

    def updateScrollBar(self):

        chatLog = self.filterLog

        if len(chatLog) > self.maxItemsVisible:
            if self.scrollBar.isHidden():
                self.scrollBar.show()
            scrollRange = len(chatLog) - self.maxItemsVisible
            currentSize = self.scrollBar['thumb_frameSize'][3]-self.scrollBar['thumb_frameSize'][2]
            if currentSize > 0.2:
                scrollRatio = float(self.maxItemsVisible)/len(chatLog)
                self.scrollBar['thumb_frameSize'] = (self.scrollBar['thumb_frameSize'][0], self.scrollBar['thumb_frameSize'][1],
                                           self.scrollBar['frameSize'][2]*scrollRatio,
                                           self.scrollBar['frameSize'][3]*scrollRatio)
        else:
            if not self.scrollBar.isHidden():
                self.scrollBar.hide()
            scrollRange = 1

        lastRange = self.scrollBar['range'][0]
        self.scrollBar['range'] = (scrollRange, 0)

        if round(self.scrollBar['value']) >= lastRange:
            self.scrollBar['value'] = scrollRange
        elif round(self.scrollBar['value']) > 0:
#            if (self.chatMode == Constants.CMSG_WHISPER_CHAT and len(chatLog) >= self.maxItems or
#                    self.chatMode != Constants.CMSG_WHISPER_CHAT and len(chatLog) == self.lastFilterSize):
            if len(chatLog) == self.lastFilterSize:
                self.scrollBar['value'] = round(self.scrollBar['value']) - 1
        
    def addMessage(self, obj):
        chatType = obj['chatMode']
        print 'ChatType: '+str(self.chatMode)
        print 'match ChatType: '+str(self.mapChatType[chatType])
#        if self.chatMode != self.mapChatType[chatType]:
#            print 'chatType donesn\'t match'
#            return; 
        name = obj['senderName']
        msg = obj['message']
        msg = 'From [ ' + name + ' ] : ' + msg
        print msg
        textNode = TextNode('text')
        textNode.setText(msg)
        textNode.setWordwrap(self.wordWrap)
        pMessage = textNode.getWordwrappedText().split('\n')

        for mObject in pMessage:
            if len(self.chatLog) == self.maxItems:
                self.chatLog.pop(0)

            self.chatLog.append(ChatObject(name, self.mapChatType[chatType], mObject))
            
            self.filterChat()

            self.updateScrollBar()
            self.scrollChatLog()
    
    def mapResponseChatType(self):
        """
        Match the response chat type sent from server
        """
        self.mapChatType = [ -1, 
                             Constants.CMSG_PVEGAME_CHAT,
                             Constants.CMSG_PVEGAME_CHAT,
                             Constants.CMSG_UNIVERSAL_CHAT,
                             Constants.CMSG_PVEWORLD_CHAT,
                             Constants.CMSG_PVEWORLD_CHAT,
                             Constants.CMSG_TEAM_CHAT,
                             Constants.CMSG_WHISPER_CHAT]
    
    def getResponseChatType(self, _type):
        
        return self.mapChatType[_type]
        
    def filterChat(self):

        self.lastFilterSize = len(self.filterLog)
        if self.lastFilterSize > 0:
            self.filterLog = []

        for cObject in self.chatLog:
            if cObject.type == self.chatMode or cObject.type == -1:
                self.filterLog.append(cObject)
                
class ChatObject:

    def __init__(self, name, _type, msg):

        self.name = name
        self.type = _type
        self.msg = msg