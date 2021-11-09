# 八皇后问题
BOARD_SIZE = 8

queens_list = [0] * BOARD_SIZE
success_count = 0


# 递归计算，可以想象为queens_list 就像盘子，从第一排起根据条件在上面放东西，放好之后交给第二排，一直往后传。
# 传到最后一排的时候，东西也放好了。
def calc_queens(row: int):
    # 递归结束条件
    if row >= BOARD_SIZE:
        global success_count
        success_count += 1
        print(queens_list)

    else:
        # 每行都有 BOARD_SIZE 种情况
        for column in range(0, BOARD_SIZE):
            # 选择可以用的这个位置后，需要根据现有的情况 queens_list 里面已有的记录，计算下一行
            if is_valid_pos(row, column):
                queens_list[row] = column
                calc_queens(row + 1)


# 判断位置是否合法，只要判断row 之前的皇后的位置，跟当前位置是否存在冲突
def is_valid_pos(row, column) -> bool:
    current_row = 0
    while current_row < row:
        # 判断是否存在同一列的情况
        if queens_list[current_row] == column:
            return False
        # 判断是否存在对角线的情况
        elif row - current_row == abs(column - queens_list[current_row]):
            return False
        current_row += 1

    return True


if __name__ == '__main__':
    print('--- eight queens sequence ---')
    calc_queens(0)

    print('\n--- solution count ---')
    print(success_count)
