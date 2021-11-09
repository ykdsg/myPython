import re

# content = 'Hello 123 4567 World_This is a Regex Demo'
# print(len(content))
# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
# print(result)
# print(result.group())
# print(result.span())

# 提取对应的内容
content = 'Hello 1234567 World_This is a Regex Demo'
queen_list = re.match('^Hello\s(\d+)\sWorld', content)
print(queen_list)
print(queen_list.group(1))
print(queen_list.span())
