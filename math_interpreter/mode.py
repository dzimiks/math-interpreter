from math_interpreter.calculator import prefix_calculation, infix_calculation, postfix_calculation


def prefix_mode(var_storage):
    while True:
        try:
            text = input('PREFIX -> ')

            if text == 'INFIX':
                infix_mode(var_storage)
            elif text == 'POSTFIX':
                postfix_mode(var_storage)
            elif text == 'EXIT':
                break

            print(prefix_calculation(text, var_storage))
        except EOFError:
            break

        if not text:
            continue

        if text == 'EXIT':
            break


def infix_mode(var_storage):
    while True:
        try:
            text = input('INFIX -> ')
            print(text)

            if text == 'POSTFIX':
                postfix_mode(var_storage)
            elif text == 'PREFIX':
                prefix_mode(var_storage)
            elif text == 'EXIT':
                print('AAA')
                break

            print(infix_calculation(text, var_storage))
        except EOFError:
            break

        if not text:
            continue

        if text == 'EXIT':
            print('YYY')
            break


def postfix_mode(var_storage):
    while True:
        try:
            text = input('POSTFIX -> ')

            if text == 'INFIX':
                infix_mode(var_storage)
            elif text == 'PREFIX':
                prefix_mode(var_storage)
            elif text == 'EXIT':
                break

            print(postfix_calculation(text, var_storage))
        except EOFError:
            break

        if not text:
            continue

        if text == 'EXIT':
            break
