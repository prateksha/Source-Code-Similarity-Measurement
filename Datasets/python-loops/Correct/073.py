# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

N = int(sys.stdin.readline())

for i in range(0,N):
    sys.stdout.write(str(i**2) + "\n")