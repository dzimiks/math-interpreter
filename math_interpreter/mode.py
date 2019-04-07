from math_interpreter.interpreter import Interpreter
from math_interpreter.lexer import Lexer
from math_interpreter.calculator import Prefixator, Postfixator

OPERATIONS = ('+', '-', '/', '*', '=', '<', '>', '!')


def prefix_calculation(text, var_storage):
    expression_to_list = []
    number = ''
    length = len(text)
    index = 0

    while index < length:
        c = text[index]

        if c == ' ':
            if number != '':
                expression_to_list.append(number)
                number = ''

            index += 1
            continue

        if c in OPERATIONS:
            if number != '':
                expression_to_list.append(number)
                number = ''

            if c == '<':
                if text[index + 1] == '=':
                    index += 1
                    expression_to_list.append('<=')
                else:
                    expression_to_list.append(c)
            elif c == '>':
                if text[index + 1] == '=':
                    index += 1
                    expression_to_list.append('>=')
                else:
                    expression_to_list.append(c)
            elif c == '!':
                if text[index + 1] == '=':
                    index += 1
                    expression_to_list.append('!=')
                else:
                    expression_to_list.append(c)
            elif c == '=':
                if text[index + 1] == '=':
                    index += 1
                    expression_to_list.append('==')
                else:
                    expression_to_list.append(c)
            else:
                expression_to_list.append(c)
        else:
            number += c

        index += 1

    expression_to_list.append(number)
    c = Prefixator()
    answer = c.convert(expression_to_list)
    ret = '?'
    ret = infix_calculation(answer, var_storage)

    # print('Prefix exp:', expression_to_list)
    # print(answer, '=', ret)
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
    length = len(text)
    index = 0

    while index < length:
        c = text[index]

        if c == ' ':
            if number != '':
                expression_to_list.append(number)
                number = ''

            index += 1
            continue

        if c in OPERATIONS:
            if number != '':
                expression_to_list.append(number)
                number = ''

            if c == '<':
                if index + 1 < length and text[index + 1] == '=':
                    index += 1
                    expression_to_list.append('<=')
                else:
                    expression_to_list.append(c)
            elif c == '>':
                if index + 1 < length and text[index + 1] == '=':
                    index += 1
                    expression_to_list.append('>=')
                else:
                    expression_to_list.append(c)
            elif c == '!':
                if index + 1 < length and text[index + 1] == '=':
                    index += 1
                    expression_to_list.append('!=')
                else:
                    expression_to_list.append(c)
            elif c == '=':
                if index + 1 < length and text[index + 1] == '=':
                    index += 1
                    expression_to_list.append('==')
                else:
                    expression_to_list.append(c)
            else:
                expression_to_list.append(c)
        else:
            number += c

        index += 1

    c = Postfixator()
    answer = c.convert(expression_to_list)
    ret = '?'
    ret = infix_calculation(answer, var_storage)

    # print('Postfix exp:', expression_to_list)
    # print(answer, '=', ret)
    # return answer
    return ret


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

            if text == 'POSTFIX':
                postfix_mode(var_storage)
            elif text == 'PREFIX':
                prefix_mode(var_storage)
            elif text == 'EXIT':
                break

            print(infix_calculation(text, var_storage))
        except EOFError:
            break

        if not text:
            continue

        if text == 'EXIT':
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
