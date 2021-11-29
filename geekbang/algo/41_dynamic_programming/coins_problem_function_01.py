from typing import List


# 使用状态转移方程，这个感觉有点像回溯算法，但是状态转移方程的出发点或者视角有点不一样。
def min_coin_num(price: int, coins: List[int], memo: List[int]):
    # 0元0个硬币
    if price == 0:
        return 0
    # 小于0，说明这个组合不存在
    if price < 0:
        return 99999

    if price in coins:
        return 1

    if memo[price] > 0:
        return memo[price]

    # 状态转移方程
    coin_num = min(min_coin_num(price - coin, coins, memo) for coin in coins) + 1
    memo[price] = coin_num
    return coin_num


if __name__ == '__main__':
    coins = [1, 3, 5]
    price = 18
    memo = [-1] * (price + 1)

    print(min_coin_num(price, coins, memo))
