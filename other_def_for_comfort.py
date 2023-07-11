def print_d(n):
    if n == 1:
        print('1 Файл: ')
        with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
            data = file.readlines()
            data_list = list()
            j = 0
            for i in range(len(data)):
                if data[i] == '\n':
                    data_list.append(''.join(data[j:i]))
                    j = i
            print(''.join(data_list))
        return data_list
    

    elif n == 2:
        print('2 Файл: ')
        with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
            data = list(file.readlines())
            print(''.join(data))
        return data