from random import randint


def check_duplicates(A, p):
    if p >= len(A):
        return A[p]
    elif A[p+1] == A[p]:
        i = p-1
        while i >= 0 and A[i] == A[p]:
            i = i - 1
        return A[i]
    else:
        return A[p]


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1


def random_partition(A, p, r):
    i = randint(p, r)
    A[i], A[r] = A[r], A[i]
    return partition(A, p, r)



def randomized_select(A, p, r, i):
    if p == r:
        return check_duplicates(A, p)
    q = random_partition(A, p, r)
    k = q - p + 1
    if i == k:  # the pivot value is the answer
        return check_duplicates(A, q)
    elif i < k:
        return randomized_select(A, p, q-1, i)
    else:
        return randomized_select(A, q+1, r, i-k)


input()
A = list(map(int, input().split(' '))) 
print(randomized_select(A,0,len(A)-1, len(A)-1))
