import sys
n, e = map(int, sys.stdin.readline().split())

adj = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(e):
    src, dst = map(int, sys.stdin.readline().split())
    adj[src-1][dst-1] = 1
    adj[dst-1][src-1] = 1
    
print(adj)