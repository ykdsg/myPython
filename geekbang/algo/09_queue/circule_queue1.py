from itertools import chain
from typing import Optional


class circule_queue:

    def __init__(self, n: int):
        self.items = []
        self.head = 0
        self.tail = 0
        self.n = n + 1

    def enqueue(self, item: str) -> bool:
        # 队列满的情况
        if (self.tail + 1) % self.n == self.head:
            return False
        else:
            self.items.append(item)
            self.tail += 1
            return True

    def dequeue(self) -> Optional[str]:
        if self.head == self.tail:
            return None
        value = self.items[self.head]
        self.head += 1
        return value

    def __repr__(self) -> str:
        if self.tail >= self.head:
            return "->".join(item for item in self.items[self.head:self.tail])
        else:
            return "->".join(item for item in chain(self.items[self.head:], self.items[:self.tail]))


if __name__ == "__main__":
    queue = circule_queue(10)
    for i in range(9):
        queue.enqueue(str(i))
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
