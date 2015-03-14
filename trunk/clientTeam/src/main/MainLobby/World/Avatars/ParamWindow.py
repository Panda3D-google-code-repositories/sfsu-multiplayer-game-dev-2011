'''
Created on Apr 7, 2012

@author: hunvil
'''
from common.Constants import Constants
from common.DirectBasicButton import DirectBasicButton
from common.DirectControls import DirectControls
from common.DirectWindow import DirectWindow
from common.DirectTextField import DirectTextField
from direct.gui.DirectFrame import DirectFrame
from direct.gui.DirectGui import DGG
from direct.gui.DirectLabel import DirectLabel
from direct.gui.DirectSlider import DirectSlider
from panda3d.core import TransparencyAttrib, TextNode
from direct.gui.DirectOptionMenu import DirectOptionMenu
from direct.gui.DirectCheckButton import DirectCheckButton

class ParamWindowControls(DirectControls):

    def __init__(self, parent):

        DirectControls.__init__(self, parent)

        self.accept('escape', parent.hide)
        self.accept('control-p', parent.toggleVisibility)

class ParamWindow:
    
    def __init__(self, params,world):
        self.params = params
        self.world = world
        self.parent = self.params.headerFrame
        self.predatorTypes=[]
        self.info = []
        self.infoLog = []
        self.itemSlider = []
        self.percentLabel = []
        self.eFocus = -1
        self.sliderValue = {}
        self.topIndexOfList=0
        self.maxItemsVisible = 8
        self.sliderScale = {}
        for i in range(self.maxItemsVisible):
            self.sliderScale[i] = 50
        self.itemCheckBox = []
        self.checkBoxValue = {}
        for i in range(self.maxItemsVisible):
            self.checkBoxValue[i] = False
        self.initWindow()
        self.createLog()
        self.createLabels()
        self.specyFrame.hide()
        self.control = ParamWindowControls(self)
        self.allTextEntriesShown = False
        self.createButtons()
        self.parameterType = None
        self.predatorChoice = None
        self.predatorCategory = None
        self.preyList = None
        #self.parameterCategory = ['Select Parameter Type','Metabolic Rate Plants(x)','Metabolic Rate Animals(x)','Relative Half Saturation Density(a)','Assimilation Efficiency(e)','Functional Response Control(q)','Predator Interference(d)']
        self.parameterCategory = ['Select Parameter Type','Metabolic Rate Animals(x)','Relative Half Saturation Density(a)','Assimilation Efficiency(e)','Functional Response Control(q)','Predator Interference(d)']        
        self.predatorList = None
        self.parametersList = {}  #predatorname vs preylist tuple(prey name , value)
        main.msgQ.addToCommandList(Constants.CMSG_GET_FUNCTIONAL_PARAMETERS, self.populatePreyList)
        
    def initParameters(self,items):
        if self.maxItemsVisible >= len(items):
            maxItems = self.maxItemsVisible
        else:
            maxItems = len(items)
        self.sliderValue = {}
        self.topIndexOfList=0  
        self.sliderScale = {}
        for i in range(maxItems):
            self.sliderScale[i] = 100/len(items)
            self.sliderValue[i] = 100/len(items)
        self.checkBoxValue = {}
        for i in range(maxItems):
            self.checkBoxValue[i] = False  
        self.allTextEntriesShown = False   
        
        if self.speciesData == 0:
            if self.predatorChoice not in self.parametersList:
                parameterType = 0
                if (self.parameterType == self.parameterCategory[3]):
                    parameterType = Constants.PARAMETER_E
                elif (self.parameterType == self.parameterCategory[5]):
                    parameterType = Constants.PARAMETER_D
                elif (self.parameterType == self.parameterCategory[4]):
                    parameterType = Constants.PARAMETER_Q
                elif (self.parameterType == self.parameterCategory[2]):
                    parameterType = Constants.PARAMETER_A  
                #send a request to server and add it to self.parametersList
                args = {'predator_name' : self.predatorChoice, 'parameter_type':parameterType}
                main.cManager.sendRequest(Constants.CMSG_GET_FUNCTIONAL_PARAMETERS, args)
        elif self.speciesData == 1:
            if self.predatorChoice not in self.parametersList:
                parameterType = 0
                if (self.parameterType == self.parameterCategory[1]):
                    parameterType = Constants.PARAMETER_X_A
                #send a request to server and add it to self.parametersList
                args = {'predator_name' : self.predatorCategory, 'parameter_type':parameterType}
                main.cManager.sendRequest(Constants.CMSG_GET_FUNCTIONAL_PARAMETERS, args)
        elif self.speciesData == 2:
            print ''
        return
   
    def initWindow(self):
        self.headerFrame = DirectWindow(frameSize=(-0.9, 1.1, -0.05, 0.05),
                                      frameColor=(0.3, 0.3, 0.3, 0.3),
                                      pos=(0, 0, 0.5),
                                      state=DGG.NORMAL)
        self.headerFrame.reparentTo(self.parent)
        self.headerFrame.hide()
        
        self.paramFrame = DirectFrame(frameSize=(-0.9, 1.1, -0.40, 0.65),
                                      frameColor=Constants.BG_COLOR,
                                      pos=(0, 0, -0.59),
                                      state=DGG.NORMAL)
        self.paramFrame.reparentTo(self.headerFrame)  
        
        self.hideButton = DirectBasicButton(text=" - ",
                                       text_fg=(1, 1, 1, 1),
                                       text_pos=(-0.007, -0.015),
                                       text_scale=0.05,
                                       frameColor=(0, 0, 0, 0.2),
                                       frameSize=(-0.04, 0.04, -0.025, 0.025),
                                       pos=(1.04, 0, 0.1),
                                       relief=DGG.FLAT,
                                       command=self.hide)
        self.hideButton.setTransparency(TransparencyAttrib.MAlpha)
        self.hideButton.reparentTo(self.headerFrame)

    def hide(self):
        self.headerFrame.hide()
        
    def toggleVisibility(self):
        
        if self.headerFrame.isHidden():
            self.headerFrame.show()
        else:
            self.headerFrame.hide()
            
    def show(self,parameterType,predatorChoice,preyList):
        self.speciesData = 0
        self.parameterType = parameterType
        self.predatorChoice = predatorChoice
        self.preyList = preyList        
        self.initParameters(preyList)
        self.parameterTypeLabel['text'] = "Parameter Type: " + parameterType
        self.predatorTypeLabel['text'] = "Predator Name: " + predatorChoice
