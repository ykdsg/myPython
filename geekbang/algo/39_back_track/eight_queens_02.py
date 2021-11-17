from typing import List


def calc_queens(row: int, queens_list: List[int], success_result: List[int]):
    if row >= BOARD_SIZE:
        success_result[0] += 1
        print(queens_list)
        return

    for colume in range(BOARD_SIZE):
        if isValid(row, colume, queens_list):
            queens_list[row] = colume
            calc_queens(row + 1, queens_list, success_result)


def isValid(row, colume, queens_list: List[int]) -> bool:
    row_index = 0
    while row_index < row:
        if queens_list[row_index] == colume:
            return False
        if abs(queens_list[row_index] - colume) == row - row_index:
            return False
        row_index += 1

    return True


if __name__ == '__main__':
    BOARD_SIZE = 8
    queens_list = [0] * BOARD_SIZE
    success_result = [0]

    print('--- eight queens sequence ---')
    calc_queens(0, queens_list, success_result)

    print('\n--- solution count ---')
    print(success_result[0])
