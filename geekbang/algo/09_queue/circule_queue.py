from itertools import chain
from typing import Optional


class circule_queue:
    def __init__(self, capacity):
        self._items = []
        self._capacity = capacity + 1
        self._head = 0
        self._tail = 0

    def enqueue(self, item: str) -> bool:
        if (self._tail + 1) % self._capacity == self._head:
            return False

        self._items.append(item)
        self._tail = (self._tail + 1) % self._capacity
        return True

    def dequeue(self) -> Optional[str]:
        if self._head != self._tail:
            item = self._items[self._head]
            self._head = (self._head + 1) % self._capacity
            return item

    def __repr__(self) -> str:
        if self._tail >= self._head:
            return " ".join(item for item in self._items[self._head: self._tail])
        else:
            return " ".join(item for item in chain(self._items[self._head:], self._items[:self._tail]))


if __name__ == "__main__":
    queue = circule_queue(10)
    for i in range(9):
        queue.enqueue(str(i))
    # queue.print()
    queue.enqueue("9")

    print(queue)
    queue.enqueue("10")
    print(queue)

    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    print(queue)

    queue.enqueue("11")
    print(queue)
    queue.enqueue("12")
    print(queue)
