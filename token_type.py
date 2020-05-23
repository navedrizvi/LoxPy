#reserved keywords and literals (lexemes) mapped to tokens used by interpreter
token_types = {

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

    #One or two character tokens.
    '!': "BANG",
    "!=": 'BANG_EQUAL',
    "=": 'EQUAL',
    "==": 'EQUAL_EQUAL',
    ">": 'GREATER',
    ">=": 'GREATER_EQUAL',
    '<': 'LESS',
    '<=': 'LESS_EQUAL',

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