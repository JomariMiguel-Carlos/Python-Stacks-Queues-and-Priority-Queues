from collections import deque

class Queue:
    def __init__(self, *elements):
        self._elements = deque(elements)

    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()

fifo = Queue ("1st", "2nd", "3rd")

for elements in fifo:
    print(elements)


class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()

lifo = Stack("1st", "2nd", "3rd")
print("")
print("Then pop or reverse then this will be the order:")
for element in lifo:
    print(element)
