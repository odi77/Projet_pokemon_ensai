"""classe statistique pour les stat d'un pokemon
"""

class Statistique:
    """_summary_
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