from abc import ABC, abstractmethod
from random import uniform

from business_object.attack.abstract_attack import AbstractAttack
import business_object.pokemon.abstract_pokemon as pkm


class AbstractFormulaAttack(AbstractAttack):

    def compute_damage(self
                       , pkmn_attcker: pkm.AbstractPokemon
                       , pkmn_targeted: pkm.AbstractPokemon) -> int:
        """
        Return the damage of the attack.

        The basic formula is : (yes it's the Pokemon damage formula)
            (((Niv×0.4+2)×Att×Pui)/(Def×50)+2)×pkemn_coefxother_modifier*random
        and we take the integer part.
        With
            Att = pkmn_attcker's Attack or Special
            Def = pkmn_targeted's Defense or Special
            Pui = attack's power
            pkemn : pkmn_attcker's damage multiplier
            other_modifier = all other modifiers (crit, status, etc)
            random = a random number between 0.85 an d1

        This method is not abstract anymore ! What does this mean ?
            - all sub attack will use the same formula
            - but it can be overridden
            - the Att and Def used for the calculation are not fixed

        To achieve this we need some other abstract methods :
            - get_attack_stat() : get the pkmn_attcker stat_max (attack or spe_atk)
            - get_defense_stat() : get the pkmn_targeted stat_max (defense or spe_def)

        The the template method pattern for more info  :
            -> https://refactoring.guru/design-patterns/template-method

        Args:
            pkmn_attcker (AbstractPokemon): the pkmn_attcker for it's stat_max
            pkmn_targeted (AbstractPokemon): the pkmn_attcker for it's stat_max

        Returns:
            int : the damage

        """
        raw_power = (pkmn_attcker.level * 0.4 + 2) * self.get_attack_stat(pkmn_attcker, pkmn_targeted) * self._power
        raw_damage = raw_power / (self.get_defense_stat(pkmn_attcker,pkmn_targeted) * 50) + 2
        rand = uniform(0.85, 1)
        final_damage = raw_damage \
                       * pkmn_attcker.get_pokemon_attack_coef() \
                       * self.other_modifier_atk(pkmn_attcker) \
                       * self.other_modifier_def(pkmn_targeted) \
                       * rand
        return int(final_damage)

    @abstractmethod
    def get_attack_stat(self
                        , pkmn_attcker: pkm.AbstractPokemon) -> float:
        """
        Get the stat_max use to compute the raw power of the attack.
        We keep the pkmn_targeted because we can want attack based on the
        pkmn_targeted stat like remaining hp.
        Args:
            pkmn_attcker (AbstractPokemon): the pkmn_attcker for it's stat_max
        Returns:
            float : the used stat_max

        """
        pass

    @abstractmethod
    def get_defense_stat(self
                         , pkmn_attcker: pkm.AbstractPokemon) -> float:
        """
        Get the stat_max use to compute the raw damage of the attack.
        We keep the pkmn_attcker because we can want damage reduction based
        on the pkmn_attcker stat like max hp.
        Args:
            pkmn_attcker (AbstractPokemon): the pkmn_attcker for it's stat_max

        Returns:
            float : the used stat_max

        """
        pass


    def other_modifier_atk(self
                           , pkmn_attcker: pkm.AbstractPokemon) -> float:
        """
        Compute all the other modifiers (status mod, etc)
        For this lab it's only a dummy function. It can be
        overridden if needed
        Args:
            pkmn_attcker (AbstractPokemon): the pkmn_attcker

        Returns:

        """
        return 1

    def other_modifier_def(self
                           , pkmn_targeted: pkm.AbstractPokemon) -> float:
        """
        Compute all the other modifiers (status mod, etc)
        For this lab it's only a dummy function. It can be
        overridden if needed
        Args:
            pkmn_targeted (AbstractPokemon): the pkmn_targeted

        Returns:

        """
        return 1
