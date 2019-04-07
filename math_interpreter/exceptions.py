class UnexpectedTokenException(Exception):
    def __init__(self, token):
        super().__init__('Unexpected token: {}!'.format(token))


class UnexpectedCharacterException(Exception):
    def __init__(self, char):
        super().__init__('Unexpected character: {}!'.format(char))


class TokenTypeMismatchException(Exception):
    def __init__(self, token_type, current_token):
        super().__init__(
            'Token type ({}) is mismatched with current token type: {}!'.format(token_type, current_token))
