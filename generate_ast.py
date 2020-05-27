# from abc import ABC, abstractmethod
from token_ import Token
import sys


class Expr():
    def __init__(self, exprtype):
        if exprtype == 'Binary':
            self.binaryexpr = Binary()

    class Binary():
        def __init__(self, left: super, opertor: Token, right: super):
            self.left = left
            self.operator = opertor
            self.right = right


def define_ast(output_dir, base_name, types):
    path = output_dir + "/" + base_name + ".py"
    with open(path, "w+", encoding='utf-8') as writerfp:
        writerfp.writelines([
            'from abc import ABC\n\n',
            "class {0}:\n".format(base_name.title()),
        ])
        for type_ in types:
            data = type_.split(":")
            class_name, class_attributes = data[0].strip(), data[1].strip()
            define_type(writerfp, base_name, class_name, class_attributes)


def define_type(writerfp, base_name, class_name, class_attributes):
    ''' Declares each field in class body '''

    class_attributes = _get_attributes_without_type(class_attributes)
    as_string = ', '.join(class_attributes)
    lines = [
        #Constructor
        f'      class {class_name}({base_name}):\n',
        f'               def __init__(self, {as_string}):\n',
    ]

    for attribute in class_attributes:
        lines.append(f'                   self.{attribute} = {attribute}\n', )
    lines.append('\n')
    writerfp.writelines(lines)


def _get_attributes_without_type(st) -> [str]:
    ''' >>> 'Type1 v1, Type2 v2'
        ['v1', 'v2'] 
    '''
    singles = st.split(',')
    singles = list(map(str.strip, singles))
    return [single.split(' ')[1] for single in singles]


def main():
    if len(sys.argv) != 2:
        print(sys.argv)
        print("Usage: python3 ast.py <output directory>")
        sys.exit(64)
    out_dir = sys.argv[1]
    define_ast(out_dir, "expr", [
        "Binary: Expr left, Token operator, Expr right",
        "Grouping: Expr expression", "Literal: object value",
        "Unary: Token operator, Expr right"
    ])


if __name__ == "__main__":
    main()
