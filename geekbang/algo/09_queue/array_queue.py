from typing import Optional


# 用数组/列表实现队列，需要注意的是对边界条件的判断，入队的时候需要判断是否需要压缩队列
class ArrayQueue:
    def __init__(self, capacity: int):
        self._items = []
        self._capacity = capacity
        self._head = 0
        self._tail = 0

    def enqueue(self, item: str) -> bool:
        if self._tail == self._capacity:
            if self._head == 0:
                return False
            # 说明需要压缩
            else:
                for i in range(0, self._tail - self._head):
                    self._items[i] = self._items[i + self._head]
                self._tail = self._tail - self._head
                self._head = 0

        self._items.insert(self._tail, item)
        self._tail += 1
        return True

    def dequeue(self) -> Optional[str]:
        if self._head != self._tail:
            item = self._items[self._head]
            self._head += 1
            return item
        else:
            return None
