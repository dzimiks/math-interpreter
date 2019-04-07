from math_interpreter.mode import infix_mode
from math_interpreter.var_storage import VarStorage


def main():
    var_storage = VarStorage()

    while True:
        try:
            infix_mode(var_storage)
        except EOFError:
            break


if __name__ == '__main__':
    main()
