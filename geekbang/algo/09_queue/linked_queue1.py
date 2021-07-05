from typing import Optional


class Node:
    def __init__(self, data: Optional[str]):
        self._data = data
        self.next: Node = None
        self.prev: Node = None


class LinkedQueue:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        # 当前队列大小
        self.num = 0

    def enqueue(self, item: str) -> bool:
        if self.num >= self.capacity:
            return False
        else:
            new_node = Node(item)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.num += 1
            return True

    def dequeue(self) -> Optional[str]:
        if self.num == 0:
            return None
        else:
            value = self.tail.prev._data
            self.tail.prev.prev.next = self.tail
            self.tail.prev = self.tail.prev.prev
            self.num -= 1
            return value

    def __repr__(self) -> str:
        current = self.head
        nums = []
        for _ in range(0, self.num):
            nums.append(current._data)
            current = current.next
        return " ".join(f"{num}]" for num in nums)


if __name__ == '__main__':
    queue = LinkedQueue(5)
    for i in range(6):
        queue.enqueue(str(i))

    print(queue)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
