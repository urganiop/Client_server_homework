import re
import os
import csv


def get_data(file_array):
    names = []
    manufs = []
    codes = []
    types = []
    headers = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    for file in file_array:
        with open(file, 'r') as f:
            for line in f.readlines():
                if line.startswith('Название ОС:'):
                    names.append(re.sub('Название ОС:','',line).strip())
                elif line.startswith('Изготовитель системы:'):
                    manufs.append(re.sub('Изготовитель системы:', '', line).strip())
                elif line.startswith('Код продукта:'):
                    codes.append(re.sub('Код продукта:', '', line).strip())
                elif line.startswith('Тип системы:'):
                    types.append(re.sub('Тип системы:', '', line).strip())

    return [headers, manufs, names, codes, types]


def create_csv(file_array):
    data = get_data(file_array)
    with open('main_data.csv', 'w', encoding='utf-8') as f:
        f_writer = csv.writer(f)
        for row in data:
            f_writer.writerow(row)


if __name__ == '__main__':
    file_names = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    files = list(os.path.join(os.getcwd(), file_name) for file_name in file_names)
    create_csv(files)