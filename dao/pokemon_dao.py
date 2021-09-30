from typing import List
from business_object.pokemon.pokemon_factory import PokemonFactory
from dao.attack_dao import AttackDao
from utils.singleton import Singleton
from dao.db_connection import DBConnection
from business_object.pokemon.abstract_pokemon import AbstractPokemon


class PokemonDao(metaclass=Singleton):

    def find_all(self
                , limit: int = 100
                , offset: int = 0) -> List[AbstractPokemon]:
        request = f"SELECT * " \
                  f"\nFROM pokemon JOIN pokemon_type ON pokemon_type.id_type_pokemon=pokemon.id_pokemon_type  "\
                  f"JOIN pokemon_type type ON pokemon.id_pokemon_type=type.id_type_pokemon" \
                  f"\nLIMIT {max(limit, 0)} OFFSET {max(offset, 0)}"

        with DBConnection().connection as connection:
                    with connection.cursor() as cursor :
                        cursor.execute(
                            request
                        )
                        res = cursor.fetchall()

        pokemons = []
        pkmn_factory = PokemonFactory()
        for row in res:
            pokemon = pkmn_factory.instantiate_pokemon(
                type= row["pokemon_type_name"]
                , hp=row["hp"]
                , attack=row["attack"]
                , defense=row["defense"]
                , sp_atk=row["spe_atk"]
                , sp_def=row["spe_def"]
                , speed=row["speed"]
                , level=row["level"]
                , name=row["name"])
            pokemons.append(pokemon)
        return pokemons

    def find_pokemon_by_name(self, name:str)-> AbstractPokemon:
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT * " \
                    "\nFROM pokemon JOIN pokemon_type ON pokemon_type.id_type_pokemon=pokemon.id_pokemon_type  "\
                    "\nJOIN pokemon_type type ON pokemon.id_pokemon_type=type.id_type_pokemon" \
                    "\nWHERE pokemon.name = %(name)s"
                    , {"name": name}
                )
                res = cursor.fetchone()
            pokemon = None
            pkmn_factory = PokemonFactory()
            if res :
                attacks = AttackDao().find_all_attacks_by_id_pokemon(res["id_pokemon"])
                pokemon = pkmn_factory.instantiate_pokemon(
                    type= res["pokemon_type_name"]
                    , id=res["id_pokemon"]
                    , hp=res["hp"]
                    , attack=res["attack"]
                    , defense=res["defense"]
                    , sp_atk=res["spe_atk"]
                    , sp_def=res["spe_def"]
                    , speed=res["speed"]
                    , level=res["level"]
                    , name=res["name"]
                    , common_attacks=attacks)
            

        return pokemon