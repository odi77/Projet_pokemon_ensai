"""classe abstraite pokemon """

from abc import ABC, abstractmethod
from ... import Statistique

class AbstractPokemon(ABC):
    """_summary_

    Parameters
    ----------
    ABC : _type_
        _description_
    """
    # constructeur
    def __init__(self, current_stat:Statistique, level, name):
        """_summary_

        Parameters
        ----------
        current_stat : _type_
            _description_
        level : _type_
            _description_
        name : _type_
            _description_
        """
        self._current_stat = current_stat
        self._name = name
        self._level = level

    @abstractmethod
    def get_pokemon_attack_coef(self):
        """méthode abstraite
        """

    def level_up(self):
        """augmente le niveau du pokemon de 1 (commun à tous les pokemon)
        """
        self._level += 1