#        self.loadInfo(preyList)
#        self.headerFrame.show()
#        self.specyFrame.show()
    def cancelClicked(self,eNum):
        print 'Cancel clicked, dismiss the message box',eNum
        
    def populatePreyList(self,preyList):
        if preyList['status'] == 1: # failed
            self.msgBox = main.createMessageBox(0, 'Not available...',self.cancelClicked,[self.eFocus])
        else:
            parameterType = preyList['parameterType']
            if parameterType == Constants.PARAMETER_X_A:
                if preyList['preyListSize'] != 0:
                    #then extract the parameters and display that
                    print 'then extract the parameters and display that'
                    preyListSize = preyList['preyListSize']
                    self.preyList = []
                    for i in range(preyListSize):
                        preyName = preyList['animalType' +str(i)]
                        percentValue = preyList['percentValue' +str(i)]
                        self.sliderScale[i] = percentValue
                        self.sliderValue[i] = percentValue
                        self.preyList.append(preyName)
                    self.loadInfo(self.preyList)
                    self.headerFrame.show()
                    self.specyFrame.show()
                else:
                    self.loadInfo(self.predatorList)
                    self.headerFrame.show()
                    self.specyFrame.show()            
            else:
                if preyList['preyListSize'] != 0:
                    #then extract the parameters and display that
                    print 'then extract the parameters and display that'
                    preyListSize = preyList['preyListSize']
                    self.preyList = []
                    for i in range(preyListSize):
                        preyName = preyList['animalType' +str(i)]
                        percentValue = preyList['percentValue' +str(i)]
                        self.sliderScale[i] = percentValue
                        self.sliderValue[i] = percentValue
                        self.preyList.append(preyName)
                    self.loadInfo(self.preyList)
                    self.headerFrame.show()
                    self.specyFrame.show()
                else:
                    self.loadInfo(self.preyList)
                    self.headerFrame.show()
                    self.specyFrame.show()      
          
    def showAnimalSpecies(self,predatorTypes,predatorCategory):
        self.speciesData = 1
        self.predatorList = predatorTypes 
        self.parameterType = self.parameterCategory[1]
        self.predatorCategory = predatorCategory
        self.initParameters(predatorTypes)
