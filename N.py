#region input
#input taken from https://pastebin.com/jtqppTiF
#READING PART
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

from math import log

K1, K2 = input().split()

K1 = int(K1)
K2 = int(K2)

N = int(input())

x = [0 for i in range(K1)]
y = [0 for i in range(K2)]

data = [{} for i in range(K1)]

for i in range(N):
    currentXValue, currentYValue = input().split()

    currentXValue = int(currentXValue) - 1
    currentYValue = int(currentYValue) - 1

    x[currentXValue] += 1
    y[currentYValue] += 1

    if data[currentXValue].get(currentYValue) == None:
        data[currentXValue][currentYValue] = 1
    else:
        data[currentXValue][currentYValue] += 1

result = 0.0

for i in range(K1):
    currentResult = 0.0

    for j in data[i].values():
        currentResult += log(j / x[i]) * j / x[i]

    result -= currentResult * x[i] / N

print(result)
