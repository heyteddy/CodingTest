import sys
n = int(sys.stdin.readline())
n_list = [1]*10

for i in range(1, n):
    for j in range(1, 10): # 길이가 n번째 길이일 때, 오르막 수의 개수
        n_list[j] += n_list[j-1]
        
result = sum(n_list) % 10007
print(result)