from business_object.attack.abstract_formula_attack import AbstractFormulaAttack
from business_object.pokemon.abstract_pokemon import AbstractPokemon


class PhysicalFormulaAttack(AbstractFormulaAttack):

    def get_attack_stat(self
                        , pkmn_attcker: AbstractPokemon
                        , pkmn_targeted: AbstractPokemon) -> float:
        return pkmn_attcker.attack_current

    def get_defense_stat(self
                         , pkmn_attcker: AbstractPokemon
                         , pkmn_targeted: AbstractPokemon) -> float:
        return pkmn_targeted.defense_current

