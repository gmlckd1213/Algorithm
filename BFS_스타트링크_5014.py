import sys
from collections import deque

f,s,g,u,d = map(int,input().split())

def bfs():
    q = deque([s])
    visited = [0]*(f+1)
    visited[s]=1
    while q:
        c = q.popleft()
        if c == g:
            print(visited[g]-1)
            return
        
        up = c+u
        down = c-d
        if up <= f and not visited[up]:
            q.append(up)
            visited[up]=visited[c]+1
            
        if down >0 and not visited[down]:
            q.append(down)
            visited[down]= visited[c]+1
    else:
        print("use the stairs")
        return


bfs()