#        self.loadInfo(predatorTypes)
#        self.headerFrame.show()
#        self.specyFrame.show()
        return
   
#    def showPlantSpecies(self,plantTypes):
#        self.speciesData = 2
#        self.plantList = plantTypes
#        self.parameterType = self.parameterCategory[1]
#        self.initParameters(plantTypes)
#        self.loadInfo(plantTypes)
#        self.headerFrame.show()
#        self.specyFrame.show()
#        return
            
    def createLabels(self):
        self.parameterTypeLabel = DirectLabel(text = "",
                                           text_fg = (1,1,1,1),
                                           text_font = Constants.FONT_TYPE_02,
                                           text_pos = ( 0, -0.015),
                                           text_scale = 0.05,
                                           frameSize = ( -0.25, 0.25, -0.06, 0.06),
                                           frameColor = (0,0,0,0),
                                           pos = (-0.2, 0,0),
                                           relief = DGG.FLAT)
        self.parameterTypeLabel.reparentTo(self.headerFrame)
        
        self.predatorTypeLabel = DirectLabel(text = "",
                                           text_fg = (1,1,1,1),
                                           text_font = Constants.FONT_TYPE_02,
                                           text_pos = ( 0, -0.015),
                                           text_scale = 0.05,
                                           frameSize = ( -0.25, 0.25, -0.06, 0.06),
                                           frameColor = (0,0,0,0),
                                           pos = (-0.2, 0,-0.1),
                                           relief = DGG.FLAT)
        self.predatorTypeLabel.reparentTo(self.headerFrame)
        return     
    
    def loadInfo(self,preyList):
        self.info = None
        self.info = preyList
        if self.maxItemsVisible <= len(self.info):
            maxItems = self.maxItemsVisible
        else:
            maxItems = len(self.info)
            
        for i in range(maxItems):
            self.infoLog[i][0]['text'] = self.info[i] #prey name
            if i in self.sliderScale: 
                self.itemSlider[i]['value'] = self.sliderScale[i]
            if i in self.checkBoxValue:
                self.itemCheckBox[i]['indicatorValue'] = self.checkBoxValue[i]
                self.itemCheckBox[i].setIndicatorValue()
        self.updateScrollBar()
            
    def createLog(self):
        self.specyFrame = DirectFrame(frameSize=(-0.8, 1.05, -0.5, 0.2),
                                     frameColor=(0, 0, 0, 0.3),
                                     pos=(0, 0, 0.25))
        self.specyFrame.reparentTo(self.paramFrame)
        self.specyFrame.setTransparency(TransparencyAttrib.MAlpha)  
        
        self.scrollBar = DirectSlider(pos=(1.0, 0, -0.1),
                                       scale=0.13,
                                       value=1,
                                       range=(1, 0),
                                       scrollSize=1,
                                       frameSize=(-0.05, 0.05, -2.9, 1.6),
                                       pageSize=3,
                                       orientation=DGG.VERTICAL,
                                       thumb_frameSize=(-0.1, 0.1, -0.2, 0.2),
                                       thumb_relief=DGG.FLAT,
                                       command = self.scrollList )
        self.scrollBar.reparentTo(self.specyFrame) 
             
        for i in range(self.maxItemsVisible):
            _z = 0.1 - i * 0.08
            _prey = DirectLabel(text='',            #text=Day,
                                text_fg=(1, 1, 1, 1),
                                text_font=Constants.FONT_TYPE_01,
                                text_pos=(0, -0.015),
                                text_scale=0.05,
                                text_align=TextNode.ALeft,
                                text_shadow=Constants.TEXT_SHADOW_COLOR,
                                frameColor=(0, 0, 0, 0),
                                pos=(-0.75, 0, _z))
            _prey.reparentTo(self.specyFrame)  
            
            self.percentLabel.append(DirectLabel(text='',
                                    text_scale=0.045,
                                    text_pos=(0,-0.015),
                                    text_fg = Constants.TEXT_COLOR,
                                    text_font = Constants.FONT_TYPE_01,
                                    text_shadow = Constants.TEXT_SHADOW_COLOR,
                                    text_align=TextNode.ALeft,
                                    frameSize = (-0.1, 0.1, -0.04, 0.04),
                                    frameColor = (0,0,0,0),
                                    pos = (0.1, 0, _z)))
            self.percentLabel[i].setTransparency(TransparencyAttrib.MAlpha)
            self.percentLabel[i].reparentTo(self.specyFrame) 
                                #1st horizontal -ve left    last vertical +ve up
            self.itemSlider.append(DirectSlider( pos = (0.6, 0, _z),
                                           scale = 0.13,
                                           value = self.sliderScale[i],
                                           range = (0, 100),
    #                                       scrollSize = 1,
                                           frameSize = (-2.,2.,-0.06,0.06),
                                           pageSize = 1,
                                           orientation = DGG.HORIZONTAL,
                                           thumb_frameSize = (-0.25, 0.25, -0.2, 0.2),
                                           thumb_relief = DGG.FLAT,
                                           command = self.setSliderScale, 
                                           extraArgs = [i]))
            self.itemSlider[i].reparentTo(self.specyFrame)
            self.itemSlider[i].hide()
            
            self.itemCheckBox.append(DirectCheckButton(text = '' ,
                                                       scale=.05,
                                                       pos = (0.95, 0, _z),
                                                       command=self.setCheckBoxText,
                                                       extraArgs = [i]))
            self.itemCheckBox[i].reparentTo(self.specyFrame)
            self.itemCheckBox[i].hide()
            
