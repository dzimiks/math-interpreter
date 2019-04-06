from math_interpreter.token import TokenType


class Interpreter:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Error in parser!')

    def eat(self, type):
        if self.current_token.type == type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        token = self.current_token

        if token.type == TokenType.INT:
            self.eat(TokenType.INT)
            return token.value
        elif token.type == TokenType.OPENED_PAREN:
            self.eat(TokenType.OPENED_PAREN)
            result = self.expr()
            self.eat(TokenType.CLOSED_PAREN)
            return result

    def string_factor(self):
        token = self.current_token

        if token.type == TokenType.STRING:
            self.eat(TokenType.STRING)
            return token.value

    def term(self):
        result = self.factor()

        while self.current_token.type in (TokenType.MUL, TokenType.DIV):
            token = self.current_token

            if token.type == TokenType.MUL:
                self.eat(TokenType.MUL)
                result = result * self.factor()
            elif token.type == TokenType.DIV:
                self.eat(TokenType.DIV)
                result = result // self.factor()
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
