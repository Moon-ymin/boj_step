# 2798 블랙잭
n, m = map(int,input().split())
cards = list(map(int,input().split()))
result = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if cards[i] + cards[j] +cards[k] > m:
                continue
            else:
                result = max(result, cards[i]+cards[j]+cards[k])
print(result)

# 다른풀이
# itertools의 combinations함수 = 하나의 리스트에서 모든 조합을 계산
from itertools import combinations

n,m = map(int,input().split())
cards = list(map(int,input().split()))
max_total = 0

for card in combinations(cards, 3):
    max_sum = sum(card)
    if max_total < max_sum <= m:
        max_total = max_sum

print(max_total)

# 2231 분해합
n = int(input()) # 입력값 입력
result = 0 # 입력값 n과 비교하기 위한 변수

for i in range(1,n+1):
    a = list(map(int,str(i))) # str한수를 통해 i의 각 자리수를 a리스트에 넣기
    result = i + sum(a)       # 값 자체 + 각 자리수
    if result == n: # 입력값 n과 비교
        print(i) 
        break
        
    if i == n:
        print(0)

# 7568 덩치
n = int(input())
body = []

# 리스트 안에 두 개 항목씩 넣기
for i in range(n):
    weight, height = map(int,input().split())
    body.append((weight, height)) # body 리스트에 ()로 키, 몸무게 넣기
    
for j in body:
    rank = 1
    for k in body:
        if j[0] < k[0] and j[1] < k[1]:
            rank += 1 # 기준보다 키, 몸무게 둘 다 큰 경우, 덩치 등수 + 1
    print(rank, end=" ")

# 1018 체스판 다시 칠하기
n,m = map(int,input().split())
li =[]
total = []

for _ in range(n):
    li.append(input())

for a in range(n-7): 
    for b in range(m-7): # 전체 체스판에서 시작점을 잡기 위한 반복문
        starts_w = 0 # W로 시작할 경우
        starts_b = 0 # B로 시작할 경우
        
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0: # 행, 열의 번호 합이 짝수, 시작점의 색과 같음
                    if li[i][j] != "W":
                        starts_w += 1
                    if li[i][j] != "B":
                        starts_b += 1
                else:
                    if li[i][j] != "B":
                        starts_w += 1
                    if li[i][j] != "W":
                        starts_b += 1
                        
        total.append(min(starts_w, starts_b))
print(min(total))

# 1436 영화감독 숌

# 1~10000까지의 숫자 안에서 작은 수부터 큰 수가 될 때까지 '666'이 연속으로 들어가는
# 숫자에 번호를 매긴 뒤 그 번호는 n번째 영화 제목에 붙는 것이다.

# 1~10000까지의 숫자 중에서 '666'이 들어간 숫자를 찾고 그 숫자가 몇 번째 숫자인지 반환
# '666'과 카운트를 문자열로 바꾸고 자리에 상관없이 포함되어 있으면 번호 매김

n = int(input())
nth = 666
count = 0

while True:
    if '666' in str(nth): #1 n번째 수에 '666'이 포함되어있다면
        count += 1        #2 카운트를 올림
    if count == n:        #4 카운트랑 n번째 수가 같다면
        print(nth)        #5 nth를 출력
        break             #6 while문 종료
    nth += 1              #3 666이 포함된 수가 나올 때 까지 nth를 1씩 증가시킴