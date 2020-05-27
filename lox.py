from sys import argv
from token_ import Token
from typing import List
from scanner import Scanner
import argparse


class Lox:
    ''' Responsible for launching interpreter '''
    had_error = False

    #core driver
    @staticmethod
    def _run(source: str):
        token_sc = Scanner(source)
        tokens = token_sc.scan_tokens()
        for token in tokens:
            print(token)

    @staticmethod
    def error(line: int, message: str):
        Lox._report(line, "", message)

    @staticmethod
    def _report(line: int, where: str, message: str):
        print(f"[line {line} ] Error {where}: {message}")
        had_error = True

    # Wrapper functions
    # read file and execute
    @staticmethod
    def run_files(file_paths: [str]):
        for file_path in file_paths:
            with open(file_path, "r") as file_io:
                file_str_repr = file_io.read()
                Lox._run(file_str_repr)
                #Indicate error
                if had_error:
                    exit(65)

    @staticmethod
    def run_prompt():
        while True:
            line = input("> ")
            Lox._run(line)
            had_error = False


def main():
    ''' Start lox interpreter session or execute source code file(s)
    invoked by: python3 lox.py [files]
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='*', help='Lox source code file(s)')
    args = parser.parse_args()  #Returns list of files if provided by user

    if args.files:
        Lox.run_files(args.files)
    else:
        Lox.run_prompt()


if __name__ == "__main__":
    main()