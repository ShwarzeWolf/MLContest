# READING PART
#input taken from https://pastebin.com/jtqppTiF
#region input
from io import BytesIO, IOBase
import os
import sys

BUFSIZE = 8192

class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


if sys.version_info[0] < 3:
    sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
else:
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)

input = lambda: sys.stdin.readline().rstrip("\r\n")
#endregion

K = int(input())
N = int(input())

xValues = []
yValues = [[] for i in range(K)]

for i in range(N):
    x, y = input().split()

    x = int(x)
    y = int(y) - 1

    xValues.append(x)
    yValues[y].append(x)

innerDistance = 0

for i in range(K):
    currentSum = 0
    yValues[i] = sorted(yValues[i])

    for j in range(len(yValues[i])):
        currentSum += yValues[i][j] * (2 * j - len(yValues[i]) + 1)

    innerDistance += currentSum

outerDistance = 0
xValues = sorted(xValues)

for j in range(len(xValues)):
    outerDistance += xValues[j] * (2 * j - len(xValues) + 1)

innerDistance *= 2
outerDistance = outerDistance * 2 - innerDistance

print(innerDistance)
print(outerDistance)
