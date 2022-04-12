
import unittest
from grid_display import GridDisplay
from tkinter import *
from custom_event import Event


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
        self.clickEvent = Event(0, 0)

    def test_clickRegistersOnCorrectTile(self):
        widget = Text()
        widget = self.spreadSheetView.edit_cell(self.clickEvent)
        TextOfWidget = widget.get("1.0", END)
        self.assertEqual(TextOfWidget.replace("\n", ""), "0")

        self.clickEvent.x_val = 199
        widget = self.spreadSheetView.edit_cell(self.clickEvent)
        TextOfWidget = widget.get("1.0", END)
        self.assertEqual(TextOfWidget.replace("\n", ""), "0")

        self.clickEvent.y_val = 49
        widget = self.spreadSheetView.edit_cell(self.clickEvent)
        TextOfWidget = widget.get("1.0", END)
        self.assertEqual(TextOfWidget.replace("\n", ""), "0")

        self.clickEvent.x_val = 200
        self.clickEvent.y_val = 0
        widget = self.spreadSheetView.edit_cell(self.clickEvent)
        TextOfWidget = widget.get("1.0", END)
        self.assertEqual(TextOfWidget.replace("\n", ""), "1")

        self.clickEvent.x_val = 200
        self.clickEvent.y_val = 50
        widget = self.spreadSheetView.edit_cell(self.clickEvent)
        TextOfWidget = widget.get("1.0", END)
        self.assertEqual(TextOfWidget.replace("\n", ""), "2")

    def test_clickAwayCreatesNewInputField(self):
        FirstWidget = self.spreadSheetView.edit_cell(self.clickEvent)
        self.clickEvent.x_val = 200
        SecondWidget = self.spreadSheetView.edit_cell(self.clickEvent)
        self.assertNotEqual(FirstWidget, SecondWidget)

    def test_gridValueUpdatesCorrectly(self):
        widget = self.spreadSheetView.edit_cell(self.clickEvent)
        widget.insert("1.0", "hello")

        # click away
        self.clickEvent.x_val = 200
        otherwidget = self.spreadSheetView.edit_cell(self.clickEvent)
        otherwidget.insert("1.0", "SecondHello")

        # click back
        self.clickEvent.x_val = 0
        BackTowidget = self.spreadSheetView.edit_cell(self.clickEvent)
        # check that the first widget has been updated
        TextOfWidget = BackTowidget.get("1.0", END)
        self.assertEqual(TextOfWidget.replace("\n", ""), "hello0|0")

        # test that the second has been updated
        self.clickEvent.x_val = 200
        BackToSecondWidget = self.spreadSheetView.edit_cell(self.clickEvent)
        TextOfSecondWidget = BackToSecondWidget.get("1.0", END)
        self.assertEqual(TextOfSecondWidget.replace(
            "\n", ""), "SecondHello1|0")
