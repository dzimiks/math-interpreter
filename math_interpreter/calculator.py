OPERATIONS = ('+', '-', '/', '*', '=', '<', '>')


class Prefixator:
    result = ''

    def __init__(self):
        self.stack = []

    def push(self, p):
        if p in OPERATIONS:
            op1 = self.stack.pop()
            op2 = self.stack.pop()
            self.stack.append('(%s %s %s)' % (op1, p, op2))
        else:
            self.stack.append(p)

    def convert(self, l):
        l.reverse()

        for e in l:
            self.push(e)

        result = self.stack.pop()
        return result


class Postfixator:
    result = ''

    def __init__(self):
        self.stack = []

    def push(self, p):
        if p in OPERATIONS:
            op1 = self.stack.pop()
            op2 = self.stack.pop()
            self.stack.append('(%s %s %s)' % (op2, p, op1))
        else:
            self.stack.append(p)

    def convert(self, l):
        for e in l:
            self.push(e)

        result = self.stack.pop()
        return result
