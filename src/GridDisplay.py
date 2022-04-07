from tkinter import *
class gridDisplay:
    def __init__(self, canvas, gridWidth, gridHeight, cellWidth, cellHeight, displayTextOffsetX, disPlayTextOffSetY, fontSize, maxLettersInCell):
       
        self.canvas = canvas
        self.cellGridValues = {}
       
        self.gridWidth = gridWidth
        self.gridHeight = gridHeight
        self.cellWidth = cellWidth
        self.cellHeight = cellHeight
       
        self.displayTextOffsetX = displayTextOffsetX
        self.disPlayTextOffSetY = disPlayTextOffSetY
        self.previewTextFontWidth  = fontSize 
       
        self.fontSize = fontSize
        self.maxLettersInCell = maxLettersInCell

        for column in range(gridWidth):
            for row in range(gridHeight):
                if column == 0 and row == 0:
                    cellValue = ""
                    fillColor = "lightgray"
                elif column == 0:
                    cellValue = f"R: {row}"
                    fillColor = "lightgray"
                elif row == 0:
                     cellValue = f"C: {column}"
                     fillColor = "lightgray"
                else:
                     cellValue = ""
                     fillColor = "white"
                newCell = self.canvas.create_rectangle(column*self.cellWidth, row*cellHeight, column*self.cellWidth+self.cellWidth, row*self.cellHeight+self.cellHeight, tags=("clickable"), fill = fillColor)        
                newCellDisplayTextId = self.canvas.create_text(column*self.cellWidth+self.displayTextOffsetX, row*self.cellHeight+self.disPlayTextOffSetY, text=cellValue, anchor=NW, justify=LEFT, width=self.cellWidth-5, font=str(self.fontSize))
                self.cellGridValues[newCellDisplayTextId] = cellValue

        #textCanvasWidget is the id of the Text widget that spawns when a rectanlge is clicked
        self.TextCanvasWidget = None
        
        #textCanvasIten is the id of the texCanvasWidget window inside the canvas
        self.TextCanvasItem = None
        
        #displayTextId is the raw text shown when a rectangle is not clicked
        self.DisplayTextId = None
   
    def onClick(self, event):
        virtualCoords = self.clipToGrid(self.canvas.canvasx(event.x), self.canvas.canvasy(event.y))
        if virtualCoords[0] != 0 and virtualCoords[1] != 0: 
            if self.DisplayTextId != None and self.TextCanvasWidget != None and self.cellGridValues != None:
                newText = self.TextCanvasWidget.get("1.0", END)
                self.canvas.itemconfig(self.DisplayTextId, text=self.generatePreviewText(newText))
                self.cellGridValues[self.DisplayTextId] = newText
                self.canvas.delete(self.TextCanvasItem)
                self.TextCanvasItem = None
            displayTextBoxId = self.canvas.find_closest(virtualCoords[0], virtualCoords[1])
            self.DisplayTextId = displayTextBoxId[0]+1
            textOfDisplayBox = self.cellGridValues[self.DisplayTextId]
            self.TextCanvasWidget = Text(self.canvas, state=NORMAL, font=str(self.fontSize))
            self.TextCanvasWidget.insert("1.0", textOfDisplayBox)
        
            self.TextCanvasWidget.focus_set()
            self.TextCanvasItem = self.canvas.create_window(virtualCoords[0], virtualCoords[1],width=self.cellWidth, height=self.cellHeight, anchor=NW, window=self.TextCanvasWidget)
            return self.TextCanvasWidget   
  
    def generatePreviewText(self, text):
        return text.replace("\n", "")[:self.maxLettersInCell]

    def clipToGrid(self, firstx, firsty):
        x = firstx - firstx % self.cellWidth
        y = firsty - firsty  % self.cellHeight
        return (x, y)

        
