import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(sys.stdin.readline())
    
arr = list(set(arr))
arr.sort()
arr.sort(key=len)

for i in arr:
    print(i)

# 참고    
# https://velog.io/@ssunykim/%EB%B0%B1%EC%A4%80-1181%EB%B2%88-%EB%8B%A8%EC%96%B4-%EC%A0%95%EB%A0%AC