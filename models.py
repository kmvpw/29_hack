class Person:
    """
    Базовый класс для персонажей.
    """
    def __init__(self, name:str, hp_quantity:int, base_attack:int, base_protection_percent:float):
        self.name = name
        self.hp_quantity = hp_quantity
        self.base_attack = base_attack
        self.base_protection_percent = base_protection_percent
        
    def set_thhings(things):
        
class Paladin(Person):
    def __init__(self, name, hp_quantity, base_attack, base_protection_percent):
        super().__init__(name, hp_quantity, base_attack, base_protection_percent)
        self.hp_quantity = 2*hp_quantity
        self.base_protection_percent = 2*base_protection_percent
      
class Warrior(Person): 
    def __init__(self, name, hp_quantity, base_attack, base_protection_percent):
        super().__init__(name, hp_quantity, base_attack, base_protection_percent)
        self.base_attack = 2*base_attack