import math
from sys import stdin
from collections import deque
import copy

def m_print(m):

    for i in range(R):
        for j in range(C):
            print(m[i][j],'',end='')
        print()

input = stdin.readline

R, C, T = map(int,input().split())

m = [list(map(int,input().split())) for _ in range(R)]

dusts = []
air = []

for i in range(R):
    for j in range(C):
        if m[i][j]>0:
            dusts.append([i,j,m[i][j]])
        if m[i][j]==-1:
            air.append(i)

di = [0,0,1,-1]
dj = [1,-1,0,0]

for i in range(T):

    for dust in dusts:
        dusti, dustj, dustv = dust
        cnt = 0
        for k in range(4):
            ni = dusti+di[k]
            nj = dustj+dj[k]

            if ni <0 or ni > R-1 or nj < 0 or nj > C-1 or m[ni][nj] == -1:
                continue

            m[ni][nj] += math.floor(dustv/5)
            cnt+=1

        m[dusti][dustj] -= (math.floor(dustv/5)*cnt)


    tQ = deque()
    tQ.append(0)

    tdj = [1,0,-1,0]
    tdi = [0,-1,0,1]
    td = 0

    tairi = air[0]
    curi,curj = tairi,1
    while tairi != curi or curj != 0:
        tQ.append(m[curi][curj])
        m[curi][curj] = tQ.popleft()

        curi = curi + tdi[td]
        curj = curj + tdj[td]

        if curj == C-1 and td ==0:
            td+=1
        elif curi == 0 and td == 1:
            td+=1
        elif curj == 0 and td == 2:
            td+=1

    bairi = air[1]
    curi, curj = bairi,1
    bdj = [1, 0, -1, 0]
    bdi = [0, 1, 0, -1]
    bd = 0

    bQ = deque()
    bQ.append(0)



    while bairi != curi or curj != 0:
        bQ.append(m[curi][curj])
        m[curi][curj] = bQ.popleft()

        curi = curi + bdi[bd]
        curj = curj + bdj[bd]

        if curj == C - 1 and bd == 0:
            bd += 1
        elif curi == R - 1 and bd == 1:
            bd += 1
        elif curj == 0 and bd == 2:
            bd += 1

    dusts = []

    for i in range(R):
        for j in range(C):
            if m[i][j] > 0:
                dusts.append([i, j, m[i][j]])

answer = 0
for dust in dusts:
    answer += dust[2]

print(answer)