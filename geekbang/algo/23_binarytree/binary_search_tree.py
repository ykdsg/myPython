import math
from queue import Queue
from typing import Optional


class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        self.parent: Optional[TreeNode] = None


class BinarySearchTree:
    def __init__(self, val_list: [int]):
        self.root: Optional[TreeNode] = None
        for n in val_list:
            self.insert(n)

    def insert(self, data):
        """
        插入
        :param data:
        :return:
        """
        assert (isinstance(data, int))

        if self.root is None:
            self.root = TreeNode(data)
        else:
            n = self.root
            while n:
                p = n
                if data < n.val:
                    n = n.left
                else:
                    n = n.right

            new_node = TreeNode(data)
            new_node.parent = p

            if data < p.val:
                p.left = new_node
            else:
                p.right = new_node

        return True

    def search(self, data: int):
        """
        搜索
        返回bst中所有值为data的节点列表
        :param data:
        :return:
        """
        assert (isinstance(data, int))

        # 所有搜索到的节点
        ret = []

        n = self.root
        while n:
            if data < n.val:
                n = n.left
            else:
                if data == n.val:
                    ret.append(n)
                n = n.right

        return ret

    def delete(self, data: int):
        """
        删除
        :param data:
        :return:
        """
        assert (isinstance(data, int))

        # 通过搜索得到需要删除的节点
        del_list = self.search(data)

        for n in del_list:
            # 父节点为空，又不是根节点，已经不在树上，不用再删除
            if n.parent is None and n != self.root:
                continue
            else:
                self._del(n)

    def _del(self, node):
        """
        删除
        所删除的节点N存在以下情况：
        1. 没有子节点：直接删除N的父节点指针
        2. 有一个子节点：将N父节点指针指向N的子节点
        3. 有两个子节点：找到右子树的最小节点M，将值赋给N，然后删除M
        :param data:
        :return:
        """
        # 1 没有子节点：直接删除N的父节点指针，需要判断是左还是右
        if node.left is None and node.right is None:
            # 情况1和2，根节点和普通节点的处理方式不同
            if node == self.root:
                self.root = None
            else:
                if node.val < node.parent.val:
                    node.parent.left = None
                else:
                    node.parent.right = None

                node.parent = None
        # 2 有一个子节点：将N父节点指针指向N的子节点
        # 2.1 仅有一个右节点
        elif node.left is None and node.right is not None:
            if node == self.root:
                self.root = node.right
                self.root.parent = None
                node.right = None
            else:
                if node.val < node.parent.val:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right

                node.right.parent = node.parent
                node.parent = None
                node.right = None
        # 2.2 仅有一个左节点
        elif node.left is not None and node.right is None:
            if node == self.root:
                self.root = node.left
                self.root.parent = None
                node.left = None
            else:
                if node.val < node.parent.val:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left

                node.left.parent = node.parent
                node.parent = None
                node.left = None
        # 3 有两个子节点：找到右子树的最小节点M，将值赋给N，然后删除M
        else:
            min_node = node.right
            # 这里是另一种算法，找到右子树的左节点，进行替换，接着对这个节点进行同样的递归操作。
            # 还有一种做法是直接走到右子树的最小节点，进行替换，就不用递归操作了
            if min_node.left:
                min_node = min_node.left

            if node.val != min_node.val:
                node.val = min_node.val
                self._del(min_node)
            # 右子树的最小值节点与被删除节点的值相等，再次删除原节点
            else:
                self._del(min_node)
                self._del(node)
                
    # 这个比较简洁，但是没有那么好懂
    def delete2(self, value: int):
        node: TreeNode = self.root
        parent = None
        # 找到要删除的节点
        while node and node.val != value:
            parent = node
            node = node.left if node.val > value else node.right

        if not node: return

        # 要删除的节点有两个子节点
        if node.left and node.right:
            # 找到右子树的最小节点，就是最左边的那个节点（不一定是子节点，可能有右子树）
            successor: TreeNode = node.right
            successor_parent = node
            while successor.left:
                successor_parent = successor
                successor = successor.left
            node.val = successor.val
            parent, node = successor_parent, successor

        # 删除节点是叶子节点或者仅有一个子节点
        child = node.left if node.left else node.right

        if not parent:
            self.root = child
        elif parent.left == node:
            parent.left = child
        else:
            parent.right = child

    def get_min(self):
        """
        返回最小值节点
        :return:
        """
        if self.root is None:
            return None

        n = self.root
        while n.left:
            n = n.left
        return n.val

    def get_max(self):
        """
        返回最大值节点
        :return:
        """
        if self.root is None:
            return None

        n = self.root
        while n.right:
            n = n.right
        return n.val

    def in_order(self):
        """
        中序遍历
        :return:
        """
        if self.root is None:
            return []

        return self._in_order(self.root)

    def _in_order(self, node):
        if node is None:
            return []

        ret = []
        n = node
        ret.extend(self._in_order(n.left))
        ret.append(n.val)
        ret.extend(self._in_order(n.right))

        return ret

    def __repr__(self):
        # return str(self.in_order())
        print(str(self.in_order()))
        return self._draw_tree()

    def _bfs(self):
        """
        bfs
        通过父子关系记录节点编号
        :return:
        """
        if self.root is None:
            return []

        ret = []
        q = Queue()
        # 队列[节点，编号]
        q.put((self.root, 1))

        while not q.empty():
            n = q.get()

            if n[0] is not None:
                ret.append((n[0].val, n[1]))
                q.put((n[0].left, n[1] * 2))
                q.put((n[0].right, n[1] * 2 + 1))

        return ret

    def _draw_tree(self):
        """
        可视化
        :return:
        """
        nodes = self._bfs()

        if not nodes:
            print('This tree has no nodes.')
            return

        layer_num = int(math.log(nodes[-1][1], 2)) + 1

        prt_nums = []

        for i in range(layer_num):
            prt_nums.append([None] * 2 ** i)

        for v, p in nodes:
            row = int(math.log(p, 2))
            col = p % 2 ** row
            prt_nums[row][col] = v

        prt_str = ''
        for l in prt_nums:
            prt_str += str(l)[1:-1] + '\n'

        return prt_str


if __name__ == '__main__':
    nums = [20, 40, 90, 50, 60, 55, 51, 56, 61, 10, 70, 30, 45]
    bst = BinarySearchTree(nums)
    print(bst)

    # 插入
    # bst.insert(10)
    # bst.insert(40)
    print(bst)

    bst.delete(50)

    print(bst)

    # 搜索
    # for n in bst.search(2):
    #     print(n.parent.val, n.val)
    #
    # # 删除
    # bst.insert(6)
    # bst.insert(7)
    # print(bst)
    # bst.delete(7)
    # print(bst)
    # bst.delete(6)
    # print(bst)
    # bst.delete(4)
    # print(bst)
    #
    # # min max
    # print(bst.get_max())
    # print(bst.get_min())
