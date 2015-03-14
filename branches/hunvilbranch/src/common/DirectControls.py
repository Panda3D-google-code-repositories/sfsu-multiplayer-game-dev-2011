#@PydevCodeAnalysisIgnore
from direct.showbase.DirectObject import DirectObject

class DirectControls(DirectObject):

    def __init__(self, parent = None):

        self.parent = parent
        self.eventMap = {}

    def accept(self, event, method, extraArgs = []):

        DirectObject.accept(self, event, method, extraArgs)
        self.eventMap[event] = (method, extraArgs)

    def isAccepting(self):

        for event in self.eventMap:
            if DirectObject.isIgnoring(self, event):
                return False

        return True

    def isIgnoring(self):

        for event in self.eventMap:
            if DirectObject.isAccepting(self, event):
                return False

        return True

    def remove(self, event):

        self.ignore(event)
        del self.eventMap[event]

    def removeAll(self):

        self.ignoreAll()
        self.eventMap.clear()

    def enable(self):

        taskMgr.remove('_enable-' + str(self))
        taskMgr.doMethodLater(0, self._enable, '_enable-' + str(self))

    def _enable(self, task):

        self.ignoreAll()

        for event, tuple in self.eventMap.iteritems():
            DirectObject.accept(self, event, tuple[0], tuple[1])

        return task.done

    def disable(self):

        taskMgr.remove('_enable-' + str(self))
        self.ignoreAll()
