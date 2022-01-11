# 10952 A+B -5

while True:
    A, B = map(int, input().split())
    
    if (A==0) & (B==0):
        break
    else:
        print(A+B)

# 10951 A+B -4
    
import sys
for line in sys.stdin:
    a, b = map(int,line.split())
    print(a+b)
    
# 1110 더하기 사이클

N = int(input())
fir = N
cycle = 0

while True:
    a = fir // 10
    b = fir % 10
    c = (a+b) % 10
    fir = (b*10) + c

    cycle += 1

    if (fir == N):

        break

print(cycle)