from typing import List


def min_coin_num(price: int, coins: List[int]):
    memo = [price] * (price + 1)
    memo[0] = 0

    for part_price in range(1, price + 1):
        for coin in coins:
            if part_price < coin:
                continue
            current_step = memo[part_price - coin] + 1
            memo[part_price] = min(memo[part_price], current_step)

    return memo[-1]


if __name__ == '__main__':
    coins = [3, 5, 1]
    price = 9

    print(min_coin_num(price, coins))
