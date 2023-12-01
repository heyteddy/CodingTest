import sys
height=160
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

for i in arr:
    if i == height:
        print('I', height)
    elif i > height:
        print('P')
    else:
        print('I', height)