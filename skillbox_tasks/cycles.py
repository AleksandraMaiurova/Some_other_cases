"""
1 While
"""

# count = 10
# while count <= 10:
#     if count == 0:
#         print('Время вышло!')
#         break
#     else:
#         print(count)
#         count -= 1

"""
2
"""

# print('Продолжаем работать? 1/0: ')
# number = int(input())
# while True:
#     if number == 0:
#         print('Приложение закрывается…')
#         break
#     else:
#         print('Продолжаем работать? 1/0: ')
#         number = int(input())
# print('Работа завершена')

"""
3
"""
# code = 1
# while True:
#     if code != 550:
#         print('Компьютер заблокирован. Вернёшь скейт - скажу код разблокировки!')
#         print('Введите код:')
#         code = int(input())
#     else:
#         print('Код верный, завершаю работу...')
#         break
# print('Работа завершена')


"""
4
"""

# print('Введите количество строчек:')
# num = int(input())
# per = 0
# while per < num:
#     per += 1
#     print('Я — программист!')


"""
5
"""

# temp_list = []
# error = 0
# while True:
#     print('Какая температура на датчике?')
#     num = int(input())
#     if num not in temp_list:
#         temp_list.append(num)
#     else:
#         print(f'Внимание: дублирующее значение температуры {num} обнаружено!')
#         error += 1
#         print('Зафиксировано сбоев датчика:', error)
#         print('Хотите продолжить сбор данных? 1 — да, 0 — нет:')
#         want_continue = int(input())
#         if not want_continue:
#             print('Сбор данных остановлен.')
#             break


"""
For 1
"""


# for meters in (100,90,95,87,102):
#     if meters % 3 == 0:
#         print(meters, 'Подходит')
#     else:
#         print(meters, 'Не подходит')

"""
For 2
"""
#num = int(input())
#for numbers in range(num):
#    print ('Ку-ку!')

"""
For 3
"""
# print('Введите первое число:')
# num = int(input())
# print('Введите первое число:')
# mun = int(input())
# sum = 0
# for i in range (num, mun+1):
#     sum = sum+i
# print(f'Сумма чисел от {num} до {mun} равна {sum}')

"""
For 4
"""
# print('Общее время эксперимента:')
# hours_total = int(input())
# print('Сколько прошло?')
# hours = int(input())
# cells = 1
#
# for i in range(1,hours+1):
#     if i % 3 == 0:
#         cells *= 2
#         print('Количество часов:', hours_total)
#         print('Прошло часов:', i)
#         print('Количество клеток:', cells)
#         print('Осталось часов:', hours_total-i)

"""
For 4
"""
# wake_up = int(input())
# N = int(input())
# volume = 0
# cal = 0
# for i in range (wake_up, 23, 3):
#     cal +=N
#     volume += 1
# print (cal, volume)

"""
For 5
"""

# N = int(input())
# for i in range(N+1):
#     for j in range(N+1):
#         print(i+j, end="\t")
#     print()

"""
For 6
"""
# N = int(input())
# for i in range(N+1):
#     for j in range(N+1):
#         if i+j > N:
#             continue
#         else:
#             print(i+j, end="\t")
#     print()

"""
For 6 Блок else для цикла
"""

while True:
    for attempt in range (1,4):
        pin = int(input())
        if pin == 1234:
            print('Верный пин!')
            break
        print('Неверный код, осталось попыток', 3-attempt)
    else:
        print('Ваша карта заблокирована')