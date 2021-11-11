is_match = False


def rmatch(regex_index, str_index, regex, main_str):
    global is_match
    if is_match:
        return

    # 表示能够匹配
    if regex_index >= len(regex):
        is_match = True
        return

    # 表示没能匹配成功
    if regex_index < len(regex) and str_index >= len(main_str):
        is_match = False
        return

    if regex[regex_index] == '*':
        for i in range(str_index, len(main_str)):
            # '*'匹配0个或者多个字符 
            rmatch(regex_index + 1, i, regex, main_str)

    if regex[regex_index] == '?':
        # '?'匹配0个或1个字符
        rmatch(regex_index + 1, str_index, regex, main_str)
        rmatch(regex_index + 1, str_index + 1, regex, main_str)

    # 当期字符匹配
    if regex[regex_index] == main_str[str_index]:
        rmatch(regex_index + 1, str_index + 1, regex, main_str)


if __name__ == '__main__':
    regex = 'ab*eee?d'

    #
    is_match = False
    main = 'abeeecd'
    rmatch(0, 0, regex, main)
    print(is_match)

    is_match = False
    main = 'abceeecd'
    rmatch(0, 0, regex, main)
    print(is_match)

    is_match = False
    main = 'abceefecd'
    rmatch(0, 0, regex, main)
    print(is_match)

#     最终结果应该是True,True,False
