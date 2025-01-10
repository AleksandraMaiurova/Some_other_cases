def mainMenu():
    print('1. Сделать хорошее действие')
    print('2. Сделать плохое действие')
    choice = int(input('Введите номер действия'))
    if choice == 1:
        good()
    elif choice == 2:
        bad()
    else:
        print('Ошибка')
        mainMenu()

def good():
    print('Вы поступили хорошо')
    input('Нажмите любую кнопку чтобы вернуться в меню')
    mainMenu()


def bad():
    print('Вы поступили плохо')
    input('Нажмите любую кнопку чтобы вернуться в меню')
    mainMenu()

mainMenu()