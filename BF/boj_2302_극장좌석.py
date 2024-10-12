n = int(input())
m = int(input())
seat = [0] * n
f = [0] * (n+1)
f[0] = 1
f[1] = 1
f[2] = 2

for i in range(3,n+1):
    f[i] = f[i-1] + f[i-2]

sum = 1

for i in range(m):
    k = int(input())
    if k !=  0 :
      k -= 1
    seat[k] = -1

cnt =0

for i in range(n):
    if seat[i] == -1:
        sum *= f[cnt]
        cnt = 0
    else:
        cnt += 1

if cnt != 0:
    sum *= f[cnt]

print(sum)