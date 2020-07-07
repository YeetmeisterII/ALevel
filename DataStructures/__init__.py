class Stack:
    def __init__(self, size):
        self._stack = list(None for i in range(size))
        self._top = 0

    def __repr__(self):
        return str(self._stack)

    def __str__(self):
        return str(self._stack)

    def pop(self):
        self._top -= 1
        self._stack[self._top], data = None, self._stack[self._top]
        return data

    def push(self, data):
        self._stack[self._top] = data
        self._top += 1

    def peak(self):
        return self._stack[self._top - 1]
