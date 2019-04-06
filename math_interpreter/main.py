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

        if text == 'exit':
            break

        lexer = Lexer(text)
        interpreter = Interpreter(lexer)
        result = interpreter.bool()
        print(result)


if __name__ == '__main__':
    main()