#            self.itemDesc.append(DirectTextField(self.headerFrame,
#                                  text_font=Constants.FONT_TYPE_01,
#                                  scale=0.04,
#                                  pos=(-0.2, 0, _z),
#                                  frameColor=(0.8, 0.8, 0.8, 0.7),
#                                  width=7,
#                                  numLines = 1,
#                                  focusInCommand=self.onWorldEntryFocus,
#                                  focusOutCommand=self.onWorldEntryFocusOut))                                             
#            self.itemDesc[i].reparentTo(self.specyFrame)
#            self.itemDesc[i].hide()
            self.infoLog.append([_prey]) 
                 
        return 
    
    def setCheckBoxText(self,status,i):
        self.checkBoxValue[self.topIndexOfList+i] = status
        #print 'self.checkBoxValue[',self.topIndexOfList+i,']',self.checkBoxValue[self.topIndexOfList+i]
        return
    
    def setSliderScale(self,enum):
        self.sliderValue[self.topIndexOfList+enum] = self.itemSlider[enum]['value']
        #print 'self.topIndexOfList', self.topIndexOfList,' enum ' ,enum, ' self.sliderValue[',self.topIndexOfList+enum,'] ',self.sliderValue[self.topIndexOfList+enum]
        self.percentLabel[enum]['text'] = str('%.2f' % self.sliderValue[self.topIndexOfList+enum]) + '%'
        return 

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
                self.infoLog[i][0]['text'] = self.info[index] #prey name
                #print 'index ',index
                if index in self.sliderValue:
                    self.percentLabel[i]['text'] = str('%.2f' % self.sliderValue[index]) + '%'
                    self.itemSlider[i]['value'] = self.sliderValue[index]
                    print index, ' ','self.sliderValue',self.sliderValue[index]
                if index in self.checkBoxValue:
                    self.itemCheckBox[i]['indicatorValue'] = self.checkBoxValue[index]
                    self.itemCheckBox[i].setIndicatorValue()
                    print index, ' ','self.checkBoxValue',self.checkBoxValue[index]
                print index, ' ','self.infoLog',self.infoLog[i][0]['text'],'self.percentLabel',self.percentLabel[i]['text']
            else:
                self.infoLog[i][0]['text'] = self.info[i] #prey name
                self.percentLabel[i]['text'] = str('%.2f' % self.sliderValue[i]) + '%'
                #print i
            
    def updateScrollBar(self):

        if len(self.info) > self.maxItemsVisible:
            if self.scrollBar.isHidden():
                self.scrollBar.show()
                
            if not self.allTextEntriesShown:
                self.showAllTextEntries()    
                
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
            self.hideTextEntries()
            scrollRange = 1

        self.scrollBar['range'] = (scrollRange, 0) 

    def hideTextEntries(self):
        
        self.allTextEntriesShown = False
        for i in range(len(self.info)):
            self.itemSlider[i].show()
            self.percentLabel[i].show()
            #self.itemCheckBox[i].show()
            
            
        for i in range(len(self.info), self.maxItemsVisible):
            self.itemSlider[i].hide()
            self.infoLog[i][0]['text'] = ''
            self.percentLabel[i].hide()
            #self.itemCheckBox[i].hide()
        
    def showAllTextEntries(self):
        for i in range(self.maxItemsVisible):
            self.itemSlider[i].show()
            self.percentLabel[i].show()
            #self.itemCheckBox[i].show()

        self.allTextEntriesShown = True 
        
    def createButtons(self):
        """Create some buttons."""
        self.submitButton = DirectBasicButton(text='Submit',
                                         text_font=Constants.FONT_TYPE_01,
                                         text_pos=(0, -0.015),
                                         text_scale=0.05,
                                         frameSize=(-0.13, 0.13, -0.05, 0.05),
                                         frameColor=(0.8, 0.8, 0.8, 0.7),
                                         pos=(-0.5, 0, -0.92),
                                         relief=DGG.FLAT,
                                         command=self.submit)
        self.submitButton.reparentTo(self.headerFrame)

        self.cancel = DirectBasicButton(text='Cancel',
                                         text_font=Constants.FONT_TYPE_01,
                                         text_pos=(0, -0.015),
                                         text_scale=0.05,
                                         frameSize=(-0.13, 0.13, -0.05, 0.05),
                                         frameColor=(0.8, 0.8, 0.8, 0.7),
                                         pos=(0, 0, -0.92),
                                         relief=DGG.FLAT,
                                         command=self.hide)
        self.cancel.reparentTo(self.headerFrame)
        
        self.reset = DirectBasicButton(text='Reset',
                                         text_font=Constants.FONT_TYPE_01,
                                         text_pos=(0, -0.015),
                                         text_scale=0.05,
                                         frameSize=(-0.13, 0.13, -0.05, 0.05),
                                         frameColor=(0.8, 0.8, 0.8, 0.7),
                                         pos=(0.5, 0, -0.92),
                                         relief=DGG.FLAT,
                                         command=self.reset)
        self.reset.reparentTo(self.headerFrame)    
        
    def reset(self):
        self.initParameters(self.info)
        
    def submit(self):
        print 'Submit called from ParamWindow'
        if self.speciesData == 0:
            preyListSize = len(self.preyList)
            totalSum = 0
            parameterType = -1
            self.percentValues = {}
            for i in range(preyListSize):
                totalSum = totalSum + self.sliderValue[i]
            
            for i in range(preyListSize):
                self.percentValues[i] = (self.sliderValue[i]/totalSum ) * 100.0
                print i, ' ',self.preyList[i], ' ',self.percentValues[i]
            
