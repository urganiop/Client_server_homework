import yaml

dict_yaml = {
            1: ['a', 'b'],
            2: 5,
            3: {'Ю12': 1, 'Ъ13': 2, 'Ё23': 3}
}

with open('file.yaml', 'w', encoding='utf-8') as f_n:
    yaml.dump(dict_yaml, f_n, default_flow_style=False, allow_unicode=True)

with open('file.yaml', 'r', encoding='utf-8') as f_n:
    data = yaml.load(f_n)
    print(data)
