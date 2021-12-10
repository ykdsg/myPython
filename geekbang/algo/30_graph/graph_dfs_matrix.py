from typing import List


def dfs_check(vertex_index: int, graph: List[List[int]], color: List[int], vertex_num: int):
    '''
    使用邻接矩阵进行深度遍历来检查是否存在环
    :param vertex_index:
    :param graph:
    :param color:
    :param vertex_num:
    :return:
    '''
    # 节点vertex_index 标记为访问过状态
    color[vertex_index] = 1
    for current_index in range(vertex_num):
        # 当前节点有指向的节点
        if graph[vertex_index][current_index] > 0:
            # 而且这个节点已经被访问过了
            if color[current_index] == 1:
                print("has loop: %d -> %d " % (vertex_index, current_index))
            elif color[current_index] == -1:
                # 当前节点后边的结点都被访问过了，直接跳下一个结点，说明之前这个数据已经排查完了，这里不用重复记录
                continue
            else:
                dfs_check(current_index, graph, color, vertex_num)
    # 遍历过所有相连的结点，本节点标记为-1
    color[vertex_index] = -1


def check_loop(vertex_num: int, graph: List[List[int]], color: List[int]):
    for vertex_index in range(vertex_num):
        # 该结点后边的节点都访问过了，直接跳过
        if color[vertex_index] == -1:
            continue
        dfs_check(vertex_index, graph, color, vertex_num)


if __name__ == '__main__':
    # 顶点个数
    vertex_num = 5

    graph = [[0] * vertex_num for _ in range(vertex_num)]
    graph[0][1] = 1
    graph[1][2] = 1
    graph[2][3] = 1
    graph[3][4] = 1
    graph[4][0] = 1

    color = [0] * vertex_num

    check_loop(vertex_num, graph, color)
