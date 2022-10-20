from view.abstract_view import AbstractView
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from view.start_view import StartView
from services.pokemon_service import PokemonService

class PokemonDetailsView(AbstractView):
    def __init__():
        self.__questions=inquirer.select(message=f'Bonjour{Session().user_name} voulez-vous les statistiques ou les attaques ?,'
        ,choices=[
            Choice('Voir les statistiques')
            ,Choice('Revenir sur les autres pokemons')
            ,Choice('Revenir sur la vue de départ')
            ,Separator()
            ,Choice('Au revoir')]
        )
    def display_info(self):
        nom=input("Donner le nom du pokemon")
        id=int(input("Donner l'identifiant du pokemon"))
        pokemon_renvoi=Pokemon_Service()
        print(pokemon_renvoi.get_pokemon_with_identifier_from_webservice(Union[id,nom]))
    
    def make_choice():
        reponse=self.__questions.execute()
        if reponse=="Voir les statistiques":
            next_view=StartView()
        elif reponse=="Revenir sur les autres pokemons":
            next_view=PokemonListView()
        else:
            next_view=StartView()
        return(next_view)
