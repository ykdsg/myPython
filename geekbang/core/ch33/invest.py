# 获取Gemini交易所报价数据
import json

import pandas as pd
import requests
from matplotlib import pyplot as plt


def get_price():
    gemini_ticker = "https://api.gemini.com/v1/pubticker/{}"
    symbol = "btcusd"
    btc_data = requests.get(gemini_ticker.format(symbol)).json()
    print(json.dumps(btc_data, indent=4))


# 获取最近一个小时交易数据并绘图
def get_hour_price():
    # 要获取的数据时间段
    periods = "3600"

    # 抓取数据
    #  这个链接现在已经失效了
    resp = requests.get("https://api.cryptowat.ch/markets/gemini/btcusd/ohlc", params={
        "periods": periods
    })
    data = resp.json()

    # 转换成pandas的data frame
    df = pd.DataFrame(
        data["result"][periods],
        columns=[
            "收盘时间",
            "开盘时间",
            "最高价",
            "最低价",
            "收盘价",
            "成交量",
            "NA"
        ]
    )

    # 输出
    print(df.head())
    ax = df["收盘价"].plot(figsize=(14, 7))
    fig = ax.get_figure()
    plt.show()


if __name__ == "__main__":
    get_price()
    get_hour_price()
