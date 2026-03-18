from Swordsman import Swordsman
from Archer import Archer
from Magician import Magician

class Boss(Swordsman, Archer, Magician):
    def __init__(self, username):
        super().__init__(username)
        self.setStr