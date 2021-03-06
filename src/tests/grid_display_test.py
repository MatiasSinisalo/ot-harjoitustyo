
import unittest
from grid_display import GridDisplay
from tkinter import *
from tests.custom_event import Event


class Testgrid_display(unittest.TestCase):
    def setUp(self) -> None:
        root = Tk()
        root.option_add('*tearOff', FALSE)
        root.title("Taulukkolaskentasovellus")
        root.geometry("500x500")
        root.configure(background='SteelBlue1')

        menubar = Menu(root)
        root['menu'] = menubar
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        gridWidth = 100
        gridHeight = 100
       
        cellWidth = 200
        cellHeight = 50
       
        cellDisplayTextOffsetpxX = 1
        cellDisplayTextOffsetpxY = 3
        fontsize = 12
        maxLettersInCell = 20
        gridCanvas = Canvas(root, bg="white", height=250, width=300)
        gridCanvas.grid(column=0, row=0, sticky=W+E+S+N)
        self.spreadSheetView = GridDisplay(gridCanvas, gridWidth, gridHeight, cellWidth, cellHeight,
                                           cellDisplayTextOffsetpxX, cellDisplayTextOffsetpxY, fontsize, maxLettersInCell)
        self.clickEvent = Event(200, 50)

    def test_clickRegistersOnCorrectTile(self):
        widget = self.spreadSheetView.edit_cell(self.clickEvent)
        TextOfWidget = widget.get("1.0", END)
        self.assertEqual(TextOfWidget.replace("\n", ""), "102")

        self.clickEvent.x = 400
        widget = self.spreadSheetView.edit_cell(self.clickEvent)
        TextOfWidget = widget.get("1.0", END)
        self.assertEqual(TextOfWidget.replace("\n", ""), "202")

        self.clickEvent.y = 100
        widget = self.spreadSheetView.edit_cell(self.clickEvent)
        TextOfWidget = widget.get("1.0", END)
        self.assertEqual(TextOfWidget.replace("\n", ""), "203")

        self.clickEvent.x = 370
        self.clickEvent.y = 70
        widget = self.spreadSheetView.edit_cell(self.clickEvent)
        TextOfWidget = widget.get("1.0", END)
        self.assertEqual(TextOfWidget.replace("\n", ""), "102")

        

    def test_clickAwayCreatesNewInputField(self):
        FirstWidget = self.spreadSheetView.edit_cell(self.clickEvent)
        self.clickEvent.x = 200
        SecondWidget = self.spreadSheetView.edit_cell(self.clickEvent)
        self.assertNotEqual(FirstWidget, SecondWidget)

    def test_gridValueUpdatesCorrectly(self):
        widget = self.spreadSheetView.edit_cell(self.clickEvent)
        widget.insert("1.0", "hello")

        # click away
        self.clickEvent.x = 400
        otherwidget = self.spreadSheetView.edit_cell(self.clickEvent)
        otherwidget.insert("1.0", "SecondHello")

        # click back
        self.clickEvent.x = 200
        BackTowidget = self.spreadSheetView.edit_cell(self.clickEvent)
        # check that the first widget has been updated
        TextOfWidget = BackTowidget.get("1.0", END)
        self.assertEqual(TextOfWidget.replace("\n", ""), "hello102")

        # test that the second has been updated
        self.clickEvent.x = 400
        BackToSecondWidget = self.spreadSheetView.edit_cell(self.clickEvent)
        TextOfSecondWidget = BackToSecondWidget.get("1.0", END)
        self.assertEqual(TextOfSecondWidget.replace(
            "\n", ""), "SecondHello202")
    
    def test_SumOfSelectedValuesIsCorrect(self):
        self.spreadSheetView.drag_selected_values = {"1":"1", "2":"2", "3":"3"}
        answer = self.spreadSheetView.get_sum_of_selection()
        self.assertEqual(answer, 6.0)
    
    def test_SumOfSelectedValuesGivesCorrectError(self):
        self.spreadSheetView.drag_selected_values = {"1":"1", "2":"hello", "3":"3"}
        answer = self.spreadSheetView.get_sum_of_selection()
        self.assertEqual(answer, "Arvoa ei voitu k????nt???? luvuksi: 'hello'")
    

    def test_AverageOfSelectedValuesIsCorrect(self):
        self.spreadSheetView.drag_selected_values = {"1":"1", "2":"2", "3":"3"}
        answer = self.spreadSheetView.get_average_of_selection()
        self.assertEqual(answer, (1+2+3)/ 3)
    
    def test_AverageOfSelectedValuesGivesCorrectError(self):
        self.spreadSheetView.drag_selected_values = {"1":"1", "2":"hello", "3":"3"}
        answer = self.spreadSheetView.get_average_of_selection()
        self.assertEqual(answer, "Arvoa ei voitu k????nt???? luvuksi: 'hello'")

    def test_DragSelectsCorrectValues(self):
        self.spreadSheetView.select(200, 50, "white")
        self.assertEqual(self.spreadSheetView.drag_selected_values, {204:102})
        self.spreadSheetView.deselect()
        self.assertEqual(self.spreadSheetView.drag_selected_values, {})
        self.spreadSheetView.select(200, 50, "white")
        self.spreadSheetView.select(200, 100, "white")
        self.assertEqual(self.spreadSheetView.drag_selected_values, {204:102, 206:103})
        self.spreadSheetView.deselect()
