from Translator import *
from tkinter import *

class Node:
    def __init__(self, pos):
        self.pos = pos
        self.parent = None
        self.around = []
class Maze:
    def __init__(self):  
        self.canvas = None
        self.window = None 
        self.width = 500
        self.height = 600
        self.robot = None
        self.memory = []
        self.way = []
        self.end = None
        self.queue = []
        self.root = None
        self.previous = None
        self.warning_txt = None
        self.error_txt = None
        self.walked = []
        self.lvl = None
        self.create_window()

    def create_window(self):
        #create window interface
        self.window = Tk()
        self.window.geometry("800x450")
        self.window.title("Maze")
        self.canvas = Canvas(self.window, width = self.width, height = self.height)
        self.canvas.pack(side = LEFT)
        self.start_program_button = Button(self.window, text = "Start program", bg = "red", command = self.go_robot)
        self.start_program_button.place(x = 550, y = 300, width = 230, height = 100)
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
        self.button = Button(self.window, text = "Enter", command = self.create_robot)
        self.button.place(x = 720, y = 220, width = 40, height = 20)
        self.lvl_button = Button(self.window, text = "Select Level", command = self.select_lvl)
        self.lvl_button.place(x = 560, y = 50, width = 210, height = 100)
        self.exit = Button(self.window, text = "Exit", command = self.window.destroy)
        self.exit.place(x = 625, y = 420, width = 70, height = 20)
        self.window.mainloop()
            
    def create_robot(self):
        if self.error_txt != None:
            self.error_txt.destroy()
        #checks if you can place robot and create it
        if self.warning_txt != None:
            self.warning_txt.destroy()
        if self.robot != None:
             self.canvas.delete(self.robot)
        try:
            int(self.input_x.get())
            int(self.input_y.get())
            if int(self.input_x.get()) != 0:
                x = int(self.input_x.get())-1
            else:
                x = int(self.input_x.get())
            if int(self.input_y.get()) != 0:
                y = int(self.input_y.get())-1
            else:
                y = int(self.input_y.get())
            if self.lvl == Translator().return_maze(r"C:\Users\Administrator\Desktop\pogromovani\VSCode\maze_repository\LVL_1.txt"):
                if self.lvl[y][x] == "0":
                    self.robot = self.canvas.create_oval((40*x)+200, (40*y)+120, 40*(x+1)+200, 40*(y+1)+120, fill = "blue")
            elif self.lvl == Translator().return_maze(r"C:\Users\Administrator\Desktop\pogromovani\VSCode\maze_repository\LVL_2.txt"):
                if self.lvl[y][x] == "0":
                    self.robot = self.canvas.create_oval((40*x)+130, (40*y)+80, 40*(x+1)+130, 40*(y+1)+80, fill ="blue")
            else:
                if self.lvl[y][x] == "0":
                    self.robot = self.canvas.create_oval((40*x)+50, (40*y)+30, 40*(x+1)+50, 40*(y+1)+30, fill = "blue")
        except ValueError:
            self.error("Please input numbers")    
             
    def select_lvl(self):
        if self.error_txt != None:
            self.error_txt.destroy()
        #create lvl buttons
        self.canvas.delete("all")
        self.lvl = None
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
    

    def find_way(self, position):
        for x in [1,-1]:
            try:
                if position.pos[0] == 0 and x == -1:
                    continue
                elif self.lvl[position.pos[1]][position.pos[0]+x] != "1":
                    way = Node([position.pos[0]+x, position.pos[1]])
                    way.parent = position
                    if way.pos not in self.memory:
                        self.memory.append(way.pos)
                        self.queue.append(way)
            except IndexError:
                continue
        for y in [1,-1]:
            try:
                if position.pos[1] == 0 and y == -1:
                    continue
                elif self.lvl[position.pos[1]+y][position.pos[0]] != "1":
                    way = Node([position.pos[0],position.pos[1]+y])
                    way.parent = position
                    if way.pos not in self.memory:
                        self.memory.append(way.pos)
                        self.queue.append(way)
            except IndexError:
                continue
        
        if self.lvl[position.pos[1]][position.pos[0]] == "2":
            knot = position
            self.way.append(knot.pos)
            while knot.parent != None:
                self.way.append(knot.parent.pos)
                knot = knot.parent
            return self

            
        
    def find_end(self):
        self.root = Node([int(self.input_x.get())-1,int(self.input_y.get())-1])
        self.memory.append(self.root.pos)
        self.queue.append(self.root)
        while self.way == []:
            self.find_way(self.queue.pop())
        return self.way

            
    def walk(self):
            try:
                x = (self.place[0]-self.previous[0])*40
                y = (self.place[1]-self.previous[1])*40
                self.canvas.move(self.robot, x, y)
                self.previous = self.place
                self.place = self.way.pop()
                x = None
                y = None
                self.window.after(600, self.walk)
                self.window.update()
            except IndexError:
                x = (self.place[0]-self.previous[0])*40
                y = (self.place[1]-self.previous[1])*40
                self.canvas.move(self.robot, x, y)
                self.window.update()
                self.game_over()
                
    def go_robot(self):
        self.error_txt = None
        #disable buttons -> need to do
        self.start_program_button["state"] = DISABLED
        self.button["state"] = DISABLED
        self.exit["state"] = DISABLED
        self.lvl_button["state"] = DISABLED
        self.play_again_but = None
        self.exit_button = None
        #checks if it is walkable -> need to do
        if self.lvl != None:
            if self.input_x.get() != "" and self.input_y.get() != "":
                if self.lvl[int(self.input_y.get())-1][int(self.input_x.get())-1] != "1":
                        try:
                            self.way = self.find_end()
                            self.previous = self.way.pop()
                            self.place = self.way.pop()
                            self.walk()
                        except IndexError:
                            self.error("Robot can't reach end")
                else:
                    self.error("Do not place robot on wall")
            else:
                self.error("Put both coordinates")
        else:
            self.error("select level")
        
    
    def error(self, text):
        if self.error_txt != None:
            self.error_txt.destroy()
        self.error_txt = Label(self.window, text = text)
        self.error_txt.place(x = 560, y = 400, width = 200, height = 20)
        self.start_program_button["state"] = NORMAL
        self.exit["state"] = NORMAL
        self.lvl_button["state"] = NORMAL
        self.button["state"] = NORMAL

    def game_over(self):
        self.window.after(500, self.canvas.delete("all"))
        self.window.update()
        self.congrats = Label(self.window, text = "CONGRATULATIONS", fg = "green", font = "Helvetica 25 bold")
        self.congrats.place(x = 80, y = 150, width = 400, height = 100)
        self.play_again_but = Button(self.window, text = "Play again", command = self.play_again)
        self.play_again_but.place(x = 225, y = 260, width = 100, height = 40)
        self.exit_button = Button(self.window, text = "Quit game", command= self.window.destroy)
        self.exit_button.place(x = 235, y = 310, width = 80, height = 40)

    def play_again(self):
        self.congrats.destroy()
        self.play_again_but.destroy()
        self.exit_button.destroy()
        self.start_program_button["state"] = NORMAL
        self.button["state"] = NORMAL
        self.lvl_button["state"] = NORMAL
        self.exit["state"] = NORMAL
        self.input_x["state"] = NORMAL
        self.input_y["state"] = NORMAL

Maze()