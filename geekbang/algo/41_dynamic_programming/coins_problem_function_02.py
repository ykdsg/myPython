# 状态转移方程，这个解法就很像回溯+缓存
from typing import List


def min_coin_num(price: int, coins: List[int], memo: List[int]):
    if price == 0:
        return 0

    if price < 0:
        return 99999

    if memo[price] > 0:
        return memo[price]

    result = min(min_coin_num(price - coin, coins, memo) for coin in coins) + 1
    memo[price] = result
    return result


if __name__ == '__main__':
    coins = [1, 3, 5]
    price = 18
    memo = [-1] * (price + 1)

    print(min_coin_num(price, coins, memo))
