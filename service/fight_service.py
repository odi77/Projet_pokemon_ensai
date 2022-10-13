"""classe Fight service
une seule instance possible

"""

# from utils.singleton import Singleton #Il faut télécharger le module utils du corrigé de Rémi.

from Projet_pokemon_ensai.business_object.pokemon.abstract_pokemon import AbstractPokemon

class FightService(metaclass=Singleton):
    """Classe FightService"""

    def get_role_multiplier(self, pokemon1:AbstractPokemon,
                        pokemon2:AbstractPokemon):



                        pass




