

from tkinter import END, LEFT, NORMAL, NW, Text


class GridDisplay:
    """Class responsible for drawing a spreadsheet. Manages the editing and selection of grid cells"""
    def __init__(self, canvas, grid_width, grid_height, cell_width,
                 cell_height, display_text_offset_x,
                 display_text_offset_y, font_size, max_letters_in_cell):

        self.canvas = canvas
        self.cell_grid_values = {}
        self.cell_grid_number_by_text_id = {}
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.cell_width = cell_width
        self.cell_height = cell_height

        self.display_text_offset_x = display_text_offset_x
        self.display_text_offset_y = display_text_offset_y
        self.previes_text_width = font_size

        self.font_size = font_size
        self.max_letters_in_cell = max_letters_in_cell

        self.drag_selected_values = {}
        self.drag_start = None
        self.drag_end = None
        cell_number = 0
        for column in range(grid_width):
            for row in range(grid_height):
                cell_number += 1
                if column == 0 and row == 0:
                    cell_value = ""
                    fill_color = "lightgray"
                elif column == 0:
                    cell_value = f"R: {row}"
                    fill_color = "lightgray"
                elif row == 0:
                    cell_value = f"C: {column}"
                    fill_color = "lightgray"
                else:
                    cell_value = cell_number
                    fill_color = "white"
                    
                self.canvas.create_rectangle(column*self.cell_width, row * cell_height,
                                             column*self.cell_width + self.cell_width,
                                             row*self.cell_height+self.cell_height,
                                             tags=("clickable"), fill=fill_color)
                new_cell_display_text_id = self.canvas.create_text(column*self.cell_width + self.display_text_offset_x,
                                                                   row*self.cell_height +  self.display_text_offset_y,
                                                                   text=cell_value, anchor=NW,
                                                                   justify=LEFT,
                                                                   width=self.cell_width-5,
                                                                   font=str(self.font_size))
                self.cell_grid_values[cell_number] = cell_value
                self.cell_grid_number_by_text_id[new_cell_display_text_id] = cell_number

        # textCanvasWidget is the id of the Text widget that spawns when a rectanlge is clicked
        self.text_canvas_widget = None

        # textCanvasIten is the id of the texCanvasWidget window inside the canvas
        self.text_canvas_item = None

        # displayTextId is the raw text shown when a rectangle is not clicked
        self.display_text_id = None
       

    def edit_cell(self, event):
        """Function to edit a single cell inside a grid based on a Tkinter mouse click event"""
        virtual_coords = self.clip_to_grid(self.canvas.canvasx(
            event.x), self.canvas.canvasy(event.y))
        if virtual_coords[0] != 0 and virtual_coords[1] != 0:

            self.cancel_cell_edit()

            display_text_box_id = self.canvas.find_closest(
                virtual_coords[0], virtual_coords[1])
           
            self.display_text_id = display_text_box_id[0]+1
            grid_cell_number = self.cell_grid_number_by_text_id[self.display_text_id]
            text_of_display_box = self.cell_grid_values[grid_cell_number]
           
            self.text_canvas_widget = Text(
                self.canvas, state=NORMAL, font=str(self.font_size))
           
            self.text_canvas_widget.insert("1.0", text_of_display_box)
            self.text_canvas_widget.lower()
            self.text_canvas_widget.focus_set()
           
            self.text_canvas_item = self.canvas.create_window(
                virtual_coords[0], virtual_coords[1],
                width=self.cell_width, height=self.cell_height,
                anchor=NW, window=self.text_canvas_widget)
        return self.text_canvas_widget

    def cancel_cell_edit(self):
        """Cancels the current editing of a cell"""
        if self.display_text_id is not None and self.text_canvas_widget is not None and self.cell_grid_values is not None:
            new_text = self.text_canvas_widget.get("1.0", END)
          
            self.canvas.itemconfig(
                self.display_text_id, text=self.generate_preview_text(new_text))
            grid_cell_number = self.cell_grid_number_by_text_id[self.display_text_id]
            self.cell_grid_values[grid_cell_number] = new_text
          
            self.canvas.delete(self.text_canvas_item)
            self.text_canvas_item = None

    def deselect(self):
        """Deselects the correct selection of cells"""
        if len(self.drag_selected_values) > 0:
            for val in self.drag_selected_values.keys():
                self.canvas.itemconfig(val-1, fill="white")
            self.drag_selected_values = {}

    def reset_drag(self):
        """resets the drag start and end points. used to select cells when dragging and pressing SHIFT"""
        self.drag_start = None
        self.drag_end = None
        self.deselect()

    def select(self, x_val, y_val, fillcolor):
        """Function to select cells. Currently called from spread_sheet_app when pressing SHIFT and dragging the mouse. 
        Puts the values of selected cells inside self.drag_selected_values.
        
            Args: 
                    x_val, y_val: the x and y values of the mouse
                    
                    fillcolor: color for highlighting the drag selected cells
        
        """
        virtual_coords = self.clip_to_grid(
            self.canvas.canvasx(x_val), self.canvas.canvasy(y_val))
        if virtual_coords[0] != 0 and virtual_coords[1] != 0:

            if self.drag_start is None:
                self.drag_start = virtual_coords
                self.drag_end = virtual_coords
            else:
                self.deselect()
                self.drag_end = virtual_coords

            # process the different ways a drag end position will influence the positions of the selection box topleft and bottomright corner
            if self.drag_start[0] < self.drag_end[0] and self.drag_start[1] < self.drag_end[1]:
                left_corner_x = self.drag_start[0]
                left_corner_y = self.drag_start[1]

                right_corner_x = self.drag_end[0]
                right_corner_y = self.drag_end[1]
            elif self.drag_start[0] > self.drag_end[0] and self.drag_start[1] > self.drag_end[1]:
                left_corner_x = self.drag_end[0]
                left_corner_y = self.drag_end[1]

                right_corner_x = self.drag_start[0]
                right_corner_y = self.drag_start[1]

            elif self.drag_start[0] < self.drag_end[0] and self.drag_start[1] > self.drag_end[1]:
                left_corner_x = self.drag_start[0]
                left_corner_y = self.drag_end[1]

                right_corner_x = self.drag_end[0]
                right_corner_y = self.drag_start[1]

            elif self.drag_start[0] > self.drag_end[0] and self.drag_start[1] < self.drag_end[1]:
                left_corner_x = self.drag_end[0]
                left_corner_y = self.drag_start[1]

                right_corner_x = self.drag_start[0]
                right_corner_y = self.drag_end[1]
            else:
                # this handles the situation where dragstart and dragend are on the same cell
                left_corner_x = self.drag_start[0]
                left_corner_y = self.drag_start[1]

                right_corner_x = self.drag_end[0]
                right_corner_y = self.drag_end[1]

            traveller_x = left_corner_x
            traveller_y = left_corner_y
            while traveller_y <= right_corner_y:
                while traveller_x <= right_corner_x:
                    cell_box_id = self.canvas.find_closest(
                        traveller_x, traveller_y)
                    self.canvas.itemconfig(cell_box_id, fill=fillcolor)
                    grid_cell_number = self.cell_grid_number_by_text_id[cell_box_id[0]+1]
                    self.drag_selected_values[cell_box_id[0]+1] = self.cell_grid_values[grid_cell_number]
                    traveller_x += self.cell_width

                traveller_y += self.cell_height
                traveller_x = left_corner_x
    
            
    def get_sum_of_selection(self):
        """Calculates the sum of currently selected values inside self.drag_selected_values
        
            Returns:
                    sum_of_selection: sum of currently selected values
        
        """
        answerString = ""
        sum_of_selection = 0
        for val in self.drag_selected_values.values():
            try:
                sum_of_selection += float(val)
            except:
                answerString = f"Arvoa ei voitu k????nt???? luvuksi: '{val}'"
                return answerString
                break
        return sum_of_selection

    def get_average_of_selection(self):
        """Calculates the average of currently selected values inside self.drag_selected_values
        
             Returns: average of currently selected values
                    

        """
        sum_of_selection = self.get_sum_of_selection()
        if isinstance(sum_of_selection, str):
            return sum_of_selection
        else:
            return sum_of_selection / len(self.drag_selected_values)
        
    def generate_preview_text(self, text):
        """Function to generate preview text that displays when cell is not edited
        
            Args:
                 text: string
            
            Returns: String that has been shortened to the lenght of self.max_letters_in_cell
                     
        
        """
        return text.replace("\n", "")[:self.max_letters_in_cell]

    def clip_to_grid(self, firstx, firsty):
        """returns the left corner coordinates of a cell given x and y

            Args:
                    firstx, firsty: x and y coordinates
            
            Returns: Tuple of (x, y) that is the top left corner of a cell
        """
        x_pos = firstx - firstx % self.cell_width
        y_pos = firsty - firsty % self.cell_height
        return (x_pos, y_pos)

    def updateViewText(self):
        """Updates the cell text that is displayed when a cell is not edited."""
        for key in self.cell_grid_number_by_text_id:
            grid_cell_number = self.cell_grid_number_by_text_id[key]
            self.canvas.itemconfig(
               key, text=self.generate_preview_text(str(self.cell_grid_values[grid_cell_number])))
    
    def handle_clicks(self, event):
            """Function to respond to click events sent from spread sheet app
            
                Args: 
                        event: Tkinter event
                        
            """
            self.reset_drag()
            self.cancel_cell_edit()
            if event.state != 1:
                self.edit_cell(event)
            elif event.state == 1:
                self.select(event.x, event.y, "lightblue")
      
    def handle_movement(self, event):
        """Function to respond to click events sent from spread sheet app
        
            Args: 
                    event: Tkinter event
        """
        if event.state == 257:
            self.select(event.x, event.y, "lightblue")
    
    

