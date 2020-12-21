import re

content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
# match ⽅法是从字符串的开头开始匹配的，⼀旦开头不匹配，那么整个匹配就失败了
# search 在匹配时会扫描整个字符串，然后返回第⼀个成功匹配的结果
result = re.search('Hello.*?(\d).*?Demo', content)
print(result)
