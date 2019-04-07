from math_interpreter.mode import prefix_mode, infix_mode, postfix_mode


def main():
    while True:
        try:
            text = input('--> ')

            if text == 'INFIX':
                infix_mode()
            elif text == 'PREFIX':
                prefix_mode()
            elif text == 'POSTFIX':
                postfix_mode()
        except EOFError:
            break

        if not text:
            continue

        if text == 'EXIT':
            break


if __name__ == '__main__':
    main()
