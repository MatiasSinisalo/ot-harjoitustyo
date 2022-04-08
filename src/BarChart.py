import tkinter as tk
import matplotlib

matplotlib.use('TkAgg')

#help from https://www.pythontutorial.net/tkinter/tkinter-matplotlib/ 
#for creating bar charts and integrating them to tkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg
)

class barChart:
    def __init__(self, title, xTitle, yTitle, xValues, yValues, sizeX, sizeY, dotsPerInch):
        self.title = title
        self.xTitle = xTitle
        self.yTitle = yTitle
        self.xValues = xValues
        self.yValues = yValues
        self.figure = Figure((sizeX, sizeY), dotsPerInch)
        
        self.axes = self.figure.add_subplot()
        self.axes.bar(self.xValues, self.yValues)
        
        self.axes.set_title(self.title)
        self.axes.set_ylabel(self.yTitle)
        self.axes.set_xlabel(self.xTitle)
    
    def getChart(self, app):
        return FigureCanvasTkAgg(self.figure)

   