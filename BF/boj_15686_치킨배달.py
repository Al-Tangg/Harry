import sys
from itertools import combinations

def cal_dis(r1,c1,r2,c2):
    return (abs(r1-r2) + abs(c1-c2))

input = sys.stdin.readline

N, M = map(int,input().split())
m = [list(map(int,input().split())) for _ in range(N)]
m_c = m + []

ch = set()

min_dis = float('inf')

h_list = []
c_list = []

for i in range(N):
    for j in range(N):
        if m[i][j]==1:
            h_list.append([i,j])
        if m[i][j]==2:
            c_list.append([i,j])

dis_list = [[0]*len(c_list) for _ in range(len(h_list))]

for i in range(len(h_list)):
    for j in range(len(c_list)):
        dis_list[i][j] = cal_dis(h_list[i][0],h_list[i][1],c_list[j][0],c_list[j][1])

for chicks in combinations(range(len(c_list)),M):
    total_dis = 0

    for i in range(len(h_list)):
        mmin_dis = float('inf')
        for chick in chicks:
            mmin_dis = min(dis_list[i][chick],mmin_dis)
        total_dis += mmin_dis

    min_dis = min(min_dis,total_dis)

print(min_dis)



