n = int(raw_input())
if n >= 1 and n<= 100:
    if n%2 != 0:
        print("Weird")
    else:    
        if n >= 2 and n < 5 :
            print("Not Weird")
        elif n >= 6 and n <= 20:
            print("Weird")
        elif n > 20 and n <= 100:
            print("Not Weird")

