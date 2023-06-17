from random import randint, uniform
from pathlib import Path


MIN = -1000
MAX = 1000

def generate_and_append_numbers(lines_amount: int, file_name: str):
    """
    1. Напишите функцию, которая заполняет файл
    (добавляет в конец) случайными парами чисел.
    ✔ Первое число int, второе - float разделены вертикальной чертой.
    ✔ Минимальное число - -1000, максимальное - +1000.
    ✔ Количество строк и имя файла передаются как аргументы функции
    """
    with open(Path(file_name), 'a', encoding='utf-8') as file:
        for line in range(lines_amount):
            file.write(f'{randint(MIN, MAX)}/{uniform(MIN, MAX)}\n')
