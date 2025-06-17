n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

visited = [0] * n
connected_components = 0
def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
for i in range(n):
    if not visited[i]:
        dfs(i)
        connected_components += 1
print(connected_components - 1)