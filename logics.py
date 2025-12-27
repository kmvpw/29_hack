def main():
    things = [
        Thing('Шлем', 0.05, 0, 10),
        Thing('Кольцо', 0.02, 5, 0),
        Thing('Кольчуга', 0.1, 2, 30),
        Thing("Амулет", 0.03, 3, 5),
        Thing("Сапоги", 0.04, 0, 10),
        Thing("Меч", 0.0, 10, 0),
    ]
    things.sort()

    names = [
        'Ахиллес', 'Рагнар', 'Гектор', 'Геракл', 'Шансунг',
        'Терминатор', 'Джеки Чан', 'Сабзиро', 'Рейден', 'Супермэн',
        'Бэтмен', 'Король Артур', 'Рокки', 'Скорпион', 'Персей',
        'Один', 'Тор', 'Локки', 'Брюс Ли', 'Чак Норрис'
    ]

    characters=[]

    for _ in range(10):
        name = random.choice(names)
        hp_quantity = random.randint()
        base_attack = random.randint()
        base_protection_percent = 

        cls = random.choice([Paladin, Warrior])
        characters.append(cls(name, hp_quantity, base_attack, base_protection_percent))

    for character in characters:
        character.set_things(random.choice(things))

    def battle():
        attacker = characters.pop(random.randint(0, len(characters) - 1))
        defender = characters.pop(random.randint(0, len(characters) - 1))

    


