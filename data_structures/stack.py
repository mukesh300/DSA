from collections import deque


class Stack:
    def __init__(self, data=None):
        self.container = deque(data) if data else deque()

    def push(self, val):
        return self.container.append(val)

    def pop(self):
        return self.container.pop()

    def size(self):
        return len(self.container)

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0


def reverse_string(data):
    s = Stack(data)
    return "".join([s.pop() for _ in range(s.size())])


def is_balanced(data):
    s = Stack()
    map = {")": "(", "}": "{", "]": "["}
    for char in data:
        if char in ["(", "{", "["]:
            s.push(char)
        if char in [")", "}", "]"]:
            if s.size() == 0:
                return False
            elif s.peek() == map[char]:
                s.pop()
    return s.size() == 0


print(reverse_string("We will conquere COVID-19"))
print(is_balanced("{[a+b]*(x+2y)*{gg+kk}}"))
