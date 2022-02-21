import random
import math
from typing import Any


def hero() -> list:
    '''Hero generator'''
    return [random.randint(10, 20), 10]


def monster() -> list:
    '''Monster generator'''
    return [random.randint(20, 30), random.randint(2, 4)]


def apple() -> list:
    '''Apple generator'''
    android = [random.randint(2, 5)]
    print('Герой нашел яблоко. Чавкая и давясь сожрал и '
          'поздоровел аж на', android[0])
    return android


def sword() -> list:
    '''Sword generator'''
    swrd = [random.randint(7, 15)]
    print('Герой встретил карликов Оглафа, сковавших чудесный МЕЧ силой в',
          swrd[0], ". Брать будете?  1 - да, 2 - нет")
    return swrd


def choice() -> Any:
    '''Choice function'''
    num = (input("Введите 1 или 2: "))
    if num in ['1', '2']:
        print("----")
        return int(num)
    else:
        print("Это не 1 и даже не 2, друг")
        choice()


def game() -> Any:
    '''Main game function'''
    hero_1 = hero()  # вызываем Героя
    global attack, hp, monster_counter
    hp = hero_1[0]
    attack = hero_1[1]
    while monster_counter < 10:
        accidental = random.randint(1, 3)  # рандомим один из трех вариантов
        if accidental == 1:
            omnom = apple()
            hp = hp + omnom[0]
            print("Здоровье героя", hp, "и меч на", attack)
            print("----")
        elif accidental == 2:
            swr = sword()
            if choice() == 1:
                attack = swr[0]
                print("Здоровье героя", hp, "и меч на", attack)
                print("----")
        else:
            mo1 = monster()
            print("БОЙ! Геройчик встречает монстра с", mo1[0], "жизнями и силой",
                  mo1[1], "Будем бить? 1 - да, 2 - нет")
            if choice() == 1:
                hp = hp - mo1[1] * (math.ceil(mo1[0] / attack))
                print("Здоровье героя", hp, "и меч на", attack)
                monster_counter = monster_counter + 1
                if hp <= 0:
                    return print("ПОРАЖЕНИЕ, боец откис на", monster_counter - 1, "фрагах")
                print("Итого", monster_counter, "фрагов")
                print("----")
    else:
        return print("ПОБЕДА, добро пожаловать на пенсию")


monster_counter = 0
hp = 0
attack = 0
game()
