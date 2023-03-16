import random
from toys import Toys

dragon = Toys(10, 'Зеленый', 'Дракоша')
solder = Toys(5, 'Синий', 'Солдатик')
transformer = Toys(20, 'Черный', 'Трансформер')
baba_yga = Toys(13, 'Красный', 'Баба Яга')
colobok = Toys(3, 'Желтый', 'Колобок')

t_l = [dragon, solder, transformer, baba_yga, colobok]
t_d = {}
i = 3

# Добавление значений из словоря и добавление рандомных ключей
for toy in t_l:
    num_d = random.randint(1, 20)
    t_d[num_d] = toy

#print(t_d) # просмотр ключей

while i != 0:
    i = i - 1

    num_win = input('Введите число от 1 до 20: ')
    # проверка правильности ввода
    if num_win.isdigit() == True:
        num_win = int(num_win)
    else:
        print('Нужно вводить число!')
        print(f'Осталось попыток {i}')
        continue

    if 0 > num_win or num_win > 20:
        print('Вы ввели не кореектное число')
        print(f'Осталось попыток {i}')
        continue
    else:
        # розыгрыш
        if num_win in t_d:
            win_toy = t_d.get(num_win)
            print(f'Вы выиграли {win_toy.name}!!!')
            break
        else:
            print('Вы не угадали!')

    print(f'Осталось попыток {i}')
