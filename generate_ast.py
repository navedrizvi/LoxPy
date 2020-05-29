from token_ import Token
import sys


def define_ast(output_dir, base_name, types):
    path = output_dir + "/" + base_name + ".py"
    with open(path, "w+", encoding='utf-8') as writerfp:
        writerfp.writelines([
            'from token_ import Token\n',
            'from abc import ABCMeta, abstractmethod\n\n',
            "class {0}:\n".format(base_name.title()),
            "    pass\n",
        ])
        class_names = []
        for type_ in types:
            data = type_.split(":")
            class_name, raw_class_attributes = data[0].strip(), data[1].strip()
            class_names.append(class_name)
            class_attributes = _parse_attributes(raw_class_attributes)
            _define_type(writerfp, base_name, class_name, class_attributes)
        _define_visitor_interface(writerfp, base_name, class_names)


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
        lines.append(' ' * 8 + f'self.{attribute[1]} = {attribute[1]}\n', )
    lines.append('\n')
    writerfp.writelines(lines)


def _define_visitor_interface(writerfp, base_name: str, class_names: [str]):
    lines = [
        'class IVisitor(metaclass = ABCMeta):\n',
    ]
    for type_name in class_names:
        #Signatures for visitor methods
        lines.append(
            f"{' '*4}@abstractmethod\n{' '*4}def visit_{type_name.lower()}_{base_name.lower()}(self, {base_name.lower()}: {type_name}):\n{' '*8}raise NotImplementedError\n\n"
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


if __name__ == "__main__":
    main()
