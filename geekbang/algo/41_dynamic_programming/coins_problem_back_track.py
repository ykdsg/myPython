# 用回溯算法实现下
from typing import List


def min_coin_num(price, coins) -> int:
    min_num = [price]
    do_min(price, coins, 0, min_num)

    return min_num[0]


# 典型的回溯算法的写法，循环每一种coin，递归每一种场景。
def do_min(price: int, coins: List[int], conin_num: int, min_coin_num: List[int]):
    if price == 0:
        min_coin_num[0] = min(min_coin_num[0], conin_num)
        return

    for coin in coins:
        if coin > price:
            continue
        do_min(price - coin, coins, conin_num + 1, min_coin_num)


if __name__ == '__main__':
    coins = [1, 3, 5]
    price = 18
    print(min_coin_num(price, coins))
