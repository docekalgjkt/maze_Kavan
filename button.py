from tkinter import *
from typing import Any

class Choose_level:
    def __init__(self):
        self.choose_lvl = None
    
    def level_selection(self):
        self.choose_lvl = Tk()
        self.choose_lvl.geometry("150x300")
        canvas = Canvas(self.choose_lvl, width = 150, height = 50)
        canvas.pack()
        for i in range(1, 8):
            name = "level {}".format(i)
            button = Button(self.choose_lvl, text = str(name))
            button.pack(side = "top")

class Place_robot:
    def __init__(self):
        self.input_x = None
        self.input_y = None
        self.coords = None
        self.place_robot = Tk()
        self.place_robot.geometry("200x200")
        canvas = Canvas(self.place_robot, width = 200, height = 40)
        canvas.pack()

    def robot_coords(self):
        self.input_x = Entry(self.place_robot)
        self.input_y = Entry(self.place_robot)
        self.input_x.place(x = 120, y = 30, width = 50, height = 20)
        self.input_y.place(x = 120, y = 90, width = 50, height = 20)
        x_position = Label(self.place_robot, text = "x position", )
        y_position = Label(self.place_robot, text = "y position")
        x_position.place(x = 20, y = 30, width = 70, height = 20)
        y_position.place(x = 20, y = 90, width = 70, height = 20)
        enter_button = Button(self.place_robot, text = "Enter", command = self.if_enter_pressed)
        enter_button.place(x = 80, y = 150, width = 40, height = 20)
        if self.input_x.get() != "" and self.input_y.get() != "":
            return int(self.input_x.get()), int(self.input_y.get())
    
    def if_enter_pressed(self):
        print(self.input_x.get())
        print(self.input_y.get())
        if self.input_x.get() == "" or self.input_y.get() == "":
            txt = Label(self.place_robot, text = "Please, enter the starting position !", fg = "red")
            txt.place(x = 10, y = 180, width = 180, height = 20)

    def Destroy(self):
        self.place_robot.destroy()