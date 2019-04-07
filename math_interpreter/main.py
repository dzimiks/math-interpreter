from math_interpreter.mode import prefix_mode, infix_mode, postfix_mode
from math_interpreter.var_storage import VarStorage


def main():
    var_storage = VarStorage()

    while True:
        try:
            text = input('--> ')

            if text == 'INFIX':
                infix_mode(var_storage)
            elif text == 'PREFIX':
                prefix_mode(var_storage)
            elif text == 'POSTFIX':
                postfix_mode(var_storage)
        except EOFError:
            break

        if not text:
            continue

        if text == 'EXIT':
            break


if __name__ == '__main__':
    main()
