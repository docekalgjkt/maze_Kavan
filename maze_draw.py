from Translator import *
from tkinter import *

class Maze:
    def __init__(self):  
        self.canvas = None
        self.window = None 
        self.width = 500
        self.height = 600
        self.robot = None
        self.warning_txt = None
        self.welcome = None
        self.create_window()

    def create_window(self):
        #create window interface
        self.window = Tk()
        self.window.geometry("800x450")
        self.window.title("Maze")
        self.canvas = Canvas(self.window, width = self.width, height = self.height)
        self.canvas.pack(side = LEFT)
        start_program_button = Button(self.window, text = "Start program", bg = "red", command = self.find_way)
        start_program_button.place(x = 550, y = 300, width = 230, height = 100)
        x = Label(self.window, text = "x position")
        y = Label(self.window, text = "y position")
        place_robot_txt = Label(self.window, text = "Place robot:", fg = "red")
        place_robot_txt.place(x = 540, y = 160, width = 80, height = 40)
        x.place(x = 540, y = 200, width = 80, height = 20)
        y.place(x = 540, y = 240, width = 80, height = 20)
        self.input_x = Entry(self.window)
        self.input_y = Entry(self.window)
        self.input_x.place(x = 640, y = 200, width = 40, height = 20)
        self.input_y.place(x = 640, y = 240, width = 40, height = 20)
        button = Button(self.window, text = "Enter", command = self.create_robot)
        button.place(x = 720, y = 220, width = 40, height = 20)
        lvl_button = Button(self.window, text = "Select Level", command = self.select_lvl)
        lvl_button.place(x = 560, y = 50, width = 210, height = 100)
        exit = Button(self.window, text = "Exit", command = self.window.destroy)
        exit.place(x = 630, y = 420, width = 70, height = 20)
        #create welcome text
        if self.welcome == None:
            self.welcome = self.canvas.create_text(250, 200, text = "WELCOME TO THE MAZE\n To begin, choose level\n then place your robot\n and finally press start!")
        self.window.mainloop()
            
    def create_robot(self):
        #checks if you can place robot and create it
        if self.warning_txt != None:
            self.warning_txt.destroy()
        if self.robot != None:
             self.canvas.delete(self.robot)
        if self.input_x.get()!= "" and self.input_y.get() != "":
            x = int(self.input_x.get())-1
            y = int(self.input_y.get())-1
            if self.lvl == Translator().return_maze(r"C:\Users\Administrator\Desktop\pogromovani\VSCode\maze_repository\LVL_1.txt"):
                if self.lvl[y][x] == "0":
                    self.robot = self.canvas.create_oval((40*x)+200, (40*y)+120, 40*(x+1)+200, 40*(y+1)+120, fill = "blue")
                elif self.lvl[y][x] == "1":
                    self.warning_txt = Label(self.window, text = "Please, do not put player on walls", fg = "red")
                    self.warning_txt.place(x=560,y=260, width = 200, height = 40) 
                elif self.lvl[y][x] == "2":
                    self.warning_txt = Label(self.window, text = "Do not choose the exit, please", fg = "red")
                    self.warning_txt.place(x=560,y=260, width = 200, height = 40)
            elif self.lvl == Translator().return_maze(r"C:\Users\Administrator\Desktop\pogromovani\VSCode\maze_repository\LVL_2.txt"):
                if self.lvl[y][x] == "0":
                    self.robot = self.canvas.create_oval((40*x)+130, (40*y)+80, 40*(x+1)+130, 40*(y+1)+80, fill ="blue")
                elif self.lvl[y][x] == "1":
                    self.warning_txt = Label(self.window, text = "Please, do not put player on walls", fg = "red")
                    self.warning_txt.place(x=560,y=260, width = 200, height = 40)
                elif self.lvl[y][x] == "2":
                    self.warning_txt = Label(self.window, text = "Do not choose the exit, please", fg = "red")
                    self.warning_txt.place(x=560,y=260, width = 200, height = 40)
            else:
                if self.lvl[y][x] == "0":
                    self.robot = self.canvas.create_oval((40*x)+50, (40*y)+30, 40*(x+1)+50, 40*(y+1)+30, fill = "blue")               
                elif self.lvl[y][x] == "1":
                    self.warning_txt = Label(self.window, text = "Please, do not put player on walls", fg = "red")
                    self.warning_txt.place(x=560,y=260, width = 200, height = 40) 
                elif self.lvl[y][x] == "2":
                    self.warning_txt = Label(self.window, text = "Do not choose the exit, please", fg = "red")
                    self.warning_txt.place(x=560,y=260, width = 200, height = 40)
                
             
    def select_lvl(self):
        #create lvl buttons
        self.canvas.delete("all")
        self.Lvl_1 = Button(self.window, text = "Level 1", command = self.draw_level_1)
        self.Lvl_1.place(x = 225,y = 30, width = 100, height = 50)
        self.Lvl_2 = Button(self.window, text = "Level 2", command = self.draw_level_2)
        self.Lvl_2.place(x = 225, y = 110, width = 100, height = 50)
        self.Lvl_3 = Button(self.window, text = "Level 3", command = self.draw_level_3)
        self.Lvl_3.place(x = 225, y = 190, width = 100, height = 50)
        self.window.mainloop()
        
    def draw_level_1(self):
        self.Lvl_1.destroy()
        self.Lvl_2.destroy()
        self.Lvl_3.destroy()
        self.lvl = Translator().return_maze(r"C:\Users\Administrator\Desktop\pogromovani\VSCode\maze_repository\LVL_1.txt")
        for y in range(len(self.lvl)):
                x = 0
                line = self.lvl[y]
                for num in line:
                    if num == "0":
                        self.canvas.create_rectangle((40*x)+200, (40*y)+120, 40*(x+1)+200, 40*(y+1)+120)
                        x += 1
                    if num == "1":
                        self.canvas.create_rectangle((40*x)+200, (40*y)+120, 40*(x+1)+200, 40*(y+1)+120, fill = "black")
                        x += 1
                    if num == "2":
                        self.canvas.create_rectangle((40*x)+200, (40*y)+120, 40*(x+1)+200, 40*(y+1)+120,fill = "red")
                        x += 1

    def draw_level_2(self):
        self.Lvl_1.destroy()
        self.Lvl_2.destroy()
        self.Lvl_3.destroy()
        self.lvl = Translator().return_maze(r"C:\Users\Administrator\Desktop\pogromovani\VSCode\maze_repository\LVL_2.txt")
        for y in range(len(self.lvl)):
                x = 0
                line = self.lvl[y]
                for num in line:
                    if num == "0":
                        self.canvas.create_rectangle((40*x)+130, (40*y)+80, 40*(x+1)+130, 40*(y+1)+80)
                        x += 1
                    if num == "1":
                        self.canvas.create_rectangle((40*x)+130, (40*y)+80, 40*(x+1)+130, 40*(y+1)+80, fill = "black")
                        x += 1
                    if num == "2":
                        self.canvas.create_rectangle((40*x)+130, (40*y)+80, 40*(x+1)+130, 40*(y+1)+80,fill = "red")
                        x += 1

    def draw_level_3(self):
        self.Lvl_1.destroy()
        self.Lvl_2.destroy()
        self.Lvl_3.destroy()
        self.lvl = Translator().return_maze(r"C:\Users\Administrator\Desktop\pogromovani\VSCode\maze_repository\LVL_3.txt")
        for y in range(len(self.lvl)):
                x = 0
                line = self.lvl[y]
                for num in line:
                    if num == "0":
                        self.canvas.create_rectangle((40*x)+50, (40*y)+30, 40*(x+1)+50, 40*(y+1)+30)
                        x += 1
                    if num == "1":
                        self.canvas.create_rectangle((40*x)+50, (40*y)+30, 40*(x+1)+50, 40*(y+1)+30, fill = "black")
                        x += 1
                    if num == "2":
                        self.canvas.create_rectangle((40*x)+50, (40*y)+30, 40*(x+1)+50, 40*(y+1)+30,fill = "red")
                        x += 1
    def find_way(self):
        pass

Maze()