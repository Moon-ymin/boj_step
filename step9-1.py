# 2581 소수
M = int(input())
N = int(input())
primes = []

for i in range(M, N+1):        # 입력값 사이만 범위로 설정하여 진행
    cnt = 0
    for j in range(1, i+1):    # 1부터 i항까지 진행 
        if i % j == 0:
            cnt += 1           # 기준 숫자가 다른 숫자로 나뉘면 cnt 증가
            if cnt > 2:        # cnt가 2보다 크면 소수가 아님. 
                break          # 소수는 1과 자기자신으로만 나뉨!
    if cnt == 2:               # cnt가 2일 때
        primes.append(i)       # 기준 숫자를 리스트에 추가
        
if len(primes) != 0:           
    print(sum(primes))         # 소수들의 합 
    print(primes[0])           # 최소 소수 출력
else:
    print('-1')                # 소수가 하나도 없으면 -1 출력

# 11653 소인수분해 
N = int(input())
m = 2

while N != 1: # N과 m을 나눴을 때 몫이 1이되면 멈춤
    if N % m == 0:
        print(m)
        N = N//m # / : 나누기 몫 // : 나누기 몫, 정수부분만 출력
    else:
        m += 1      

# 1929 소수 구하기
# 에라토스테네스의 체를 이용한 소수 구하기
M, N = map(int,input().split())

def prime_list(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
for i in range(M, N+1):
    if prime_list(i):
        print(i)

# 4948 베르트랑 공준
def prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5)+1):  # 제곱근이 있는 수 중에
        if n % i == 0:         
            return False                 # 약수가 있으면 False
    return True                          # 이외에는 소수

all_list = list(range(2,246912))
prime_list = []

for i in all_list:
    if primes(i):
        prime_list.append(i)

while True:
    n = int(input())
    cnt = 0

    if n == 0:
        break
    for i in prime_list:
        if n < i <= n*2:
            cnt += 1
    print(cnt)

# 9020 골드바흐의 추측
sosu = [0 for i in range(10001)]
sosu[1] = 1

for i in range(2,98):
    for j in range(i*2, 10001, i):
        sosu[j] = 1
t = int(input())
for i in range(t):
    a = int(input())
    b = a // 2
    for j in range(b,1,-1):
        if sosu[a-j] == 0 and sosu[j] == 0:
            print(j, a-j)
            break

# 1085 직사각형에서 탈출
x,y,w,h = map(int,input().split())
li = [x, w-x,y,h-y]

print(min(li))

# 3009 네 번째 점
a, A = map(int,input().split())
b, B = map(int,input().split())
c, C = map(int,input().split())
d = 0 
D = 0

if a == b:
    d = c
elif a == c:
    d = b
else:
    d = a
    
if A == B:
    D = C
elif A == C:
    D = B
else:
    D = A
    
print(d, D)

# 4153 직각삼각형
while True:
    # 리스트 형태로 입력받기
    length = list(map(int, input().split()))
    max_length = max(length)
    
    if sum(length) == 0:
        break
    length.remove(max_length) # 가장 큰 값을 리스트에서 빼기
    
    if length[0] ** 2 + length[1] ** 2 == max_length ** 2:
        print("right")
    else:
        print("wrong")

# 3053 택시 기하학
import math # pi함수 쓰려고~

r = int(input())
print(r*r*math.pi) # 원의 넓이
print(2*r*r) # 택시 기하학 원의 넓이 

# 소수점 6자리를 지정하기
# print(f'{r*r*math.pi:.6f}')

# 1002 터렛
t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    r = ((x1-x2) ** 2 + (y1-y2) ** 2) ** (1/2)
    R = [r1,r2,r]
    
    m = max(R)
    R.remove(m)
    print(-1 if (r == 0 and r1 == r2) else 1 if (r == r1+r2 or m == sum(R)) else 0 if (m>sum(R)) else 2)