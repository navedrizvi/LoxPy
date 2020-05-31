from expr import Binary, Expr, Grouping, IVisitor, Literal, Unary
from collections import deque
from token_ import Token
from token_type import TokenTypes


class AstPrinter(IVisitor):
    '''Given a Abstract Syntax Tree, print() produces string of text that is valid syntax in source language (used for post-order traversal eval on AST as done by the interpreter)'''
    ''' Adds functionality to the Expr subclasses '''
    def print(self, expr: Expr):
        return expr.accept(self)

    def visit_binary_expr(self, expr: Binary):
        return self._parenthesize(expr.operator.lexeme,
                                  [expr.left, expr.right])

    def visit_grouping_expr(self, expr: Grouping):
        return self._parenthesize("group", [expr.expression])

    def visit_literal_expr(self, expr: Literal):
        if expr.value is None:
            return "nil"
        return str(expr.value)

    def visit_unary_expr(self, expr: Unary):
        return self._parenthesize(expr.operator.lexeme, [expr.right])

    def _parenthesize(self, name: str, expr_attrs: [str]):
        ''' Builds the expression as a string in prefix/polish notation (similar to lisp)'''
        out = deque()
        out.append("(")
        out.append(name)
        for expr in expr_attrs:
            out.append(" ")
            out.append(expr.accept(self))
        out.append(")")
        return ''.join(out)


def test():
    expression = Binary(Unary(Token('MINUS', "-", None, 1), Literal(123)),
                        Token('STAR', "*", None, 1),
                        Grouping(Literal(45.67)))  # Visitor

    print(
        AstPrinter().print(expression))  # Expected: (* (- 123) (group 45.67))


if __name__ == "__main__":
    test()