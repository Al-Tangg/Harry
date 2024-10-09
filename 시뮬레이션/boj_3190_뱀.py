from collections import deque

N = int(input())  # 보드의 크기
K = int(input())  # 사과의 개수
m = [[0] * N for _ in range(N)]  # 보드 생성
answer = 0  # 시간 계산

# 사과 위치 입력
for _ in range(K):
    i, j = map(int, input().split())
    m[i-1][j-1] = 1

L = int(input())  # 방향 전환 정보 개수
direction_changes = []  # 방향 전환 정보 저장
for _ in range(L):
    sec, D = input().split()
    direction_changes.append((int(sec), D))

# 동 남 서 북 (시계 방향)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def game():
    global answer
    d = 0  # 처음 방향은 동쪽
    snake = deque([(0, 0)])  # 뱀의 초기 위치
    current_time = 0  # 현재 시간
    direction_index = 0  # 현재 방향 전환 인덱스

    while True:
        answer += 1  # 시간 1초 증가
        head_y, head_x = snake[0]  # 뱀 머리 좌표
        ny, nx = head_y + dy[d], head_x + dx[d]  # 새로운 머리 좌표

        # 벽에 부딪히거나 자기 몸과 부딪히면 게임 종료
        if ny < 0 or ny >= N or nx < 0 or nx >= N or (ny, nx) in snake:
            return

        # 뱀 머리를 새로운 위치로 이동
        snake.appendleft((ny, nx))

        # 이동한 위치에 사과가 있으면 사과를 먹음 (꼬리는 그대로)
        if m[ny][nx] == 1:
            m[ny][nx] = 0  # 사과 제거
        else:
            # 사과가 없으면 꼬리를 줄임
            snake.pop()

        # 방향 전환 시간이 되었으면 방향을 바꿈
        if direction_index < L and answer == direction_changes[direction_index][0]:
            if direction_changes[direction_index][1] == 'L':
                d = (d - 1) % 4  # 왼쪽으로 90도 회전
            else:
                d = (d + 1) % 4  # 오른쪽으로 90도 회전
            direction_index += 1  # 다음 방향 전환 인덱스로 이동

# 게임 시작
game()
print(answer)
