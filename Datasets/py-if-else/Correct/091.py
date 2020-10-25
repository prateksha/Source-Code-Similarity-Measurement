N = int(input().strip())
if( N % 2 != 0):
    print("Weird")
else:
    if(N > 20 or N in range(2, 6)):
        print("Not Weird")
    else:
        print("Weird")