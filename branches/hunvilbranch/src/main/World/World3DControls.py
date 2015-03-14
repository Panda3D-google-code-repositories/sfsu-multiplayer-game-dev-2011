from common.DirectControls import DirectControls

class World3DControls(DirectControls):

    def __init__(self, parent):

        DirectControls.__init__(self, parent)

        self.accept('tab', parent.toggleEntry, [1])
        self.accept('shift-tab', parent.toggleEntry, [-1])
