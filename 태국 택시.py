class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y

def minimum_cost(N, taxi_routes):
    taxi_routes.sort(key=lambda x: x[2])  # 가중치 기준으로 정렬
    uf = UnionFind(N)
    total_cost = 0
    edges_added = 0
    
    for a, b, c in taxi_routes:
        if uf.find(a - 1) != uf.find(b - 1):
            uf.union(a - 1, b - 1)
            total_cost += c
            edges_added += 1
            if edges_added == N - 1:  # MST 완성
                break
    
    return total_cost

# 입력 받기
N, M = map(int, input().split())
taxi_routes = []

for _ in range(M):
    a, b, c = map(int, input().split())
    taxi_routes.append((a, b, c))

# 최소 비용 계산 및 출력
result = minimum_cost(N, taxi_routes)
print(result)