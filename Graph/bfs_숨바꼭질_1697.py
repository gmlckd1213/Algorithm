from collections import deque
a, b = map(int,input().split())
MAX = 200000
dist = [0]*(MAX+1)

def bfs():
    q = deque()
    q.append(a)
    while q:
        x = q.popleft()
        if x == b:
            print(dist[x])
            break
        for j in (x-1,x+1,2*x):
            if 0 <= j <= MAX and  dist[j] ==0:
                dist[j] = dist[x]+1
                q.append(j)
bfs()
        
    