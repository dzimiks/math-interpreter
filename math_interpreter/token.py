from enum import Enum


class Token:
    def __init__(self, token_type, value=None):
        self.type = token_type
        self.value = value

    def __str__(self):
        return '<{} {}>'.format(self.type, self.value)


class TokenType(Enum):
    # Integer
    INT = 'INT'
    # String
    STRING = 'STRING'
    # =
    ASSIGN = 'ASSIGN'
    # +
    ADD = 'ADD'
    # -
    SUB = 'SUB'
    # *
    MUL = 'MUL'
    # /
    DIV = 'DIV'
    # >
    GT = 'GT'
    # >=
    GTE = 'GTE'
    # <
    LT = 'LT'
    # <=
    LTE = 'LTE'
    # ==
    EQ = 'EQ'
    # !=
    NE = 'NE'
    # (
    OPENED_PAREN = 'OPENED_PAREN'
    # )
    CLOSED_PAREN = 'CLOSED_PAREN'
    # Roman
    ROMAN = 'ROMAN'
    # EXIT
    EXIT = 'EXIT'
    # EOF
    EOF = 'EOF'