#            if (self.parameterType == self.parameterCategory[1]):
#                parameterType = Constants.PARAMETER_X_A
#            
            if (self.parameterType == self.parameterCategory[3]):
                parameterType = Constants.PARAMETER_E
            elif (self.parameterType == self.parameterCategory[5]):
                parameterType = Constants.PARAMETER_D
            elif (self.parameterType == self.parameterCategory[4]):
                parameterType = Constants.PARAMETER_Q
            elif (self.parameterType == self.parameterCategory[2]):
                parameterType = Constants.PARAMETER_A       
            #predatorId = self.world.gameState.getAnimalTypeID(self.predatorChoice)
            args = {'parameterType' : parameterType,
                    'predator'      : self.predatorChoice,
                    'preyListSize'  : preyListSize}
            for i in range(preyListSize):
                #preyId = self.world.gameState.getAnimalTypeID(self.preyList[i])
                args['animalType'+str(i)]   = self.preyList[i]
                args['percentValue'+str(i)]   = self.percentValues[i]
            print args
            main.cManager.sendRequest(Constants.CMSG_CHANGE_FUNCTIONAL_PARAMETERS, args)
            self.hide()  
        elif self.speciesData == 1:
            predatorListSize = len(self.predatorList)
            totalSum = 0
            parameterType = -1
            self.percentValues = {}
