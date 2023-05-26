import Translator
from button import *
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
        self.create_grid()
        self.window.mainloop()
    
    def create_grid(self):
        for i in range(int(450/20)):
            i += 1
            for j in range(int(530/20)):
                self.canvas.create_rectangle(j*20, i*20, (j+1)*20, (i+1)*20)
        self.create_buttons()
    
    def create_buttons(self):
        self.level_button_bool = False
        choose_level_button =Button(self.window, text = "Choose level", command = Choose_level().level_selection)
        choose_level_button.place(x = 565, y = 50, width = 200, height = 75)

        set_position_button = Button(self.window, text = "Place Robot", command = self.place_robot)
        set_position_button.place(x= 565, y = 175, width = 200, height = 75)

        start_program_button = Button(self.window, text = "Start_program", bg = "red")
        start_program_button.place(x = 550, y = 300, width = 230, height = 100)

    def place_robot(self):
        x = Label(self.window, text = "x position")
        y = Label(self.window, text = "y position")
        x.place(x = 40, y = 0, width = 80, height = 20)
        y.place(x = 180, y = 0, width = 80, height = 20)
        self.input_x = Entry(self.window)
        self.input_y = Entry(self.window)
        self.input_x.place(x = 120, y = 0, width = 40, height = 20)
        self.input_y.place(x = 260, y = 0, width = 40, height = 20)
        button = Button(self.window, text = "Enter", command = self.create_robot)
        button.place(x = 320, y = 0, width = 40, height = 20)
        self.window.mainloop()
            
    def create_robot(self):
        pressed = None
        warning_txt = None
        if self.input_x.get()!= "" and self.input_y.get() != "":
            x = int(self.input_x.get())
            y = int(self.input_y.get())+1
            self.canvas.create_oval(20*x, 20*y, 20*x+20, 20*y+20)
            pressed = True
        elif self.input_x.get() == "" or self.input_y.get() == "":
            warning_txt = Label(self.window, text = "Enter position !", fg = "red")
            warning_txt.place(x = 380,y = 0, width = 80, height = 20)
        if pressed == True and warning_txt != None:
            warning_txt.destroy()

        
        
        
        
        

Maze()