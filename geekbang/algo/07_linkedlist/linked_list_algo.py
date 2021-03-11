from typing import Optional


# 单链表在处理的时候使用slow 和fast 的概念能够比较方便的找到中心位点（利用fast 比slow 快一倍），以及倒数n的位置（fast 比slow 领先n个位置）
class Node:
    def __init__(self, data: int, next=None):
        self.__data = data
        self.__next = next

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next_node(self):
        return self.__next

    @next_node.setter
    def next_node(self, next_node):
        self.__next = next_node


def reverse(head: Node) -> Optional[Node]:
    resvered_head = None
    current = head
    while current:
        resvered_head, resvered_head.next_node, current = current, resvered_head, current.next_node
    return resvered_head


def has_cycle(head: Node) -> bool:
    slow, fast = head, head
    while fast and fast.next_node:
        slow = slow.next_node
        fast = fast.next_node.next_node
        if slow == fast:
            return True
    return False


def remove_nth_from_end(head: Node, n: int) -> Optional[Node]:
    '''
    删除倒数第n个节点。假设n大于0
    :param head:
    :param n:
    :return:
    '''
    fast = head
    count = 0
    while fast and count < n:
        fast = fast.next_node
        count += 1

    # 说明链表长度没这么长
    if not fast and count < n:
        return head

    if not fast and count == n:
        return head.next_node

    slow = head  # 这个时候slow 到fast的距离就是n
    # 如果fast触底了，那就说明slow 所在的位置就是倒数n的前一个位置
    while fast.next_node:
        fast = fast.next_node
        slow = slow.next_node

    slow.next_node = slow.next_node.next_node
    return head
