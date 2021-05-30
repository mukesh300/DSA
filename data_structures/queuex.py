from collections import deque


class Queue:
    def __init__(self, data=None):
        self.container = deque(data) if data else deque()

    def enque(self, val):
        return self.container.appendleft(val)

    def deque(self):
        return self.container.pop()

    def size(self):
        return len(self.container)

    def is_empty(self):
        return len(self.container) == 0

    def peek(self):
        return self.container[-1]


