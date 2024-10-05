import sys

input = sys.stdin.readline

N = int(input())
s = [list(map(int,input().split())) for i in range(N)]
dp = [0 for i in range(N+1)]

for i in range(N-1,-1,-1):
    if i + s[i][0] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1],s[i][1]+dp[i +s[i][0]])
    print(dp)

print(dp[0])