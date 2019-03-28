from enum import Enum


class Token():
    def __init__(self, token_type, value=None):
        self.type = token_type
        self.value = value

    def __str__(self):
        out = str(self.type.name)

        if self.value is not None:
            out += '({0})'.format(str(self.value))

        return out


class TokenType(Enum):
    ID = 1
    # Integer
    INT = 2
    # =
    ASSIGN = 3
    # +
    ADD = 4
    # -
    SUB = 5
    # *
    MUL = 6
    # /
    DIV = 7
    # >
    GT = 8
    # >=
    GTE = 9
    # <
    LT = 10
    # <=
    LTE = 11
    # ==
    EQ = 12
    # ,
    COMMA = 13
    # (
    OPEN_PAREN = 14
    # )
    CLOSED_PAREN = 15
    # Exit
    EXIT = 16
    # End of token stream
    EOF = 17
    BINOP = 18


class TokenGroups:
    numbers = [
        TokenType.ID,
        TokenType.INT
    ]

    bin_commands_1 = [
        TokenType.ADD,
        TokenType.SUB
    ]

    bin_commands_2 = [
        TokenType.MUL,
        TokenType.DIV
    ]

    boolean_commands = [
        TokenType.GT,
        TokenType.LT,
        TokenType.GTE,
        TokenType.LTE,
        TokenType.EQ
    ]
