from direct.showbase.DirectObject import DirectObject
from common.Constants import Constants
from common.DirectBasicButton import DirectBasicButton
from common.DirectControls import DirectControls
from common.DirectWindow import DirectWindow
from direct.gui.DirectFrame import DirectFrame
from direct.gui.DirectGui import DGG
from direct.gui.DirectLabel import DirectLabel
from direct.gui.DirectSlider import DirectSlider
from panda3d.core import TransparencyAttrib, TextNode
from common.Events import Events
from common.DirectBasicWindow import DirectBasicWindow

class TenDayStatsControls(DirectControls):

    def __init__(self, parent):

        DirectControls.__init__(self, parent)

#        self.accept('escape', parent.hide)
        self.accept('control-t', parent.toggleVisibility)

class TenDayStats(DirectObject):
    
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
        self.maxItemsVisible = 11
        self.createMainFrame()
        self.createSpeciesInfo()
        self.createLog()
        self.currentDay = None
        self.control = TenDayStatsControls(self)
#        self.loadSpeciesInfo()
        main.msgQ.addToCommandList(Constants.SMSG_STATISTICS,self.loadSpeciesInfo)
        self.statReceived = False
        self.taskManagerAdded  = False
        
#############################All fields pertaining to the stat interface###########
        self.statinfo = []
        self.statinfoLog=[]
        self.statbiomass=[]
        self.statkeyZone = 'zone'
        self.statkeySpecies = 'species'
        self.statkeyCount = 'count'
        self.statzoneInfo=[]
        self.stattopIndexOfList=0
        self.statmaxItemsVisible = 7
        #self.statcreateMainFrame()
        self.statcreateSpeciesInfo()
        self.statcreateLog()

        self.statisticsList = {}
        self.accept(Events.EVENT_TOTAL_ANIMAL, self.setAnimalData)
        self.accept(Events.EVENT_TOTAL_PLANT, self.setPlantData)
        
        
    def loadSpeciesInfo(self,obj):
        """
        stats is tuple object
        """
        #self.info = self.world.gameState.getStatistics()
        obj1 = self.parse(obj)
        self.info = obj1
        if self.maxItemsVisible <= len(self.info):
            maxItems = self.maxItemsVisible
        else:
            maxItems = len(self.info)
            
        for i in range(maxItems):
            self.infoLog[i][0]['text'] = self.info[i][0] #day
            self.infoLog[i][1]['text'] = self.info[i][1]      #species
            self.infoLog[i][2]['text'] = self.info[i][2]      #activity
            self.infoLog[i][3]['text'] = self.info[i][3]      #count
            #self.infoLog[i][3]['text'] = str(self.info[i][3])  #envScore  
            #self.infoLog[i][4]['text'] = str(self.info[i][4])  #message  
            #print self.info[i][0],self.info[i][1],self.info[i][2]
   
        self.updateScrollBar()  
        self.statReceived = True
           
    def createMainFrame(self):
 
        self.headerFrame = DirectWindow(frameSize=(-1.5, -0.2, -0.03, 0.04),
                                      #frameColor=(0.3, 0.3, 0.3, 0.3),
                                      frameColor=(0, 0, 0, 0.3),
                                      pos=(0, 0, 0.7),
                                      state=DGG.NORMAL)
        self.headerFrame.reparentTo(self.parent)
        self.headerFrame.hide()
        
        self.statFrame = DirectFrame(frameSize=(-1.5, -0.2, -1.20, 0.55),
                                      #frameColor=Constants.BG_COLOR,
                                      frameColor=(0, 0, 0, 0.3),
                                      pos=(0, 0, -0.59),
                                      state=DGG.NORMAL)
        self.statFrame.reparentTo(self.headerFrame)
        
        self.hideButton = DirectBasicButton(text=" - ",
                                       text_fg=(1, 1, 1, 1),
                                       text_pos=(-0.007, -0.015),
                                       text_scale=0.05,
                                       frameColor=(0, 0, 0, 0.2),
                                       frameSize=(-0.04, 0.04, -0.025, 0.025),
                                       pos=(-0.24, 0, 0),
                                       relief=DGG.FLAT,
                                       command=self.hide)
        self.hideButton.setTransparency(TransparencyAttrib.MAlpha)
        self.hideButton.reparentTo(self.headerFrame)
        
        _imageDir = 'models/2d'
        self.refreshButton = DirectBasicButton(text='',
                                       image=(_imageDir + '/refresh.png',
                                              ),
                                       image_pos=(0, 0, 0),
                                       image_scale=(0.04, 0, 0.03),
                                       text_fg=(1, 1, 1, 1),
                                       text_pos=(-0.007, -0.015),
                                       text_scale=0.05,
                                       frameColor=(0, 0, 0, 0.2),
                                       frameSize=(-0.01, 0.01, -0.025, 0.025),
                                       pos=(-0.34, 0, 0),
                                       relief=DGG.FLAT,
                                       command=self.show)
        self.refreshButton.setTransparency(TransparencyAttrib.MAlpha)
        self.refreshButton.reparentTo(self.headerFrame)        
        
