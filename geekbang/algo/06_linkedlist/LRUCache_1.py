from dataclasses import dataclass


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev: Node = None
        self.next: Node = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_dict = {}
        # 增加哨兵节点，方便后续处理
        self.head: Node = Node(None, None)
        self.tail: Node = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def put(self, key, value):
        if key in self.key_dict.keys():
            cur = self.key_dict[key]
            cur.value = value
            self._move_new_to_top(cur)
        else:
            cur = Node(key, value)
            self.key_dict[key] = cur
            self._put_to_top(cur)
            # 如果超出长度，干掉尾节点。
            if len(self.key_dict) > self.capacity:
                self.key_dict.pop(self.tail.prev.key)
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev

    def get(self, key):
        if key in self.key_dict.keys():
            cur = self.key_dict[key]
            self._move_new_to_top(cur)
            return cur.value
        return None

    def _move_new_to_top(self, cur: Node):
        """
        将节点从原来位置移到头部
        :param cur:
        :return:
        """
        cur.prev.next = cur.next
        cur.next.prev = cur.prev
        self._put_to_top(cur)

    def _put_to_top(self, cur: Node):
        """
        将节点放入头部
        :param cur:
        :return:
        """

        cur.prev = self.head
        cur.next = self.head.next
        self.head.next.prev = cur
        self.head.next = cur

    def __repr__(self):
        vals = []
        p = self.head.next
        while p.next:
            vals.append(str(p.value))
            p = p.next
        return '->'.join(vals)


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache)
    cache.get(1)  # 返回  1
    cache.put(3, 3)  # 该操作会使得密钥 2 作废
    print(cache)
    cache.get(2)  # 返回 -1 (未找到)
    cache.put(4, 4)  # 该操作会使得密钥 1 作废
    print(cache)
    cache.get(1)  # 返回 -1 (未找到)
    cache.get(3)  # 返回  3
    print(cache)
    cache.get(4)  # 返回  4
    print(cache)
