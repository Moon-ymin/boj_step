# 한 개의 소수 구하기
n = 100

def isPrime(a):
    if(a<2):
        return False
    for i in range(2,a):
        if(a%i == 0):
            return False
    return True
for i in range(n+1):
    if(isPrime(i)):
        print(i)

# 에라토스테네스의 체 : 범위의 모든 소수 구하기
# 지워지지 않는 소수 제일작은 n을 택하고, n의 배수 다 지우기 -> n+1로 넘어감
# 1번 코드
def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우 
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]
# 2번 코드
n=1000
a = [False,False] + [True]*(n-1) # n개 요소에 True로 설정(소수로 간주)
primes=[]

for i in range(2,n+1):
  if a[i]:                       # i가 소수인 경우
    primes.append(i)
    for j in range(2*i, n+1, i): # i이후 i의 배수들을 False로 판정
        a[j] = False
print(primes)

# 1978 소수 찾기
n = int(input())
numbers = map(int, input().split())
sosu = 0

for num in numbers:
    error = 0
    if num > 1 :
        for i in range(2, num):  # 2부터 n-1까지
            if num % i == 0:
                error += 1  # 2부터 n-1까지 나눈 몫이 0이면 error가 증가
        if error == 0:
            sosu += 1  # error가 없으면 소수.
print(sosu)