#        self.stopButton = DirectBasicButton(text="Stop",
#                                       text_fg=(1, 1, 1, 1),
#                                       text_pos=(-0.007, -0.015),
#                                       text_scale=0.05,
#                                       frameColor=(0, 0, 0, 0.2),
#                                       frameSize=(-0.04, 0.04, -0.025, 0.025),
#                                       pos=(-0.44, 0, 0),
#                                       relief=DGG.FLAT,
#                                       command=self.stop)
#        self.stopButton.setTransparency(TransparencyAttrib.MAlpha)
#        self.stopButton.reparentTo(self.headerFrame)
#        
#        self.startButton = DirectBasicButton(text="Start",
#                                       text_fg=(1, 1, 1, 1),
#                                       text_pos=(-0.007, -0.015),
#                                       text_scale=0.05,
#                                       frameColor=(0, 0, 0, 0.2),
#                                       frameSize=(-0.04, 0.04, -0.025, 0.025),
#                                       pos=(-0.64, 0, 0),
#                                       relief=DGG.FLAT,
#                                       command=self.start)
#        self.startButton.setTransparency(TransparencyAttrib.MAlpha)
#        self.startButton.reparentTo(self.headerFrame)
   
    def start(self):
        self.show()   
        
    def stop(self):
        self.statReceived = False
        self.taskManagerAdded  = False
        self.unload()
          
    def show(self):
        if  self.world.gameState.currentDay is not None:
            print 'TenDay Stats Execute'
            #self.currentDay = self.world.gameState.currentDay
            self.currentDay =  (self.world.gameState.currentYear - 1) * 12 + self.world.gameState.currentDay
            activityEndDay = self.currentDay
            activityStartDay = 0
            if(activityEndDay-10 > 0):
                activityStartDay = activityEndDay - 10
                
            rContents = { 'activityStartDay': activityStartDay, 'activityEndDay':activityEndDay}
            main.cManager.sendRequest(Constants.CMSG_STATISTICS,rContents)
            self.headerFrame.show()
            #self.loadSpeciesInfo()
