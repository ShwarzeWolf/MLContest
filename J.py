N = int(input())

data = [[0 for i in range(4)] for j in range(N)]

for i in range(N):
    x, y = input().split()

    data[i][0] = int(x)
    data[i][1] = int(y)

data = sorted(data, key=lambda x: x[0])
for i in range(N):
    data[i][2] = i

data = sorted(data, key=lambda x: x[1])
for i in range(N):
    data[i][3] = i

D = 0.0
for i in range (N):
    D += pow(data[i][2] - data[i][3], 2)

coefficient = 6.0 / (N * (N * N - 1.0))
print(1.0 - coefficient * D)