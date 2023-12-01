import sys
n = int(sys.stdin.readline())
n_list = [0,1,2]

for i in range(3, n+1):
    n_list.append(n_list[i-1] + n_list[i-2])
result = n_list[n]%10007
print(result)
