from direct.gui.DirectGui import DGG
from direct.gui.DirectLabel import DirectLabel
from direct.gui.DirectSlider import DirectSlider
from direct.interval.IntervalGlobal import Sequence
from direct.interval.LerpInterval import LerpColorScaleInterval

from panda3d.core import TextNode
from panda3d.core import TransparencyAttrib

from common.Constants import Constants
from common.DatabaseHelper import DatabaseHelper
from common.DirectBasicButton import DirectBasicButton
from common.DirectBasicLabel import DirectBasicLabel
from common.DirectDropDownMenu import DirectDropDownMenu
from common.DirectWindow import DirectWindow

from main.MainLobby.World.GameShop.GameShopControl import GameShopControl

class GameShop:
    """
    1). Load all item images from models directory
    2). Create Animal, Plant, Research and Vaccine Buttons
    3). Implement left and right scrolling through images
    4). Pop up window when mouse hover over
    """
    
    def __init__(self, world):

        self.parent = world.mainFrame

        self.categoryList = []
        self.categoryMap = {}
        self.shopButtons = []
        self.shopMode = 0

        self.animals = {}
        self.plants = {}

        self.itemList = []
        self.maxItemsVisible = 5

        self.researches=[]
        self.vaccine=[]
        self.items = []
        self.newItems = []
        self.newOptionLabels = {}
        self.itemsName = []

        self.key_type = 'itemName'
        self.key_cost = 'priceOfItem'
        self.key_image='image'
        self.key_prey_list='preyList'
        self.key_predator_list='predatorList'
        self.key_description='desc'
        self.key_effect='effect'
        self.key_model_id="model_id"
        self.key_biomass='biomass'

        self.loadResearchItems()
        self.loadVaccineItems()

        self.createMainFrame()
        self.createButtons()
        self.createDescriptionFrame()
        self.createScrollBar()

        self.putToCommandList()
        main.cManager.sendRequest(Constants.CMSG_SHOP_LIST_ANIMAL, None)
        main.cManager.sendRequest(Constants.CMSG_SHOP_LIST_PLANT, None)
