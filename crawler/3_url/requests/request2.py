import requests

# r = requests.get('https://github.com/favicon.ico')
# print(r.text)
# print(r.content)
# 没有headers 会报错
heads = {
    'User-Agent': 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'}
r = requests.get('https://www.zhihu.com/explore', headers=heads)
print(r.text)

r = requests.get('https://github.com/favicon.ico')
with open('favicon.ico', 'wb') as f:
    f.write(r.content)
