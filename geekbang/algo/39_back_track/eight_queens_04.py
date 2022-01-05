from typing import List


def calc_queens(row_index: int, queen_locaions: List[int], success_count: List[int]):
    board_size = len(queen_locaions)

    if row_index >= board_size:
        success_count[0] += 1
        print(queen_locaions)
        return

    for column_index in range(0, board_size):
        if check_valid(row_index, column_index, queen_locaions):
            queen_locaions[row_index] = column_index
            calc_queens(row_index + 1, queen_locaions, success_count)
        else:
            continue


def check_valid(row_index: int, column_index: int, queen_locaions: List[int]):
    for current_row in range(row_index):
        if queen_locaions[current_row] == column_index:
            return False
        # 判断是否在对角线
        elif abs(queen_locaions[current_row] - column_index) == row_index - current_row:
            return False

    return True


if __name__ == '__main__':
    board_size = 8
    queen_locaions = [0] * board_size
    success_count = [0]

    calc_queens(0, queen_locaions, success_count)
    print("success count:", success_count[0])
