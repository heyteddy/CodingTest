import sys
n = int(sys.stdin.readline())
n_list = [0]*1001
n_list[0] = 1
n_list[1] = 1
n_list[2] = 3

for i in range(3, n+1):
    n_list[i] = n_list[i-1] + (2*n_list[i-2])
result = n_list[n]%10007
print(result)