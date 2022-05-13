
import unittest
import json
from spread_sheet_app import SpreadSheetApp
from tests.custom_event import Event
class TestSpreadSheetApp(unittest.TestCase):
    def setUp(self):
        self.app = SpreadSheetApp()
        self.app.init_front_end()
        self.file = open("test.json", "a+")
        self.file.close()
    
    def test_app_inits_correctly(self):
        self.assertIsNot(self.app.spread_sheet_view, None)
        self.assertIsNot(self.app.canvas_chart_manager, None)
    
    def test_app_saves_cells_correctly(self):
        self.file = open("test.json", "w")
        self.app.saveStateToFile(self.file)
        
        file = open("test.json")

        data = json.load(file)
        cellValues = data["cell_values"]
        self.assertEqual(cellValues["102"], 102)
        file.close()
        
    
    def test_app_saves_edited_cells_correctly(self):
        self.file = open("test.json", "w")
        self.app.spread_sheet_view.cell_grid_values[102] = "This is a test"
        self.app.saveStateToFile(self.file)
      
        file = open("test.json")
        data = json.load(file)
        cellValues = data["cell_values"]
        self.assertEqual(cellValues["102"], "This is a test")
        self.app.spread_sheet_view.cell_grid_values[1] = 0
        file.close()
        
        
    
    def test_app_saves_bar_chart_correctly(self):
        newChart = self.app.canvas_chart_manager.add_new_bar_chart("test", "x_title", "y_title", [1,2,3], [10,20,30], 6, 4, 100, 100, 100)
        removeEvent = Event(100.0, 100.0)
        removeEvent.widget = newChart
        self.file = open("test.json", "w")
        self.app.saveStateToFile(self.file)
        
        file = open("test.json")
        data = json.load(file)
        charts = data["chart_values"]
        chart_values = charts["0"]
        self.assertEqual(chart_values["type"], "Bar")
        self.assertEqual(chart_values["title"], "test")
        self.assertEqual(chart_values["x_title"], "x_title")
        self.assertEqual(chart_values["y_title"], "y_title")
        self.assertEqual(chart_values["x_values"], [1, 2, 3])
        self.assertEqual(chart_values["y_values"], [10, 20, 30])
        self.assertEqual(chart_values["dots"], 100)
        self.assertEqual(chart_values["coords"], [100.0, 100.0])
        self.app.canvas_chart_manager.delete_chart(removeEvent)
        file.close()
        
    
    def test_app_saves_pie_chart_correctly(self):
        newChart = self.app.canvas_chart_manager.add_new_pie_chart("test", "x_title", "y_title", [1,2,3], [10,20,30], 6, 4, 100, 100, 100)
        removeEvent = Event(100.0, 100.0)
        removeEvent.widget = newChart
        self.file = open("test.json", "w")
        self.app.saveStateToFile(self.file)
        
        file = open("test.json")
        data = json.load(file)
        charts = data["chart_values"]
        chart_values = charts["0"]
        self.assertEqual(chart_values["type"], "Pie")
        self.assertEqual(chart_values["title"], "test")
        self.assertEqual(chart_values["x_title"], "x_title")
        self.assertEqual(chart_values["y_title"], "y_title")
        self.assertEqual(chart_values["x_values"], [1, 2, 3])
        self.assertEqual(chart_values["y_values"], [10, 20, 30])
        self.assertEqual(chart_values["dots"], 100)
        self.assertEqual(chart_values["coords"], [100.0, 100.0])
        self.app.canvas_chart_manager.delete_chart(removeEvent)
        file.close()
        
           
      


       


        
