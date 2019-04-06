from math_interpreter.interpreter import Interpreter
from math_interpreter.lexer import Lexer
from math_interpreter.calculator import Calculator

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
            expression_to_list.append(c)
        else:
            number += c
            continue

    expression_to_list.append(number)
    c = Calculator()

    print(expression_to_list)
    return c.convert(expression_to_list)
    # return infix_calculation(c.convert(expression_to_list))


def infix_calculation(text):
    lexer = Lexer(text)
    interpreter = Interpreter(lexer)
    result = interpreter.bool()
    return str(result)


def postfix_calculation(text):
    return text


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
