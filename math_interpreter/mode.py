from math_interpreter.interpreter import Interpreter
from math_interpreter.lexer import Lexer
from math_interpreter.calculator import Prefixator, Postfixator
from math_interpreter.var_storage import VarStorage

OPERATIONS = ('+', '-', '/', '*', '=', '<', '>')


def prefix_calculation(text, var_storage):
    expression_to_list = []
    number = ''

    for c in text:
        if c == ' ':
            if number != '':
                expression_to_list.append(number)
                number = ''

            continue

        if c in OPERATIONS:
            if number != '':
                expression_to_list.append(number)
                number = ''

            expression_to_list.append(c)
        else:
            number += c
            continue

    expression_to_list.append(number)
    c = Prefixator()
    answer = c.convert(expression_to_list)
    ret = '?'
    ret = infix_calculation(answer, var_storage)

    print('Prefix exp:', expression_to_list)
    print(answer, '=', ret)
    # return answer
    return ret


def infix_calculation(text, var_storage):
    lexer = Lexer(text)
    interpreter = Interpreter(lexer, var_storage)
    result = interpreter.bool()
    return str(result)


def postfix_calculation(text, var_storage):
    expression_to_list = []
    number = ''

    for c in text:
        if c == ' ':
            if number != '':
                expression_to_list.append(number)
                number = ''

            continue

        if c in OPERATIONS:
            if number != '':
                expression_to_list.append(number)
                number = ''

            expression_to_list.append(c)
        else:
            number += c
            continue

    c = Postfixator()
    answer = c.convert(expression_to_list)
    ret = '?'
    ret = infix_calculation(answer, var_storage)

    print('Postfix exp:', expression_to_list)
    print(answer, '=', ret)
    # return answer
    return ret


def prefix_mode():
    while True:
        try:
            text = input('PREFIX -> ')

            if text == 'INFIX':
                infix_mode()
            elif text == 'POSTFIX':
                postfix_mode()
            elif text == 'EXIT':
                break

            print(prefix_calculation(text))
        except EOFError:
            break

        if not text:
            continue

        if text == 'EXIT':
            break


def infix_mode():
    var_storage = VarStorage()

    while True:
        try:
            text = input('INFIX -> ')

            if text == 'POSTFIX':
                postfix_mode()
            elif text == 'PREFIX':
                prefix_mode()
            elif text == 'EXIT':
                break

            print(infix_calculation(text, var_storage))
        except EOFError:
            break

        if not text:
            continue

        if text == 'EXIT':
            break


def postfix_mode():
    while True:
        try:
            text = input('POSTFIX -> ')

            if text == 'INFIX':
                infix_mode()
            elif text == 'PREFIX':
                prefix_mode()
            elif text == 'EXIT':
                break

            print(postfix_calculation(text))
        except EOFError:
            break

        if not text:
            continue

        if text == 'EXIT':
            break
