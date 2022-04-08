
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
        ChartWidget.bind("<Motion>", lambda event: self.onChartDrag(event))
        self.CanvasItems[ChartWidget] = (self.parent.create_window(xpos, ypos, width=500, height = 500, window=ChartWidget), ChartMatPlotItem)
        return ChartWidget

    def onChartDrag(self, event):
        if event.state == 256:
            self.parent.move(self.CanvasItems[event.widget][0], self.parent.canvasx(event.x), self.parent.canvasy(event.y))
            self.CanvasItems[event.widget][1].draw_idle()
           # self.parent.update_idletasks()
    def updateAllCharts(self):
        for val in self.CanvasItems.values():
            val[1].draw_idle()
        return 0

           
           
         
   
    
    
    







        


