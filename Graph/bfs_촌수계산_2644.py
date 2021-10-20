n = int(input())
x,y = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
result = [0]*(n+1)
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

from collections import deque
def bfs(start):
    q = deque()
    q.append(start)
    visit = [0 for i in range(n+1)]
    visit[start] = 1
    while q:
        d = q.popleft()
        for i in graph[d]:
            if visit[i] == 0:
                visit[i] = 1
                result[i] = result[d] + 1
                q.append(i)
bfs(y)

print(result[x] if result[x] != 0 else -1)
