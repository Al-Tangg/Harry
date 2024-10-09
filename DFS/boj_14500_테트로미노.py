import sys

input = sys.stdin.readline

# 상하좌우 이동을 위한 방향 벡터
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

# DFS를 통한 탐색
def dfs(si, sj, depth, total):
    global max_sum
    if depth == 4:  # 길이가 4인 폴리오미노 완성
        max_sum = max(max_sum, total)
        return

    for i in range(4):
        ny = si + dy[i]
        nx = sj + dx[i]
        if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(ny, nx, depth + 1, total + grid[ny][nx])
            visited[ny][nx] = False

# ㅗ, ㅜ, ㅓ, ㅏ 모양을 따로 처리
def check_t_shape(si, sj):
    global max_sum
    # 4방향 모두 탐색해서 ㅗ, ㅜ, ㅓ, ㅏ 모양을 확인
    for i in range(4):
        total = grid[si][sj]
        valid = True
        for j in range(3):  # 'ㅗ' 모양은 3개의 인접 칸을 더해줌
            ni = si + dy[(i + j) % 4]
            nj = sj + dx[(i + j) % 4]
            if 0 <= ni < N and 0 <= nj < M:
                total += grid[ni][nj]
            else:
                valid = False
                break
        if valid:
            max_sum = max(max_sum, total)

# 입력 처리
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]
max_sum = 0

# 모든 좌표에서 탐색을 시작
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, grid[i][j])  # 길이가 1인 경로부터 시작
        visited[i][j] = False
        check_t_shape(i, j)  # ㅗ 모양은 따로 처리

# 결과 출력
print(max_sum)
