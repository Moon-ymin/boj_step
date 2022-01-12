# 재귀함수 
# 함수 정의 내에 같은 이름의 함수가 올 때 이를 재귀함수
# 같은 행위가 반복될 때 재귀함수를 사용
# 반드시 탈출조건이 있어야 stack overflow를 방지할 수 있다.

# 10872 팩토리얼
n = int(input())

def factorial(n):
    facto = 1
    if n > 0:
        facto = n * factorial(n-1)
    return facto
    
print(factorial(n))

# 10870 피보나치 수 5
def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

n = int(input())
print(fibo(n))

# 2447 별 찍기 - 10
# 별 만들 함수
def get_stars(n):
    # 별 담을 리스트
    Temp = []
    for i in range(3*len(n)):
    # n(즉 len(stars))이 3으로 나누어 떨어지지 않는다면(1이 남는다면) 가운데 공백 줌(n의 길이만큼)
        if i // len(n) == 1:
            Temp.append(n[i % len(n)] + " " * len(n) + n[i%len(n)])
        
        # n이 3으로 나누어 떨어진다면, 공백 없이 가득 채움
        else:
            Temp.append(n[i % len(n)] * 3)
    return Temp

stars = ["***","* *","***"]
n = int(input())
k = 0

# 만약 n이 3이 될 때까지 n은 3으로 나눠준 값을 다시 n값으로 지정하고 k는 1씩 추가
while n != 3:
    n = int(n/3)
    # k는 함수를 몇번 실행할지 정하는 변수
    k += 1

for i in range(k):
    stars = get_stars(stars)
for i in stars:
    print(i)

# 11729 하노이 탑 이동 순서
n = int(input())
def hanoi(n,a,b,c): # a,b,c : 1,2,3 번 째 장대
    if n == 1:
        print(a,c)
    else:
        hanoi(n-1,a,c,b) # 1단계 : n-1개의 원판을 2번 장대로 옮김
        print(a,c)       # 2단계 : 남은 1개의 원판을 1-3으로 옮김
        hanoi(n-1,b,a,c) # 3단계 : 다시 n-1개의 원판을 2-3장대로 옮김
sum = 1
for i in range(n-1):
    sum = sum * 2 + 1
print(sum)
hanoi(n,1,2,3)