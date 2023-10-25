"""Main game's module with gameplay."""
from random import randint

from graphic_arts.start_game_banner import run_screensaver


class Character():
    def __init__(self, name):
        self.name = name

    def attack(self):
        pass

    def defence(self):
        pass

    def special(self):
        pass


class Warrior(Character):
    pass


class Mage(Character):
    pass


class Healer(Character):
    pass