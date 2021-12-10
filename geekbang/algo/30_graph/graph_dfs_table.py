from typing import Dict, List


def dfs_check(vertex_index: int, graph: Dict[int, List[int]], color: List[int], memo: List[int]):
    '''
    使用邻接表的方式进行计算
    :param vertex_index:
    :param graph:
    :param color:
    :return:
    '''
    # 表示当前这个节点正在处理
    color[vertex_index] = 1
    memo.append(vertex_index)

    for current_index in graph[vertex_index]:
        if color[current_index] == 1:
            print("has loop: %d -> %d " % (vertex_index, current_index))
            print("loop:", memo, current_index)
        elif color[current_index] == -1:
            continue
        else:
            dfs_check(current_index, graph, color, memo)

    # 表示当前节点整条链路都已经处理完了，后面其他节点遇到现在这个节点的时候可以直接跳过了，因为已经处理过了，就是上面for循环中color[current_index] == -1 的逻辑。
    color[vertex_index] = -1
    memo.remove(vertex_index)


def check_loop(vertex_num: int, graph: Dict[int, List[int]], color: List[int]):
    memo = []
    for vertex_index in range(vertex_num):
        if color[vertex_index] == -1:
            continue
        dfs_check(vertex_index, graph, color, memo)


if __name__ == '__main__':
    # 顶点个数
    vertex_num = 5
    graph = {}
    graph[0] = [1]
    graph[1] = [2, 3]
    graph[2] = [3]
    graph[3] = [4, 0]
    graph[4] = [0, 1]

    color = [0] * vertex_num
    check_loop(vertex_num, graph, color)
