

from tkinter import Frame
import matplotlib
from matplotlib.widgets import Widget
from graphs.bar_chart import BarChart
from graphs.pie_chart import PieChart

matplotlib.use('TkAgg')


class ChartManager:
    """Class responsible for managing the charts created by matplotlib libary"""
    def __init__(self, parent):
        """Inits the dictionaries canvas_items and chartInformation for keeping track of existing charts
        
            Args:
                  parent: a canvas tkinter widget
        """
        self.parent = parent
        self.canvas_items = {}
        self.chartInformation = {}

    def add_new_bar_chart(self, title, x_title, y_title, x_values, y_values,
                          size_x, size_y, dots_per_inch, xpos, ypos):
        """Creates a new matplotlib bar chart"""
        new_chart = BarChart(title, x_title, y_title, x_values,
                             y_values, size_x, size_y, dots_per_inch)
        
        return self.display_chart(title, x_title, y_title, x_values, y_values,
                          size_x, size_y, dots_per_inch, xpos, ypos, new_chart, "Bar")
    
    

    def add_new_pie_chart(self, title, x_title, y_title, x_values, y_values,
                          size_x, size_y, dots_per_inch, xpos, ypos):
        """Creates a new matplotlib pie chart"""
       
        new_chart = PieChart(title, x_title, y_title, x_values,
                             y_values, size_x, size_y, dots_per_inch)

        return self.display_chart(title, x_title, y_title, x_values, y_values,
                          size_x, size_y, dots_per_inch, xpos, ypos, new_chart, "Pie")


        

    def display_chart(self, title, x_title, y_title, x_values, y_values,
                          size_x, size_y, dots_per_inch, xpos, ypos, new_chart, chartType):
        """Helper function responsible for creating the tkinter widget and tkinter chart window for displaying the chart for the user.
        """
        chartContainer = Frame(self.parent)

        chart_matplot_item = new_chart.get_chart(chartContainer)
        chart_widget = chart_matplot_item.get_tk_widget()
        chart_widget.config(highlightcolor="lightblue", highlightthickness=3)
        chart_widget.widgetName = "chartWidget"
        chart_widget.bind("<Motion>", self.on_chart_drag)
        chart_widget.bind("<Delete>", self.delete_chart)
        chart_widget.bind("<1>", self.on_click)
        chart_widget.grid(column=0, row=0)
       
        new_chart_id = len(self.chartInformation)
        chart_widget_windowid = self.parent.create_window(
            xpos, ypos, window=chartContainer, tags=f"{new_chart_id}")
        
        
        self.chartInformation[new_chart_id] = {"type":chartType, "title":title,  "x_title":x_title, "y_title":y_title, 
                                                "x_values":x_values, "y_values":y_values,
                                                "size_x":size_x, "size_y":size_y, 
                                                "dots":dots_per_inch, "coords":self.parent.coords(chart_widget_windowid)}
        
        
        self.canvas_items[chart_widget] = (
            chart_widget_windowid, chart_matplot_item, new_chart_id)
        return chart_widget
        
        
    def get_chart_widget_canvas_item(self, widget_id):
        """Helper function to get the tkinter chart window id"""
        return self.canvas_items[widget_id][0]

    def on_click(self, event):
        """Function to handle click events sent by tkinter"""
        event.widget.focus_set()
        event.widget.master.lift()
        
    def on_chart_drag(self, event):
        """Function to move the chart when it is dragged"""
        if event.state == 256:
            
            canvasItem = self.canvas_items[event.widget][0]
            chartId = self.canvas_items[event.widget][2]

            self.parent.move(
                canvasItem, event.x, event.y)
            self.parent.update_idletasks()
            self.update_all_charts()
            self.chartInformation[chartId]["coords"] = self.parent.coords(canvasItem)
            

    def update_all_charts(self):
        """Updates every chart widget. Used to make dragging the charts less choppy"""
        for val in self.canvas_items.values():
            val[1].draw_idle()
        return 0

    def delete_chart(self, event):
        """Removes a chart stored inside the class based on tkinter event"""
        self.parent.delete(self.canvas_items[event.widget][0])
        chart_id_to_delete = self.canvas_items.pop(event.widget)[2]
        self.chartInformation.pop(chart_id_to_delete)
    

    def delete_all_charts(self):
        for key in self.canvas_items:
            self.parent.delete(self.canvas_items[key][0])
        self.canvas_items = {}
        self.chartInformation = {}
        


        
