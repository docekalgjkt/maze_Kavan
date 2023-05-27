import Translator
from tkinter import *

class Maze:
    def __init__(self):  
        self.canvas = None
        self.window = None  
        self.create_window()

    def create_window(self):
        self.window = Tk()
        self.window.geometry("800x450")
        self.window.title("Maze")
        self.canvas = Canvas(self.window, width = 800, height = 450)
        self.canvas.pack()
        start_program_button = Button(self.window, text = "Start_program", bg = "red")
        start_program_button.place(x = 550, y = 300, width = 230, height = 100)
        self.place_robot()
        self.window.mainloop()
    

    def place_robot(self):
        x = Label(self.window, text = "x position")
        y = Label(self.window, text = "y position")
        x.place(x = 540, y = 200, width = 80, height = 20)
        y.place(x = 540, y = 240, width = 80, height = 20)
        self.input_x = Entry(self.window)
        self.input_y = Entry(self.window)
        self.input_x.place(x = 640, y = 200, width = 40, height = 20)
        self.input_y.place(x = 640, y = 240, width = 40, height = 20)
        button = Button(self.window, text = "Enter", command = self.create_robot)
        button.place(x = 720, y = 220, width = 40, height = 20)
        self.window.mainloop()
            
    def create_robot(self):
        if self.input_x.get()!= "" and self.input_y.get() != "":
            x = int(self.input_x.get())
            y = int(self.input_y.get())+1
            self.canvas.create_oval(20*x, 20*y, 20*x+20, 20*y+20)
        
        

        
        
        
        
        

Maze()