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