#            for i in range(predatorListSize):
#                totalSum = totalSum + self.sliderValue[i]
#            
#            for i in range(predatorListSize):
#                self.percentValues[i] = (self.sliderValue[i]/totalSum ) * 100.0
#                print i, ' ',self.predatorList[i], ' ',self.percentValues[i]
            for i in range(predatorListSize):
                self.percentValues[i] = self.sliderValue[i]
            if (self.parameterType == self.parameterCategory[1]):
                parameterType = Constants.PARAMETER_X_A
                
            args = {'parameterType' : parameterType,
                    'predator'      : self.predatorCategory,
                    'preyListSize'  : predatorListSize}
            for i in range(predatorListSize):
                #preyId = self.world.gameState.getAnimalTypeID(self.preyList[i])
                args['animalType'+str(i)]   = self.predatorList[i]
                args['percentValue'+str(i)]   = self.percentValues[i]
            print args
            main.cManager.sendRequest(Constants.CMSG_CHANGE_FUNCTIONAL_PARAMETERS, args)
            self.hide()   
#        elif self.speciesData == 2:
#            plantListSize = len(self.plantList)
#            totalSum = 0
#            parameterType = -1
#            self.percentValues = {}
##            for i in range(plantListSize):
##                totalSum = totalSum + self.sliderValue[i]
##            
##            for i in range(plantListSize):
##                self.percentValues[i] = (self.sliderValue[i]/totalSum ) * 100.0
##                print i, ' ',self.plantList[i], ' ',self.percentValues[i]
#            for i in range(plantListSize):
#                self.percentValues[i] = self.sliderValue[i]
#            if (self.parameterType == self.parameterCategory[1]):
#                parameterType = Constants.PARAMETER_X
#                
#            args = {'parameterType' : parameterType,
#                    'predator'      : '0',
#                    'preyListSize'  : plantListSize}
#            for i in range(plantListSize):
#                #preyId = self.world.gameState.getAnimalTypeID(self.preyList[i])
#                args['animalType'+str(i)]   = self.plantList[i]
#                args['percentValue'+str(i)]   = self.percentValues[i]
#            print args
#            main.cManager.sendRequest(Constants.CMSG_CHANGE_FUNCTIONAL_PARAMETERS, args)
#            self.hide() 