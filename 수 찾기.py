import sys

N = int(sys.stdin.readline())
A = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

for n in M_list:
    if n in A:
        print(1)
    else:
        print(0)