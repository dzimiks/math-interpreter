from token import Token, TokenType


# class Interpreter:
#     def __init__(self, text):
#         self.pos = 0
#         self.text = text
#         self.current_token = None
#
#     def error(self):
#         raise Exception('Error in parser!')
#
#     def eat(self, type):
#         if self.current_token.type == type:
#             self.current_token = self.get_next_token()
#         else:
#             self.error()
#
#     def get_next_token(self):
#         token = ''
#
#         while self.pos < len(self.text) and self.text[self.pos].isspace():
#             self.pos += 1
#
#         if self.pos > len(self.text) - 1:
#             return Token(TokenType.EOF, None)
#
#         current_char = self.text[self.pos]
#         number = ''
#
#         if current_char.isdigit():
#             while self.pos < len(self.text) and self.text[self.pos].isdigit():
#                 number += self.text[self.pos]
#                 self.pos += 1
#
#             self.pos -= 1
#             token = Token(TokenType.INT, int(number))
#         elif current_char == '+' or current_char == '-' or current_char == '*' or current_char == '/':
#             token = Token(TokenType.BINOP, current_char)
#         # elif current_char == '+':
#         #     token = Token(TokenType.ADD, current_char)
#         # elif current_char == '-':
#         #     token = Token(TokenType.SUB, current_char)
#         # elif current_char == '*':
#         #     token = Token(TokenType.MUL, current_char)
#         # elif current_char == '/':
#         #     token = Token(TokenType.DIV, current_char)
#         else:
#             self.error()
#
#         self.pos += 1
#         return token
#
#     def expr(self):
#         self.current_token = self.get_next_token()
#
#         left = self.current_token
#         self.eat(TokenType.INT)
#
#         while self.current_token.value is not None:
#             op = self.current_token
#             self.eat(TokenType.BINOP)
#
#             right = self.current_token
#             self.eat(TokenType.INT)
#
#             if op.value == '+':
#                 left.value += right.value
#             elif op.value == '-':
#                 left.value -= right.value
#             elif op.value == '*':
#                 left.value *= right.value
#             elif op.value == '/':
#                 left.value /= right.value
#
#         return left.value

class Interpreter():
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Error in parsing!')

    def eat(self, type):
        if self.current_token.type == type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        token = self.current_token

        if token.type == TokenType.OPENED_PAREN:
            self.eat(TokenType.OPENED_PAREN)
            result = self.expr()
            self.eat(TokenType.CLOSED_PAREN)
            return result
        elif token.type == TokenType.INT:
            self.eat(TokenType.INT)
            return token.value

        # if token.type == TokenType.INT:
        #     self.eat(TokenType.INT)
        #     return token.value
        # elif token.type == TokenType.OPENED_PAREN:
        #     self.eat(TokenType.OPENED_PAREN)
        #     result = self.expr()
        #     self.eat(TokenType.CLOSED_PAREN)
        #     return result

    def term(self):
        result = self.factor()

        while self.current_token.type in (TokenType.MUL, TokenType.DIV):
            token = self.current_token

            if token.type == TokenType.MUL:
                self.eat(TokenType.MUL)
                result = result * self.factor()
            elif token.type == TokenType.DIV:
                self.eat(TokenType.DIV)
                result = result / self.factor()
            else:
                self.error()

        return result

    def expr(self):
        result = self.term()

        while self.current_token.type in (TokenType.ADD, TokenType.SUB):
            token = self.current_token

            if token.type == TokenType.ADD:
                self.eat(TokenType.ADD)
                result = result + self.term()
            elif token.type == TokenType.SUB:
                self.eat(TokenType.SUB)
                result = result - self.term()
            else:
                self.error()

        return result
