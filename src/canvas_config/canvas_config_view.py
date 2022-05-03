from tkinter import N,W,S,E, Button, Entry, Frame, Label

from canvas_config.canvas_config_calculations import CanvasCalculationsView
from canvas_config.canvas_config_view_chart_creator import CanvasChartCreatorView


class CanvasConfigView:
    """Class for managing the functions of the right config bar of the application"""
    def __init__(self, root, app) -> None:
        """Creates the chart creator view and calculations view"""
        self.root = root
        self.app = app
        canvas_configurer_view = Frame(self.root, width=300, bg="white")
        canvas_configurer_view.grid(column=2, row=0, sticky=N+W+S+E)
        self.canvasChartCreatorView = CanvasChartCreatorView(canvas_configurer_view, self.app)
        self.calculationView = CanvasCalculationsView(canvas_configurer_view, self.app)
        