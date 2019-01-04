# imports
from actors import Wizard, Creature


def main():
    print_header()
    game_loop()


def print_header():
    print('*' * 30)
    print('       WIZARD APP')
    print('*' * 30)
    print()


def game_loop():

    creatures = [
        Creature('bat', 1),
        Creature('toad', 5),
        Creature('tiger', 12),
        Creature('Dragon', 50),
        Creature('Evil Wizard', 1000)
    ]

    hero = Wizard('Krondor', 75)

    print(creatures)

    while True:
        cmd = input('Would you like to [a]ttack, [l]ook around, or [r]unaway?')
        cmd = cmd.lower()

        if cmd == 'a':
            print('attacking')
        elif cmd == 'l':
            print('looking around')
        elif cmd == 'r':
            print('running away')
        else:
            print('Exiting')
            break


if __name__ == '__main__':
    main()
