from itertools import groupby


def compress(text):
    res = ''
    for key, group in groupby(text, lambda x: x):
        res = res + '({1}, {0})'.format(key, len(list(group))) + ' '
    print(res)


text = input()
compress(text)
