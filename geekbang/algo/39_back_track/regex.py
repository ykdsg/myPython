is_match = False


def rmatch(regex_index: int, str_index: int, regex: str, main_str: str):
    global is_match
    if is_match:
        return

    # 说明正则表达式全部匹配
    if regex_index >= len(regex):
        is_match = True
        return
    # 主字符串已经没得匹配了，但是正则还没匹配完
    if str_index >= len(main_str) and regex_index < len(regex):
        is_match = False
        return

    # 匹配1个或多个字符的情况
    if regex[regex_index] == '*':
        for i in range(str_index, len(main_str)):
            rmatch(regex_index + 1, i + 1, regex, main_str)
    elif regex[regex_index] == '?':
        # 匹配0个字符和1个字符的情况
        rmatch(regex_index + 1, str_index, regex, main_str)
        rmatch(regex_index + 1, str_index + 1, regex, main_str)
    else:
        if regex[regex_index] == main_str[str_index]:
            rmatch(regex_index + 1, str_index + 1, regex, main_str)
            
    pass


if __name__ == '__main__':
    regex = 'ab*eee?d'
    main = 'abcdsadfkjlekjoiwjiojieeecd'
    rmatch(0, 0, regex, main)
    print(is_match)
