# 3.3. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
#Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
#Достаточно вернуть один допустимый вариант.

from operator import itemgetter

my_diction = {'палатка': 5, 'посуда': 3, 'надувная лодка': 7, 'спальный мешок': 1, 'удочка': 1, 'мангал': 2, 'рыболовные снасти': 6}
max_capacity_backpack = 15
weight = 0
capacity_backpack = 0
print("Рюкзак: ", my_diction)
print("Список вещей по максимально возможной грузоподьемности рюкзака в ", max_capacity_backpack, "кг")
for things, value in dict(sorted(my_diction.items(), key=itemgetter(1))).items():
    weight += my_diction[things]

    if weight <= max_capacity_backpack:
        print(things, ' = ', value)
        capacity_backpack += my_diction[things]

print("Общий вес рюкзака c вещами: ", capacity_backpack, "кг")

