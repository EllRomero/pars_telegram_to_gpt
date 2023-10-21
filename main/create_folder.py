from os import makedirs


def create_fold(name: str):
    try:
        makedirs(f'{name}')
        print(f'Создаем деррикторию {name}')
    except FileExistsError:
        print(f'Дерриктория найдена {name}')
    

