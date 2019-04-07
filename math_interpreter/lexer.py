from math_interpreter.token import Token, TokenType


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Unexpected char {}!'.format(self.current_char))

    def advance(self):
        self.pos += 1

        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def integer(self):
        number = ''

        while self.current_char is not None and self.current_char.isdigit():
            number += self.current_char
            self.advance()

        return int(number)

    def string(self):
        string = ''

        while self.current_char is not None and (
                self.current_char.isalpha() or self.current_char.isdigit() or self.current_char == '_'):
            string += self.current_char
            self.advance()

        print('Parsed str:', string)
        return string

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()

            # if self.current_char.isalpha():
            #     string = self.string()
            #     print('get_next_token alpha:', string)
            #
            #     if string == 'RIM':
            #         # print('curr char:', self.current_char)
            #
            #         if self.current_char == '(':
            #             string += self.current_char
            #             self.advance()
            #
            #     if len(string) > 3 and string[:4] == 'RIM(':
            #         return Token(TokenType.ROMAN, string)
            #
            #     return Token(TokenType.STRING, string)

            if self.current_char.isalpha():
                return Token(TokenType.STRING, self.string())

            if self.current_char.isdigit():
                return Token(TokenType.INT, self.integer())

            if self.current_char == '+':
                self.advance()
                return Token(TokenType.ADD, '+')

            if self.current_char == '-':
                self.advance()
                return Token(TokenType.SUB, '-')

            if self.current_char == '*':
                self.advance()
                return Token(TokenType.MUL, '*')

            if self.current_char == '/':
                self.advance()
                return Token(TokenType.DIV, '/')

            if self.current_char == '(':
                self.advance()
                return Token(TokenType.OPENED_PAREN, '(')

            if self.current_char == ')':
                self.advance()
                return Token(TokenType.CLOSED_PAREN, ')')

            # if self.current_char == ':':
            #     self.advance()
            #
            #     if self.current_char == '=':
            #         self.advance()
            #         return Token(TokenType.ASSIGN, ':=')

            if self.current_char == '<':
                self.advance()

                if self.current_char == '=':
                    self.advance()
                    return Token(TokenType.LTE, '<=')

                return Token(TokenType.LT, '<')

            if self.current_char == '>':
                self.advance()

                if self.current_char == '=':
                    self.advance()
                    return Token(TokenType.GTE, '>=')

                return Token(TokenType.GT, '>')

            if self.current_char == '=':
                self.advance()

                if self.current_char == '=':
                    self.advance()
                    return Token(TokenType.EQ, '==')
                else:
                    return Token(TokenType.ASSIGN, '=')

            if self.current_char == '!':
                self.advance()

                if self.current_char == '=':
                    self.advance()
                    return Token(TokenType.NE, '!=')

                self.error()

            self.error()

        return Token(TokenType.EOF, None)
