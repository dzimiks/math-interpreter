from token import Token
from token_type import TokenType


class Interpreter():
    def __init__(self, text):
        self.pos = 0
        self.text = text
        self.current_token = None

    def error(self):
        raise Exception('Error in parser!')

    def eat(self, type):
        if self.current_token.type == type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def get_next_token(self):
        token = ""

        while self.pos < len(self.text) and self.text[self.pos].isspace():
            self.pos += 1

        if self.pos > len(self.text) - 1:
            return Token(TokenType.EOF, None)

        current_char = self.text[self.pos]
        number = ''

        if current_char.isdigit():
            while self.pos < len(self.text) and self.text[self.pos].isdigit():
                number += self.text[self.pos]
                self.pos += 1

            self.pos -= 1
            token = Token(TokenType.INTEGER, int(number))
        elif current_char == '+' or current_char == '-':
            token = Token(TokenType.BINOP, current_char)
        else:
            self.error()

        self.pos += 1
        return token

    def expr(self):
        self.current_token = self.get_next_token()

        left = self.current_token
        self.eat(TokenType.INTEGER)

        while self.current_token.value is not None:
            op = self.current_token
            self.eat(TokenType.BINOP)

            right = self.current_token
            self.eat(TokenType.INTEGER)

            if op.value == '+':
                left.value += right.value
            elif op.value == '-':
                left.value -= right.value

        return left.value
