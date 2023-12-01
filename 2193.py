import sys
n = int(sys.stdin.readline())
n_list = [0]*1000
n_list[1] = 1

for i in range(2,n+1):
    n_list[i] = n_list[i-1]+n_list[i-2] # 점화식
result = n_list[n]
print(result)