from token import Token
from token_type import token_types
from lox import Lox


class Scanner:
    '''Responsible for scanning input characters from source file to tokens parsed by the interpreter'''
    def __init__(self, source: str):
        self.source = source
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 1

    def scan_tokens(self) -> [Token]:
        while not self.__is_at_end():  # Each turn of loop scans a single token
            # At the beginning of the next lexeme here
            start = self.current
            self.__scan_token()
        self.tokens.append(Token("eof", "", None,
                                 self.line))  #eof token is the final token
        return self.tokens

    def __scan_token(self):
        c = self.__advance()  #consumes the next character in the source file
        print(c)
        token = token_types.get(c, None)
        # if token:
        #     __add_token(token_types[c])  #add associated token to output
        # else:  #not a valid token
        #     Lox.error(self.line, "Unexpected character.")

    def __is_at_end(self):
        return self.current >= len(self.source)

    def __advance(self):
        self.current += 1
        return self.source[self.current - 1]

    def __add_token(self, token_type, literal=None):
        text = self.source[start:current]
        self.tokens.append(Token(token_type, text, literal, self.line))


def test():
    sc = Scanner('var test')
    sc.scan_tokens()


if __name__ == "__main__":
    test()