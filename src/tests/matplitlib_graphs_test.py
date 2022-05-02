
import unittest
from graphs.matplotlib_graphs import ChartManager
from tkinter import *
from custom_event import Event

class Test_matplitlib_graphs(unittest.TestCase):
    def setUp(self) -> None:
       
        root = Tk()
        root.option_add('*tearOff', FALSE)
        root.title("Taulukkolaskentasovellus")
        root.geometry("500x500")
        self.canvas = Canvas(root)
        self.chartManager = ChartManager(self.canvas)
        self.canvas.grid(column = 0, row=0)
        
       
      
    def test_bar_chart_is_created(self):
        #test if the chartmanager has created an bar chart canvas object
        barChart = self.chartManager.add_new_bar_chart("test", "x_title", "y_title", [1,2,3], [10,20,30], 6, 4, 100, 100, 100)
        barChartWindow =  self.chartManager.get_chart_widget_canvas_item(barChart)
        self.assertEqual(barChart.widgetName, "chartWidget")
    
    def test_bar_chart_is_created(self):
        #test if the chartmanager has created an bar pie canvas object
        pieChart = self.chartManager.add_new_pie_chart("test", "x_title", "y_title", [1,2,3], [10,20,30], 6, 4, 100, 100, 100) 
        self.assertEqual(pieChart.widgetName, "chartWidget")
    
    def test_bar_chart_can_be_moved(self):
        #First drag event sets the start coord of the drag, but doesnt move it
        barChart = self.chartManager.add_new_bar_chart("test", "x_title", "y_title", [1,2,3], [10,20,30], 6, 4, 100, 100, 100)
        barChartWindow =  self.chartManager.get_chart_widget_canvas_item(barChart)
        dragevent = Event(0, 0)
        dragevent.widget = barChart
        dragevent.state = 256
        self.chartManager.on_chart_drag(dragevent)
        self.assertEqual(self.canvas.coords(barChartWindow)[0], 100.0)
        self.assertEqual(self.canvas.coords(barChartWindow)[1], 100.0)

        #second event moves the chart
        dragevent.x = 100
        dragevent.y = 100
        self.chartManager.on_chart_drag(dragevent)
        self.assertEqual(self.canvas.coords(barChartWindow)[0], 200.0)
        self.assertEqual(self.canvas.coords(barChartWindow)[1], 200.0)
    
    def test_pie_chart_can_be_moved(self):
        #First drag event sets the start coord of the drag, but doesnt move it
        pieChart = self.chartManager.add_new_pie_chart("test", "x_title", "y_title", [1,2,3], [10,20,30], 6, 4, 100, 100, 100)
        pieChartWindow =  self.chartManager.get_chart_widget_canvas_item(pieChart)
        dragevent = Event(0, 0)
        dragevent.widget = pieChart
        dragevent.state = 256
        self.chartManager.on_chart_drag(dragevent)
        self.assertEqual(self.canvas.coords(pieChartWindow)[0], 100.0)
        self.assertEqual(self.canvas.coords(pieChartWindow)[1], 100.0)

        #second event moves the chart
        dragevent.x = 100
        dragevent.y = 100
        self.chartManager.on_chart_drag(dragevent)
        self.assertEqual(self.canvas.coords(pieChartWindow)[0], 200.0)
        self.assertEqual(self.canvas.coords(pieChartWindow)[1], 200.0)
