def rdint(n=None):
    if n is None:
        return int(input())
    return [rdint() for _ in range(n)]

n = rdint()
for i in range(n):
    print(i * i)