#        else:
#            obj = [(6, 'Oribi', 'Birth', 5), (7, 'Oribi', 'Death', 15), (8, 'Oribi', 'Death', 10), (9, 'Oribi', 'Death', 5), (10, 'Oribi', 'Death', 2), (11, 'Oribi', 'Death', 1), (5, 'Grass and herbs', 'Purchase', 7), (6, 'Grass and herbs', 'Death', 8)]
#            self.loadSpeciesInfo(obj)
#            self.headerFrame.show()
#            if self.taskManagerAdded  == False:
#                self.taskManagerAdded =True
#                taskMgr.add(self.updateRoutine, 'updateRoutine-getStatistics', 60*4)
        
    def hide(self):
        self.headerFrame.hide()
        self.statReceived = False
        self.taskManagerAdded  = False
        self.unload()
    
    def toggleVisibility(self):
        
        if self.headerFrame.isHidden():
            self.show()
        else:
            self.hide()
    
    def createSpeciesInfo(self):

        self.infoHeaderFrame = DirectFrame(frameSize=(-1.49, -0.21, -0.05, 0.05),
                                     frameColor=(0, 0, 0, 0.3),
                                     pos=(0, 0, -0.24)) #-0.49
        self.infoHeaderFrame.reparentTo(self.statFrame)
        
        self.specy = DirectLabel(text='YY:MM',
                                text_fg=(1, 1, 1, 1),
                                text_font=Constants.FONT_TYPE_01,
                                text_pos=(0, -0.015),
                                text_scale=0.055,
                                text_align=TextNode.ALeft,
                                text_shadow=Constants.TEXT_SHADOW_COLOR,
                                frameColor=(0, 0, 0, 0),
                             pos=(-1.5, 0, 0))
        self.specy.reparentTo(self.infoHeaderFrame)
        
        self.a = DirectLabel(text='Species',
                                text_fg=(1, 1, 1, 1),
                                text_font=Constants.FONT_TYPE_01,
                                text_pos=(0, -0.015),
                                text_scale=0.055,
                                text_align=TextNode.ALeft,
                                text_shadow=Constants.TEXT_SHADOW_COLOR,
                                frameColor=(0, 0, 0, 0),
                             pos=(-1.30, 0, 0))
        self.a.reparentTo(self.infoHeaderFrame)
        
        self.b = DirectLabel(text='Activity',
                                text_fg=(1, 1, 1, 1),
                                text_font=Constants.FONT_TYPE_01,
                                text_pos=(0, -0.015),
                                text_scale=0.055,
                                text_align=TextNode.ALeft,
                                text_shadow=Constants.TEXT_SHADOW_COLOR,
                                frameColor=(0, 0, 0, 0),
                             pos=(-0.7, 0, 0)) 
        self.b.reparentTo(self.infoHeaderFrame)
        
        self.c = DirectLabel(text='Count',
                                text_fg=(1, 1, 1, 1),
                                text_font=Constants.FONT_TYPE_01,
                                text_pos=(0, -0.015),
                                text_scale=0.055,
                                text_align=TextNode.ALeft,
                                text_shadow=Constants.TEXT_SHADOW_COLOR,
                                frameColor=(0, 0, 0, 0),
                             pos=(-0.4, 0, 0)) 
        self.c.reparentTo(self.infoHeaderFrame)
        
