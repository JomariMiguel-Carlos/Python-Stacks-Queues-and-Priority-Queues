class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()

lifo = Stack("1st", "2nd", "3rd")
for elements in lifo:
    print(element)
