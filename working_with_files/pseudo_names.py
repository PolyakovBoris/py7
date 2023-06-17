from random import randint, choice
from pathlib import Path

GLAS = 'aejiouu'
SOGL = 'bcdfghklmnprstvwxz'


def generate_names(names_amount: int, file_name: str):
#     """
#     ✔ Напишите функцию, которая генерирует
#     псевдоимена.
#     ✔ Имя должно начинаться с заглавной буквы,
#     состоять из 4-7 букв, среди которых
#     обязательно должны быть гласные.
#     ✔ Полученные имена сохраните в файл
#     """

    for _ in range(names_amount):
        name_len = randint(4,7)
        name: str = ''

        for letter in range(name_len):
            name = (name + choice(SOGL) if letter % 2 == 0 else name + choice(GLAS)).capitalize()

        with open(Path(file_name), 'a', encoding='utf-8') as file:
            file.write(name + '\n')