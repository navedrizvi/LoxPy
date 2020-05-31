from sys import argv
from token_ import Token
from typing import List
from scanner import Scanner
from parser_ import Parser
import argparse
from pprint_ast import AstPrinter


class Lox:
    ''' Responsible for launching interpreter '''
    had_error = False

    #Core driver
    def _run(self, source: str):
        token_sc = Scanner(source)
        tokens = token_sc.scan_tokens()

        parser = Parser(tokens)
        expression = parser.parse()

        if self.had_error:  #if syntax error stop interpreting
            return
        print(AstPrinter().print(expression))

    @staticmethod
    def error_line(line: int, message: str):
        Lox._report(line, "", message)

    @staticmethod
    def error_token(token: Token, message: str):
        if token.token_type_repr == 'EOF':
            Lox._report(token.line, " at end", message)
        else:
            Lox._report(token.line, " at '" + token.lexeme + "'", message)

    @staticmethod
    def _report(line: int, where: str, message: str):
        print(f"[line {line} ] Error {where}: {message}")
        had_error = True

    #Wrapper functions
    @staticmethod
    def run_files(file_paths: [str]):
        for file_path in file_paths:
            with open(file_path, "r") as file_io:
                file_str_repr = file_io.read()
                Lox._run(file_str_repr)
                #Indicate error
                if had_error:
                    exit(65)

    def run_prompt(self):
        while True:
            line = input("> ")
            self._run(line)
            self.had_error = False


def main():
    ''' Start lox interpreter session or execute source code file(s)
    invoked by: python3 lox.py [files]
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='*', help='Lox source code file(s)')
    args = parser.parse_args()  #Returns list of files if provided by user

    lox = Lox()

    if args.files:
        Lox.run_files(args.files)
    else:
        lox.run_prompt()


if __name__ == "__main__":
    main()