#        self.control = GameShopControl(self)
#        self.control.disable()

    def putToCommandList(self):
        
        main.msgQ.addToCommandList(Constants.CMSG_SHOP_LIST_ANIMAL, self.loadAnimalItemInfo)
        main.msgQ.addToCommandList(Constants.CMSG_SHOP_LIST_PLANT, self.loadPlantItemInfo)

    def debugPrint(self,msg):
        #print msg
        return

    def loadAnimalItemInfo(self, args):
        """
        Load animal des, cost etc. from server
        """
        self.debugPrint('receive animal item info from server')

        animals = args['items']
        initial = args['initial']

        for animal in animals:

            if animal[self.key_type] not in self.animals:
                animal[self.key_image] = 'models/shoppingcart/animal/' + animal[self.key_type] + '.jpg'

                if not animal[self.key_type]:
                    animal[self.key_type] = 'Unknown'

                if not animal[self.key_predator_list]:
                    animal[self.key_predator_list] = 'None'

                if not animal[self.key_prey_list]:
                    animal[self.key_prey_list] = 'None'

                category = animal['category']

                if category not in self.categoryList:
                    self.categoryList.append(category)
                    self.categoryMap[category] = {}
                    self.categoryMenu.setItem(category)

                    if len(self.categoryList) == 1:
                        self.categoryMenu.selectOptionByIndex(0)

                itemButton = self.createItem(animal)

                shopMode = self.categoryList.index(category)

                speciesList = self.categoryMap.get(category)
                speciesList[animal[self.key_type]] = itemButton

                if not initial:
                    self.createNewItemLabel(itemButton)

                    if shopMode != self.shopMode:
                        self.createNewOptionLabel(shopMode)

                    if shopMode == self.shopMode:
                        self.itemList.append(itemButton)
                        self.updateScrollBar()

                        self.categoryMenu.startMainLabelGlow()
                    else:
                        self.categoryMenu.startMainButtonGlow()
                else:
                    if shopMode == self.shopMode:
                        self.itemList.append(itemButton)
                        self.updateScrollBar()

                self.animals[animal[self.key_type]] = animal

    def createNewItemLabel(self, itemButton):

        newItemLabel = DirectBasicLabel( text = 'New',
                                         text_scale = 0.045,
                                         text_pos = (0.002, -0.02),
                                         text_fg = Constants.TEXT_COLOR,
                                         text_font = Constants.FONT_TYPE_01,
                                         text_shadow = Constants.TEXT_SHADOW_COLOR,
                                         frameColor = (0, 0, 0, 0),
                                         pos = (-0.055, 0, 0.05) )
        newItemLabel.reparentTo(itemButton)
        newItemLabel.setR(-45)

        newSequence = Sequence( LerpColorScaleInterval(newItemLabel, 1.5, Constants.TEXT_TYPE_LEVEL_UP, Constants.TEXT_COLOR),
                                LerpColorScaleInterval(newItemLabel, 1.5, Constants.TEXT_COLOR, Constants.TEXT_TYPE_LEVEL_UP) )
        newSequence.loop()

        self.newItems.append((newItemLabel, newSequence))

    def createNewOptionLabel(self, index):

        if index not in self.newOptionLabels:
            optionLabel = self.categoryMenu.getOptionLabel(index)

            newLabel = DirectLabel( text = 'New',
                                    text_fg = Constants.TEXT_COLOR,
                                    text_font = Constants.FONT_TYPE_01,
                                    text_scale = 0.035,
                                    text_shadow = Constants.TEXT_SHADOW_COLOR,
                                    frameColor = (0, 0, 0, 0),
                                    pos = (0.19, 0, 0.005))
            newLabel.reparentTo(optionLabel)

            self.newOptionLabels[index] = newLabel

            self.categoryMenu.startOptionGlow(index)

    def clearNewItems(self):

        for tuple in self.newItems:
            tuple[0].destroy()
            tuple[1].clearToInitial()

        del self.newItems[:]

        for index, label in self.newOptionLabels.items():
            label.destroy()

            self.categoryMenu.stopMainLabelGlow()
            self.categoryMenu.stopMainButtonGlow()
            self.categoryMenu.stopOptionGlow(index)

        self.newOptionLabels.clear()

    def loadPlantItemInfo(self, args):
        """
        Load animal des, cost etc. from server
        """
        self.debugPrint( 'receive plant item info from server')

        plants = args['items']
        initial = args['initial']

        for plant in plants:    
            if plant[self.key_type] not in self.plants:
                plant[self.key_image] = 'models/shoppingcart/plant/' + plant[self.key_type] + '.jpg'

                if not plant[self.key_predator_list]:
                    plant[self.key_predator_list] = 'None'

                plant[self.key_prey_list] = 'None'

                category = plant['category']

                if category not in self.categoryList:
                    self.categoryList.append(category)
                    self.categoryMap[category] = {}
                    self.categoryMenu.setItem(category)

                    if len(self.categoryList) == 1:
                        self.categoryMenu.selectOptionByIndex(0)

                itemButton = self.createItem(plant)

                shopMode = self.categoryList.index(category)

                speciesList = self.categoryMap.get(category)
                speciesList[plant[self.key_type]] = itemButton

                if not initial:
                    self.createNewItemLabel(itemButton)

                    if shopMode != self.shopMode:
                        self.createNewOptionLabel(shopMode)

                    if shopMode == self.shopMode:
                        self.itemList.append(itemButton)
                        self.updateScrollBar()

                        self.categoryMenu.startMainLabelGlow()
                    else:
                        self.categoryMenu.startMainButtonGlow()
                else:
                    if shopMode == self.shopMode:
                        self.itemList.append(itemButton)
                        self.updateScrollBar()

                self.plants[plant[self.key_type]] = plant

    def createMainFrame(self):
        
        self.mainFrame = DirectWindow( frameSize = (-0.73, 0.73, -0.24, 0.24),
                                       frameColor = (0, 0, 0, 0.2),
                                       pos = (-0.42, 0, -0.63) )
        self.mainFrame.reparentTo(self.parent)

    def createButtons(self):

        self.categoryMenu = DirectDropDownMenu( frameColor = (0, 0, 0, 0.2),
                                                width = 0.5,
                                                max_items = 10,
                                                direction = 'up',
                                                command = self.switchCategory )
        self.categoryMenu.reparentTo(self.mainFrame)

        self.categoryMenu.setPos(-0.48, 0, 0.194)

    def createScrollBar(self):
        
        self.scrollBar = DirectSlider( pos = (0, 0, -0.2),
                                       range = (0, 1),
                                       scrollSize = 1,
                                       frameSize = (-0.68, 0.68, -0.01, 0.01),
                                       thumb_frameSize = (-0.015, 0.015, -0.015, 0.015),
                                       thumb_relief = DGG.FLAT,
                                       command = self.scrollList )
        self.scrollBar.reparentTo(self.mainFrame) 
        self.scrollBar.hide()

    def scrollList(self):

