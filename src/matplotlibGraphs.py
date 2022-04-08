import tkinter as tk
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
       
    
    def addNewBarChart(self, title, xTitle, yTitle, xValues, yValues, sizeX, sizeY, dotsPerInch):
        newChart = barChart(title, xTitle, yTitle, xValues, yValues, sizeX, sizeY, dotsPerInch)
        ChartWidget = newChart.getChart(self.parent)
        return ChartWidget
    
    
    







        


