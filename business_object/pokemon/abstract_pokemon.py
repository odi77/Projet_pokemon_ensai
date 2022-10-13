"""classe abstraite pokemon """

from abc import ABC, abstractmethod
from Projet_pokemon_ensai.business_object.statistique import Statistique

class AbstractPokemon(ABC):
    """_summary_

    Parameters
    ----------
    ABC : _type_
        _description_

    Pas d'Examples car classe abstraite

    >>> from Projet_pokemon_ensai.business_object.statistique import Statistique
    >>> grosse_stat = Statistique(100, 100, 100, 100, 100, 100)
    >>> print(grosse_stat._attack)
    100
    """
    # constructeur
    def __init__(self,current_stat:Statistique, level, name):
        """_summary_

        Parameters
        ----------
        current_stat : Statistique
            les stats actuelles du pokemon
        level : int
            _description_
        name : str
            _description_

        Pas d'Examples car classe abstraite
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




if __name__ == "__main__":
    import doctest
    doctest.testmod()