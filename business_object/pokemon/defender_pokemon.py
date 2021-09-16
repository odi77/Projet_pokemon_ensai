from business_object.attack.physical_attack import PhysicalFormulaAttack
from business_object.pokemon.abstract_pokemon import AbstractPokemon


class DefenderPokemon(AbstractPokemon):
    def __init__(self
                 , stat_max=None
                 , stat_current=None
                 , level=None
                 , name=None
                 , gear=None
                 , common_attacks = []) -> None:
        special_attack = PhysicalFormulaAttack(power=60
                                               , name="Elbow tackle"
                                               , description="{pokemon.name} hits with a massive tackle ")

        super().__init__(stat_max=stat_max
                         , stat_current=stat_current
                         , level=level
                         , name=name
                         , gear=gear
                         , special_attack=special_attack
                         , common_attacks=common_attacks)

    def get_pokemon_attack_coef(self) -> float:
        return 1 + (self.attack_current + self.defense_current) / 200
