from math_interpreter.mode import prefix_mode, infix_mode, postfix_mode


def main():
    while True:
        try:
            text = input('--> ')

            if text == 'infix':
                infix_mode()
            elif text == 'prefix':
                prefix_mode()
            elif text == 'postfix':
                postfix_mode()
        except EOFError:
            break

        if not text:
            continue

        if text == 'exit':
            break


if __name__ == '__main__':
    main()
