import re

if __name__ == '__main__':
    str1 = 'Untappd 3.99人数1.9K'
    str3 = 'Untappd 4.28/5'

    str2 = 'Un评分:4.23'
    str5 = 'Untappd：4.1'

    reg1 = r'Untappd.*?([0-9]*\.[0-9]+|[0-9]+)'
    reg2 = r'Un评分.*?([0-9]*\.[0-9]+|[0-9]+)'
    match = re.match(reg1, str1)
    score1 = match.group(1)

    score2 = re.match(reg1, str5).group(1)
    print(score2)

    # print(type(score1))
    # print(float(score1))
