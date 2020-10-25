#!/bin/python3

import sys
n = int(input().strip())

message = "Weird" if n % 2 != 0  else "Not Weird" if 2 <= n <= 5 else "Weird" if 6 <= n <= 20 else "Not Weird"
print(message)