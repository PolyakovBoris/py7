from pathlib import Path


def mult_name_files(file_name1, file_name2, file_name3):
    """Напишите функцию, которая открывает на чтение созданные
    в прошлых задачах файлы с числами и именами.
    ✔ Перемножьте пары чисел. В новый файл сохраните
    имя и произведение:
    ✔ если результат умножения отрицательный, сохраните имя
    записанное строчными буквами и произведение по модулю
    ✔ если результат умножения положительный, сохраните имя
    прописными буквами и произведение округлённое до целого.
    ✔ В результирующем файле должно быть столько же строк,
    сколько в более длинном файле.
    ✔ При достижении конца более короткого файла,
    возвращайтесь в его начало.
    """
    file1 = Path(file_name1)
    file2 = Path(file_name2)
    file3 = Path(file_name3)
    with (open(file1, 'r', encoding='utf-8') as f1_num,
        open(file2, 'r', encoding='utf-8') as f2_names):
            file1_len = sum(1 for _ in f1_num)
            file2_len = sum(1 for _ in f2_names)
            min_file = f1_num if file1_len < file2_len else f2_names
            f1_num.seek(0,0)
            f2_names.seek(0,0)
            for line in range(max(file1_len, file2_len)):
                if line == min(file1_len, file2_len):
                    min_file.seek(0,0)
                num1, num2 = f1_num.readline().split('/')
                num1 = float(num1)
                num2 = float(num2)
                mult_nums: float = num1 * num2
                name = f2_names.readline().replace('\n', ' ')
                if mult_nums > 0:
                    with open(file3,'a',encoding='utf-8') as f3:
                        f3.write(f'{name.lower()}{int(mult_nums)}\n')
                else:
                    with open(file3,'a',encoding='utf-8') as f3:
                        f3.write(f'{name.upper()}{abs(mult_nums)}\n')


