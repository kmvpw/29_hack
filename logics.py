import random

from model import Thing, Person, Warrior, Paladin


things = [
    Thing('Шлем', 0.05, 0, 10),
    Thing('Кольцо', 0.02, 5, 0),
    Thing('Кольчуга', 0.10, 2, 30),
    Thing("Амулет", 0.03, 3, 5),
    Thing("Сапоги", 0.04, 0, 10),
    Thing("Меч", 0.0, 10, 0),
]
things.sort(key=lambda x: x.protection_percent)

names = [
    'Ахиллес', 'Рагнар', 'Гектор', 'Геракл', 'Шансунг',
    'Терминатор', 'Джеки Чан', 'Сабзиро', 'Рейден', 'Супермэн',
    'Бэтмен', 'Король Артур', 'Рокки', 'Скорпион', 'Персей',
    'Один', 'Тор', 'Локки', 'Брюс Ли', 'Чак Норрис'
]

characters = []

for _ in range(10):
    name = random.choice(names)
    hp_quantity = random.randint(80, 120)
    base_attack = random.randint(10, 20)
    base_protection_percent = round(random.uniform(0.05, 0.10), 2)

    cls = random.choice([Paladin, Warrior])
    characters.append(cls(name, hp_quantity, base_attack, base_protection_percent))

for character in characters:
    character.set_things(things)

while len(characters) > 1:
    attacker, defender = random.sample(characters, 2)

    damage = attacker.attack(defender)

    print(
        f'{attacker.name} наносит удар по {defender.name} '
        f'на {damage:.1f} урона'
    )

    if defender.hp_quantity <= 0:
        print(f'{defender.name} выбыл из боя\n')
        characters.remove(defender)

print(f'ПОБЕДИТЕЛЬ: {characters[0].name}')





    


