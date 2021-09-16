from business_object.attack.special_attack import SpecialFormulaAttack
from business_object.pokemon.abstract_pokemon import AbstractPokemon


class AllRounderPokemon(AbstractPokemon):
    def __init__(self
                 , stat_max=None
                 , stat_current=None
                 , level=None
                 , name=None
                 , gear=None
                 , common_attacks = []) -> None:
        special_attack = SpecialFormulaAttack(power=80
                                              , name="Dragon laser"
                                              , description="{pokemon.name} a dark laser shoots a dark laser ")

        super().__init__(stat_max=stat_max
                         , stat_current=stat_current
                         , level=level
                         , name=name
                         , gear=gear
                         , special_attack=special_attack
                         , common_attacks=common_attacks)

    def get_pokemon_attack_coef(self) -> float:
        return 1 + (self.sp_atk_current + self.sp_def_current) / 200
