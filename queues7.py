from collections import deque
from heapq import heappop, heappush
from itertools import count

class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()

class PriorityQueue:
    def __init__(self):
        self._elements = []
        self._counter = count()

    def enqueue_with_priority(self,priority,value):
        element = (-priority, next(self._counter), value)
        heappush(self._elements, elements)

    def dequeue(self):
        return heappop(self._elements)[1]