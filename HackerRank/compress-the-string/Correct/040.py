from itertools import groupby


def RLE(s):
    return [(len(list(g)), k) for k, g in groupby(s)]


def main():
    s = input()

    r = RLE(s)
    for i in r:
        print("({0}, {1})".format(i[0], i[1]), end=" ")
    print()

    
if __name__ == '__main__':
    main()
