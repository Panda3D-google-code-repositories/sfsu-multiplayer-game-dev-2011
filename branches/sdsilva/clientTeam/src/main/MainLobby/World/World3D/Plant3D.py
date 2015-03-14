from common.Constants import Constants
class Plant3D():
    def __init__(self):
        self.models = []
        self.healthy = True
        self.x = 0
        self.y = 0
        self.zone = None
    def tree(self, myzone, x, y):
        self.models.append(loader.loadModel("models/bigTree/bigTree"))
        self.models[0].reparentTo(myzone.root)
        self.x = x
        self.y = y
        self.zone = myzone
        self.models[0].setX(self.zone.x + self.x)
        self.models[0].setY(self.zone.y + self.y)
        self.models[0].setZ(20)
        return self
