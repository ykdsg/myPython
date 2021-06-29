from typing import Optional


class Node:
    def __init__(self, value: Optional[int], next=None):
        self.value = value
        self.next: Node = next


class SinglyLinkedList:
    def __init__(self):
        self.head: Node = Node(None)
        self.tail: Node = Node(None)
        self.head.next = self.tail

    def insert(self, value: int):
        cur = Node(value)
        cur.next = self.head.next
        self.head.next = cur

    # 这种方式比较直观，但是比较繁琐，而且需要处理像tail.next之类的细节。
    def reverse(self):
        """
        单链表反转
        :return: 
        """
        pre = self.head
        cur = self.head.next
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node

        self.head, self.tail = self.tail, self.head
        # 这里原来的head 里的next指针还指向原来的地址，作为tail需要置空，否则会形成循环队列。
        self.tail.next = None

    def reverse_2(self):
        new_tail = self.head
        current = self.head
        new_head = None
        while current:
            pre = new_head
            new_head = current
            # 这里的顺序不能错，否则current的next就被提前变更为pre了
            current = current.next
            new_head.next = pre

        self.head = new_head
        self.tail = new_tail

    # 利用并行赋值可以简化代码
    def reverse_1(self):
        """
        单链表反转
        :return:
        """
        new_head: Node = None
        new_tail = self.head
        current = self.head
        while current:
            new_head, new_head.next, current = current, new_head, current.next

        self.head = new_head
        self.tail = new_tail

    # 检测环，利用快慢游标进行比较
    def has_cycle(self) -> bool:
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

    # 通过fast游标，先位移n个位置，然后用slow游标 从头开始跟fast一起往后移动，最后在fast.next碰到tail的时候停止，这个之后slow所在的就是倒数n的前一个位置
    def remove_nth_from_end(self, n: int):
        """
        删除倒数第n个节点。假设n大于0
        :param n:
        :return:
        """
        fast_node = self.head
        count = 0
        while fast_node.next != self.tail and count < n:
            fast_node = fast_node.next
            count += 1
        # 说明list中没有这么多node，直接不操作
        if fast_node.next == self.tail and count < n:
            return

        slow_node = self.head
        while fast_node.next != self.tail:
            slow_node = slow_node.next
            fast_node = fast_node.next
        slow_node.next = slow_node.next.next

    def __repr__(self):
        vals = []
        p = self.head.next
        while p.next:
            vals.append(str(p.value))
            p = p.next
        return '->'.join(vals)


# 有序列表合并，因为SinglyLinkedList 默认是降序的，所以这里也按照降序排
def merge_sorted_list(l1: SinglyLinkedList, l2: SinglyLinkedList) -> Optional[SinglyLinkedList]:
    if l1.head.next == l1.tail:
        return l2
    if l2.head.next == l2.tail:
        return l1

    n1_cursor = l1.head.next
    n2_cursor = l2.head.next
    new_head = Node(None)
    current = new_head

    while n1_cursor.value and n2_cursor.value:
        if n1_cursor.value >= n2_cursor.value:
            current.next = n1_cursor
            n1_cursor = n1_cursor.next
        else:
            current.next = n2_cursor
            n2_cursor = n2_cursor.next
        current = current.next

    new_tail = None
    if n1_cursor.value:
        current.next = n1_cursor
        new_tail = l1.tail
    elif n2_cursor.value:
        current.next = n2_cursor
        new_tail = l2.tail

    new_list = SinglyLinkedList()
    new_list.head = new_head
    new_list.tail = new_tail
    return new_list


def create_list() -> SinglyLinkedList:
    linkedList = SinglyLinkedList()
    linkedList.insert(1)
    linkedList.insert(2)
    linkedList.insert(3)
    return linkedList


if __name__ == '__main__':
    linkedList = create_list()
    print(linkedList)
    linkedList.reverse()
    print(linkedList)
    linkedList.reverse_1()
    print(linkedList)
    linkedList.reverse_2()
    print(linkedList)
    print(linkedList.has_cycle())

    list2 = create_list()
    list2.tail.next = list2.head
    print(list2.has_cycle())

    list4 = create_list()
    list5 = create_list()

    list6 = merge_sorted_list(list4, list5)
    print(list6)

    list7 = create_list()
    list7.remove_nth_from_end(3)
    print(list7)
    list7.remove_nth_from_end(1)
    print(list7)
