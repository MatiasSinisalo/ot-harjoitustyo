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
        
        self.dragSelectedValues = {}
        self.dragStart = None
        self.dragEnd = None
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
   
    def editCell(self, event):
        virtualCoords = self.clipToGrid(self.canvas.canvasx(event.x), self.canvas.canvasy(event.y))
        if virtualCoords[0] != 0 and virtualCoords[1] != 0: 
           
            self.cancelCellEdit()
            
            displayTextBoxId = self.canvas.find_closest(virtualCoords[0], virtualCoords[1])
            self.DisplayTextId = displayTextBoxId[0]+1
            textOfDisplayBox = self.cellGridValues[self.DisplayTextId]
            self.TextCanvasWidget = Text(self.canvas, state=NORMAL, font=str(self.fontSize))
            self.TextCanvasWidget.insert("1.0", textOfDisplayBox)
        
            self.TextCanvasWidget.focus_set()
            self.TextCanvasItem = self.canvas.create_window(virtualCoords[0], virtualCoords[1],width=self.cellWidth, height=self.cellHeight, anchor=NW, window=self.TextCanvasWidget)
            return self.TextCanvasWidget   
    def cancelCellEdit(self):
        if self.DisplayTextId != None and self.TextCanvasWidget != None and self.cellGridValues != None:
            newText = self.TextCanvasWidget.get("1.0", END)
            self.canvas.itemconfig(self.DisplayTextId, text=self.generatePreviewText(newText))
            self.cellGridValues[self.DisplayTextId] = newText
            self.canvas.delete(self.TextCanvasItem)
            self.TextCanvasItem = None
    
    def deselect(self):
        if len(self.dragSelectedValues) > 0:
            for val in self.dragSelectedValues.keys():
                self.canvas.itemconfig(val+1, fill="white")
            self.dragSelectedValues = {}
    
    def resetDrag(self):
        self.dragStart = None
        self.dragEnd = None 
        self.deselect()   
        
        

    def select(self, x, y, fillcolor):
        virtualCoords = self.clipToGrid(self.canvas.canvasx(x), self.canvas.canvasy(y))
        if virtualCoords[0] != 0 and virtualCoords[1] != 0:
            
            if  self.dragStart == None:
                self.dragStart = virtualCoords
                self.dragEnd = virtualCoords
            else:
                self.deselect()
                self.dragEnd = virtualCoords
            
        
            
            #process the different ways a drag end position will influence the positions of the selection box topleft and bottomright corner
            if self.dragStart[0] < self.dragEnd[0] and self.dragStart[1] < self.dragEnd[1]:
                leftCornerX = self.dragStart[0]
                leftCornerY = self.dragStart[1]
              
                rightCornerX = self.dragEnd[0]
                rightCornerY = self.dragEnd[1]
            elif self.dragStart[0] > self.dragEnd[0] and self.dragStart[1] > self.dragEnd[1]:
                leftCornerX = self.dragEnd[0]
                leftCornerY = self.dragEnd[1]
              
                rightCornerX = self.dragStart[0]
                rightCornerY = self.dragStart[1]
               
            elif self.dragStart[0] < self.dragEnd[0] and self.dragStart[1] > self.dragEnd[1]:
                leftCornerX = self.dragStart[0]
                leftCornerY = self.dragEnd[1]
               
                rightCornerX = self.dragEnd[0]
                rightCornerY = self.dragStart[1]
            
            elif self.dragStart[0] > self.dragEnd[0] and self.dragStart[1] < self.dragEnd[1]:
                leftCornerX = self.dragEnd[0]
                leftCornerY = self.dragStart[1]
              
                rightCornerX = self.dragStart[0]
                rightCornerY = self.dragEnd[1]
            else:
                #this handles the situation where dragstart and dragend are on the same cell
                leftCornerX = self.dragStart[0]
                leftCornerY = self.dragStart[1]
               
                rightCornerX = self.dragEnd[0]
                rightCornerY = self.dragEnd[1]
            
            travellerX = leftCornerX
            travellerY = leftCornerY
            while travellerY <=  rightCornerY:
                while travellerX <= rightCornerX:
                    cellBoxID = self.canvas.find_closest(travellerX, travellerY)
                    self.canvas.itemconfig(cellBoxID, fill=fillcolor)
                    self.dragSelectedValues[cellBoxID[0]-1] = True
                    travellerX += self.cellWidth
               
                travellerY += self.cellHeight
                travellerX = leftCornerX
           
         
           
       
   

    def generatePreviewText(self, text):
        return text.replace("\n", "")[:self.maxLettersInCell]

    def clipToGrid(self, firstx, firsty):
        x = firstx - firstx % self.cellWidth
        y = firsty - firsty % self.cellHeight
        return (x, y)

        
