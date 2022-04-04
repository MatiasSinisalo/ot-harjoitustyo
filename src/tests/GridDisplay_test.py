
import unittest
from GridDisplay import gridDisplay
from tkinter import *
from CustomEvent import event
class TestGridDisplay(unittest.TestCase):
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
        self.spreadSheetView = gridDisplay(gridCanvas, gridWidth, gridHeight, cellWidth, cellHeight, cellDisplayTextOffsetpxX, cellDisplayTextOffsetpxY, fontsize, maxLettersInCell)
        self.clickEvent = event(0, 0)
    def test_clickRegistersOnCorrectTile(self):
       
          
            Widget = self.spreadSheetView.onClick(self.clickEvent)
            TextOfWidget = Widget.get("1.0", END)
            self.assertEqual(TextOfWidget.replace("\n", ""), "0|0")

            self.clickEvent.x = 199
            Widget = self.spreadSheetView.onClick(self.clickEvent)
            TextOfWidget = Widget.get("1.0", END)
            self.assertEqual(TextOfWidget.replace("\n", ""), "0|0")

            self.clickEvent.y = 49
            Widget = self.spreadSheetView.onClick(self.clickEvent)
            TextOfWidget = Widget.get("1.0", END)
            self.assertEqual(TextOfWidget.replace("\n", ""), "0|0")

            self.clickEvent.x = 200
            self.clickEvent.y = 0
            Widget = self.spreadSheetView.onClick(self.clickEvent)
            TextOfWidget = Widget.get("1.0", END)
            self.assertEqual(TextOfWidget.replace("\n", ""), "1|0")

            self.clickEvent.x = 200
            self.clickEvent.y = 50
            Widget = self.spreadSheetView.onClick(self.clickEvent)
            TextOfWidget = Widget.get("1.0", END)
            self.assertEqual(TextOfWidget.replace("\n", ""), "1|1")
    
    def test_clickAwayCreatesNewInputField(self):
         FirstWidget = self.spreadSheetView.onClick(self.clickEvent)
         self.clickEvent.x = 200
         SecondWidget = self.spreadSheetView.onClick(self.clickEvent)
         self.assertNotEqual(FirstWidget, SecondWidget)
    
    def test_gridValueUpdatesCorrectly(self):
        widget = self.spreadSheetView.onClick(self.clickEvent)
        widget.insert("1.0", "hello")
        
        #click away
        self.clickEvent.x = 200
        otherwidget = self.spreadSheetView.onClick(self.clickEvent)
        otherwidget.insert("1.0", "SecondHello")

        
        #click back
        self.clickEvent.x = 0
        BackTowidget = self.spreadSheetView.onClick(self.clickEvent)
        #check that the first widget has been updated
        TextOfWidget = BackTowidget.get("1.0", END)
        self.assertEqual(TextOfWidget.replace("\n", ""), "hello0|0")

        #test that the second has been updated
        self.clickEvent.x = 200
        BackToSecondWidget = self.spreadSheetView.onClick(self.clickEvent)
        TextOfSecondWidget = BackToSecondWidget.get("1.0", END)
        self.assertEqual(TextOfSecondWidget.replace("\n", ""), "SecondHello1|0")





    






