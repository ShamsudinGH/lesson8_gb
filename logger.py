from data_create import input_user_data
from other_def_for_comfort import print_d


def input_data():    
    id_u, name, surname, phone, adress = input_user_data()
    var = int(input(f'\nВ каком виде записать данные?\n'
                    f'1 Вариант: \n'
                    f'{id_u}\n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант: \n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'Ваш выбор: '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'\n{id_u}\n'
                       f'{name}\n'
                       f'{surname}\n'
                       f'{phone}\n'
                       f'{adress}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')

    print(f'Данные добавленны в {var} файл')



def print_data():
    print_d(1)
    print_d(2)



def delete_data():
    commad_d = int(input('1 - Удалять из 1-го файла\n'
                     '2 - Удалять из 2-го файла\n'))
    if commad_d == 1:
        l = print_d(1)
        id_del = int(input('Введите id пользователя, которого хотите удалить: ')) -1
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            l = l[0:id_del]+l[id_del+1:len(l)] +['\n']
            for i in l:    
                file.write(i)
        print('Готово!')
    elif commad_d == 2:
        l = print_d(2)
        id_del = int(input('Введите id пользователя, которого хотите удалить: ')) -1
        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            l = l[0:id_del]+l[id_del+1:len(l)] +['\n']
            for i in l:
                file.write(i)
        print('Готово!')

def edit_data():
    commad_e = int(input('1 - Редактировать 1 файл\n'
                     '2 - Редактировать 2 файл\n'))
    if commad_e == 1:
        l = print_d(1)
        id_del = int(input('Введите id пользователя, которого хотите редактировать: ')) -1
        id_u, name, surname, phone, adress = input_user_data()
        l_i = [f'{id_u}\n'
                       f'{name}\n'
                       f'{surname}\n'
                       f'{phone}\n'
                       f'{adress}\n']

        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            l = l[0:id_del] + ['\n'] + l_i + l[id_del+1:len(l)]
            for i in l:    
                file.write(i)
        print('Готово!')

    elif commad_e == 2:
        l = print_d(2)
        id_del = int(input('Введите id пользователя, которого хотите редактировать: ')) -1
        id_u, name, surname, phone, adress = input_user_data()
        l_i = [f'{id_u};{name};{surname};{phone};{adress}\n']

        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            l = l[0:id_del]  + l_i + l[id_del+1:len(l)] + ['\n']
            for i in l:
                file.write(i)
        print('Готово!')
    