import sys
from collections import deque
import copy
from collections import defaultdict

input = sys.stdin.readline

# K 횟수, M 유물 조각 개수
K,M = map(int,input().split())

# 실제 유물 그래프
graph = [list(map(int,input().split())) for _ in range(5)]

# 3 3 격자 중심이 모여 있는 그래프
rotate_graph = [[]*3 for _ in range(3)]

# 유물조각 디큐 앞에서 빼서 뒤로 넣을꺼임
plates = deque(map(int,input().split()))

mi = [-1,-1,-1,0,1,1,1,0]
mj = [-1,0,1,1,1,0,-1,-1]

def print_graph(g):
    for i in g:
        print(i)
    print()

def bfs(graph_copy):

    visited = [[False] * 5 for _ in range(5)]
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    total_v =[]

    for i in range(5):
        for j in range(5):
            if visited[i][j]:
                continue

            Q = deque()
            Q.append([i,j])
            visited[i][j] = True
            v = [[i,j]]
            while Q:
                ci,cj = Q.pop()
                num = graph_copy[ci][cj]
                for a in range(4):
                    ni = dx[a] + ci
                    nj = dy[a] + cj

                    if ni < 0 or ni > 4 or nj < 0 or nj >4:
                        continue

                    if not visited[ni][nj] and num == graph_copy[ni][nj]:
                        v.append([ni,nj])
                        visited[ni][nj] = True
                        Q.append([ni,nj])

            if len(v) >= 3:
                total_v += v

    return sorted(total_v, key=lambda x:(x[1],-x[0]))

def select_3by3():
    global graph

    # 중앙기준 0,0 ~ 2,2까지 돌려보기
    max_change = []

    for j in range(3):
        for i in range(3):
            si = i +1
            sj = j +1

            nums = deque()
            for q in range(8):
                ni = mi[q] + si
                nj = mj[q] + sj
                nums.append(graph[ni][nj])

            # i =0 90 i=1 180 i=2 279
            for aaa in range(1,4):
                graph_copy = copy.deepcopy(graph)
                nums.appendleft(nums.pop())
                nums.appendleft(nums.pop())

                # 90~270 그래프 세팅완료
                for aaaa in range(8):
                    ni = mi[aaaa] + si
                    nj = mj[aaaa] + sj
                    graph_copy[ni][nj] = nums[aaaa]

                chage = bfs(graph_copy)
                if len(max_change) < len(chage):
                    max_change = chage
                    remember_map = copy.deepcopy(graph_copy)

    graph = copy.deepcopy(remember_map)
    return max_change

def game():
    for _ in range(K):
        answer = 0
        change_list = select_3by3()
        answer += len(change_list)

        print(change_list)

        # 1차 변경
        for i,j in change_list:
            num = plates.popleft()
            graph[i][j] = num
            plates.append(num)

        change_list = bfs(graph)

        print_graph(graph)

        # 연쇄 변경
        while change_list :
            print(change_list)
            answer += len(change_list)

            for i, j in change_list:
                num = plates.popleft()
                graph[i][j] = num
                plates.append(num)

            print_graph(graph)

            change_list = bfs(graph)

        print(answer,end=" ")
game()