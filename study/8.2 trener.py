class Character():

    def move(self, direction, distance):

        directions_list = {"north": "на север", "south": "на юг", "west": "на запад", "east": "на восток"}

        if direction == "north":
            print(self.name, "движется", distance, "метров", "на север")
        elif direction == "south":
            print(self.name, "движется", distance, "метров", "на юг")
        elif direction == "west":
            print(self.name, "движется", distance, "метров", "на запад")
        elif direction == "east":
            print(self.name, "движется", distance, "метров", "на восток")
        else:
            print(self.name, "движется непонятно куда")

        if direction not in directions_list.keys():
            print(self.name, "движется непонятно куда")
        else:
            print(self.name, "движется", distance, "метров", directions_list[direction])


class Hero(Character):

    def __init__(self, name):
        self.name = name


class Enemy(Character):

    def __init__(self, name):
        self.name = name


class Enemy():

    def __init__(self, name, health):
        self.is_alive = True;
        self.name = name
        self.health = health


class Dragon(Enemy):

    def bite(self):
        print("я кусаюсь")

    def burn(self):
        print("я дышу огнем")


dragon = Dragon("Инхеритий Проворный", 300)

# Не удаляйте код ниже, это проверка!

dragon.bite()
dragon.burn()


class Hero():

    def __init__(self, name, posessions):
        self.name = name
        self.posessions = posessions

    def __repr__(self):
        return f'Герой {self.name} взял с собой {", ".join(self.posessions)}'


hero = Hero("Питомир", ["меч", "плащ", "шляпа"])
print(hero)


class Box():
    def __init__(self, size, weight, contains):
        self.size = size
        self.weight = weight
        self.contains = contains

    def observe(self):
        return f'Это похоже на ящик размером {self.size} и весом {self.weight}кг'


class Container():
    def open(self):
        return f"В ящике размером {self.size} и ёвесом {self.weight} оказалось {self.contains} апельсин"


box_1 = Container('30x30', 1, '15 золотых монет')
container_1 = Container('50x30', 2, '7 золотых монет')
