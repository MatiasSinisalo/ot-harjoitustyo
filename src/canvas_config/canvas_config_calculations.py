from tkinter import N,W,S,E, Button, Entry, Frame, Label


class CanvasCalculationsView:
    def __init__(self, root, app) -> None:
        self.root = root
        self.app = app

        calculations_view = Frame(self.root, width=300, bg="lightgray")
        calculations_view.grid(column=0, row=2,  sticky=N+W+S+E,  pady=10, padx=10)

        get_sum_of_selection_button = Button(calculations_view, text="Laske valinnan summa", 
                                            command=self.set_answer_text_to_sum)
        get_sum_of_selection_button.grid(column=0, row=1, sticky=E+W)
        
        self.sum_result_text = Label(calculations_view)
        self.sum_result_text.grid(column=0, row=2, sticky=E+W)

        get_average_of_selection_button = Button(calculations_view, text="Laske valinnan keskiarvo", 
                                            command=self.set_answer_text_to_average)
        get_average_of_selection_button.grid(column=0, row=3, sticky=E+W)
        
        self.average_result_text = Label(calculations_view)
        self.average_result_text.grid(column=0, row=4, sticky=E+W)
   
    def set_answer_text_to_sum(self):
        answer = self.app.spread_sheet_view.get_sum_of_selection()
        self.sum_result_text.config(text = answer)

    def set_answer_text_to_average(self):
        answer = self.app.spread_sheet_view.get_average_of_selection()
        self.average_result_text.config(text = answer)