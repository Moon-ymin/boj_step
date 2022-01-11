# 2739 구구단

N = int(input())

for i in range(1,10):
    print(N,"*",i,"=",N*i)

# 10950 A+B -3

n = int(input())
num = 0

for i in range(1,n+1):
    num = num + i
    
print(num)

# 8393 합

n = int(input())
num = 0

for i in range(1,n+1):
    num = num + i
    
print(num)

# 15552  빠른 A+B

N = int(input())

for i in range(N):
    i += 1
    print(i)

# 2741 N 찍기 

N = int(input())

for i in range(N):
    i += 1
    print(i)

# 2742 기찍 N

T = int(input())

for i in range(T):
    a, b = map(int,input().split())
    c = a+b
    print("Case #%d: %d"%(i+1, c))

# 11021 A+B -7

T = int(input())

for i in range(T):
    a, b = map(int,input().split())
    c = a+b
    print("Case #%d: %d"%(i+1, c))

# 11022 A+B -8

T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    c = a+b
    print("Case #%d: %d + %d = %d"%(i+1, a, b, c))

# 2438 별 찍기 -1

N = int(input())

for i in range(N):
    print("*"*(i+1))

# 2439 별 찍기 -2

N = int(input())

for i in range(N):
    print(" "*(N-i-1)+"*"*(i+1))

# 10871 X보다 작은 수 

N, X = map(int, input().split())

A = list(map(int,input().split()))

for i in range(N):
    if A[i] < X:
        print(A[i], end=" ")