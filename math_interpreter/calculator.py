class Calculator:
    result = ''

    def __init__(self):
        self.stack = []

    def push(self, p):
        if p in ['+', '-', '*', '/']:
            op1 = self.stack.pop()
            op2 = self.stack.pop()
            self.stack.append('(%s %s %s)' % (op1, p, op2))
        elif p == '!':
            op = self.stack.pop()
            self.stack.append('%s!' % op)
        elif p in ['sin', 'cos', 'tan']:
            op = self.stack.pop()
            self.stack.append('%s(%s)' % (p, op))
        else:
            self.stack.append(p)

    def convert(self, l):
        l.reverse()

        for e in l:
            self.push(e)

        result = self.stack.pop()
        return result
