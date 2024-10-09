import sys
from collections import deque
import copy
def bfs():
    global max_safe

    d = deque()
    m_temp = copy.deepcopy(m)

    for i in range(N):
        for j in range(M):
            if m_temp[i][j]==2:
                d.append([i,j])

    while d:
        i, j  = d.popleft()

        for k in range(4):
            y = i+dy[k]
            x = j+dx[k]
            if 0<= x <M and 0<= y <N and not m_temp[y][x]:
                m_temp[y][x] = 2
                d.append([y,x])

    safe_cnt = 0

    for i in range(N):
        safe_cnt += m_temp[i].count(0)

    max_safe = max(max_safe,safe_cnt)

def wall(cnt):

    if cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if m[i][j] == 0:
                m[i][j] = 1
                wall(cnt+1)
                m[i][j] = 0


input = sys.stdin.readline

N, M = map(int,input().split())

m = [list(map(int,input().split())) for _ in range(N)]

dy = [-1,0,1,0]
dx = [0,1,0,-1]

max_safe = -float('inf')

wall(0)
print(max_safe)