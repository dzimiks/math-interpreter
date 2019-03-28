from interpreter import Interpreter


def main():
    while True:
        try:
            text = input(' --> ')
        except EOFError:
            break

        if not text:
            continue

        if text == 'exit':
            break

        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()
