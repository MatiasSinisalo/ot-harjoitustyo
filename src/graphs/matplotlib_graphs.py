

import matplotlib
from graphs.bar_chart import BarChart
from graphs.pie_chart import PieChart

matplotlib.use('TkAgg')


class ChartManager:
    def __init__(self, parent):
        self.parent = parent
        self.canvas_items = {}
        self.chartInformation = {}

    def add_new_bar_chart(self, title, x_title, y_title, x_values, y_values,
                          size_x, size_y, dots_per_inch, xpos, ypos):
      
        new_chart = BarChart(title, x_title, y_title, x_values,
                             y_values, size_x, size_y, dots_per_inch)
        
        return self.display_chart(title, x_title, y_title, x_values, y_values,
                          size_x, size_y, dots_per_inch, xpos, ypos, new_chart, "Bar")
    
    

    def add_new_pie_chart(self, title, x_title, y_title, x_values, y_values,
                          size_x, size_y, dots_per_inch, xpos, ypos):
       
        new_chart = PieChart(title, x_title, y_title, x_values,
                             y_values, size_x, size_y, dots_per_inch)

        return self.display_chart(title, x_title, y_title, x_values, y_values,
                          size_x, size_y, dots_per_inch, xpos, ypos, new_chart, "Pie")


        

    def display_chart(self, title, x_title, y_title, x_values, y_values,
                          size_x, size_y, dots_per_inch, xpos, ypos, new_chart, chartType):
        chart_matplot_item = new_chart.get_chart(self.parent)
        chart_widget = chart_matplot_item.get_tk_widget()
        chart_widget.config(highlightcolor="lightblue", highlightthickness=3)
        chart_widget.widgetName = "chartWidget"
        chart_widget.bind("<Motion>", self.on_chart_drag)
        chart_widget.bind("<Delete>", self.delete_chart)
        chart_widget.bind("<1>", self.on_click)
        chart_widget_windowid = self.parent.create_window(
            xpos, ypos, window=chart_widget)
        
        new_chart_id = len(self.chartInformation)
        self.chartInformation[new_chart_id] = {"type":chartType, "title":title,  "x_title":x_title, "y_title":y_title, 
                                                "x_values":x_values, "y_values":y_values,
                                                "size_x":size_x, "size_y":size_y, 
                                                "dots":dots_per_inch, "coords":self.parent.coords(chart_widget_windowid)}
        
        
        self.canvas_items[chart_widget] = (
            chart_widget_windowid, chart_matplot_item, new_chart_id)
        return chart_widget
        
        
    def get_chart_widget_canvas_item(self, widget_id):
        return self.canvas_items[widget_id][0]

    def on_click(self, event):
        event.widget.focus_set()

    def on_chart_drag(self, event):
        
        if event.state == 256:
            
            canvasItem = self.canvas_items[event.widget][0]
            matplotLibGraph = self.canvas_items[event.widget][1]
            chartId = self.canvas_items[event.widget][2]

            self.parent.move(
                canvasItem, event.x, event.y)
            matplotLibGraph.draw_idle()
            self.parent.update_idletasks()
            self.chartInformation[chartId]["coords"] = self.parent.coords(canvasItem)

    def update_all_charts(self):
        for val in self.canvas_items.values():
            val[1].draw_idle()
        return 0

    def delete_chart(self, event):
        self.parent.delete(self.canvas_items[event.widget][0])
        chart_id_to_delete = self.canvas_items.pop(event.widget)[2]
        self.chartInformation.pop(chart_id_to_delete)

        
