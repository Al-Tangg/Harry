import copy
import sys
from collections import deque

input = sys.stdin.readline

# N 세로, M 가로
N, M = map(int,input().split())

# 맵 받기
graph = [list(map(int,input().split())) for _ in range(N)]

# 연구소 리스트, 벽을 세울 수 있는 곳 리스트 만들기
empty = []
virus = []

# 최대 안전영역
max_cnt = -float('inf')

for i in range(N):
    for j in range(M):
        if graph[i][j]==0:
            empty.append([i,j])
        if graph[i][j]==2:
            virus.append([i,j])

def virus_move(graph_copy):

    visited = [[False]*M for _ in range(N)]

    di = [0,0,1,-1]
    dj = [-1,1,0,0]

    for v in virus:
        vi,vj = v
        Q = deque()
        Q.append([vi,vj])
        visited[vi][vj] = True

        while Q:
            si,sj = Q.popleft()
            for i in range(4):
                ni = si + di[i]
                nj = sj + dj[i]

                if ni <0 or ni > N-1 or nj <0 or nj > M-1:
                    continue

                if not visited[ni][nj] and not graph_copy[ni][nj]:
                    visited[ni][nj] = True
                    graph_copy[ni][nj] = 2
                    Q.append([ni,nj])

    return graph_copy

def count_safe(new_graph):
    global max_cnt
    cnt = 0
    for g in new_graph:
        cnt += g.count(0)
    max_cnt = max(cnt,max_cnt)

def stall_wall(selected_walls,index):

    if len(selected_walls) == 3:
        graph_copy = copy.deepcopy(graph)

        for wall in selected_walls:
            wi, wj = wall
            graph_copy[wi][wj] = 1

        new_graph = virus_move(graph_copy)
        count_safe(new_graph)
        return

    for idx in range(index,len(empty)):
        selected_walls.append(empty[idx])
        stall_wall(selected_walls,idx+1)
        selected_walls.pop()

def game():
    stall_wall([],0)

game()

print(max_cnt)