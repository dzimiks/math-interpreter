from math_interpreter.interpreter import Interpreter
from math_interpreter.lexer import Lexer


def main():
    while True:
        try:
            text = input('--> ')
        except EOFError:
            break

        if not text:
            continue

        if text == 'EXIT':
            break

        lexer = Lexer(text)
        interpreter = Interpreter(lexer)

        if interpreter is None:
            print('End of program!')
            break

        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()
