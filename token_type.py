from enum import Enum


class TokenTypes(Enum):
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
    IDENTIFIER = 'IDENTIFIER'
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


#reserved keywords and literals mapped to tokens (aka lexemes) used by interpreter
token_mapping_singles = {
    #Single-character tokens.
    '(': 'LEFT_PAREN',
    ')': 'RIGHT_PAREN',
    '{': 'LEFT_BRACE',
    '}': 'RIGHT_BRACE',
    ',': 'COMMA',
    '.': 'DOT',
    '-': 'MINUS',
    '+': 'PLUS',
    ';': 'SEMICOLON',
    '/': 'SLASH',
    '*': 'STAR',
}

token_mapping_doubles = {
    #One or two character tokens.
    '!': "BANG",
    "!=": 'BANG_EQUAL',
    "=": 'EQUAL',
    "==": 'EQUAL_EQUAL',
    ">": 'GREATER',
    ">=": 'GREATER_EQUAL',
    '<': 'LESS',
    '<=': 'LESS_EQUAL',
}

token_mapping_keywords = {
    #Literals.
    'id': 'IDENTIFIER',
    'string': 'STRING',
    'number': 'NUMBER',
    #Keywords.
    'and': 'AND',
    'class': 'CLASS',
    'else': 'ELSE',
    'false': 'FALSE',
    'fun': 'FUN',
    'for': 'FOR',
    'if': 'IF',
    'nil': 'NIL',
    'or': 'OR',
    'print': 'PRINT',
    'return': 'RETURN',
    'super': 'SUPER',
    'this': 'THIS',
    'true': 'TRUE',
    'var': 'VAR',
    'while': 'WHILE',
    'eof': 'EOF',
}
