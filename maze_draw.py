import maze_readline
from button import *
from tkinter import *

maze = maze_readline.returnmaze()
list(maze)

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
        get_coords = Place_robot().robot_coords()
        print(get_coords)
        
        

Maze()