from itertools import combinations

N = int(input())
m = [list(map(int, input().split())) for _ in range(N)]

all_people = set(range(N))

min_sum = float('inf')

for start_team in combinations(range(N), N // 2):
    link_team = all_people - set(start_team)

    # 스타트 팀 능력치 계산
    s_sum = 0
    for i in start_team:
        for j in start_team:
            s_sum += m[i][j]

    # 링크 팀 능력치 계산
    l_sum = 0
    for i in link_team:
        for j in link_team:
            l_sum += m[i][j]

    min_sum = min(min_sum, abs(s_sum - l_sum))
print(min_sum)
