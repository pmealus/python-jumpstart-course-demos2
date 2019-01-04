import random


class Wizard:

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return "Wizard: {}, Level: {}".format(self.name, self.level)

    def attack(self, creature):
        print("The wizard {} attacks {}".format(self.name, creature))

        my_roll = random.randint(1,12) * self.level
        creature_roll = random.randint(1,12) * creature.level

        if my_roll >= creature_roll:
            print("{} has triumphed over the {}".format(self.name, creature.name))
            return True
        else:
            print("{} has been defeated by {}".format(self.name, creature.name))
            return False

class Creature:

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return "Creature:{}, Level:{}".format(self.name, self.level)


