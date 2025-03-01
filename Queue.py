from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
    def append(self, data):
        self.queue.appendleft(data)
    def pop(self):
        return self.queue.pop()
    def size(self):
        return len(self.queue)
    def list(self):
        return list(self.queue)

q = Queue()
q.append(2)
q.append(3)
q.append(5.5)
print(q.pop())
print(q.size())
print(q.list())

