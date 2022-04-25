from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg
)
from matplotlib.figure import Figure
import matplotlib

matplotlib.use('TkAgg')



#help from matplotlib documentation for creating a pie chart
#https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html
class PieChart:
    def __init__(self, title, x_title, y_title, x_values, y_values, size_x, size_y, dots_per_inch):
        self.title = title
        self.x_title = x_title
        self. y_title = y_title
        self.x_values = x_values
        self.y_values = y_values
        self.figure = Figure((size_x, size_y), dots_per_inch)

        self.axes = self.figure.add_subplot()
        self.axes.pie(self.y_values, labels=self.x_values)
        self.axes.axis("equal")
        self.axes.set_title(self.title)
        self.axes.set_ylabel(self.y_title)
        self.axes.set_xlabel(self.x_title)

    def get_chart(self, parent):
        return FigureCanvasTkAgg(self.figure, parent)