#        self.d = DirectLabel(text='EnvScore',
#                                text_fg=(1, 1, 1, 1),
#                                text_font=Constants.FONT_TYPE_01,
#                                text_pos=(0, -0.015),
#                                text_scale=0.055,
#                                text_align=TextNode.ALeft,
#                                text_shadow=Constants.TEXT_SHADOW_COLOR,
#                                frameColor=(0, 0, 0, 0),
#                             pos=(0.3, 0, 0)) 
#        self.d.reparentTo(self.infoHeaderFrame)
#        
#        self.e = DirectLabel(text='Message',
#                                text_fg=(1, 1, 1, 1),
#                                text_font=Constants.FONT_TYPE_01,
#                                text_pos=(0, -0.015),
#                                text_scale=0.055,
#                                text_align=TextNode.ALeft,
#                                text_shadow=Constants.TEXT_SHADOW_COLOR,
#                                frameColor=(0, 0, 0, 0),
#                             pos=(0.6, 0, 0)) 
#        self.e.reparentTo(self.infoHeaderFrame)
    
    def createLog(self):
        
        self.specyFrame = DirectFrame(frameSize=(-1.49, -0.21, -0.5, 0.26),
                                     frameColor=(0, 0, 0, 0.3),
                                     #pos=(0, 0, 0.17))
                                     pos=(0, 0, -0.57))
        self.specyFrame.reparentTo(self.statFrame)
        self.specyFrame.setTransparency(TransparencyAttrib.MAlpha)  
        
        self.scrollBar = DirectSlider(pos=(-0.255, 0, 0),
                                       scale=0.13,
                                       value=1,
                                       range=(1, 0),
                                       scrollSize=1,
                                       frameSize=(-0.05, 0.05, -4.7, 1.7),
                                       pageSize=3,
                                       orientation=DGG.VERTICAL,
                                       thumb_frameSize=(-0.1, 0.1, -0.2, 0.2),
                                       thumb_relief=DGG.FLAT,
                                       command = self.scrollList )
        self.scrollBar.reparentTo(self.specyFrame) 
             
        for i in range(self.maxItemsVisible):
            _z = 0.2 - i * 0.08
            _day = DirectLabel(text='',            #text=Day,
                                text_fg=(1, 1, 1, 1),
                                text_font=Constants.FONT_TYPE_01,
                                text_pos=(0, -0.015),
                                text_scale=0.05,
                                text_align=TextNode.ALeft,
                                text_shadow=Constants.TEXT_SHADOW_COLOR,
                                frameColor=(0, 0, 0, 0),
                             pos=(-1.45, 0, _z))
            _day.reparentTo(self.specyFrame)
        
            _species = DirectLabel(text='',               #text='species',
                                text_fg=(1, 1, 1, 1),
                                text_font=Constants.FONT_TYPE_01,
                                text_pos=(0, -0.015),
                                text_scale=0.05,
                                text_align=TextNode.ALeft,
                                text_shadow=Constants.TEXT_SHADOW_COLOR,
                                frameColor=(0, 0, 0, 0),
                             pos=(-1.30, 0, _z))
            _species.reparentTo(self.specyFrame)
        
            _activity = DirectLabel(text='',               #text='activity ',
                            text_fg=(1, 1, 1, 1),
                            text_font=Constants.FONT_TYPE_01,
                            text_pos=(0, -0.015),
                            text_scale=0.05,
                            text_align=TextNode.ALeft,
                            text_shadow=Constants.TEXT_SHADOW_COLOR,
                            frameColor=(0, 0, 0, 0),
                             pos=(-0.7, 0, _z))  
            _activity.reparentTo(self.specyFrame)
 
 
            _count = DirectLabel(text='',               #text='count ',
                            text_fg=(1, 1, 1, 1),
                            text_font=Constants.FONT_TYPE_01,
                            text_pos=(0, -0.015),
                            text_scale=0.05,
                            text_align=TextNode.ALeft,
                            text_shadow=Constants.TEXT_SHADOW_COLOR,
                            frameColor=(0, 0, 0, 0),
                             pos=(-0.4, 0, _z))  
            _count.reparentTo(self.specyFrame)
            
            
