# 这个解法就很像回溯+缓存
def min_coin_num(price: int, memo: [int], coins: [int]) -> int:
    # 如果刚好等于面额直接返回
    if price in coins:
        return 1

    if memo[price] > 0:
        return memo[price]

    pre_temp = []
    for coin in coins:
        if price < coin:
            continue
        pre_temp.append(min_coin_num(price - coin, memo, coins))

    pre_step = min(pre_temp)

    current_step = pre_step + 1
    memo[price] = current_step
    return current_step


if __name__ == '__main__':
    coins = [1, 3, 5]
    price = 9
    memo = [-1] * (price + 1)

    print(min_coin_num(price, memo, coins))
