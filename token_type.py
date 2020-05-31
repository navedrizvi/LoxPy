from enum import Enum


class TokenType(Enum):
    ''' Enumeration of all token types in PyLox. Used by Scanner '''
    LEFT_PAREN = 'LEFT_PAREN'
    RIGHT_PAREN = 'RIGHT_PAREN'
    LEFT_BRACE = 'LEFT_BRACE'
    RIGHT_BRACE = 'RIGHT_BRACE'
    COMMA = 'COMMA'
    DOT = 'DOT'
    MINUS = 'MINUS'
    PLUS = 'PLUS'
    SEMICOLON = 'SEMICOLON'
    SLASH = 'SLASH'
    STAR = 'STAR'
    BANG = 'BANG'
    BANG_EQUAL = 'BANG_EQUAL'
    EQUAL = 'EQUAL'
    EQUAL_EQUAL = 'EQUAL_EQUAL'
    GREATER = 'GREATER'
    GREATER_EQUAL = 'GREATER_EQUAL'
    LESS = 'LESS'
    LESS_EQUAL = 'LESS_EQUAL'
    IDENTIFIER = 'IDENTIFIER'  # used for identifying a variable or class
    STRING = 'STRING'
    NUMBER = 'NUMBER'
    AND = 'AND'
    CLASS = 'CLASS'
    ELSE = 'ELSE'
    FALSE = 'FALSE'
    FUN = 'FUN'
    FOR = 'FOR'
    IF = 'IF'
    NIL = 'NIL'
    OR = 'OR'
    PRINT = 'PRINT'
    RETURN = 'RETURN'
    SUPER = 'SUPER'
    THIS = 'THIS'
    TRUE = 'TRUE'
    VAR = 'VAR'
    WHILE = 'WHILE'
    EOF = 'EOF'


keyword_token_map = {
    'and': 'AND',
    'class': 'CLASS',
    'else': 'ELSE',
    'false': 'FALSE',
    'for': 'FOR',
    'fun': 'FUN',
    'if': 'IF',
    'nil': 'NIL',
    'or': 'OR',
    'print': 'PRINT',
    'return': 'RETURN',
    'super': 'SUPER',
    'this': 'THIS',
    'true': 'TRUE',
    'var': 'VAR',
    'while': 'WHILE'
}
