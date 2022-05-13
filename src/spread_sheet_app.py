from tkinter import E, HORIZONTAL, N, S, VERTICAL, W, Button, Canvas, Frame, Label, Menu, Scrollbar, StringVar, Text, Tk, filedialog
from canvas_config.canvas_config_view import CanvasConfigView
from grid_display import GridDisplay
from graphs.matplotlib_graphs import ChartManager
from file_saver import FileSaver

class SpreadSheetApp:
    """
        The main application class
    """
    def __init__(self):
        """Initiates the applications root and filesaver"""
      
       
        self.root = Tk()
        self.root.option_add('*tearOff', False)
        self.root.title("Taulukkolaskentasovellus")
        self.root.geometry("1200x600")
        self.root.configure(background='SteelBlue1')

        self.filesaver = FileSaver()
       
        
    def init_front_end(self):
        """Function for starting and displaying the UI"""

        self.main_canvas_container = Frame( self.root, bg="white")
        self.main_canvas_container.grid(column=0, row=0, sticky=N+W+S+E)
        self.main_canvas_container.columnconfigure(0, weight=1)
        self.main_canvas_container.rowconfigure(0, weight=1)

        self.init_menu_bar()
        self.init_grid_scrollBars()
        self.init_grid()
        
        self.canvas_chart_manager = ChartManager(self.grid_canvas)
        
        self.canvas_config_view = CanvasConfigView(self.root, self)

        self.init_bind_events()
        
    def start(self):
        """Enters the Tkinter root mainloop"""
        self.root.mainloop()

    def init_bind_events(self):
        """Function for binding events to the application"""
        self.grid_canvas.bind('<1>', self.handle_clicks)
        self.grid_canvas.bind('<Motion>', self.spread_sheet_view.handle_movement)
    
    def handle_clicks(self, event):
        """Function for delegating click events to different classes
        
            Args: 
                event: Tkinter event
        """
        if event.widget.widgetName == "gridCanvas":
           self.spread_sheet_view.handle_clicks(event)
        if event.widget.widgetName == "chartWidget":
            self.canvas_chart_manager.on_click(event)

    def handle_x_scroll(self, a_val, b_val):
        """Function for updating classes effected by grid horizontal scroll

            Args:
                    a_val, b_val: values provided by tkinter for scrolling
        
        """
        self.grid_canvas.xview(a_val, b_val)
        self.canvas_chart_manager.update_all_charts()

    def handle_y_scroll(self, a_val, b_val):
        """Function for updating classes effected by grid vertical scroll
            
            Args:
                    a_val, b_val: values provided by tkinter for scrolling
        """
        self.grid_canvas.yview(a_val,  b_val)
        self.canvas_chart_manager.update_all_charts()

  

    def init_grid(self):
        """Inits the grid_canvas Tkinter widget and the GridDisplay class for drawing a grid"""
        GRID_WIDTH = 100
        GRID_HEIGHT = 100
        CELL_WIDTH = 200
        CELL_HEIGHT = 50
        CELL_DISPLAY_TEXT_OFFSET_PX_X = 1
        CELL_DISPLAY_TEXT_OFFSET_PX_Y = 3
        FONT_SIZE = 12
        MAX_LETTERS_IN_CELL = 20
        
        self.grid_canvas = Canvas(self.main_canvas_container, bg="white",
                            xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)
        self.grid_canvas.widgetName = "gridCanvas"
        self.grid_canvas.grid(column=0, row=0, sticky=N+W+S+E)
        self.grid_canvas.configure(
            scrollregion=[0, 0, GRID_WIDTH*CELL_WIDTH, GRID_HEIGHT*CELL_HEIGHT])

        self.spread_sheet_view = GridDisplay(self.grid_canvas, GRID_WIDTH, GRID_HEIGHT, CELL_WIDTH, CELL_HEIGHT,
                                    CELL_DISPLAY_TEXT_OFFSET_PX_X, CELL_DISPLAY_TEXT_OFFSET_PX_Y,
                                    FONT_SIZE, MAX_LETTERS_IN_CELL)

    def init_grid_scrollBars(self):
        """Inits the scrollbars for scrolling the grid"""
        self.hbar = Scrollbar(self.main_canvas_container, orient=HORIZONTAL)
        self.vbar = Scrollbar(self.main_canvas_container, orient=VERTICAL)
      
      
        self.vbar.config(command=self.handle_y_scroll)
        self.vbar.grid(column=1, row=0, sticky=N+S)

        self.hbar.config(command=self.handle_x_scroll)
        self.hbar.grid(column=0, row=1, sticky=E+W)
          
    
        

    def init_menu_bar(self):
        """Inits the UI for menu bar"""
        menubar = Menu(self.root)
        self.root['menu'] = menubar
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        menu_file = Menu(menubar)
        menubar.add_cascade(menu=menu_file, label='Tiedosto')
        menu_file.add_command(label="Avaa tiedosto", command=self.openSaveFile)
        menu_file.add_command(label="Tallenna tiedostoon", command=self.createSaveFile)

    def openSaveFile(self):
        """Launches the operating system file browser"""
        #help from https://docs.python.org/3/library/dialog.html#module-tkinter.filedialog 
        file = filedialog.askopenfile("r", defaultextension=".json", filetypes=[("JSON","*.json")])
        self.loadStateFromFile(file)
    
    def createSaveFile(self):
        self.spread_sheet_view.cancel_cell_edit()
        file = filedialog.asksaveasfile("w", defaultextension=".json", filetypes=[("JSON","*.json")])
        self.saveStateToFile(file)

  


    def saveStateToFile(self, file):
        """Saves the app state as a dictionary to a file which is correctly test.json"""
        self.filesaver.bind_data_to_save("cell_values", self.spread_sheet_view.cell_grid_values)
        self.filesaver.bind_data_to_save("chart_values", self.canvas_chart_manager.chartInformation)
        self.filesaver.save_dict_to_file(file)
     
    

    
    def loadStateFromFile(self, file):
        """loads app state from a file which is correctly test.json"""
        state = self.filesaver.read_dict_from_file(file)
        if state != None:
            
            for key in state["cell_values"]:
                self.spread_sheet_view.cell_grid_values[int(key)] = state["cell_values"][key]
            self.spread_sheet_view.updateViewText()

            self.canvas_chart_manager.delete_all_charts()
            for chart in state["chart_values"]:
                information = state["chart_values"][chart]
                if information["type"] == "Bar":
                    self.canvas_chart_manager.add_new_bar_chart(information["title"], information["x_title"], 
                                                                information["y_title"], information["x_values"], 
                                                                information["y_values"], information["size_x"], 
                                                                information["size_y"], information["dots"], 
                                                                information["coords"][0], information["coords"][1])
                elif information["type"] == "Pie":
                        self.canvas_chart_manager.add_new_pie_chart(information["title"], information["x_title"], 
                                                                information["y_title"], information["x_values"], 
                                                                information["y_values"], information["size_x"], 
                                                                information["size_y"], information["dots"], 
                                                                information["coords"][0], information["coords"][1])

           
        
            
        
      
        
        
    
    
        

        
       
       