from dataclasses import dataclass

from business_object.pokemon.abstract_pokemon import AbstractPokemon


@dataclass
class Round:
    pkmn_attcker: AbstractPokemon
    pkmn_targeted: AbstractPokemon
    dealt_damage: int
    attack_description: str
