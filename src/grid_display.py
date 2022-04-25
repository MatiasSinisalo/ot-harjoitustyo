

from tkinter import END, LEFT, NORMAL, NW, Text


class GridDisplay:
    def __init__(self, canvas, grid_width, grid_height, cell_width,
                 cell_height, display_text_offset_x,
                 display_text_offset_y, font_size, max_letters_in_cell):

        self.canvas = canvas
        self.cell_grid_values = {}

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
                    cell_value = f"{cell_number}"
                    fill_color = "white"
                    cell_number += 1
                self.canvas.create_rectangle(column*self.cell_width, row*cell_height,
                                             column*self.cell_width + self.cell_width,
                                             row*self.cell_height+self.cell_height,
                                             tags=("clickable"), fill=fill_color)
                new_cell_display_text_id = self.canvas.create_text(column*self.cell_width +
                                                                   self.display_text_offset_x,
                                                                   row*self.cell_height +
                                                                   self.display_text_offset_y,
                                                                   text=cell_value, anchor=NW,
                                                                   justify=LEFT,
                                                                   width=self.cell_width-5,
                                                                   font=str(self.font_size))
                self.cell_grid_values[new_cell_display_text_id] = cell_value

        # textCanvasWidget is the id of the Text widget that spawns when a rectanlge is clicked
        self.text_canvas_widget = None

        # textCanvasIten is the id of the texCanvasWidget window inside the canvas
        self.text_canvas_item = None

        # displayTextId is the raw text shown when a rectangle is not clicked
        self.display_text_id = None

    def edit_cell(self, event):
        virtual_coords = self.clip_to_grid(self.canvas.canvasx(
            event.x), self.canvas.canvasy(event.y))
        if virtual_coords[0] != 0 and virtual_coords[1] != 0:

            self.cancel_cell_edit()

            display_text_box_id = self.canvas.find_closest(
                virtual_coords[0], virtual_coords[1])
           
            self.display_text_id = display_text_box_id[0]+1
            text_of_display_box = self.cell_grid_values[self.display_text_id]
           
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
        if self.display_text_id is not None and self.text_canvas_widget is not None and self.cell_grid_values is not None:
            new_text = self.text_canvas_widget.get("1.0", END)
          
            self.canvas.itemconfig(
                self.display_text_id, text=self.generate_preview_text(new_text))
          
            self.cell_grid_values[self.display_text_id] = new_text
          
            self.canvas.delete(self.text_canvas_item)
            self.text_canvas_item = None

    def deselect(self):
        if len(self.drag_selected_values) > 0:
            for val in self.drag_selected_values.keys():
                self.canvas.itemconfig(val-1, fill="white")
            self.drag_selected_values = {}

    def reset_drag(self):
        self.drag_start = None
        self.drag_end = None
        self.deselect()

    def select(self, x_val, y_val, fillcolor):
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
                    self.drag_selected_values[cell_box_id[0]+1] = self.cell_grid_values[cell_box_id[0]+1]
                    traveller_x += self.cell_width

                traveller_y += self.cell_height
                traveller_x = left_corner_x
            
            
    def GetSumOfSelection(self):
        answerString = ""
        sum = 0
        for val in self.drag_selected_values.values():
            try:
                sum += float(val)
            except:
                answerString = f"Arvoa ei voitu kääntää luvuksi: '{val}'"
                return answerString
                break
        answerString = str(sum)
        return answerString

    def generate_preview_text(self, text):
        return text.replace("\n", "")[:self.max_letters_in_cell]

    def clip_to_grid(self, firstx, firsty):
        x_pos = firstx - firstx % self.cell_width
        y_pos = firsty - firsty % self.cell_height
        return (x_pos, y_pos)
