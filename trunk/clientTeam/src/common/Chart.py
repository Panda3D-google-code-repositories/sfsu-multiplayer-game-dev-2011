from math import ceil
from random import uniform

from direct.gui.DirectFrame import DirectFrame
from direct.gui.DirectGui import DGG
from direct.gui.DirectSlider import DirectSlider

from panda3d.core import AntialiasAttrib
from panda3d.core import LineSegs
from panda3d.core import TextNode
from panda3d.core import TransparencyAttrib

from common.Constants import Constants
from common.DirectBasicButton import DirectBasicButton
from common.DirectBasicLabel import DirectBasicLabel
from common.DirectBasicWindow import DirectBasicWindow

class Chart:

    def __init__(self, parent):

        self.parent = parent.mainFrame

        self.csvList = {}
        self.lineList = {}
        self.colorList = {}
        self.hideList = []

        self.itemList = []

        self.maxItemsVisible = 10

        self.xStart = -0.55
        self.xEnd = 0.55
        self.yStart = -0.35
        self.yEnd = 0.35

        self.xAxisLength = self.xEnd - self.xStart
        self.yAxisLength = self.yEnd - self.yStart

        self.xUnitLength = 0
        self.yUnitLength = 0

        self.xRange = (0, 1)

        self.createChartFrame()
        self.createChart()
        self.createVertexTextBox()
        self.createScrollBar()

    def createChartFrame(self):

        self.chartFrame = DirectFrame(frameSize = (-1.05, 1.05, -0.55, 0.55),
                                      frameColor = (0, 0, 0, 0.2),
                                      pos = (0, 0, 0))

    def setPos(self, x, y, z):
        self.chartFrame.setPos(x, y, z)

    def reparentTo(self, parent):
        self.chartFrame.reparentTo(parent)

    def createChart(self):

        self.chartNode = self.chartFrame.attachNewNode('ChartNode')
        self.chartNode.setPos(-0.25, 0, 0.05)

        self.chartAxis = LineSegs()
        self.chartAxis.setColor((0.8, 0.8, 0.8, 1))
        self.chartAxis.setThickness(2)
        self.chartAxis.moveTo((self.xStart - 0.015, 0, self.yStart))
        self.chartAxis.drawTo((self.xEnd, 0, self.yStart))

        self.chartAxis.moveTo((self.xStart, 0, self.yStart - 0.015))
        self.chartAxis.drawTo((self.xStart, 0, self.yEnd))

        self.chartNode.attachNewNode(self.chartAxis.create())

        self.xAxisLabel = DirectBasicLabel( text = 'Month',
                                            text_fg = Constants.TEXT_COLOR,
                                            text_font = Constants.FONT_TYPE_01,
                                            text_scale = 0.045,
                                            text_shadow = Constants.TEXT_SHADOW_COLOR,
                                            frameColor = (0, 0, 0, 0),
                                            pos = (0, 0, -0.55) )
        self.xAxisLabel.reparentTo(self.chartNode)

        self.yAxisLabel = DirectBasicLabel( text = 'Biomass',
                                            text_fg = Constants.TEXT_COLOR,
                                            text_font = Constants.FONT_TYPE_01,
                                            text_scale = 0.045,
                                            text_shadow = Constants.TEXT_SHADOW_COLOR,
                                            frameColor = (0, 0, 0, 0),
                                            pos = (-0.73, 0, 0) )
        self.yAxisLabel.reparentTo(self.chartNode)
        self.yAxisLabel.setR(-90)

        self.chartSubNode = self.chartNode.attachNewNode('ChartSubNode')

    def setAxisLabels(self, x, y):
        self.xAxisLabel['text'] = x
        self.yAxisLabel['text'] = y

    def createVertexTextBox(self):

        self.vertexTextBox = DirectFrame( frameColor = Constants.BG_COLOR,
                                          pos = (0, 0, 0) )
        self.vertexTextBox.reparentTo(self.chartNode, 10)
        self.vertexTextBox.hide()

        self.vertexText = DirectBasicLabel( text = '',
                                            text_fg = Constants.TEXT_COLOR,
                                            text_font = Constants.FONT_TYPE_01,
                                            text_pos = (0, 0.01),
                                            text_scale = 0.04,
                                            frameColor = (0, 0, 0, 0.3),
                                            pos = (0, 0, 0) )
        self.vertexText.reparentTo(self.vertexTextBox)

        self.vertexTextNode = TextNode('vertexTextNode')

    def showVertexTextBox(self, node):

        name = node.getNetTag('name')
        value = node.getNetTag('value')

        text = name + '\n' + value

        self.vertexText['text'] = text

        self.vertexTextNode.setText(text)
        buttonWidth = 0.025 * self.vertexTextNode.getWidth()

        self.vertexTextBox['frameSize'] = (-buttonWidth - 0.006, buttonWidth + 0.006, -0.066, 0.066)
        self.vertexText['frameSize'] = (-buttonWidth, buttonWidth, -0.06, 0.06)

        self.vertexTextBox.setPos(node.getX(), 0, node.getZ() + 0.09)
        self.vertexTextBox.show()

    def createScrollBar(self):
        
        self.scrollBar = DirectSlider( pos = (0.9, 0, 0.05),
                                       range = (1, 0),
                                       scrollSize = 1,
                                       orientation = DGG.VERTICAL,
                                       frameSize = (-0.01, 0.01, -0.35, 0.35),
                                       thumb_frameSize = (-0.015, 0.015, -0.015, 0.015),
                                       thumb_relief = DGG.FLAT,
                                       command = self.scrollList )
        self.scrollBar.reparentTo(self.chartFrame) 
        self.scrollBar.hide()

        self.buttonFrame = DirectFrame( frameSize = (-0.166, 0.166, -0.046, 0.046),
                                        frameColor = Constants.BG_COLOR,
                                        pos = (0.65, 0, -0.375),
                                        state = DGG.NORMAL )
        self.buttonFrame.reparentTo(self.chartFrame)

        self.toggleButton = DirectBasicButton( text = 'Hide All',
                                               text_fg = Constants.TEXT_COLOR,
                                               text_font = Constants.FONT_TYPE_01,
                                               text_pos = (0, -0.015),
                                               text_scale = 0.045,
                                               text_shadow = Constants.TEXT_SHADOW_COLOR,
                                               frameSize = (-0.16, 0.16, -0.04, 0.04),
                                               frameColor = (0, 0, 0, 0.2),
                                               pos = (0, 0, 0),
                                               relief = DGG.FLAT,
                                               command = self.toggleLines )
        self.toggleButton.reparentTo(self.buttonFrame)

    def scrollList(self):

        if len(self.itemList) > self.maxItemsVisible:
            sliderValue = int(self.scrollBar['value'])

            for i in range(len(self.itemList)):
                item = self.itemList[i]
                item.setZ(0.364 - (i - sliderValue) * 0.07)

                if i < sliderValue or i >= sliderValue + self.maxItemsVisible:
                    item.hide()
                else:
                    item.show()

    def updateScrollBar(self):

        if len(self.itemList) > self.maxItemsVisible:
            self.scrollBar.show()

            percent = min(1.0, float(self.maxItemsVisible) / len(self.itemList))
            self.scrollBar['thumb_frameSize'] = (self.scrollBar['thumb_frameSize'][0],
                                                 self.scrollBar['thumb_frameSize'][1],
                                                 self.scrollBar['frameSize'][2] * percent,
                                                 self.scrollBar['frameSize'][3] * percent)
        else:
            self.scrollBar.hide()

        self.scrollBar['range'] = (max(1, len(self.itemList) - self.maxItemsVisible), 0)

    def createItem(self, name, color):

        if len(name) < 10:
            text = name
        else:
            text = name[:10] + '...'

        itemLabel = DirectBasicLabel( text = text,
                                      text_align = TextNode.ALeft,
                                      text_fg = Constants.TEXT_COLOR,
                                      text_font = Constants.FONT_TYPE_01,
                                      text_pos = (-0.10, -0.015),
                                      text_scale = 0.045,
                                      text_shadow = Constants.TEXT_SHADOW_COLOR,
                                      frameSize = (-0.2, 0.2, -0.035, 0.035),
                                      frameColor = (0, 0, 0, 0),
                                      pos = (0.65, 0, 0.364 - len(self.itemList) * 0.07),
                                      state = DGG.NORMAL,
                                      onMouseOver = self.focusLine,
                                      onMouseOverExtraArgs = [0, name],
                                      onMouseOut = self.focusLine,
                                      onMouseOutExtraArgs = [1, name] )
        itemLabel.reparentTo(self.chartFrame)
        itemLabel.bind(DGG.B1PRESS, self.toggleLine, [itemLabel])

        itemLabel.setTag('name', name)
        itemLabel.setTag('status', 'On')

        self.itemList.append(itemLabel)

        colorBox = DirectFrame(frameSize = (-0.03, 0.03, -0.015, 0.015),
                               frameColor = color,
                               pos = (-0.15, 0, 0))
        colorBox.reparentTo(itemLabel)

        self.updateScrollBar()

    def toggleLine(self, label, param = None):

        self.clearGraphContent()

        name = label.getNetTag('name')

        if label.getNetTag('status') == 'Off':
            if name in self.hideList:
                self.hideList.remove(name)
                label.setTag('status', 'On')
            label['text_fg'] = Constants.TEXT_COLOR
        else:
            if name not in self.hideList:
                self.hideList.append(name)
                label.setTag('status', 'Off')
            label['text_fg'] = Constants.TEXT_D_COLOR

        self.refresh()

    def clearGraphContent(self):
        self.chartSubNode.removeNode()
        self.lineList.clear()

    def toggleLines(self):

        self.clearGraphContent()

        for label in self.itemList:
            name = label.getNetTag('name')

            if self.toggleButton['text'] == 'Hide All':
                label['text_fg'] = Constants.TEXT_D_COLOR
                if name not in self.hideList:
                    self.hideList.append(name)
                    label.setTag('status', 'Off')
            elif self.toggleButton['text'] == 'Show All':
                label['text_fg'] = Constants.TEXT_COLOR
                if name in self.hideList:
                    self.hideList.remove(name)
                label.setTag('status', 'On')

        self.refresh()

        if self.toggleButton['text'] == 'Hide All':
            self.toggleButton['text'] = 'Show All'
        elif self.toggleButton['text'] == 'Show All':
            self.toggleButton['text'] = 'Hide All'

    def show(self):
        self.chartFrame.show()

    def hide(self):
        self.chartFrame.hide()

    def toggleVisibility(self):

        if self.chartFrame.isHidden():
            self.chartFrame.show()
        else:
            self.chartFrame.hide()

    def parseCSV(self, data):

        csvList = []

        for set in data.split('\n'):
            set = set.split(',')
            for i in range(len(set)):
                set[i] = set[i].strip('\"')

            csvList.append(set)

        csvList[0][0] = '.xLabels'

        newList = {}

        for i in range(0, len(csvList[0])):
            tempList = []

            for j in range(1, len(csvList)):
                value = csvList[j][i]

                if value != '':
                    if '.' in value:
                        value = float(value)
                    else:
                        value = int(value)
                else:
                    value = -1

                tempList.append(value)

            newList[csvList[0][i]] = tempList

        return newList

    def setInitialChartData(self, data):

        self.chartSubNode.removeNode()
        self.lineList.clear()

