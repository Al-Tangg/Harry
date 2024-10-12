from sys import stdin

input = stdin.readline

#
min_chicken_dis = float('inf')

# NxN, 최대 M개
N, M = map(int, input().split())

# 지도
graph = [list(map(int, input().split())) for _ in range(N)]

# 집 리스트, 치킨집 리스트 뽑아내기
houses = []
chickens = []


def cal_distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

def dfs(selected_chicken,index):
    global min_chicken_dis

    if len(selected_chicken) == M:
        dis_sum = 0
        for house in houses:
            hx, hy = house
            min_one_house_dis = float('inf')
            for chicken in selected_chicken:
                cx, cy = chicken
                min_one_house_dis = min(min_one_house_dis,cal_distance(hx, hy, cx, cy))
            dis_sum += min_one_house_dis
        min_chicken_dis = min(min_chicken_dis, dis_sum)
        return

    for i in range(index, len(chickens)):
        selected_chicken.append(chickens[i])
        dfs(selected_chicken, i + 1)
        selected_chicken.pop()


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            houses.append([i, j])
        if graph[i][j] == 2:
            chickens.append([i, j])

dfs([],0)
print(min_chicken_dis)
