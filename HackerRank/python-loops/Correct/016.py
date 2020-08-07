# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())

if N >= 1 & N <= 20:
    i = 0
    while i < N:
        print(i**2)
        i += 1