import math
from sys import stdin
from collections import deque

input = stdin.readline

N,L,R = map(int,input().split())
m = [list(map(int,input().split())) for _ in range(N)]
answer=0
marking = []
unions = []


def bfs(si, sj,index):
    global visited

    if marking[si][sj] != 0:
        return

    Q = deque()  # 큐
    Q.append((si, sj))
    marking[si][sj] = index

    il = [-1, 1, 0, 0]
    jl = [0, 0, -1, 1]

    while Q:
        nodei, nodej = Q.popleft()
        marking[nodei][nodej] = index
        for c in range(4):
            newi = nodei + il[c]
            newj = nodej + jl[c]

            if (0 <= newi <= N - 1) and (0 <= newj <= N - 1):
                gap = abs(m[nodei][nodej] - m[newi][newj])
                if not marking[newi][newj] and L <= gap <= R:
                    marking[newi][newj] = index
                    Q.append((newi, newj))

def move():
    global answer, marking

    while True:
        marking = [[0]*N for _ in range(N)]
        index = 1
        for i in range(N):
            for j in range(N):
                bfs(i, j,index)
                index +=1

        d = dict()
        for i in range(N*N+1):
            d[i+1] = []

        for i in range(N):
            for j in range(N):
                d[marking[i][j]].append([i,j])

        new_d = {k:v for k,v in d.items() if len(v) >=2}

        if new_d :
            for k,v in new_d.items():
                hab = 0
                for i,j in v:
                    hab += m[i][j]
                avg = math.floor(hab/len(v))

                for i,j in v:
                    m[i][j]= avg
            answer +=1
        else:
            return answer

print(move())