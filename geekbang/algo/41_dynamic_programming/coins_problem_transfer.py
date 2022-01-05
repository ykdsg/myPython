# 动态规划-状态转移表解决方案
from typing import List


def min_coin_num(price: int, coins: List[int]):
    # 这里初始化memo，理论上硬币的个数不会超过price 的面额（最大个数就是都用1元硬币来组成）
    memo = [price] * (price + 1)
    memo[0] = 0

    for price_part in range(1, price + 1):
        for coin in coins:
            if price_part < coin:
                continue
            else:
                # price_part-coin 最小次数 +当前这枚coin ，就组成 price_part 所需的最小硬币数
                current_coin_step = memo[price_part - coin] + 1
                memo[price_part] = min(memo[price_part], current_coin_step)

    return memo[-1]


if __name__ == '__main__':
    coins = [1, 3, 5]
    price = 9

    print(min_coin_num(price, coins))
