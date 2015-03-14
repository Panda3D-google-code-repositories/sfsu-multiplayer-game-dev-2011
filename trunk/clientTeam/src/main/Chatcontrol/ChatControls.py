from common.DirectControls import DirectControls

class ChatControls(DirectControls):

    def __init__(self, parent):

        DirectControls.__init__(self, parent)

        self.accept('tab', parent.toggleChatMode, [1])
        self.accept('shift-tab', parent.toggleChatMode, [-1])
