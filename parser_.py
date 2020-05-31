from token_ import Token, TokenType
from expr import Binary, Expr, Grouping, Literal, Unary


class ParseError(RuntimeError):
    pass


class Parser:
    current = 0

    def __init__(self, tokens: [Token]):
        self.tokens = tokens

    def _expression(self) -> Expr:
        return self._equality()

    #Rule- equality → comparison ( ( "!=" | "==" ) comparison )*
    def _equality(self) -> Expr:
        expr = self._comparison()
        while self._match('BANG_EQUAL', 'EQUAL_EQUAL'):
            operator: Token = self._previous(
            )  #Since match() advances the parser
            right: Expr = self._comparison()
            expr = Binary(expr, operator, right)
        return expr

    def _match(self, *types) -> bool:
        for type_ in types:
            if self._check(type_):
                self._advance()
                return True
        return False

    def _check(self, type_: TokenType) -> bool:
        if self._is_at_end():
            return False
        return self._peek().token_type_repr == type_

    def _advance(self) -> Token:
        if not self._is_at_end():
            self.current += 1
        return self._previous()

    def _is_at_end(self):
        return self._peek().token_type_repr == 'EOF'

    def _peek(self) -> Token:
        return self.tokens[self.current]

    def _previous(self) -> Token:
        return self.tokens[self.current - 1]

    #Rule- comparison → addition ( ( ">" | ">=" | "<" | "<=" ) addition )*
    def _comparison(self) -> Expr:
        expr = self._addition()
        while self._match('LESS', 'LESS_EQUAL', 'GREATER', 'GREATER_EQUAL'):
            operator = self._previous()
            right = self._addition()
            expr = Binary(expr, operator, right)
        return expr

    def _addition(self):
        expr = self._multiplication()
        while self._match('MINUS', 'PLUS'):
            operator = self._previous()
            right = self._multiplication()
            expr = Binary(expr, operator, right)
        return expr

    def _multiplication(self):
        expr = self._unary()
        while self._match('SLASH', 'STAR'):
            operator = self._previous()
            right = self._unary()
            expr = Binary(expr, operator, right)
        return expr

    #Rule- unary → ( "!" | "-" ) unary  | primary
    def _unary(self):
        if self._match('BANG', 'MINUS'):
            operator = self._previous()
            right = self._unary()
            return Unary(operator, right)
        return self._primary()

    #Rule- primary → NUMBER | STRING | "false" | "true" | "nil" | "(" expression ")"
    def _primary(self):
        if self._match('FALSE'):
            return Literal(False)
        if self._match('TRUE'):
            return Literal(True)
        if self._match('nil'):
            return Literal(None)

        if self._match('NUMBER', 'STRING'):
            return Literal(self._previous().literal)

        if self._match('LEFT_PAREN'):
            expr = self._expression()
            self._consume('RIGHT_PAREN', "Expected ')' after expression.")
            return Grouping(expr)

        raise self._error(self._peek(), "Expected an expression.")

    def _consume(self, msg: str):
        if self._check():
            return self._advance()
        raise self._error(self._peek(), msg)

    def _error(self, token, msg):
        from lox import Lox
        Lox.error_token(token, msg)
        return ParseError()

    def _synchronize(self):
        self._advance()
        while not self._is_at_end():
            if self._previous().token_type_repr == 'SEMICOLON':
                return

            curr_token = self._peek().token_type_repr
            if curr_token == 'CLASS':
                pass
            elif curr_token == 'FUN':
                pass
            elif curr_token == 'VAR':
                pass
            elif curr_token == 'FOR':
                pass
            elif curr_token == 'IF':
                pass
            elif curr_token == 'WHILE':
                pass
            elif curr_token == 'PRINT':
                pass
            elif curr_token == 'RETURN':
                pass

            self._advance()

    def parse(self):
        try:
            return self._expression()
        except ParseError:
            return None