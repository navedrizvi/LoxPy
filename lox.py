from sys import argv
from tokenize import tokenize
from token import Token
from typing import List


class Lox:
    ''' Responsible for launching interpreter '''

    had_error = False

    #TODO: implement
    def main(self):
        if len(argv) > 1:
            print("Usage: plox [script]")
            exit(64)  #user-defined exit code
        elif len(argv) == 1:
            self.run_file(argv[0])
        else:
            self.run_prompt()

    #core driver
    def run(self, source: str):
        tokens = tokenize(source)  #TODO: implement core
        # for token in tokens:
        #     print(token)
        pass

    def error(self, line: int, message: str):
        self.report(line, "", message)

    def __report(self, line: int, where: str, message: str):
        print(f"[line {line} ] Error {where}: {message}")
        self.had_error = True

    # Wrapper functions
    # read file and execute
    def run_file(self, path: str):
        file_io = open(path, "r")
        file_str_repr = file_io.read()
        self.run(file_str_repr)
        #Indicate error
        if self.had_error:
            exit(65)

    def run_prompt(self):
        io_stream = input()
        while True:
            print("> ", end="")
            run(io_stream.readline())
            self.had_error = False