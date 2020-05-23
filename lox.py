from sys import argv
from token import Token
from typing import List
import argparse


class Lox:
    ''' Responsible for launching interpreter '''
    had_error = False

    #core driver
    @staticmethod
    def __run(source: str):
        tokens = []

    @staticmethod
    def error(line: int, message: str):
        Lox.__report(line, "", message)

    @staticmethod
    def __report(line: int, where: str, message: str):
        print(f"[line {line} ] Error {where}: {message}")
        had_error = True

    # Wrapper functions
    # read file and execute
    @staticmethod
    def run_files(file_paths: [str]):
        for file_path in file_paths:
            with open(file_path, "r") as file_io:
                file_str_repr = file_io.read()
                Lox.__run(file_str_repr)
                #Indicate error
                if had_error:
                    exit(65)

    @staticmethod
    def run_prompt():
        line = input("> ")
        Lox.__run(line)
        had_error = False
        Lox.run_prompt()


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