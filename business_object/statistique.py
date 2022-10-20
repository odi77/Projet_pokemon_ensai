"""classe statistique pour les stat d'un pokemon
"""

class Statistique:
    """les statistiques de combat du Pokemon

    Examples
    --------
    >>> grosse_stat = Statistique(100, 100, 100, 100, 100, 100)
    >>> type(grosse_stat)
    <class '__main__.Statistique'>
    >>> print(grosse_stat._attack)
    100
    """
    def __init__(self,
                    hp,
                    attack,
                    defense,
                    spe_atk,
                    spe_def,
                    vitesse):
        """_summary_

        Parameters
        ----------
        hp : int
            points de vie
        attack : int
            force de l'attaque
        defense : int
            force de la défense
        spe_atk : int
            vitesse de l'attaque
        spe_def : int
            vitesse de la défense
        vitesse : int
            vitesse du pokemon
        """
        self._hp = hp
        self._attack = attack
        self._vitesse = vitesse
        self._spe_atk = spe_atk
        self._spe_def = spe_def
        self._vitesse = vitesse

if __name__ == "__main__":
    import doctest
    doctest.testmod()
