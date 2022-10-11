"""classe du pokemon Defender
"""

from abstract_pokemon import AbstractPokemon

class Defender(AbstractPokemon):
    """type defender

    Parameters
    ----------
    AbstractPokemon : AbstractPokemon
        _description_
    """
    def __init__(self, current_stat, level, name, attack_current, defense_current):
        super().__init__(current_stat, level, name)
        self.attack_current = attack_current
        self.defense_current = defense_current

    def get_pokemon_attack_coef(self):
        return 1 + (self.attack_current + self.defense_current)/200
