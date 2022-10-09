"""classe attacker"""

from abstract_pokemon import AbstractPokemon

class Attacker(AbstractPokemon):

    def __init__(self, current_stat, level, name, speed_current, speed_attack):
        super.__init__(self, current_stat, level, name)



    def get_pokemon_attack_coef(self):
        return




