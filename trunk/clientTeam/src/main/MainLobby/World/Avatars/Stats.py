from direct.showbase.DirectObject import DirectObject

from direct.gui.DirectFrame import DirectFrame
from direct.gui.DirectGui import DGG
from direct.gui.DirectLabel import DirectLabel
from direct.gui.DirectSlider import DirectSlider

from panda3d.core import TextNode
from panda3d.core import TransparencyAttrib

from common.Constants import Constants
from common.DirectBasicWindow import DirectBasicWindow
from common.DirectControls import DirectControls
from common.Events import Events

class StatsControls(DirectControls):

    def __init__(self, parent):

        DirectControls.__init__(self, parent)

#        self.accept('escape', parent.hide)
        self.accept('control-s', parent.toggleVisibility)

class Stats(DirectObject):
    
    def __init__(self, world):
        
        self.world = world
        self.parent=self.world.mainFrame
        self.info = []
        self.infoLog=[]
        self.biomass=[]
        self.keyZone = 'zone'
        self.keySpecies = 'species'
        self.keyCount = 'count'
        self.zoneInfo=[]
        self.topIndexOfList=0
        self.maxItemsVisible = 16
        self.createMainFrame()
        self.createSpeciesInfo()
        self.createLog()

        self.statList = {}
        
        self.control = StatsControls(self)

        self.accept(Events.EVENT_TOTAL_ANIMAL, self.setAnimalData)
        self.accept(Events.EVENT_TOTAL_PLANT, self.setPlantData)

    def setAnimalData(self, zone_id, species_id, amount):

        name = game.animalNameList[species_id]
        self.statList[name] = (zone_id, amount)

        self.updateScrollBar()

    def setPlantData(self, zone_id, species_id, amount):

        name = game.plantNameList[species_id]
        self.statList[name] = (zone_id, amount)

        self.updateScrollBar()
           
    def createMainFrame(self):

        self.statFrame = DirectBasicWindow(title = 'Stats',
                                           onClose = self.toggleVisibility,
                                           frameSize = (-0.6, 0.6, -0.90, 0.55),
                                           frameColor = Constants.BG_COLOR,
                                           pos = (-0.6, 0, 0.2),
                                           state = DGG.NORMAL)
        self.statFrame.reparentTo(self.parent)
        self.statFrame.hide()

    def show(self):
        self.statFrame.show()

    def hide(self):
        self.statFrame.hide()

    def toggleVisibility(self):

        if self.statFrame.isHidden():
            self.statFrame.show()
        else:
            self.statFrame.hide()

    def createSpeciesInfo(self):

        self.infoHeaderFrame = DirectFrame(frameSize=(-0.59, 0.59, -0.05, 0.05),
                                     frameColor=(0, 0, 0, 0.3),
                                     pos=(0, 0, 0.49))
        self.infoHeaderFrame.reparentTo(self.statFrame)
        
        self.specy = DirectLabel(text='Zone',
                                text_fg=(1, 1, 1, 1),
                                text_font=Constants.FONT_TYPE_01,
                                text_pos=(0, -0.015),
                                text_scale=0.055,
                                text_align=TextNode.ALeft,
                                text_shadow=Constants.TEXT_SHADOW_COLOR,
                                frameColor=(0, 0, 0, 0),
                             pos=(-0.56, 0, 0))
        self.specy.reparentTo(self.infoHeaderFrame)
        
        self.x = DirectLabel(text='Species',
                                text_fg=(1, 1, 1, 1),
                                text_font=Constants.FONT_TYPE_01,
                                text_pos=(0, -0.015),
                                text_scale=0.055,
                                text_align=TextNode.ALeft,
                                text_shadow=Constants.TEXT_SHADOW_COLOR,
                                frameColor=(0, 0, 0, 0),
                             pos=(-0.3, 0, 0))
        self.x.reparentTo(self.infoHeaderFrame)
        
        self.w = DirectLabel(text='Count',
                                text_fg=(1, 1, 1, 1),
                                text_font=Constants.FONT_TYPE_01,
                                text_pos=(0, -0.015),
                                text_scale=0.055,
                                text_align=TextNode.ALeft,
                                text_shadow=Constants.TEXT_SHADOW_COLOR,
                                frameColor=(0, 0, 0, 0),
                             pos=(0.35, 0, 0)) 
        self.w.reparentTo(self.infoHeaderFrame)
    
    def createLog(self):
        
        self.specyFrame = DirectFrame(frameSize=(-0.59, 0.59, -1.05, 0.26),
                                     frameColor=(0, 0, 0, 0.3),
                                     pos=(0, 0, 0.17))
        self.specyFrame.reparentTo(self.statFrame)
        self.specyFrame.setTransparency(TransparencyAttrib.MAlpha)  
        
        self.scrollBar = DirectSlider(pos=(0.555, 0, 0),
                                       scale=0.13,
                                       value=1,
                                       range=(1, 0),
                                       scrollSize=1,
                                       frameSize=(-0.05, 0.05, -7.7, 1.7),
                                       pageSize=3,
                                       orientation=DGG.VERTICAL,
                                       thumb_frameSize=(-0.1, 0.1, -0.2, 0.2),
                                       thumb_relief=DGG.FLAT,
                                       command = self.scrollList )
        self.scrollBar.reparentTo(self.specyFrame) 
        self.scrollBar.hide()
             
        for i in range(self.maxItemsVisible):
            _z = 0.2 - i * 0.08
            _zone = DirectLabel(text='',            #text='Zone'+str(i),
                                text_fg=(1, 1, 1, 1),
                                text_font=Constants.FONT_TYPE_01,
                                text_pos=(0, -0.015),
                                text_scale=0.05,
                                text_align=TextNode.ALeft,
                                text_shadow=Constants.TEXT_SHADOW_COLOR,
                                frameColor=(0, 0, 0, 0),
                             pos=(-0.56, 0, _z))
            _zone.reparentTo(self.specyFrame)
        
            _x = DirectLabel(text='',               #text='species',
                                text_fg=(1, 1, 1, 1),
                                text_font=Constants.FONT_TYPE_01,
                                text_pos=(0, -0.015),
                                text_scale=0.05,
                                text_align=TextNode.ALeft,
                                text_shadow=Constants.TEXT_SHADOW_COLOR,
                                frameColor=(0, 0, 0, 0),
                             pos=(-0.3, 0, _z))
            _x.reparentTo(self.specyFrame)
        
            _w = DirectLabel(text='',               #text='count ',
                            text_fg=(1, 1, 1, 1),
                            text_font=Constants.FONT_TYPE_01,
                            text_pos=(0, -0.015),
                            text_scale=0.05,
                            text_align=TextNode.ALeft,
                            text_shadow=Constants.TEXT_SHADOW_COLOR,
                            frameColor=(0, 0, 0, 0),
                             pos=(0.4, 0, _z))  
            _w.reparentTo(self.specyFrame)
            
            self.infoLog.append([_zone, _x, _w])
            
    def scrollList(self):
        
        sliderValue = int(round(self.scrollBar['value']))
        self.topIndexOfList = sliderValue
        
        if len(self.statList) < self.maxItemsVisible:
            maxItems = len(self.statList)
        else:
            maxItems = self.maxItemsVisible

        statList = sorted(self.statList.keys())

        for i in range(maxItems):
            if len(self.statList) > self.maxItemsVisible:
                index = sliderValue + i

                name = statList[index]
                zone_id = self.statList[name][0]
                amount = self.statList[name][1]

                self.infoLog[i][0]['text'] = str(zone_id)
                self.infoLog[i][1]['text'] = name
                self.infoLog[i][2]['text'] = str(amount)
            else:
                name = statList[i]
                zone_id = self.statList[name][0]
                amount = self.statList[name][1]

                self.infoLog[i][0]['text'] = str(zone_id)
                self.infoLog[i][1]['text'] = name
                self.infoLog[i][2]['text'] = str(amount) 

    def updateScrollBar(self):

        if len(self.statList) > self.maxItemsVisible:
            if self.scrollBar.isHidden():
                self.scrollBar.show()
                
            scrollRange = len(self.statList) - self.maxItemsVisible
            
            currentSize = self.scrollBar['thumb_frameSize'][3] - self.scrollBar['thumb_frameSize'][2]
            if currentSize > 0.2:
                scrollRatio = float(self.maxItemsVisible) / len(self.statList)
                if (scrollRatio * currentSize) > 0.2:
                    self.scrollBar['thumb_frameSize'] = (self.scrollBar['thumb_frameSize'][0],
                                                         self.scrollBar['thumb_frameSize'][1],
                                                         self.scrollBar['frameSize'][2]*scrollRatio,
                                                         self.scrollBar['frameSize'][3]*scrollRatio)
                else:
                    self.scrollBar['thumb_frameSize'] = (self.scrollBar['thumb_frameSize'][0],
                                                         self.scrollBar['thumb_frameSize'][1],
                                                         - 0.1, 0.1)
        else:
            self.scrollBar.hide()
            scrollRange = 1

        self.scrollBar['range'] = (scrollRange, 0)            
