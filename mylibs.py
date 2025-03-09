def welcome_message(message):
    border_style = '=' * len(message)
    print(border_style)
    print(message)
    print(border_style)

def gua():
    str = '|____|'
    array = [str] * 4
    space = ' ' * 5
    len_string = len(space * 3) + len(str) * 4
    border_style = '=' * len_string
    print(border_style)
    print(space, *array, space)
    print(border_style)
    print(f'Berikut adalah 4 gua yang berbeda:')
    print('terdapat gua |1| |2| |3| |4|')