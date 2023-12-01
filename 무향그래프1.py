import sys
node, edge = map(int, sys.stdin.readline().split())
adj = [[0 for _ in range(node) for _ in range(node)]]

for _ in range(edge):
    src, dest = map(int, sys.stdin.readline().split())
    adj[src-1][dest-1] = 1
    adj[dest-1][src-1] = 1