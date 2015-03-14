#@PydevCodeAnalysisIgnore
from panda3d.core import Point2

from common.Constants import Constants

class MiscUtil:

    @staticmethod
    def map3Dto2D(nodePath, position):
        pos2D = Point2()

        if base.camLens.project(base.cam.getRelativePoint(nodePath, position), pos2D):
            return aspect2d.getRelativePoint(render2d, (pos2D.getX(), 0, pos2D.getY()))
