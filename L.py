K = int(input())
N = int(input())

data = [[] for i in range(K)]
for i in range(N):
    currentX, currentY = input().split()

    x = int(currentX) - 1
    y = int(currentY)

    data[x].append(y)

result = 0.0
for i in data:
    numberOfElements = len(i)

    if (numberOfElements != 0):
        sumOfSquares = 0
        sumOfElements = 0


        for j in i:
            sumOfSquares += pow(j, 2)
            sumOfElements += j

        result += (sumOfSquares * numberOfElements - pow(sumOfElements, 2)) / numberOfElements

print(result / N)
