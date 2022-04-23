fish = [

    {"specie": "Белуга", "water": "fresh"},
    {"specie": "Карась", "water": "fresh"},
    {"specie": "Красноперка", "water": "fresh"},

    {"specie": "Морской окунь", "water": "sea"},
    {"specie": "Тунец", "water": "sea"},
    {"specie": "Скумбрия", "water": "sea"},

]

sea_water = []
fresh_water = []

for indigo in fish:
    if indigo["water"] == "fresh":
        fresh_water.append(indigo['specie'])
    else:
        sea_water.append(indigo['specie'])

print(f"Морские: {', '.join(sea_water)}")
print(f"Пресноводные: {', '.join(fresh_water)}")

order = [
    {"skolko": 5.0, "poroda": "тунец", "sred_razmer": 300},
    {"skolko": 15.0, "poroda": "окунь", "sred_razmer": 250},
    {"skolko": 20.0, "poroda": "щука", "sred_razmer": 460},
]
order_converted = []

for fish in order:
    new_fish = {'count': int(fish["skolko"]), 'specie': fish["poroda"].title(), "avg_size": fish["sred_razmer"] // 10}
    order_converted.append(new_fish)

ponds = [
    {"pk": 1, "volume": 10000, "fish": "тунец"},
    {"pk": 192, "volume": 20000, "fish": "морская камбала"},
    {"pk": 206, "volume": 10000, "fish": "треска"},
    {"pk": 322, "volume": 25000, "fish": "тунец"},
    {"pk": 420, "volume": 20000, "fish": "морская камбала"},
    {"pk": 704, "volume": 10000, "fish": "треска"},
    {"pk": 920, "volume": 25000, "fish": "тунец"},
]

for i in ponds:
    if i["fish"] == "тунец":
        ponds.remove(i)

for pond in ponds:
    print(pond["pk"])

fish = [

    {"specie": "Белуга", "water": "fresh"},
    {"specie": "Карась", "water": "fresh"},
    {"specie": "Красноперка", "water": "fresh"},

    {"specie": "Морской окунь", "water": "sea"},
    {"specie": "Тунец", "water": "sea"},
    {"specie": "Скумбрия", "water": "sea"}, ]


def get_fish(fish_name):
    for i in fish:
        if i["specie"] == fish_name:
            fishsd, water = i["specie"], i["water"]
            return fishsd, water
