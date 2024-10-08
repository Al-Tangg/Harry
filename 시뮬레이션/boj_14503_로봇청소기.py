import sys

input = sys.stdin.readline

N, M  = map(int,input().split())
r,c,d = map(int,input().split())

m = [list(map(int,input().split())) for _ in range(N)]

# 북 동 남 서
dy = [-1,0,1,0]
dx = [0,1,0,-1]

clean = 0

while True:

    if m[r][c] == 0:
        m[r][c] = -1
        clean += 1

    if m[r+dy[0]][c+dx[0]] !=0 and m[r+dy[1]][c+dx[1]] !=0 and m[r+dy[2]][c+dx[2]] !=0 and m[r+dy[3]][c+dx[3]] !=0:
        y = r-dy[d]
        x = c-dx[d]

        if 0 < x < M-1 and 0 < y < N-1 and m[y][x] != 1:
            r = y
            c = x
            continue
        else:
            print(clean)
            break

    for _ in range(4):
        d -= 1
        if d == -1:
            d = 3

        y = r + dy[d]
        x = c + dx[d]

        if m[y][x] == 0:
            r = y
            c = x
            break