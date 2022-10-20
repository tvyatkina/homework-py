import controller

while True:
    try:
        expression = input('Введите выражение: ')

        if controller.SHOW_ACTIONS:
            print(expression, '= ?')

        expression_without_spaces = controller.remove_spaces(expression)
        answer = controller.work(expression_without_spaces)

        actions = 1

        if controller.SHOW_ACTIONS:
            print('Ответ: ', answer)
        else:
            print(expression, ' = ', answer)
    except:
        break
    break