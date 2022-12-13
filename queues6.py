from collections import deque
from heapq import heappop,heappush

class PriorityQueue:
    def __init__(self):
        self._elements = []

    def enqueue_with_priority(self, priority, value):
        heappush(self._elements,(priority,value))

    def dequeue(self):
        return heappop(self._elements)

CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1

messages = PriorityQueue()
messages.enqueue_with_priority(IMPORTANT,"Windshields wipers turned on")
messages.enqueue_with_priority(NEUTRAL,"Radio station tuned in")
messages.enqueue_with_priority(CRITICAL,"Brake pedal depressed")
messages.enqueue_with_priority(IMPORTANT,"Hazard lights turned on")


class PriorityQueue:
    def __init__(self):
        self._elements = []

    def enqueue_with_priority(self, priority, value):
        heappush(self._elements, (-priority,value))

    def dequeue(self):
        return heappop(self._elements)[1]

print(messages.dequeue())
print(messages.dequeue())
print(messages.dequeue())
print(messages.dequeue())