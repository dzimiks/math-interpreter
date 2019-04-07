from math_interpreter.interpreter import Interpreter
from math_interpreter.lexer import Lexer
from math_interpreter.calculator import Prefixator, Postfixator

OPERATIONS = ('+', '-', '/', '*', '=')


def prefix_calculation(text):
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
    ret = infix_calculation(answer)

    print('Prefix exp:', expression_to_list)
    print(answer, '=', ret)
    # return answer
    return ret


def infix_calculation(text):
    lexer = Lexer(text)
    interpreter = Interpreter(lexer)
    result = interpreter.bool()
    return str(result)


def postfix_calculation(text):
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
    ret = infix_calculation(answer)

    print('Postfix exp:', expression_to_list)
    print(answer, '=', ret)
    # return answer
    return ret


def prefix_mode():
    while True:
        try:
            text = input('prefix -> ')

            if text == 'infix':
                infix_mode()
            elif text == 'postfix':
                postfix_mode()
            elif text == 'exit':
                break

            print(prefix_calculation(text))
        except EOFError:
            break

        if not text:
            continue

        if text == 'exit':
            break


def infix_mode():
    while True:
        try:
            text = input('infix -> ')

            if text == 'postfix':
                postfix_mode()
            elif text == 'prefix':
                prefix_mode()
            elif text == 'exit':
                break

            print(infix_calculation(text))
        except EOFError:
            break

        if not text:
            continue

        if text == 'exit':
            break


def postfix_mode():
    while True:
        try:
            text = input('postfix -> ')

            if text == 'infix':
                infix_mode()
            elif text == 'prefix':
                prefix_mode()
            elif text == 'exit':
                break

            print(postfix_calculation(text))
        except EOFError:
            break

        if not text:
            continue

        if text == 'exit':
            break
