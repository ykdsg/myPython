while True:
    try:
        line = input()
        num = line.split()
        print(int(num[0]) + int(num[1]))
    except:
        break
