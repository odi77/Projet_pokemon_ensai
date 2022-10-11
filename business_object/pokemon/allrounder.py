"""allrounder
"""

from abstract_pokemon import AbstractPokemon

class Allrounder(AbstractPokemon):
    """classe Allrounder

    Args:
        AbstractPokemon (classe): classe abstraite
    """
    def __init__(self, current_stat, level, name, sp_atk_current, sp_def_current):
        super().__init__(current_stat, level, name)
        self.sp_atk_current = sp_atk_current
        self.sp_def_current = sp_def_current

    def get_pokemon_attack_coef(self):
        return 1 + (self.sp_atk_current + self.sp_def_current)/200
