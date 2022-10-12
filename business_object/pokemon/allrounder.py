"""allrounder
"""

from Projet_pokemon_ensai.business_object.pokemon.abstract_pokemon import AbstractPokemon


class Allrounder(AbstractPokemon):
    """classe Allrounder

    Args:
        AbstractPokemon (classe): classe abstraite

    Examples
    --------
    >>> from business_object.statistique import Statistique
    >>> stat_pikachu = Statistique(20, 20, 20, 10, 10, 15)
    >>> stat_pikachu._attack
    20
    >>> pikachu = Allrounder(stat_pikachu, 1, "Pikachu")
    >>> pikachu._name
    'Pikachu'


    """
    def __init__(self, current_stat, level, name):
        """_summary_

        Parameters
        ----------
        current_stat : Statistique
            les stats du pokemon
        level : int
            le niveau du pokemon
        name : str
            le type du pokemon

        Examples
        ---------

        """
        super().__init__(current_stat, level, name)


    def get_pokemon_attack_coef(self):
        """_summary_

        Returns
        -------
        _type_
            _description_

        Examples
        --------
        >>> from business_object.statistique import Statistique
        >>> stat_pikachu = Statistique(20, 20, 20, 10, 10, 15)
        >>> pikachu = Allrounder(stat_pikachu, 1, "Pikachu")
        >>> pikachu.get_pokemon_attack_coef()
        1.1

        """
        return 1 + (self._current_stat._spe_atk + self._current_stat._spe_def)/200


if __name__ == "__main__":
    import doctest
    doctest.testmod()
