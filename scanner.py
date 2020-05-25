from token_ import Token
from token_type import TokenTypes, one_char_tokens_map, two_char_tokens_map, keyword_token_map


class Scanner:
    '''Responsible for scanning input characters from source file to tokens parsed by the interpreter
    
    input: raw source doe
    output: scan_tokens() returns list of tokens understood by interpreter
    '''
    def __init__(self, source: str):
        self.source = source
        self.tokens = []

        # Current position tracking
        self.line = 1  # Current line number
        self.lexeme_starts_at = 0  # First char offset in current lexeme being scanned
        self.current = 0  # Current char being scanned

    def scan_tokens(self) -> [Token]:
        ''' Core of scanner. Consumes source code characters in a loop. '''
        # Each turn of the loop scans a single token
        while not self.__is_at_end():
            self.lexeme_starts_at = self.current
            self.__scan_token()
        final_token = Token(TokenTypes.EOF, "", None, self.line)
        self.tokens.append(final_token)
        return self.tokens

    def __advance(self) -> str:
        self.current += 1
        return self.source[self.current - 1]

    def __is_at_end(self):
        return self.current == len(self.source)

    def __is_next_char_in_source(self, expected: chr):
        if self.__is_at_end():
            return False
        if self.source[self.current] != expected:
            return False
        self.current += 1
        return True

    def __scan_token(self):
        '''Figures out lexeme of the source code character by consuming it 
         and any following chars part of that lexeme. Emits a token ypon reaching end of the lexeme'''

        # Inner-function used as dict dispatcher (alternative for switch-case)
        def get_token(char):
            switcher = {
                '(':
                lambda: self.__add_token(TokenTypes.LEFT_PAREN),
                ')':
                lambda: self.__add_token(TokenTypes.RIGHT_PAREN),
                '{':
                lambda: self.__add_token(TokenTypes.LEFT_BRACE),
                '}':
                lambda: self.__add_token(TokenTypes.RIGHT_BRACE),
                ',':
                lambda: self.__add_token(TokenTypes.COMMA),
                '.':
                lambda: self.__add_token(TokenTypes.DOT),
                '+':
                lambda: self.__add_token(TokenTypes.PLUS),
                ';':
                lambda: self.__add_token(TokenTypes.SEMICOLON),
                '/':
                lambda: self.__add_token(TokenTypes.SLASH),
                '*':
                lambda: self.__add_token(TokenTypes.STAR),

                #One or two character tokens
                '!':
                lambda: self.__add_token(TokenTypes.BANG_EQUAL
                                         if self.__is_next_char_in_source('=')
                                         else TokenTypes.BANG),
                "=":
                lambda: self.__add_token(TokenTypes.EQUAL_EQUAL
                                         if self.__is_next_char_in_source('=')
                                         else TokenTypes.EQUAL),
                ">":
                lambda: self.__add_token(TokenTypes.GREATER_EQUAL
                                         if self.__is_next_char_in_source('=')
                                         else TokenTypes.GREATER),
                '<':
                lambda: self.__add_token(TokenTypes.LESS_EQUAL
                                         if self.__is_next_char_in_source('=')
                                         else TokenTypes.LESS),

                #Edge cases
                '/':
                lambda: self.__handle_slash_case(),
                '\n':
                lambda: self.__incr_line(),
                '"':
                lambda: self.__add_string_token(),

                #Ignore white spaces
                ' ':
                lambda: None,
                '\r':
                lambda: None,
                '\t':
                lambda: None,
            }
            try:
                return switcher.get(char, None)()
            except TypeError:
                self.__Lox_error("Invalid token")

        c = self.__advance()
        token = get_token(c)

    def __add_token(self, token_type, literal=None):
        text = self.source[self.lexeme_starts_at:self.current]
        self.tokens.append(Token(token_type, text, literal, self.line))

    def __incr_line(self):
        self.line += 1

    def __handle_slash_case(self):
        if self.__is_next_char_in_source("/"):
            while (self.__peek() != '\n' and not self.__is_at_end()):
                self.__advance()
        else:
            self.__add_token(TokenTypes.SLASH)

    def __add_string_token(self):
        ''' Returns string token present between opening and closing quotes (string literals) '''
        #Consumes chacaters till ending quote is reached
        while self.__peek() != '"' and not self.__is_at_end():
            if self.__peek() == '\n':
                self.line += 1
            self.__advance()

        if self.__is_at_end():
            self.__Lox_error("Unterminated string.")
            return

        #Create the token (string value) that is used by interpreter
        self.__advance()
        value = self.source[self.lexeme_starts_at + 1, self.current - 1]
        self.__add_token(TokenTypes.STRING, value)

    def __peek(self):
        if self.__is_at_end():
            return '\0'
        return self.source[self.current]

    def __Lox_error(self, message):
        from lox import Lox
        Lox.error(self.line, message)
