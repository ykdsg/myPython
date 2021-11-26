from typing import List


def calc_queens(row_inext: int, queen_locaions: List[int], success_count: List[int]):
    board_size = len(queen_locaions)

    if row_inext >= board_size:
        success_count[0] += 1
        print(queen_locaions)
        return

    for column_index in range(0, board_size):
        # 如果当前位置可以放，那就接着到下一行
        if is_valid_location(row_inext, column_index, queen_locaions):
            queen_locaions[row_inext] = column_index
            calc_queens(row_inext + 1, queen_locaions, success_count)


def is_valid_location(row, column, queen_locaions) -> bool:
    # 判断是否在同一列上还是简单的
    for current_row in range(row):
        if queen_locaions[current_row] == column:
            return False
        elif abs(queen_locaions[current_row] - column) == row - current_row:
            return False

    return True


if __name__ == '__main__':
    board_size = 8
    queen_locaions = [0] * board_size
    success_count = [0]

    calc_queens(0, queen_locaions, success_count)
    print("success count:", success_count[0])