#            _envScore = DirectLabel(text='',               #text='envScore ',
#                            text_fg=(1, 1, 1, 1),
#                            text_font=Constants.FONT_TYPE_01,
#                            text_pos=(0, -0.015),
#                            text_scale=0.05,
#                            text_align=TextNode.ALeft,
#                            text_shadow=Constants.TEXT_SHADOW_COLOR,
#                            frameColor=(0, 0, 0, 0),
#                             pos=(0.3, 0, _z))  
#            _envScore.reparentTo(self.specyFrame)
# 
#
#            _message = DirectLabel(text='',               #text='message ',
#                            text_fg=(1, 1, 1, 1),
#                            text_font=Constants.FONT_TYPE_01,
#                            text_pos=(0, -0.015),
#                            text_scale=0.05,
#                            text_align=TextNode.ALeft,
#                            text_shadow=Constants.TEXT_SHADOW_COLOR,
#                            frameColor=(0, 0, 0, 0),
#                             pos=(0.6, 0, _z))  
#            _message.reparentTo(self.specyFrame)
                        
            self.infoLog.append([_day, _species, _activity,_count])
            
    def scrollList(self):
        
        sliderValue = int(round(self.scrollBar['value']))
        self.topIndexOfList = sliderValue
        
        if len(self.info) < self.maxItemsVisible:
            maxItems = len(self.info)
        else:
            maxItems = self.maxItemsVisible
        
        for i in range(maxItems):
            if len(self.info) > self.maxItemsVisible:
                index = sliderValue + i
                self.infoLog[i][0]['text'] = self.info[index][0] #day
                self.infoLog[i][1]['text'] = self.info[index][1]      #species
                self.infoLog[i][2]['text'] = self.info[index][2]      #activity
                self.infoLog[i][3]['text'] = self.info[index][3]      #count
                #self.infoLog[i][3]['text'] = str(self.info[index][3])  #envScore  
                #self.infoLog[i][4]['text'] = str(self.info[index][4])  #message 
            else:
                self.infoLog[i][0]['text'] = self.info[i][0] #day
                self.infoLog[i][1]['text'] = self.info[i][1]      #species
                self.infoLog[i][2]['text'] = self.info[i][2]      #activity
                self.infoLog[i][3]['text'] = self.info[i][3]      #count
                #self.infoLog[i][3]['text'] = str(self.info[i][3])  #envScore  
                #self.infoLog[i][4]['text'] = str(self.info[i][4])  #message 
                       
    def updateScrollBar(self):

        if len(self.info) > self.maxItemsVisible:
            if self.scrollBar.isHidden():
                self.scrollBar.show()
                
            scrollRange = len(self.info) - self.maxItemsVisible
            
            currentSize = self.scrollBar['thumb_frameSize'][3] - self.scrollBar['thumb_frameSize'][2]
            if currentSize > 0.2:
                scrollRatio = float(self.maxItemsVisible) / len(self.info)
                #scrollRatio = 0.7
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
                    
#    def updateRoutine(self,task):
#        #print 'updateRoutine getStatistics'
#        self.loadSpeciesInfo()
#        return task.cont
#    
#    def unload(self):
#        taskMgr.remove('updateRoutine-getStatistics')    

    def parse(self,obj):
        self.dictLevel1 = {}
        self.statList = []
        for item in obj:
            key = item[0]
            value = item[1:]
            #print 'key ',key,' item ',item
            # Despite the empty lists, it's still possible to 
            # test for the existance of values easily:
            if self.dictLevel1.has_key(key) and self.dictLevel1[key]:
                self.dictLevel1.setdefault(key, []).append(value)
            else:
                self.dictLevel1.setdefault(key, []).append(value)
            
        #print '-----1st level key value pair is done, self.dictLevel1 has all the values',self.dictLevel1

        dictLevel1 = self.dictLevel1.keys()
        dictLevel1.sort(reverse=True)
        for item in dictLevel1:
            totalMonths = item
            if totalMonths < 13 :
                year = 1
                month = totalMonths
                print 'year ',year,' month ', month
                yearMonth = str(year) + ":" + str(month)
                print yearMonth
            else:
                year = (totalMonths / 12) + 1
                month = totalMonths % 12
                print 'year ',year,' month ', month
                yearMonth = str(year) + ":" + str(month)
                print yearMonth
            self.statList.append((str(yearMonth),'','',''))
            listValues = self.dictLevel1[item]
            #print 'key ',item,' values ',listValues
            self.dictLevel2 = {}
            for i in listValues:
                key = i[0]
                value = i[1:]
                #print 'key ',key,' value ',value
                if self.dictLevel2.has_key(key) and self.dictLevel2[key]:
                    self.dictLevel2.setdefault(key, []).append(value)
                    self.statList.append(('','',value[0],str(value[1])))
                else:
                    self.dictLevel2.setdefault(key, []).append(value)
                    #self.statList.append(('',key,'',''))
                    #self.statList.append(('','',value[0],str(value[1]))) 
                    self.statList.append(('',key,value[0],str(value[1])))
            #(activityDay,animalName,activityType,count)
            #print item, ' - ' ,self.dictLevel2
            #temp = (item,key,value[0],value[1])
            #self.statList.append(temp)
        return self.statList

    def updateRoutine(self,task):
        #print 'updateRoutine getStatistics'
        if(self.statReceived == True):
            self.statReceived = False
            self.show()
        return task.cont
    
    def unload(self):
        taskMgr.remove('updateRoutine-getStatistics')  
        
