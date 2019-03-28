from enum import Enum


class TokenType(Enum):
    PLUS = 0
    INTEGER = 1
    EOF = 3
    MINUS = 4
    BINOP = 5
