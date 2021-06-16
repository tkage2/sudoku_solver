from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from string import ascii_uppercase
import sudoku




class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        
    # Function for creating widgets and creating visual matrix in GUI
    def create_widgets(self):
        self.entries = []

        for x in range(0, 9):
            self.entries.append([tk.Button(self.master, name=str(x)+str(y),  text="X", font=("Courier", "12"), height=2, width=5, command=lambda x = x, y = y: self.change_button_value_dialog((x,y))) for y in range(0, 9)])
                 
        for x in self.entries:
            for y in x:
                y.grid(row=self.entries.index(x), column=x.index(y))
                
        self.run_btn = tk.Button(self.master, text="Run", bg="green", width=5, command=self.run)
        self.run_btn.grid(row=10, column=4)

        
    # Dialog for changing value of X-marked button in matrix
    def change_button_value_dialog(self, button_widget_coords):
        window = tk.Toplevel()
        button_widget = self.entries[button_widget_coords[0]][button_widget_coords[1]]
        e = tk.Entry(window)
        btn_ok = tk.Button(window, text="OK", command=lambda: self.change_button_value(window, button_widget, e.get()))
        e.grid(row=0, column=0)
        btn_ok.grid(row=0, column=1)
        
    # Changes the value of button in matrix    
    def change_button_value(self, window, widget, value):
        try:
            if value != "X":
                val = int(value)
                if val <= 0 or val >= 10:
                    raise ValueError
            widget.configure(text = value)
            window.destroy()
        except:
            messagebox.showinfo("Invalid character", "Only numbers between 1-9 or X allowed!")
            window.focus_force()
            
    # Creates matrix
    def create_matrix(self):
        matrix = []
        for x in self.entries:
            indice_list = []
            for y in x:
                indice_list.append(y['text'])
            matrix.append(indice_list)
            
        return matrix
        
    # Refreshes GUI    
    def update_gui(self, matrix):
        for x1, x2 in zip(self.entries, matrix):
            for y1, y2 in zip(x1, x2):
                y1.configure(text=y2)
                self.master.update_idletasks()         
                
            
    def run(self):
        self.run_btn['state'] = "disabled"
        sudoku.set_matrix(self.create_matrix())
        sudoku.subscribe_to_matrix_changes(self.update_gui)
        sudoku.solve_matrix(sudoku.get_matrix())
        self.run_btn['state'] = "normal"

        

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sudoku solver")
    app = Application(master=root)
    app.mainloop()