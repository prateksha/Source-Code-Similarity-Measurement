# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
N = int(sys.stdin.readline())
i = 0
while i<N:
    a = str(pow(i,2))
    sys.stdout.write(a + '\n')
    i = i+1