from itertools import chain
from typing import Optional


class CirculeQueue:
    def __init__(self, capcity):
        self._capacity = capcity + 1
        # 这里需要初始化下_items，不然后面通过下标进行操作的时候会报错
        self._items = [None] * self._capacity
        self._head = 0
        self._tail = 0

    def enqueue(self, item: str) -> bool:
        # 说明收尾相接，队列满了
        next_tail = (self._tail + 1) % self._capacity
        if next_tail == self._head:
            return False

        self._items[self._tail] = item
        self._tail = next_tail
        return True

    def dequeue(self) -> Optional[str]:
        if self._tail == self._head:
            return None

        value = self._items[self._head]
        self._head = (self._head + 1) % self._capacity
        return value

    def __repr__(self) -> str:
        # 需要判断tail 是否超出一个环
        if self._tail >= self._head:
            return "->".join(item for item in self._items[self._head:self._tail])
        else:
            return "->".join(item for item in chain(self._items[self._head:], self._items[:self._tail]))

    def print(self):
        for item in self._items[self._head:self._tail]:
            print(str(item))


if __name__ == "__main__":
    queue = CirculeQueue(10)
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
