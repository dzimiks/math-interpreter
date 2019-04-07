from math_interpreter.token import TokenType
from math_interpreter.roman import Roman
from math_interpreter.exceptions import UnexpectedTokenException, TokenTypeMismatchException


class Interpreter:
    def __init__(self, lexer, var_storage):
        self.lexer = lexer
        self.var_storage = var_storage
        self.current_token = self.lexer.get_next_token()
        self.variables = dict()

    def error(self):
        raise UnexpectedTokenException(self.current_token)

    def eat(self, type):
        if self.current_token.type == type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise TokenTypeMismatchException(type, self.current_token)

    def factor(self):
        token = self.current_token
        # print('FACTOR TOKEN TYPE:', token.type)
        # print('FACTOR TOKEN VALUE:', token.value)

        if token.type == TokenType.INT:
            self.eat(TokenType.INT)
            return token.value
        elif token.type == TokenType.OPENED_PAREN:
            self.eat(TokenType.OPENED_PAREN)
            result = self.expr()

            if self.current_token.type == TokenType.GT:
                self.eat(TokenType.GT)
                result2 = self.expr()
                result = result > result2

            if self.current_token.type == TokenType.LT:
                self.eat(TokenType.LT)
                result2 = self.expr()
                result = result < result2

            self.eat(TokenType.CLOSED_PAREN)
            return result
        elif token.type == TokenType.STRING:
            self.eat(TokenType.STRING)

            if token.value == 'RIM' and self.current_token.type == TokenType.OPENED_PAREN:
                self.eat(TokenType.OPENED_PAREN)
                rumun = self.current_token
                self.eat(TokenType.STRING)
                self.eat(TokenType.CLOSED_PAREN)

                romaninho = Roman()
                result = romaninho.roman(rumun.value)
                return result
            else:
                variable = token.value

                if self.current_token.type == TokenType.ASSIGN:
                    self.eat(TokenType.ASSIGN)
                    variable_value = self.expr()
                    self.var_storage.set(variable, variable_value)
                    return variable_value
                else:
                    if self.var_storage.get(variable) is None:
                        self.var_storage.set(None)

                    return self.var_storage.get(variable)

    def string_factor(self):
        token = self.current_token

        if token.type == TokenType.STRING:
            self.eat(TokenType.STRING)
            return token.value

    def term(self):
        result = self.factor()
        # print('TERM RESULT:', result)
        # print('TYPE:', self.current_token.type)

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

        return int(result)

    def expr(self):
        # print('CURR TYPE:', self.current_token.type)
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

    def bool(self):
        result = True
        left = self.expr()

        if self.current_token.type in (
                TokenType.LT, TokenType.GT, TokenType.EQ, TokenType.NE, TokenType.LTE, TokenType.GTE):
            right = None

            while self.current_token.type in (
                    TokenType.LT, TokenType.GT, TokenType.EQ, TokenType.NE, TokenType.LTE, TokenType.GTE):
                if self.current_token.type == TokenType.LT:
                    self.eat(TokenType.LT)
                    right = self.expr()

                    if not (left < right):
                        result = False

                    left = right
                elif self.current_token.type == TokenType.GT:
                    self.eat(TokenType.GT)
                    right = self.expr()

                    if not (left > right):
                        result = False

                    left = right
                elif self.current_token.type == TokenType.EQ:
                    self.eat(TokenType.EQ)
                    right = self.expr()

                    if not (left == right):
                        result = False

                    left = right
                elif self.current_token.type == TokenType.NE:
                    self.eat(TokenType.NE)
                    right = self.expr()

                    if not (left != right):
                        result = False

                    left = right
                elif self.current_token.type == TokenType.LTE:
                    self.eat(TokenType.LTE)
                    right = self.expr()

                    if not (left <= right):
                        result = False

                    left = right
                elif self.current_token.type == TokenType.GTE:
                    self.eat(TokenType.GTE)
                    right = self.expr()

                    if not (left >= right):
                        result = False

                    left = right

            return result
        else:
            return left
