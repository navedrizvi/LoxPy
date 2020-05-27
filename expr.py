from abc import ABC

class Expr:
      class Binary(expr):
               def __init__(self, left, operator, right):
                   self.left = left
                   self.operator = operator
                   self.right = right

      class Grouping(expr):
               def __init__(self, expression):
                   self.expression = expression

      class Literal(expr):
               def __init__(self, value):
                   self.value = value

      class Unary(expr):
               def __init__(self, operator, right):
                   self.operator = operator
                   self.right = right

