from typing import Optional


class Node:
    def __init__(self, data: int):
        self._data = data
        self.next = None


class LinkedStack:
    def __init__(self):
        self._top: Node = None

    def push(self, value: int):
        new_top = Node(value)
        new_top.next = self._top
        self._top = new_top

    def pop(self) -> Optional[int]:
        if self._top:
            value = self._top._data
            self._top = self._top.next
            return value

    def __repr__(self) -> str:
        current = self._top
        nums = []
        while current:
            nums.append(current._data)
            current = current.next
        return " ".join(f"{num}]" for num in nums)


if __name__ == "__main__":
    stack = LinkedStack()
    for i in range(9):
        stack.push(i)
    print(stack)
    for _ in range(3):
        stack.pop()
    print(stack)
