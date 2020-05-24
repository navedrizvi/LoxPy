from token_ import Token

from token_type import TokenTypes, token_mapping_singles


class Scanner:
    '''Responsible for scanning input characters from source file to tokens parsed by the interpreter'''
    def __init__(self, source: str):
        self.source = source
        self.tokens = []

        # Current position tracking
        self.line = 1  # current line number
        self.lexeme_starts_at = 0  # first char offset in current lexeme being scanned
        self.current = 0  # current char being scanned

    def scan_tokens(self) -> [Token]:
        while not self.__is_at_end():  # Each turn of loop scans a single token
            # At the beginning of the next lexeme here
            self.lexeme_starts_at = self.current
            self.__scan_token()
        final_token = Token(TokenTypes.EOF, "", None, self.line)
        self.tokens.append(final_token)
        return self.tokens

    def __is_at_end(self):
        return self.current == len(self.source)

    def __scan_token(self):
        c = self.__advance()  #consumes the next character in the source file
        token = token_mapping_singles.get(c, None)
        if token:
            token_type = TokenTypes[token_mapping_singles[c]]
            self.__add_token(token_type)  #add associated token to output
        else:  #not a valid token
            from lox import Lox
            Lox.error(self.line, "Unexpected character.")

    def __advance(self):
        while self.current < len(
                self.source) and self.source[self.current] != " ":
            self.current += 1
        return self.source[self.current - 1]

    def __add_token(self, token_type, literal=None):
        text = self.source[self.lexeme_starts_at:self.current]
        self.tokens.append(Token(token_type, text, literal, self.line))


def test():
    sc = Scanner('var test')
    sc.scan_tokens()


if __name__ == "__main__":
    test()