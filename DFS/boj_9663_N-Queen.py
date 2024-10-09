from sys import stdin
input = stdin.readline
n = int(input())

cnt = 0

def is_available(candidate, current_col):
    current_row = len(candidate)
    for queen_row in range(current_row):
        # 수직 체크 or 대각선 체크
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            return False
    return True

def DFS(N, current_row, current_candidate):
    global cnt
    if current_row == N:  # 여기에 도달했다는 것은 퀸의 배치가 완료된 것.
        cnt += 1
        return

    for candidate_col in range(N):
        if is_available(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            DFS(N, current_row + 1, current_candidate)
            current_candidate.pop()  # 백트래킹

def solve_n_queens(N):
    DFS(N, 0, [])
    print(cnt)
    return

solve_n_queens(n)
