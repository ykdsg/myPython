# 1.单链表的插入、删除、查找操作；
# 2.链表中存储的数据类型是Int
from typing import Optional


class Node(object):
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        """Node节点存储数据的设置方法.
        参数:
            data:新的存储数据
        """
        self.__data = data

    @property
    def next_node(self):
        """获取Node节点的next指针值.
        返回:
            next指针数据
        """
        return self.__next

    @next_node.setter
    def next_node(self, next_node):
        """Node节点next指针的修改方法.
        参数:
            next:新的下一个Node节点的引用
        """
        self.__next = next_node


class SinglyLinkedList(object):
    def __init__(self):
        self.__head = None

    def find_by_value(self, value) -> Optional[Node]:
        """按照数据值在单向列表中查找.
        参数:
            value:查找的数据
        返回:
            Node
        """
        node = self.__head
        while (node is not None) and (node.__data != value):
            node = node.next_node
        return node

    def find_by_index(self, index) -> Optional[Node]:
        node = self.__head
        pos = 0
        while (node is not None) and (pos != index):
            node = node.next_node
            pos += 1
        return node

    def insert_to_head(self, value):
        node = Node(value)
        node.next_node = self.__head
        self.__head = node

    def insert_value_after(self, node, value):
        """
        指定node节点之后插入一个存储value 的node节点
        :param node:
        :param value:
        :return:
        """
        new_node = Node(value)
        self.insert_node_after(node, new_node)

    def insert_node_after(self, node: Node, new_node: Node):
        if node is None:
            return
        new_node.next_node = node.next_node
        node.next_node = new_node

    def insert_node_before(self, node: Node, new_node: Node):
        if not self.__head or not node or not new_node:
            return

        if self.__head == node:
            new_node.next_node = self.__head
            self.__head = new_node

        current_node = self.__head
        while current_node and current_node.next_node != node:
            current_node = current_node.next_node

        if not current_node:
            return
        self.insert_node_after(current_node, new_node)

    def insert_value_before(self, node: Node, value: int):
        if not value:
            return
        self.insert_node_before(node, Node(value))

    def delete_by_node(self, node: Node):
        if not self.__head or not node:
            return
        if self.__head == node:
            self.__head = node.next_node
            return

        current_node = self.__head
        while current_node and current_node.next_node != node:
            current_node = current_node.next_node

        if not current_node:
            return
        current_node.next_node = node.next_node

    def delete_by_value(self, value: int):
        if not self.__head or not value:
            return
        if self.__head.__data == value:
            self.__head = self.__head.next_node
            return
        current_node = self.__head
        while current_node:
            next_node_ = current_node.next_node
            if not next_node_:
                break
            elif next_node_.__data == value:
                current_node.next_node = next_node_.next_node
                break
            else:
                current_node = current_node.next_node

    def __str__(self) -> str:
        return "->".join(str(node.__data) for node in self)

    __repr__ = __str__

    def __iter__(self):
        node = self.__head
        while node:
            yield node
            node = node.next_node


if __name__ == "__main__":
    linkedList = SinglyLinkedList()
    for i in range(15):
        linkedList.insert_to_head(i)
    node9 = linkedList.find_by_value(9)
    linkedList.insert_value_before(node9, 20)
    linkedList.insert_value_before(node9, 16)
    linkedList.insert_value_before(node9, 16)
    print(linkedList)
    linkedList.delete_by_value(16)
    node11 = linkedList.find_by_index(3)
    linkedList.delete_by_node(node11)
    headNode = linkedList.find_by_index(0)
    linkedList.delete_by_node(headNode)
    linkedList.delete_by_value(13)
    print(linkedList)

    node01 = Node(1)
    node02 = Node(1)
    print(node01 == node02)
