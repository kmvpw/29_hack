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
            hp_quantity: float,
            base_attack: float,
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
        total_attack = self.base_attack
        for thing in self.things:
            total_attack += thing.attack
        return total_attack

    def finalProtection(self):
        total_protection = self.base_protection_percent
        for thing in self.things:
            total_protection += thing.protection_percent
        return total_protection

    def HitPoints(self):
        for thing in self.things:
            self.hp_quantity += thing.life
        return self.hp_quantity

    def attack(self, target):
        damage = self.attack_damage()*(1 - target.finalProtection())
        target.take_damage(damage)
        return damage

    def take_damage(self, damage):
        self.hp_quantity -= damage
        return damage


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
        