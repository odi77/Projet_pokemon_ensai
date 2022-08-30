from dataclasses import dataclass, field
from typing import List

from business_object.battle.round import Round
from business_object.pokemon.abstract_pokemon import AbstractPokemon

class Battle:
    def __init__(self
                 , pkmn1 : AbstractPokemon
                 , pkmn2: AbstractPokemon) -> None:
            
        self.__pkmn1: AbstractPokemon = pkmn1
        self.__pkmn2: AbstractPokemon = pkmn2
        self.__rounds: List[Round] = []
        self.__winner: AbstractPokemon = None
        self.__final_phrase: str = ""


    def add_round(self
                  , pkmn_attcker
                  , pkmn_targeted
                  , dealt_damage
                  , attack_description):
        self.__rounds.append(Round(pkmn_attcker=pkmn_attcker
                                   , pkmn_targeted=pkmn_targeted
                                   , dealt_damage=dealt_damage
                                   , attack_description=attack_description))

    
    @property
    def first_monstie(self):
        return self.__first_monstie

    @property
    def pkmn2(self):
        return self.__pkmn2

    @property
    def rounds(self):
        return self.__rounds


    @property
    def winner(self):
        return self.__winner

    @winner.setter
    def winner(self, value):
        self.__winner = value

    @property
    def final_phrase(self):
        return self.__final_phrase

    @winner.setter
    def final_phrase(self, value):
        self.__final_phrase = value
