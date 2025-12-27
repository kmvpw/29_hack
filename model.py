class Thing:
    """
    Класс для боевых предметов.
    """
    def __init__(self, name:str, protection_percent:float=None, attack:int=None, life:int=None):
        self.name = name
        self.protection_percent = protection_percent
        self.attack = attack
        self.life = life

class Person:
    """
    Базовый класс для персонажей.
    """
    def __init__(self, name:str, hp_quantity:int, base_attack:int, base_protection_percent:float):
        self.name = name
        self.hp_quantity = hp_quantity
        self.base_attack = base_attack
        self.base_protection_percent = base_protection_percent

class Paladin(Person):
    
    