#        if len(self.itemList) > self.maxItemsVisible:
            sliderValue = int(self.scrollBar['value'])

            for i in range(len(self.itemList)):
                item = self.itemList[i]
                item.setX(-0.56 + (i - sliderValue) * 0.28)

                if i < sliderValue or i >= sliderValue + self.maxItemsVisible:
                    item.hide()
                else:
                    item.show()

    def updateScrollBar(self):

        if len(self.itemList) > self.maxItemsVisible:
            self.scrollBar.show()

            percent = min(1.0, float(self.maxItemsVisible) / len(self.itemList))
            self.scrollBar['thumb_frameSize'] = (self.scrollBar['frameSize'][0] * percent,
                                                 self.scrollBar['frameSize'][1] * percent,
                                                 self.scrollBar['thumb_frameSize'][2],
                                                 self.scrollBar['thumb_frameSize'][3])
        else:
            self.scrollBar.hide()

        self.scrollBar['range'] = (0, max(1, len(self.itemList) - self.maxItemsVisible))
        self.scrollBar['value'] = self.scrollBar['value']

    def createItem(self, args):

        organism_type = None
        type_id = 0
        if 'animalTypeID' in args:
            organism_type = 'animal'
            type_id = args['animalTypeID']
        else:
            organism_type = 'plant'
            type_id = args['plantTypeID']

        itemButton = DirectBasicButton( text = args[self.key_cost],
                                        text_scale = 0.05,
                                        text_pos = (0.05, -0.08),
                                        image_pos = (0, 0, 0),
                                        text_fg = Constants.TEXT_COLOR,
                                        text_font = Constants.FONT_TYPE_01,
                                        text_shadow = Constants.TEXT_SHADOW_COLOR,
                                        image = args[self.key_image],
                                        image_scale = (0.1, 0.1, 0.1),
                                        frameSize = (-0.12, 0.12, -0.12, 0.12),
                                        frameColor = (0, 0, 0, 0),
                                        pos = (-0.56, 0, 0.02),
                                        command = self.buyItem,
                                        extraArgs = [organism_type, type_id, args['model_id'], args[self.key_image]] )
        itemButton.setTransparency(TransparencyAttrib.MAlpha)
        itemButton.reparentTo(self.mainFrame)
        itemButton.hide()

        itemButton.setOnMouseOver(self.showDescriptionFrame)
        itemButton.setOnMouseOverExtraArgs([args[self.key_type],
                                            args[str(self.key_cost)], 
                                            args[self.key_image],
                                            args[self.key_description],
                                            args[self.key_prey_list],
                                            args[self.key_predator_list],
                                            args[self.key_biomass]])
        itemButton.setOnMouseOut(self.hideDescriptionFrame)

        name = args[self.key_type]

        if len(name) < 9:
            text = name
        else:
            text = name[:8] + '...'

        itemLabel = DirectBasicLabel( text = text,
                                      text_scale = 0.04,
                                      text_pos = (0, -0.015),
                                      text_fg = Constants.TEXT_COLOR,
                                      text_font = Constants.FONT_TYPE_01,
                                      text_shadow = Constants.TEXT_SHADOW_COLOR,
                                      frameSize = (-0.135, 0.135, -0.03, 0.03),
                                      frameColor = (0, 0, 0, 0),
                                      pos = (0, 0, -0.15),
                                      state = DGG.NORMAL,
                                      onMouseOverGlow = False,
                                      onMouseOver = self.showFullText,
                                      onMouseOut = self.hideFullText )
        itemLabel.reparentTo(itemButton)

        itemLabel.setTag('name', name)
        itemLabel.setTag('text', text)

        itemLabel.setOnMouseOverExtraArgs([itemLabel])
        itemLabel.setOnMouseOutExtraArgs([itemLabel])

        return itemButton

    def showFullText(self, label):

        label['text'] = label.getNetTag('name')
        label['text_pos'] = (0, 0)

    def hideFullText(self, label):

        label['text'] = label.getNetTag('text')
        label['text_pos'] = (0, -0.015)

    def setFocus(self, mode):
        """ Change color when click on one of the buttons """
        _frameColor = (0.5,0.5,0.5,0.7)
        for i in range(5):
            if i == mode:
                self.shopButtons[i]['frameColor']=_frameColor
            else:
                self.shopButtons[i]['frameColor']=Constants.BG_COLOR
                
    def switchCategory(self, mode):

        for itemButton in self.itemList:
            itemButton.hide()

        del self.itemList[:]

        speciesList = self.categoryMap.get(self.categoryList[mode])

        for key in sorted(speciesList.keys()):
            self.itemList.append(speciesList[key])

        self.updateScrollBar()

        if mode != self.shopMode:
            self.scrollBar['value'] = 0

        if self.shopMode in self.newOptionLabels:
            self.categoryMenu.stopOptionGlow(self.shopMode)

            newLabel = self.newOptionLabels.pop(self.shopMode)
            newLabel.destroy()

        if mode in self.newOptionLabels:
            self.categoryMenu.startMainLabelGlow()
            self.categoryMenu.stopOptionGlow(mode)

            newLabel = self.newOptionLabels.pop(mode)
            newLabel.destroy()
        else:
            self.categoryMenu.stopMainLabelGlow()

        if len(self.newOptionLabels) == 0:
            self.categoryMenu.stopMainButtonGlow()

        self.shopMode = mode

    def createDescriptionFrame(self):
        
        self.bgFrame = DirectWindow(frameSize=(-0.9, 1.3, -0.75, 0.5),
                                      frameColor=Constants.BG_COLOR,
                                      pos=(0, 0, 0.15))
        self.bgFrame.reparentTo(self.parent)
        self.bgFrame.hide()
        
        self.descriptionFrame = DirectWindow(frameSize=(self.bgFrame['frameSize'][0]+0.01, 
                                                        self.bgFrame['frameSize'][1]-0.01, 
                                                        self.bgFrame['frameSize'][2]+0.01, 
                                                        self.bgFrame['frameSize'][3]-0.01),
                                             frameColor=(0,0,0,0.3),
                                             pos=(0, 0, 0))
        self.descriptionFrame.reparentTo(self.bgFrame)
