
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
        ChartWidget = newChart.getChart(self.parent)
  
        ChartWidget.bind("<Motion>", lambda event: self.onChartDrag(event))
      #  ChartWidget.place(x = xpos, y = ypos)
        self.CanvasItems[ChartWidget] = self.parent.create_window(xpos, ypos, width=500, height = 500, window=ChartWidget)
        return ChartWidget

    def onChartDrag(self, event):
        if event.state == 256:
            self.parent.move(self.CanvasItems[event.widget], event.x, event.y)
            self.parent.update_idletasks()
           
           
         
   
    
    
    







        


