from view.abstract_view import AbstractView
from view.pokemondetailsview import PokemonDetailsView
from services.pokemon_service import PokemonService


class PokemonListView(AbstractView):
    def __init__(self):
        self.__questions=inquirer.select(message=f'Bonjour{Session().user_name} voulez-vous voir un seul pokemon ?,'
        ,choices=[
            Choice('Voir une liste de 30')
            ,Choice('Voir un pokemon particulier')
            ,Separator()
            ,Choice('Au revoir')]
        )
    def display_info(self):
        """Générer une liste de liste de 30 pokemons sommairement"""
        poke_service=PokemonService()
        vue=poke_service.get_pokemon_from_webservice(30,0)
        print(vue)

    def make_choice(self):
        reponse=self.__questions.execute()
        if reponse=='Voir une liste de 30':
            next_view=self.display_info()
        else:
            next_view=PokemonDetailsView()
        return(nextview)

