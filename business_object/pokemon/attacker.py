"""classe attacker"""

from abstract_pokemon import AbstractPokemon

class Attacker(AbstractPokemon):

    def __init__(self, current_stat, level, name, speed_current, speed_attack):
        super.__init__(self, current_stat, level, name)
        self.speed_current= speed_current
        self.speed_attack = speed_attack



    def get_pokemon_attack_coef(self):
        return 1 + (self.speed_current + self.speed_attack)/200