#        for label in self.itemList:
#            label.destroy()
#        del self.itemList[:]

        self.csvList = data

        xLength = len(self.csvList.values()[0])
        self.xRange = (max(0, xLength - 10), xLength)
#        self.xRange = (0, xLength)

        self.refresh()

    def setRange(self, min, max):
        self.xRange = (min, max)

    def createAxisLabels(self, xMax, yMax):

        self.chartSubNode = self.chartNode.attachNewNode('ChartSubNode')

        axisUnitBars = LineSegs()
        axisUnitBars.setColor((0.8, 0.8, 0.8, 1))
        axisUnitBars.setThickness(2)

        self.xUnitLength = self.xAxisLength / xMax
        self.yUnitLength = self.yAxisLength / 8.0

        for i in range(1, xMax):
            xPos = self.xStart + i * self.xUnitLength

            axisUnitBars.moveTo((xPos, 0, self.yStart))
            axisUnitBars.drawTo((xPos, 0, self.yStart - 0.015))

        for i in range(1, 9):
            yPos = self.yStart + i * self.yUnitLength

            axisUnitBars.moveTo((self.xStart - 0.015, 0, yPos))
            axisUnitBars.drawTo((self.xStart + self.xAxisLength, 0, yPos))

        self.chartSubNode.attachNewNode(axisUnitBars.create())

        for i in range(0, xMax):
            xPos = self.xStart + i * self.xUnitLength + self.xUnitLength / 2

            xUnitLabel = DirectBasicLabel( text = self.csvList['.xLabels'][self.xRange[0] + i],
                                           text_align = TextNode.ARight,
                                           text_fg = Constants.TEXT_COLOR,
                                           text_font = Constants.FONT_TYPE_01,
                                           text_pos = (-0.001, -0.01),
                                           text_scale = 0.035,
                                           text_shadow = Constants.TEXT_SHADOW_COLOR,
                                           frameColor = (0, 0, 0, 0),
                                           pos = (xPos, 0, self.yStart - 0.04) )
            xUnitLabel.reparentTo(self.chartSubNode)
            xUnitLabel.setR(-45)

        for i in range(0, 9):
            yPos = self.yStart + i * self.yUnitLength

            value = round(yMax / 8.0 * i, 2)

            if '.' not in str(yMax):
                value = int(ceil(value))

            yUnitLabel = DirectBasicLabel( text = str(value),
                                           text_align = TextNode.ARight,
                                           text_fg = Constants.TEXT_COLOR,
                                           text_font = Constants.FONT_TYPE_01,
                                           text_pos = (-0.001, -0.01),
                                           text_scale = 0.035,
                                           text_shadow = Constants.TEXT_SHADOW_COLOR,
                                           frameColor = (0, 0, 0, 0),
                                           pos = (self.xStart - 0.04, 0, yPos) )
            yUnitLabel.reparentTo(self.chartSubNode)

    def refresh(self):

        if len(self.csvList) > 0:
            xMax = self.xRange[1] - self.xRange[0]
            yMax = 0

            for key, set in self.csvList.items():
                if not key.startswith('.') and key not in self.hideList:
                    for i in range(self.xRange[0], self.xRange[1]):
                        yMax = max(set[i], yMax)

