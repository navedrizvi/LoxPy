from token_ import Token
import sys


def main():
    if len(sys.argv) != 2:
        print(sys.argv)
        print("Usage: python3 ast.py <output directory>")
        sys.exit(64)
    out_dir = sys.argv[1]
    #used for scripting the syntax tree classes
    expr_params = [
        "Binary: Expr left, Token operator, Expr right",
        "Grouping: Expr expression", "Literal: object value",
        "Unary: Token operator, Expr right"
    ]
    define_ast(out_dir, "expr", expr_params)


def define_ast(output_dir, base_name, raw_typedefn):
    path = output_dir + "/" + base_name + ".py"
    with open(path, "w+", encoding='utf-8') as writerfp:
        writerfp.writelines([
            'from token_ import Token\n',
            'from abc import ABCMeta, abstractmethod\n\n',
            f"class {base_name.title()}:\n",
            "    pass\n",
        ])

        parsed_typedefns: [(str, [(str, str)])
                           ] = _get_parsed_typedefns(raw_typedefn)

        _define_visitor_interface(writerfp, base_name, parsed_typedefns)

        #Define AST Classes
        for class_name, class_attributes in parsed_typedefns:
            _define_type(writerfp, base_name, class_name, class_attributes)


def _get_parsed_typedefns(raw_defns: str) -> [(str, [(str, str)])]:
    ''' Returns type definitions as list of tuples of class names and associated attributes 
    Output format- [(class_name, [(attr 1, val 1)...)...] 
    '''
    parsed_defn: [(str, [(str, str)])] = []
    for raw_defn in raw_defns:
        data = raw_defn.split(":")
        class_name, raw_class_attributes = data[0].strip(), data[1].strip()
        class_attributes = _parse_attributes(raw_class_attributes)
        parsed_defn.append((class_name, class_attributes))
    return parsed_defn


def _define_type(writerfp, base_name: str, class_name: str,
                 class_attributes: [(str, str)]):
    ''' Declares each field in class body '''
    as_string = ', '.join(
        [f"{attribute[1]}: {attribute[0]}" for attribute in class_attributes])
    lines = [
        #Constructor
        f'class {class_name}({base_name.title()}):\n',
        f'    def __init__(self, {as_string}):\n',
    ]
    for attribute in class_attributes:
        lines.append(f'{" " * 8}self.{attribute[1]} = {attribute[1]}\n')
    lines.append('\n')
    lines.extend([
        f'{" "*4}def accept(self, visitor: IVisitor):\n',
        f'{" "*8}return visitor.visit_{class_name.lower()}_expr(self)\n\n',
    ])
    writerfp.writelines(lines)


def _define_visitor_interface(writerfp, base_name: str,
                              parsed_defn: [(str, [(str, str)])]):
    lines = [
        'class IVisitor(metaclass = ABCMeta):\n',
    ]
    for type_name, _ in parsed_defn:
        #Signatures for visitor methods
        lines.append(
            f"{' '*4}@abstractmethod\n{' '*4}def visit_{type_name.lower()}_{base_name.lower()}(self, {base_name.lower()}):\n{' '*8}raise NotImplementedError\n\n"
        )
    lines.append('\n')
    writerfp.writelines(lines)


def _parse_attributes(st) -> [(str, str)]:
    ''' >>> 'Type1 v1, Type2 v2'
        [('Type1', 'v1'), ('Type2', 'v2')] 
    '''
    singles = st.split(',')
    singles = list(map(str.strip, singles))
    return [(single.split(' ')[0], single.split(' ')[1]) for single in singles]


if __name__ == "__main__":
    main()
