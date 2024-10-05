import sys
import math

input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
B, C = map(int,input().split())

s = 0

for i in A:
    if i < B:
        s+=1
    else:
        s += 1+ math.ceil((i - B)/C)

print(s)