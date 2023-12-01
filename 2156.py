import sys
n = int(sys.stdin.readline())
n_list = [0]*10000
for i in range(n):
    n_list[i]=int(sys.stdin.readline())

d = [0]*10000
d[0] = n_list[0]
d[1] = n_list[0]+n_list[1]
d[2] = max(n_list[2]+n_list[0], n_list[2]+n_list[1], d[1])
for i in range(3,n):
    d[i] = max(n_list[i]+d[i-2], n_list[i]+n_list[i-1]+d[i-3], d[i-1])

print(max(d))