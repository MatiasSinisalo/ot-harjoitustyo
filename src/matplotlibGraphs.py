
import tkinter as tk
from turtle import width
import matplotlib
from BarChart import barChart
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg
)


from BarChart import barChart

class chartManager:
    def __init__(self, parent):
       self.parent = parent
       self.CanvasItems = {}
    def addNewBarChart(self, title, xTitle, yTitle, xValues, yValues, sizeX, sizeY, dotsPerInch, xpos, ypos):
        newChart = barChart(title, xTitle, yTitle, xValues, yValues, sizeX, sizeY, dotsPerInch)
        ChartMatPlotItem = newChart.getChart(self.parent)
        ChartWidget = ChartMatPlotItem.get_tk_widget()
        ChartWidget.config(highlightcolor="lightblue", highlightthickness=3)
        ChartWidget.widgetName = "chartWidget"
        ChartWidget.bind("<Motion>", lambda event: self.onChartDrag(event))
        ChartWidget.bind("<Delete>", lambda event: self.deleteChart(event))
        ChartWidgetWindowid = self.parent.create_window(xpos, ypos, window=ChartWidget)
     
        self.CanvasItems[ChartWidget] = (ChartWidgetWindowid, ChartMatPlotItem)
        return ChartWidget

    def onChartDrag(self, event):
        if event.state == 256:
            self.parent.move(self.CanvasItems[event.widget][0], event.x, event.y)
            self.CanvasItems[event.widget][1].draw_idle()
            self.parent.update_idletasks()
    def updateAllCharts(self):
        for val in self.CanvasItems.values():
            val[1].draw_idle()
        return 0

    def deleteChart(self, event):
        self.parent.delete(self.CanvasItems[event.widget][0])
        self.CanvasItems.pop(event.widget)

           
         
   
    
    
    







        


