from typing import List, Optional
from business_object.attack.abstract_attack import AbstractAttack
from dao.db_connection import DBConnection
from utils.singleton import Singleton
class TypeAttackDAO(metaclass=Singleton):
    """
    Communicate with the attack_type table
    """

    def find_all_attack_type(self)->List[str] :
        """
        Get all the attack_type and return a list with all the type

        :return: A list with all the type
        :rtype: List of str
        """
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT * FROM attack_type"
                )
                res = cursor.fetchall()
        type_attack:List[str] = []
        if res :
            for row in res :
                type_attack.append(row["attack_type_name"])
        return type_attack

    def find_id_by_label(self, label:str)->Optional[int]:
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT id_attack_type FROM attack_type "
                    "WHERE attack_type_name = %(attack_name)s"
                , {"attack_name":label})
                res = cursor.fetchone()
        if res:
            return res["id_attack_type"]

    
