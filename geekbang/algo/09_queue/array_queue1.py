from typing import Optional


class ArrayQueue:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head: int = 0
        self.tail: int = 0
        self.items = []

    def enqueue(self, item: str) -> bool:
        # 如果满了需要重新整理
        if self.tail == self.capacity:
            if self.head == 0:
                return False
            else:
                for i in range(0, self.tail - self.head):
                    self.items[i] = self.items[i + self.head]

        self.items.append(item)
        self.tail += 1
        return True

    def dequeue(self) -> Optional[str]:
        if self.head == self.capacity:
            return None
        value = self.items[self.head]
        self.head += 1
        return value

    def __repr__(self) -> str:
        return " ".join(f"{self.items[i]}]" for i in range(self.head, self.tail))


if __name__ == '__main__':
    queue = ArrayQueue(5)
    for i in range(6):
        queue.enqueue(str(i))

    print(queue)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
