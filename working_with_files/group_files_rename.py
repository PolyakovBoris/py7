# Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов
# внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени.
## Например для диапазона [3, 6]
# берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os


def group_renaming(digits_in_counter: int, extension_for_rename: str, extension_for_new_file: str,
                   start_cut_name: int, end_cut_name: int, new_name: str = ''):
    list_files = os.listdir()
    for file_name in list_files:
        *_, extension_in_current_file = file_name.split('.')

        if extension_in_current_file == extension_for_rename:
            name, *_ = file_name.split('.')
            if end_cut_name > len(name):
                print('диапазон обрезки имени файла превышает размер имени файла')
            os.rename(file_name, file_name[start_cut_name:end_cut_name] + new_name + str(digits_in_counter+1) + '.'
                      + extension_for_new_file)
            digits_in_counter =+ 1
            print(f'переименован {file_name}')
