class Translator:
    def __init__(self, document):
        self.return_maze(document)

    def return_maze(self, doc):
        script = open(doc)
        level = script.readline()
        lines = level.split(";")
        for line in lines:
            list(line)
        return lines
Translator(r"C:\Users\Administrator\Desktop\pogromovani\VSCode\maze_repository\text_line.txt")