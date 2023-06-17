from random import choices, randint

ALPHABET = 'aejiouubcdfghklmnprstvwxz'

def create_name(extension: str, min_name_len = 6, max_name_len = 30, min_byte = 256, max_byte = 4096, \
                number_of_files = 42) -> None:
    """     Создайте функцию, которая создаёт файлы с указанным расширением.
    Функция принимает следующие параметры:
    ✔ расширение
    ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
    ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
    ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
    ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
    ✔ количество файлов, по умолчанию 42
    ✔ Имя файла и его размер должны быть в рамках переданного диапазона."""

    for _ in range(number_of_files):
        new_file_name = ''
        new_file_name = new_file_name.join(item for item in choices(ALPHABET, k = randint(min_name_len, max_name_len)))

        with open(f'{new_file_name}.{extension}', 'w') as file:
            for _ in range(randint(min_byte, max_byte)):
                file.write(str(randint(0,1)))
                if file.tell() % 64 == 0:
                    file.write('\n')