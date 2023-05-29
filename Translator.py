class Translator:
    def return_maze(self, doc):
        script = open(doc)
        level = script.readlines()
        lines = []
        for line in level:
            line.split(",")
            lines.append(line)
        for line in lines:
            list(line)
        return lines