#            roundTo = int('5' + '0' * max(0, len(str(int(yMax))) - 2))
#            yMax = int(roundTo * ceil(float(yMax) / roundTo))

            self.createAxisLabels(xMax, yMax)

            for key, set in self.csvList.items():
                if key.startswith('.') or key in self.hideList:
                    continue

                if key not in self.colorList:
                    color = (uniform(0.3, 0.9), uniform(0.3, 0.9), uniform(0.3, 0.9), 1)
                    self.colorList[key] = color
                    self.createItem(key, color)
                else:
                    color = self.colorList[key]

                lastValue = -1

                lineNode = self.chartSubNode.attachNewNode('LineNode')
                lineNode.setAntialias(AntialiasAttrib.MAuto)

                lineSegment = LineSegs()
                lineSegment.setColor(color)
                lineSegment.setThickness(2)

                lineGlow = LineSegs()
                lineGlow.setColor((color[0], color[1], color[2], 0.3))
                lineGlow.setThickness(6)

                vertexList = []
                vertexIndex = 0

                for i in range(xMax):
                    value = set[self.xRange[0] + i]

                    if lastValue == -1 and value != -1:
                        xPos = self.xStart + self.xUnitLength / 2 + i * self.xUnitLength
                        if yMax == 0:
                            operand = 0
                        else:
                            operand = (value / float(yMax))
                        yPos = self.yStart + self.yAxisLength * operand

                        lineSegment.moveTo((xPos, 0, yPos))
                        lineGlow.moveTo((xPos, 0, yPos))

                    lastValue = value

                    if value != -1:
                        xEnd = self.xStart + self.xUnitLength / 2 + i * self.xUnitLength
                        if yMax == 0:
                            operand = 0
                        else:
                            operand = (value / float(yMax))
                        yEnd = self.yStart + self.yAxisLength * operand

                        lineSegment.drawTo((xEnd, 0, yEnd))
                        lineGlow.drawTo((xEnd, 0, yEnd))

                        vertexDot = DirectBasicLabel( text = '',
                                                      text_fg = Constants.TEXT_COLOR,
                                                      text_font = Constants.FONT_TYPE_01,
                                                      text_scale = 0.045,
                                                      image = 'models/dot.png',
                                                      image_scale = 0.015,
                                                      frameColor = (0, 0, 0, 0),
                                                      pos = (xEnd, 0, yEnd),
                                                      state = DGG.NORMAL,
                                                      onMouseOver = self.showData,
                                                      onMouseOverExtraArgs = [0, key, vertexIndex],
                                                      onMouseOut = self.showData,
                                                      onMouseOutExtraArgs = [1, key, vertexIndex] )
                        vertexDot.reparentTo(lineNode, 1)
                        vertexDot.setColorScale(color)
                        vertexDot.setTransparency(TransparencyAttrib.MAlpha)

                        vertexDot.setTag('name', key)
                        vertexDot.setTag('value', str(value))

                        vertexGlow = DirectBasicLabel( text = '',
                                                       text_fg = Constants.TEXT_COLOR,
                                                       text_font = Constants.FONT_TYPE_01,
                                                       text_scale = 0.045,
                                                       image = 'models/dot.png',
                                                       image_scale = 0.025,
                                                       frameColor = (0, 0, 0, 0),
                                                       pos = (xEnd, 0, yEnd) )
                        vertexGlow.reparentTo(lineNode)
                        vertexGlow.setColorScale((color[0], color[1], color[2], 0.3))
                        vertexGlow.setTransparency(TransparencyAttrib.MAlpha)
                        vertexGlow.hide()

                        vertexList.append((vertexDot, vertexGlow))

                        vertexIndex += 1

                lineGlowNode = lineNode.attachNewNode(lineGlow.create())
                lineGlowNode.hide()

                lineSegmentNode = lineNode.attachNewNode(lineSegment.create())

                self.lineList[key] = (lineNode, (lineSegmentNode, lineSegment), (lineGlowNode, lineGlow), vertexList)

    def focusLine(self, type, name):

        if name in self.lineList:
            lineTuple = self.lineList[name]
            node = lineTuple[0]
            glow = lineTuple[2][0]

            if type == 0:
                node.reparentTo(node.getParent(), 1)
                glow.show()

                for vertex in lineTuple[3]:
                    vertex[1].show()
            else:
                glow.hide()

                for vertex in lineTuple[3]:
                    vertex[1].hide()

    def showData(self, type, name, index):

        if name in self.lineList:
            self.focusLine(type, name)

            vertex = self.lineList[name][3][index]
            dot = vertex[0]
            glow = vertex[1]

            if type == 0:
                self.showVertexTextBox(dot)
                glow.show()
            else:
                self.vertexTextBox.hide()
                glow.hide()
