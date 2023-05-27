class Translator:
    def return_maze(self, doc):
        script = open(doc)
        level = script.readline()
        lines = level.split(";")
        for line in lines:
            list(line)
        return lines