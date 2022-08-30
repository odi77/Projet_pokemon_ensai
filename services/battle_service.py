from random import randint, random, choice
from typing import Tuple

from business_object.attack.abstract_attack import AbstractAttack
from business_object.battle.battle import Battle
from business_object.pokemon.abstract_pokemon import AbstractPokemon
from utils.singleton import Singleton


class BattleService(metaclass=Singleton):
    def resolve_battle(self
                       , pkmn1: AbstractPokemon
                       , pkmn2: AbstractPokemon) -> Battle:
        """
        A battle is divide in round. Each round one pokemon will be
        the attacker, the other the pkmn_targeted. The battle end one
        one pokemon has 0 hp or less.

        This method create a Battle object, witch contain all the
        dealt damages and pkmns' state at each round. This object
        can be send to a client for exemple to display the battle in
        a nice way.

        Args:
            pkmn1 (AbstractPokemon): a pokemon
            pkmn2 (AbstractPokemon): another pokemon

        Returns:
            Battle : all the battle sequence round by round

        """

        # select the first attacker and pkmn_targeted
        pkmn_attcker, pkmn_targeted = self.get_order(pkmn1, pkmn2)

        battle = Battle(pkmn1=pkmn_attcker, pkmn2=pkmn_targeted)

        # The battle end only when one pokemon is down.
        while pkmn_attcker.hp_current > 0 and pkmn_targeted.hp_current > 0:
            attack_used = self.choose_attack(pkmn_attcker)
            damage = attack_used.compute_damage(pkmn_attcker=pkmn_attcker
                                                , pkmn_targeted=pkmn_targeted)
            pkmn_targeted.get_hit(damage=damage)
            battle.add_round(pkmn_attcker=pkmn_attcker
                             , pkmn_targeted=pkmn_targeted
                             , dealt_damage=damage
                             , attack_description=attack_used.description)
            # switch the role
            pkmn_attcker, pkmn_targeted = pkmn_targeted, pkmn_attcker
        # Because of the switch the winner is the defenser now
        battle.winner = pkmn_targeted
        return battle

    def get_order(self
                  , pkmn1: AbstractPokemon
                  , pkmn2: AbstractPokemon) -> Tuple[AbstractPokemon, AbstractPokemon]:
        """
        Determine the first pokemon to attack.
        It compute a random int in [0; 50[ and add it to the pokemon speed.
        The pokemon with the higher speed+rand strike first.
        Args:
            pkmn1 (AbstractPokemon):
            pkmn2 (AbstractPokemon):

        Returns:
            Tuple[AbstractPokemon, AbstractPokemon]: the order
        """

        speed_pkmn1 = pkmn1.speed_current + randint(0, 50)
        speed_pkmn2 = pkmn2.speed_current + randint(0, 50)
        # We do not want any draw. If there is on we reroll
        while speed_pkmn1 == speed_pkmn2:
            speed_pkmn1 = pkmn1.speed_current + randint(0, 50)
            speed_pkmn2 = pkmn2.speed_current + randint(0, 50)
        if speed_pkmn1 > speed_pkmn2:
            first, second = pkmn1, pkmn2
        elif speed_pkmn1 < speed_pkmn2:
            first, second = pkmn2, pkmn1
        return first, second

    def choose_attack(self, pkmn_attcker: AbstractPokemon) -> AbstractAttack:
        """
        Choose the attack used by the pokemon randomly.
        Roll a float in [0;1] :
            <0.95 : choose a  basic attack at random
            >=0.95 : use the special attack

        Args:
            attacker (AbstractPokemon):

        Returns:
            AbstractAttack : an attack
        """

        roll = random()
        if roll < 0.75:
            selected_attack = choice(pkmn_attcker.common_attacks)
        else:
            selected_attack = pkmn_attcker.special_attack

        return selected_attack
