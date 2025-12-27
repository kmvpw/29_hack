from random import randint, sample


class Thing:
    """
    Класс для боевых предметов.
    """
    def __init__(
            self,
            name: str,
            protection_percent: float = 0,
            attack: int = 0,
            life: int = 0
            ):
        self.name = name
        self.protection_percent = protection_percent
        self.attack = attack
        self.life = life


class Person:
    """
    Базовый класс для персонажей.
    """
    def __init__(
            self,
            name: str,
            hp_quantity: int,
            base_attack: int,
            base_protection_percent: float
        ):
        self.name = name
        self.hp_quantity = hp_quantity
        self.base_attack = base_attack
        self.base_protection_percent = base_protection_percent
        self.things = []

    def set_things(self, things: list):
        num_to_select = randint(1, 4)
        selected = sample(things, num_to_select)
        self.things.extend(selected)

    def attack_damage(self):
        for thing in self.things:
            self.base_attack += thing.attack
        return self.base_attack

    def finalProtection(self):
        for thing in self.things:
            self.base_protection_percent += thing.protection_percent
        return self.base_protection_percent

    def HitPoints(self):
        for thing in self.things:
            self.hp_quantity += thing.life
        return self.hp_quantity


class Paladin(Person):
    def __init__(
            self,
            name,
            hp_quantity,
            base_attack,
            base_protection_percent
    ):
        super().__init__(
            name,
            hp_quantity,
            base_attack,
            base_protection_percent
        )
        self.hp_quantity = 2*hp_quantity
        self.base_protection_percent = 2*base_protection_percent


class Warrior(Person):
    def __init__(
            self,
            name,
            hp_quantity,
            base_attack,
            base_protection_percent
    ):
        super().__init__(
            name,
            hp_quantity,
            base_attack,
            base_protection_percent
        )
        self.base_attack = 2*base_attack
