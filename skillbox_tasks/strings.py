"""
1
"""
# string = 'У       нас         пошёл                    снег    !     '
# string = ' '.join(string.split())
# print(string)

"""
2 Срезы создают новые объекты. Лучше использовать методы строк
"""

# path_right = 'C:/user/docs/folder/new_file.txt'
# path_wrong = 'D:/user/docs/folder/new_file.txtx'
# path = input()
# if path.endswith('.txt') and path.startswith('C:'):
#     print('Путь корректен!')
# else:
#     print('Путь не тот!')

"""
3
"""
# string = input()
# low = 0
# up = 0
# for i in string:
#     if i.islower():
#         low += 1
#     elif i == ' ':
#         continue
#     else:
#         up += 1
# if low > up:
#     print(string.lower())
# else:
#     print(string.upper())

"""
4 Форматирование строк внутри вывода. Placeholders. Список тут - https://www.w3schools.com/python/ref_string_format.asp
"""
details = 50000000
price = 23.987242
increase = 0.16546

print("У нас есть {:,d} деталей".format(details))
print("Каждая стоит {:.2f}".format(price))
print("Цена увеличивается на {:%}".format(increase))

