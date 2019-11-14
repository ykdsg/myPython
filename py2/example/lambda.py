__author__ = 'wuzheng.yk'


def make_repeater(n):
    return lambda s: s * n

a=lambda s,n: s * n

twice = make_repeater(2)

print twice('word')
print twice(5)
print a(5,1)