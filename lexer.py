from token import Token, TokenType


class LexerException(Exception):
    pass


class LexerStream:
    def __init__(self, line):
        self.line = line
        self.index = 0

    def peek(self):
        if self.at_end():
            return None

        return self.line[self.index]

    def get(self):
        char = self.peek()

        if char is not None:
            self.index += 1

        return char

    def at_end(self):
        return self.index == len(self.line)


class Lexer:
    def __init__(self, line):
        self.stream = LexerStream(line)

        self.keywords = {
            'EXIT': TokenType.EXIT
        }

        self.specials = {
            '=': TokenType.ASSIGN,
            '+': TokenType.ADD,
            '-': TokenType.SUB,
            '*': TokenType.MUL,
            '/': TokenType.DIV,
            '>': TokenType.GT,
            '>=': TokenType.GTE,
            '<': TokenType.LT,
            '<=': TokenType.LTE,
            '==': TokenType.EQ,
            ',': TokenType.COMMA,
            '(': TokenType.OPEN_PAREN,
            ')': TokenType.CLOSED_PAREN
        }

    def token_generator(self):
        while not self.stream.at_end():
            if self.stream.peek().isspace():
                self.stream.get()
            elif self.stream.peek().isalpha():
                alpha_string = self.get_alpha_string(self.stream)

                if alpha_string in self.keywords:
                    yield Token(self.keywords[alpha_string])
                else:
                    yield Token(TokenType.ID, alpha_string)
            elif self.stream.peek().isdigit():
                digit_str = self.get_digit_string(self.stream)
                yield Token(TokenType.INT, int(digit_str))
            else:
                specials_string = self.stream.get()

                if specials_string in ['>', '<', '=']:
                    if self.stream.peek() == '=':
                        specials_string += self.stream.get()

                if specials_string in self.specials:
                    yield Token(self.specials[specials_string])
                else:
                    raise LexerException(
                        'Unknown char(s) {0} ending on index {1}'.format(specials_string, self.stream.index))

        yield Token(TokenType.EOF)

    @staticmethod
    def get_alpha_string(stream):
        alpha_str = ''

        while stream.peek() is not None and stream.peek().isalpha():
            alpha_str += stream.get()

        return alpha_str

    @staticmethod
    def get_digit_string(stream):
        digit_str = ''

        while stream.peek() is not None and stream.peek().isdigit():
            digit_str += stream.get()

        return digit_str
