from business_object.attack.abstract_attack import AbstractAttack
from business_object.attack.fixed_damage_attack import FixedDamageAttack
from business_object.attack.physical_attack import PhysicalFormulaAttack
from business_object.attack.special_attack import SpecialFormulaAttack
from utils.singleton import Singleton


class AttackFactory(metaclass=Singleton):
    def instantiate_attack(self
                            , type:str
                            , power: int = None
                            , name: str = None
                            , description: str = None )->AbstractAttack:
        """
        Instantiate an AbstractAttack based on the provided type

        :param type: the attack type
        :type type: str
        :param power: the attack power, defaults to None
        :type power: int, optional
        :param name: the attack name, defaults to None
        :type name: str, optional
        :param description: the attack descritpion, defaults to None
        :type description: str, optional
        :raises Exception: if the type is unknown, an exception is raised
        :return: the instantiate attack
        :rtype: AbstractAttack
        """
        if type=="special attack":
            attack = SpecialFormulaAttack(power=power
                                        , name=name
                                        , description=description
                                    )
        elif type=="physical attack":
            attack = PhysicalFormulaAttack(power=power
                                        , name=name
                                        , description=description
                                    )
        elif type=="fixed damage":
            attack = FixedDamageAttack(power=power
                                        , name=name
                                        , description=description
                                    )
        else :
            raise Exception(f"Le type {type} n'est pas utilisé")
        return attack