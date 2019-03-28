from interpreter import Interpreter


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

        interpreter = Interpreter(text)

        if interpreter is None:
            print('End of program!')
            break

        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()
