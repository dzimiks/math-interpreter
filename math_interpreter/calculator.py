from math_interpreter.interpreter import Interpreter
from math_interpreter.lexer import Lexer

OPERATIONS = ('+', '-', '/', '*', '=')
OPERATIONS_BIG = ('+', '-', '/', '*', '=', '<', '>', '!')
BOOLS = ('<', '>', '<=', '>=', '!=', '==')


class Prefixator:
    result = ''

    def __init__(self):
        self.stack = []

    def push(self, p):
        if p in OPERATIONS:
            op1 = self.stack.pop()
            op2 = self.stack.pop()
            self.stack.append('(%s %s %s)' % (op1, p, op2))
        elif p in BOOLS:
            op1 = self.stack.pop()
            op2 = self.stack.pop()
            self.stack.append('%s %s %s' % (op1, p, op2))
        else:
            self.stack.append(p)

    def convert(self, l):
        l.reverse()

        for e in l:
            self.push(e)

        result = self.stack.pop()
        print(result)
        return result


class Postfixator:
    result = ''

    def __init__(self):
        self.stack = []

    def push(self, p):
        if p in OPERATIONS:
            op1 = self.stack.pop()
            op2 = self.stack.pop()
            self.stack.append('(%s %s %s)' % (op2, p, op1))
        elif p in BOOLS:
            op1 = self.stack.pop()
            op2 = self.stack.pop()
            self.stack.append('%s %s %s' % (op2, p, op1))
        else:
            self.stack.append(p)

    def convert(self, l):
        for e in l:
            self.push(e)

        result = self.stack.pop()
        return result


def parse_string(text):
    if text is not None and (text.isalpha() or text.isdigit() or text in ('_', '(', ')')):
        return True

    return False


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

        if c in OPERATIONS_BIG:
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
        elif c.isdigit():
            number += c
        else:
            var = ''

            while index + 1 < length and parse_string(text[index + 1]):
                var += text[index]
                index += 1

            var += text[index]
            expression_to_list.append(var)

        index += 1

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
    print(var_storage)
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

        if c in OPERATIONS_BIG:
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
        elif c.isdigit():
            number += c
        else:
            var = ''

            while index + 1 < length and parse_string(text[index + 1]):
                var += text[index]
                index += 1

            var += text[index]
            print('VAR:', var)
            expression_to_list.append(var)

        index += 1

    c = Postfixator()
    answer = c.convert(expression_to_list)
    ret = '?'
    ret = infix_calculation(answer, var_storage)

    print('Postfix exp:', expression_to_list)
    print(answer, '=', ret)
    # return answer
    return ret
