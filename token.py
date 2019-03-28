from enum import Enum


class Token():
    def __init__(self, token_type, value=None):
        self.type = token_type
        self.value = value

    def __str__(self):
        out = str(self.type.name)

        if self.value is not None:
            out += "({0})".format(str(self.value))

        return out


class TokenType(Enum):
    ID = 1
    # Integer
    INT = 2
    # =
    ASSIGN = 3
    # +
    OP_ADD = 4
    # -
    OP_SUB = 5
    # *
    OP_MUL = 6
    # /
    OP_DIV = 7
    # >
    OP_GT = 8
    # >=
    OP_GTE = 9
    # <
    OP_LT = 10
    # <=
    OP_LTE = 11
    # ==
    OP_EQ = 12
    # ,
    COMMA = 13
    # (
    PAREN_LEFT = 14
    # )
    PAREN_RIGHT = 15
    # Exit
    EXIT = 16
    # End of token stream
    EOF = 17


class TokenGroups:
    numbers = [
        TokenType.INT,
        TokenType.ID
    ]

    bin_ops_1 = [
        TokenType.OP_ADD,
        TokenType.OP_SUB
    ]

    bin_ops_2 = [
        TokenType.OP_MUL,
        TokenType.OP_DIV
    ]

    boolean_ops = [
        TokenType.OP_GT,
        TokenType.OP_LT,
        TokenType.OP_GTE,
        TokenType.OP_LTE,
        TokenType.OP_EQ
    ]
