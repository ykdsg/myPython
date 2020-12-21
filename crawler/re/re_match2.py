import re

content = '''Hello 1234567 World_This 
is a Regex Demo
'''
# . 匹配换行符之外的任意字符，.* 匹配多个任意字符，.*? 非贪婪匹配多个任意支付
# 如果匹配的结果在字符串结尾，.*? 就有可能匹配不到任何内容了，因为它会匹配尽可能少的字符
# 因此这里会报错，因为存在换行
# result = re.match('^He.*?(\d+).*?Demo$', content)
# print(result.group(1))

# re.S 的作用是使. 匹配包括换行符在内的所有字符
result = re.match('^He.*?(\d+).*?Demo$', content, re.S)
print(result.group(1))
