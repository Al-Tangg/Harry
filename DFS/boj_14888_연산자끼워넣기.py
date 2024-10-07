import sys

input = sys.stdin.readline
from collections import deque

N = int(input())
a = list(map(int, input().split()))
c = list(map(int, input().split()))

v_max = -1000000000
v_min = +1000000000

def update_max_min(v):
    global v_max, v_min

    if v_max < v:
        v_max = v

    if v_min > v:
        v_min = v

def dfs(start,c, sum):
    if start == N:
        update_max_min(sum)
        return

    if c[0] > 0:
        c[0] -= 1
        dfs(start+1, c, sum + a[start])
        c[0] += 1

    if c[1] > 0:
        c[1] -= 1
        dfs(start+1, c, sum - a[start])
        c[1] += 1

    if c[2] > 0:
        c[2] -= 1
        dfs(start + 1, c, sum*a[start])
        c[2] += 1

    if c[3] > 0:
        c[3] -= 1
        if(sum < 0 and a[start]>0):
            sum *=-1
            dfs(start + 1, c, -(sum//a[start]))
        else:
            dfs(start + 1, c, sum//a[start])
        c[3] += 1

dfs(1,c,a[0])

print(v_max)
print(v_min)