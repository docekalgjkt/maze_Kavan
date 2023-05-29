class Translator:
    def return_maze(self, doc):
        script = open(doc)
        lines = []
        level = script.readlines()
        for line in level:
            lines.append(line)
        for line in lines:
            list(line)
        return lines