#        self.hideButton = DirectBasicButton(text=" - ",
#                                       text_fg=(1, 1, 1, 1),
#                                       text_pos=(-0.007, -0.015),
#                                       text_scale=0.05,
#                                       frameColor=(0, 0, 0, 0.2),
#                                       frameSize=(-0.04, 0.04, -0.025, 0.025),
#                                       pos=(0.54, 0, 0.36),
#                                       relief=DGG.FLAT,
#                                       command=self.hideDescriptionFrame)
#        self.hideButton.setTransparency(TransparencyAttrib.MAlpha)
#        self.hideButton.reparentTo(self.descriptionFrame)
        
        self.title = DirectLabel(text = 'Item Type',
                                 text_align = TextNode.ALeft,
                                 text_scale=0.08,
                                 text_pos=(0, -0.025),
                                 text_fg = Constants.TEXT_COLOR,
                                 text_font = Constants.FONT_TYPE_01,
                                 text_shadow = Constants.TEXT_SHADOW_COLOR,
                                 frameSize=(-0.1, 0.1, -0.04, 0.04),
                                 pos=(-0.83, 0, 0.4),
                                 frameColor=(0, 0, 0, 0))
        self.title.reparentTo(self.descriptionFrame)
        
        self.objImage = DirectLabel(image_pos=(0,0,0),
                                    image_scale=(0.1,0.1,0.1),
                                 frameSize=(-0.2, 0.2, -0.04, 0.04),
                                 pos=(-0.68, 0, 0.2),
                                 frameColor=(0, 0, 0, 0))
        self.objImage.setTransparency(TransparencyAttrib.MAlpha)
        self.objImage.reparentTo(self.descriptionFrame)
        
        self.itemDesc = DirectLabel( text = '',
                                     text_scale = 0.045,
                                     text_pos = (0, -0.025),
                                     text_fg = Constants.TEXT_COLOR,
                                     text_font = Constants.FONT_TYPE_01,
                                     text_align = TextNode.ALeft,
                                     text_wordwrap = 43,
                                     text_shadow = Constants.TEXT_SHADOW_COLOR,
                                     frameSize = (-0.4, 0.4, -0.04, 0.04),
                                     pos = (-0.83, 0, 0),
                                     frameColor = (0, 0, 0, 0) )
        self.itemDesc.reparentTo(self.descriptionFrame)

        self.desc = DirectLabel(text = '',
                                 text_scale=0.045,
                                 text_pos=(0, -0.025),
                                 text_fg = Constants.TEXT_COLOR,
                                 text_font = Constants.FONT_TYPE_01,
                                 text_align=TextNode.ALeft,
                                 text_wordwrap = 33,
                                 text_shadow = Constants.TEXT_SHADOW_COLOR,
                                 frameSize=(-0.1, 0.1, -0.04, 0.04),
                                 pos=(-0.49, 0, 0.3),
                                 frameColor=(0, 0, 0, 0))
        self.desc.reparentTo(self.descriptionFrame)
        
        self.cost = DirectLabel(text = '',
                                text_align = TextNode.ARight,
                                 text_scale=0.06,
                                 text_pos=(0, -0.025),
                                 text_fg = Constants.TEXT_COLOR,
                                 text_font = Constants.FONT_TYPE_01,
                                 text_wordwrap = 15,
                                 text_shadow = Constants.TEXT_SHADOW_COLOR,
                                 frameSize=(-0.1, 0.1, -0.04, 0.04),
                                 pos=(1.21, 0, 0.4),
                                 frameColor=(0, 0, 0, 0))
        self.cost.reparentTo(self.descriptionFrame)

    def showDescriptionFrame(self, itemType, cost, image, description, preyList, predatorList,biomass):

        predatorListF = predatorList

        if predatorListF != 'None':
            pList = sorted(predatorListF.split(', '))
            eList = self.animals.keys()
            nList = ''
            for item in pList:
                if item in eList:
                    nList += '\1white\1' + item
                else:
                    nList += '\1gray\1\1shadow_off\1' + item + '\2\2'

                if pList.index(item) < len(pList) - 1:
                    nList += '\1white\1, '

            predatorListF = str(nList).strip('[]').replace('\'', '').replace('\"', '')

        preyListF = preyList

        if preyListF != 'None':
            pList = sorted(preyListF.split(', '))

            if 'Acacia' in self.plants or 'Big Tree' in self.plants or 'Boabab' in self.plants:
                xList = ['Trees and Shrubs', 'Plant Juices', 'Fruits and Nectar', 'Grains and Seeds']
            else:
                xList = []

            eList = self.animals.keys() + self.plants.keys() + xList
            nList = ''
            for item in pList:
                if item in eList:
                    nList += '\1white\1' + item + '\2'
                else:
                    nList += '\1gray\1\1shadow_off\1' + item + '\2\2'

                if pList.index(item) < len(pList) - 1:
                    nList += '\1white\1, '

            preyListF = str(nList).strip('[]').replace('\'', '').replace('\"', '')

        self.bgFrame.show()

        self.objImage['image'] = image
        self.objImage['image_scale'] = (0.1, 0.1, 0.1)

        self.title['text'] = itemType + ' \1scale_05\1' + 'Biomass - ' + str(biomass)
        self.cost['text'] = str(cost) + ' G'
        self.desc['text'] = description

        if self.categoryList[self.shopMode] != 'Plant':
            self.itemDesc['text'] = 'PREYS: '+ preyListF + '\n\n' + 'PREDATORS: '+ predatorListF        
        else:
            if itemType == 'Grass and Herbs':
                self.itemDesc['text'] = 'PREDATOR LIST: ' + predatorListF
            else:
                if itemType == 'Acacia':
                    self.itemDesc['text'] = '22% Plant Juices\n22% Fruits and Nectar\n22% Grains and Seeds\n33% Trees and Shrub'
                elif itemType == 'Big Tree':
                    self.itemDesc['text'] = '33% Plant Juices\n8% Fruits and Nectar\n25% Grains and Seeds\n33% Trees and Shrub'
                elif itemType == 'Boabab':
                    self.itemDesc['text'] = '23% Plant Juices\n23% Fruits and Nectar\n23% Grains and Seeds\n30% Trees and Shrub'

                self.itemDesc['text'] += '\n\n'
                self.itemDesc['text'] += 'PREDATOR LIST: ' + 'Plant Juices Eater, Fruits and Nectar Eater, Grains and Seeds Eater, Trees and Shrub Eater'

    def hideDescriptionFrame(self):
        self.bgFrame.hide()
        
    def hide(self):
        self.mainFrame.hide()
    
    def show(self):
        self.mainFrame.show()

    def buyItem(self, group_type, type_id, model_id, image = None):
        if Constants.DEBUG:
            print 'Buy Item: ',group_type, type_id, model_id
        game.mPicker.createObject(group_type, type_id, model_id, image)

    def loadResearchItems(self):
        imageDirectory = "models/weathers"
        _reaserchType = ["Weather1",
                       "Weather2",
                       "Weather3",
                       "Weather4",
                       "Weather5",
                       "Weather6",
                       "Weather7",
                       "Weather8"]
        _costs=[100, 300, 20, 50, 40, 60, 70, 80]
        _images=[imageDirectory+'/Ice.png',
                 imageDirectory+'/Night_Rain.png',
                 imageDirectory+'/Moon_Phase_Full.png',
                 imageDirectory+'/Sunny.png',
                 imageDirectory+'/Pollen_Flower.png',
                 imageDirectory+'/Rainbow.png',
                 imageDirectory+'/Snow_Occasional.png',
                 imageDirectory+'/Sleet.png']
        _desc = ['Ice',
                 'Night_Rain',
                 'Moon_Phase_Full',
                 'Sunny',
                 'Pollen_Flower',
                 'Rainbow',
                 'Snow_Occasional',
                 'Sleet']
        _effect=['18', '28', '38', '48', '58', '68', '78', '88']
        _prey_list=['', '', '', '','','','','']
        _predator_list=['', '', '', '','','','','']
        for i in range(8):
            self.researches.append({self.key_type: _reaserchType[i],
                                    self.key_cost: str(_costs[i]), 
                            self.key_image: _images[i], 
                            self.key_prey_list: _prey_list[i],
                            self.key_predator_list:_predator_list[i],
                            self.key_description:_desc[i],
                            self.key_effect: 'Effect: '+_effect[i]})  
        
    def loadVaccineItems(self):
        imageDirectory = "models/weathers"
        _vaccineType = ["animal1",
                       "animal2",
                       "animal3",
                       "animal4",
                       "animal5",
                       "animal6",
                       "animal7",
                       "animal8"]
        _costs=['$100', '$300', '$20', '$50', '$40', '$60', '&70']
        _images=[imageDirectory+'/Ice.png',
                 imageDirectory+'/Night_Rain.png',
                 imageDirectory+'/Moon_Phase_Full.png',
                 imageDirectory+'/Sunny.png',
                 imageDirectory+'/Pollen_Flower.png',
                 imageDirectory+'/Rainbow.png',
                 imageDirectory+'/Sleet.png']
        _desc = ['some description of the purchasable item should go here',
                 'some description of the purchasable item should go here',
                 'some description of the purchasable item should go here',
                 'some description of the purchasable item should go here',
                 'some description of the purchasable item should go here',
                 'some description of the purchasable item should go here',
                 'some description of the purchasable item should go here']
        _effect=['18', '28', '38', '48', '68', '78', '88']
        _prey_list=['', '', '', '','','','']
        _predator_list=['', '', '','','','','']
        for i in range(7):
            self.vaccine.append({self.key_type: _vaccineType[i],
                                 self.key_cost: _costs[i], 
                                 self.key_image: _images[i], 
                                 self.key_prey_list: _prey_list[i],
                                 self.key_predator_list:_predator_list[i],
                                 self.key_description:_desc[i],
                                 self.key_effect:'Effect: '+_effect[i]})  

    def unload(self):
        self.mainFrame.destroy()