#############################All methods pertaining to the stat interface###########
        
    def setAnimalData(self, zone_id, species_id, amount):

        name = game.animalNameList[species_id]
        self.statisticsList[name] = (zone_id, amount)

        self.updateScrollBar2()

    def setPlantData(self, zone_id, species_id, amount):

        name = game.plantNameList[species_id]
        self.statisticsList[name] = (zone_id, amount)

        self.updateScrollBar2()
        
#    def statcreateMainFrame(self):
#
#        self.statMainFrame = DirectBasicWindow(title = 'Stats',
#                                           onClose = self.toggleVisibility,
#                                           frameSize = (-0.6, 0.6, -0.90, 0.55),
#                                           frameColor = Constants.BG_COLOR,
#                                           pos = (-0.6, 0, 0.2),
#                                           state = DGG.NORMAL)
#        self.statMainFrame.reparentTo(self.parent)
#        self.statMainFrame.hide()

    def statcreateSpeciesInfo(self):

        self.infoHeaderFrame2 = DirectFrame(frameSize=(-1.49, -0.21, -0.05, 0.05),
                                     frameColor=(0, 0, 0, 0.3),
                                     pos=(0, 0, 0.49))
        self.infoHeaderFrame2.reparentTo(self.statFrame)
        
        self.specy = DirectLabel(text='Zone',
                                text_fg=(1, 1, 1, 1),
                                text_font=Constants.FONT_TYPE_01,
                                text_pos=(0, -0.015),
                                text_scale=0.055,
                                text_align=TextNode.ALeft,
                                text_shadow=Constants.TEXT_SHADOW_COLOR,
                                frameColor=(0, 0, 0, 0),
                             #pos=(-0.56, 0, 0))
                             pos=(-1.5, 0, 0))
        self.specy.reparentTo(self.infoHeaderFrame2)
        
        self.x = DirectLabel(text='Species',
                                text_fg=(1, 1, 1, 1),
                                text_font=Constants.FONT_TYPE_01,
                                text_pos=(0, -0.015),
                                text_scale=0.055,
                                text_align=TextNode.ALeft,
                                text_shadow=Constants.TEXT_SHADOW_COLOR,
                                frameColor=(0, 0, 0, 0),
                              #pos=(-0.3, 0, 0))
                              pos=(-1.24, 0, 0))
        self.x.reparentTo(self.infoHeaderFrame2)
        
        self.w = DirectLabel(text='Count',
                                text_fg=(1, 1, 1, 1),
                                text_font=Constants.FONT_TYPE_01,
                                text_pos=(0, -0.015),
                                text_scale=0.055,
                                text_align=TextNode.ALeft,
                                text_shadow=Constants.TEXT_SHADOW_COLOR,
                                frameColor=(0, 0, 0, 0),
                              #pos=(0.4, 0, 0))
                              pos=(-0.5, 0, 0)) 
        self.w.reparentTo(self.infoHeaderFrame2)
        
    def statcreateLog(self):
        
        self.specyFrame2 = DirectFrame(frameSize=(-0.59, 0.69, -0.35, 0.26),
                                     frameColor=(0, 0, 0, 0.3),
                                     pos=(-0.9, 0, 0.17))
        self.specyFrame2.reparentTo(self.statFrame)
        self.specyFrame2.setTransparency(TransparencyAttrib.MAlpha)  
        
        self.scrollBar2 = DirectSlider(pos=(0.655, 0, 0),
                                       scale=0.13,
                                       value=1,
                                       range=(1, 0),
                                       scrollSize=1,
                                       frameSize=(-0.05, 0.05, -2.2, 1.7),
                                       pageSize=3,
                                       orientation=DGG.VERTICAL,
                                       thumb_frameSize=(-0.1, 0.1, -0.2, 0.2),
                                       thumb_relief=DGG.FLAT,
                                       command = self.statscrollList )
        self.scrollBar2.reparentTo(self.specyFrame2) 
        self.scrollBar2.hide()
             
        for i in range(self.statmaxItemsVisible):
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
            _zone.reparentTo(self.specyFrame2)
        
            _x = DirectLabel(text='',               #text='species',
                                text_fg=(1, 1, 1, 1),
                                text_font=Constants.FONT_TYPE_01,
                                text_pos=(0, -0.015),
                                text_scale=0.05,
                                text_align=TextNode.ALeft,
                                text_shadow=Constants.TEXT_SHADOW_COLOR,
                                frameColor=(0, 0, 0, 0),
                             pos=(-0.3, 0, _z))
            _x.reparentTo(self.specyFrame2)
        
            _w = DirectLabel(text='',               #text='count ',
                            text_fg=(1, 1, 1, 1),
                            text_font=Constants.FONT_TYPE_01,
                            text_pos=(0, -0.015),
                            text_scale=0.05,
                            text_align=TextNode.ALeft,
                            text_shadow=Constants.TEXT_SHADOW_COLOR,
                            frameColor=(0, 0, 0, 0),
                             pos=(0.4, 0, _z))  
            _w.reparentTo(self.specyFrame2)
            
            self.statinfoLog.append([_zone, _x, _w])
            
    def statscrollList(self):
        
        sliderValue = int(round(self.scrollBar2['value']))
        self.stattopIndexOfList = sliderValue
        
        if len(self.statisticsList) < self.statmaxItemsVisible:
            maxItems = len(self.statisticsList)
        else:
            maxItems = self.statmaxItemsVisible

        statList = sorted(self.statisticsList.keys())

        for i in range(maxItems):
            if len(self.statisticsList) > self.statmaxItemsVisible:
                index = sliderValue + i

                name = statList[index]
                zone_id = self.statisticsList[name][0]
                amount = self.statisticsList[name][1]

                self.statinfoLog[i][0]['text'] = str(zone_id)
                self.statinfoLog[i][1]['text'] = name
                self.statinfoLog[i][2]['text'] = str(amount)
            else:
                name = statList[i]
                zone_id = self.statisticsList[name][0]
                amount = self.statisticsList[name][1]

                self.statinfoLog[i][0]['text'] = str(zone_id)
                self.statinfoLog[i][1]['text'] = name
                self.statinfoLog[i][2]['text'] = str(amount) 

    def updateScrollBar2(self):

        if len(self.statisticsList) > self.statmaxItemsVisible:
            if self.scrollBar2.isHidden():
                self.scrollBar2.show()
                
            scrollRange = len(self.statisticsList) - self.statmaxItemsVisible
            
            currentSize = self.scrollBar2['thumb_frameSize'][3] - self.scrollBar2['thumb_frameSize'][2]
            if currentSize > 0.2:
                scrollRatio = float(self.statmaxItemsVisible) / len(self.statisticsList)
                if (scrollRatio * currentSize) > 0.2:
                    self.scrollBar2['thumb_frameSize'] = (self.scrollBar2['thumb_frameSize'][0],
                                                         self.scrollBar2['thumb_frameSize'][1],
                                                         self.scrollBar2['frameSize'][2]*scrollRatio,
                                                         self.scrollBar2['frameSize'][3]*scrollRatio)
                else:
                    self.scrollBar2['thumb_frameSize'] = (self.scrollBar2['thumb_frameSize'][0],
                                                         self.scrollBar2['thumb_frameSize'][1],
                                                         - 0.1, 0.1)
        else:
            self.scrollBar2.hide()
            scrollRange = 1

        self.scrollBar2['range'] = (scrollRange, 0)            
