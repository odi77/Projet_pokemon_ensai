from InquirerPy import inquirer
from view.abstract_view import AbstractView
from business_object.pokemon.pokemon_factory import PokemonFactory
from services.attack_service import AttackService
from view.session import Session
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator


class CreatePokemonView(AbstractView):
    def __init__(self):
        self.__id=inquirer.number(message="What is the id of the pokemon ?")
        self.__speed=inquirer.number(message="What is its speed")
        self.__defense=inquirer.text(message="What is its defense")
        self.__level=inquirer.number(message="What is its level ?")
        self.__spe_atk=inquirer.number(message="What is its spe_atk")
        self.__spe_def=inquirer.number(message="What is its spe_def")
        self.__attack=inquirer.number(message="What is its attack ?")
        self.__number_attack=inquirer.number(message="What is the number of Attacks ?")
        self.__hp=inquirer.number(message="What is its health points ?")
        self.__name=inquirer.text(message="What is the name of the pokemon ?")
        self.__type=inquirer.select(message=f'Can you choose the type of Pokemon{Session().user_name}',
        choices=[Choice("Defender"),Choice("Speedster"),Choice("Attacker")
        ,Choice("Supporter"),Separator(),Choice("Au revoir")])

        self.__satisfaction=inquirer.select(message="Etes-vous satisfait ?",
        choices=[Choice("oui"),Separator(),Choice("non")])
    
    def display_info(self):
        type=self.__type.execute()
        poke_factory=PokemonFactory()
        service=AttackService()
        id=self.__id.execute()
        niveau=self.__level.execute()
        hp=self.__hp.execute()
        nom=self.__name.execute()
        speed=self.__speed.execute()
        spe_atk=self.__spe_atk.execute()
        spe_def=self.__spe_def.execute()
        attaque=self.__attack.execute()
        defense=self.__defense.execute()
        nombre_attaques=self.__number_attack.execute()
        liste_attaque=[]
        for i in range(0,int(nombre_attaques)):
            attack=service.get_attack_with_identifier_from_webservice(int(input("Quel est l'identifiant de l'attaque ?")))
            liste_attaque.append(attack)
        pokemon=poke_factory.instantiate_pokemon(type,
        id,hp,attaque,defense,spe_atk,spe_def,
        speed,niveau,nom,liste_attaque)
        Session().selected_pokemon=pokemon
        print(pokemon.common_attacks[0])
        print(pokemon)

    def make_choice(self):
        """L'utilisateur en ayant créé le pokemon peut être satisfait ou non. Il va répondre à cette question. 
        Si oui, on renvoie sur welcome view. Sinon, on recommence le même raisonnement"""
        #mise en session en mettant cette fois comme pokemon le pokemon créé dans la méthode.
        #rappel ) classe singleton donc instanciée qu'une seule fois.  
        if self.__satisfaction.execute()=="oui":
            nextview=WelcomeView()
        else:
            self.make_choice()
        return(nextview)




        