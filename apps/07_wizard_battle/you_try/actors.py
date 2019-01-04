class Wizard:

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return "Wizard: {}, Level: {}".format(self.name, self.level)


class Creature:

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return "Creature:{}, Level:{}".format(self.name, self.level)


