from collections import deque

class Queue:
    def __init__(self):
        self.elements = deque()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()

from queues import Queue

fifo = Queue()
fifo.enqueue("1st")
fifo.enqueue("2nd")
fifo.enqueue("3rd")

print(fifo.dequeue())
'1st'
print(fifo.dequeue())
'2nd'
print(fifo.dequeue())
'3rd'
