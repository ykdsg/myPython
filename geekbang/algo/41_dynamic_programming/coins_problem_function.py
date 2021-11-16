# 状态转移方程，这个解法就很像回溯+缓存
def min_coin_num(price: int, memo: [int], coins: [int]) -> int:
    if price == 0:
        return 0

    # 如果刚好等于面额直接返回
    if price in coins:
        return 1

    if memo[price] > 0:
        return memo[price]

    pre_min_coin = 999999
    for coin in coins:
        if price < coin:
            continue
        else:
            pre_min_coin = min(pre_min_coin, min_coin_num(price - coin, memo, coins))

    current_step = pre_min_coin + 1
    memo[price] = current_step
    return current_step


if __name__ == '__main__':
    coins = [1, 3, 5]
    price = 9
    memo = [-1] * (price + 1)

    print(min_coin_num(price, memo, coins))
