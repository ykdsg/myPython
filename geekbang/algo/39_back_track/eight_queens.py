# 八皇后问题

# 棋盘尺寸
# BOARD_SIZE = 8

# list的下标表示棋盘的行，对应的值表示皇后的位置
queen_list = [0] * 8

solution_count = 0


def eight_queens(row: int):
    # 表示棋盘都放好了
    if row >= 8:
        global solution_count
        solution_count += 1
        print(queen_list)

    else:
        # 每一行都有 8 种放法
        for column in range(8):
            if is_valid_pos(row, column):
                # 第row行的旗子放到了column列
                queen_list[row] = column
                # 考察下一行的情况
                eight_queens(row + 1)


def is_valid_pos(cur_column: int, pos: int) -> bool:
    i = 0
    while i < cur_column:
        # 同一列的情况
        if queen_list[i] == pos:
            return False
        # 对角线情况
        elif cur_column - i == abs(pos - queen_list[i]):
            return False
        i += 1

    return True


if __name__ == '__main__':
    print('--- eight queens sequence ---')
    eight_queens(0)

    print('\n--- solution count ---')
    print(solution_count)
