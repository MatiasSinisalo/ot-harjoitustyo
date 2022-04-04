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
                placeholder = f"{column}|{row}"
                newCell = self.canvas.create_rectangle(column*self.cellWidth, row*cellHeight, column*self.cellWidth+self.cellWidth, row*self.cellHeight+self.cellHeight, tags=("clickable"))        
                newCellDisplayTextId = self.canvas.create_text(column*self.cellWidth+self.displayTextOffsetX, row*self.cellHeight+self.disPlayTextOffSetY, text=placeholder, anchor=NW, justify=LEFT, width=self.cellWidth-5, font=str(self.fontSize))
                self.cellGridValues[newCellDisplayTextId] = placeholder

        #textCanvasWidget is the id of the Text widget that spawns when a rectanlge is clicked
        self.TextCanvasWidget = None
        
        #textCanvasIten is the id of the texCanvasWidget window inside the canvas
        self.TextCanvasItem = None
        
        #displayTextId is the raw text shown when a rectangle is not clicked
        self.DisplayTextId = None
   
    def onClick(self, event):
        virtualCoords = self.clipToGrid(self.canvas.canvasx(event.x), self.canvas.canvasy(event.y))
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

        
