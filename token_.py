from token_type import TokenType


class Token:
    '''A bundle containing the raw lexeme along with associated metadata.'''
    def __init__(self, token_type, lexeme, literal, line):
        self.token_type_repr = TokenType[token_type].value
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __str__(self):
        return f"{self.token_type_repr} {self.lexeme} {self.literal}"