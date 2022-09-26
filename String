"""
Given a string, S, of length N that is indexed from 0 to , N-1 print its even-indexed and odd-indexed
characters as 2 space-separated strings on a single line (see the Sample below for more detail).

Note:  is considered to be an even index.
"""

# Solution: 

t = int(input())
for i in range(t):
    S = input().strip()
    arr = ["",""]
    for i in range(len(S)):
        arr[i&1] += (S[i])

    print(f"{arr[0]} {arr[1]}")
