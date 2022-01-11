# 1712 손익분기점
A, B, C = map(int, input().split())


if B >= C :
    print(-1)
else :
    print(int(A/(C-B))+1)

# 2292 벌집삼겹살
n = int(input())
first = 1
plus = 6
room = 1

while n > first:
    room += 1
    first += plus
    plus += 6

print(room)

# 1193 분수찾기
# 몰라서 찾아봄! 

# 1. 입력받은 수가 몇 번째 라인에 있는가?
x = int(input())

y = 0 # 사선 라인
max_num = 0 # 입력된 숫자의 라인에서 가장 큰 숫자

# while문 반복하면서 점점 커지는 max_num이 입력받은 수 보다 커지면 반복문 중단
while x > max_num:
    y += 1
    max_num += y
# 2. 사선 라인이 짝수인지 홀수인지에 따라 분수가 찾는 규칙 달라짐.
gap = max_num - x 
if y % 2 == 0: # 사선 라인이 짝수번째 일 때
    top = y - gap # 분자
    under = gap + 1 # 분모
else :         # 사선 라인이 홀수번째 일 때
    top = gap + 1
    under = y - gap

print(f'{top}/{under}') 

# 2869 달팽이는 올라가고 싶다
# 몰라서 찾아봄!
# 시간 초과 -> 반복문을 돌지 않고 한번에 계산

# 1번 방법
import sys
import math
# 시간초과 걸릴까봐 sys.~ 씀!
a,b,v = map(int, sys.stdin.readline().split())
days = (v-b) / (a-b)

print(math.ceil(days)) # 소수로 나오는 경우, 올림 처리 -> 정수 반환

# 2번 방법
a,b,v=map(int, input().split())
day = (v-b)/(a-b) # 정상에 한번 도달하면 밤에 미끄러지지 않는 것을 고려
print(int(day) if day == int(day) else int(day)+1) # 소수일 경우, 올림

# 10250 ACM 호텔
t = int(input())

# H층, W호실, N번째 손님

for i in range(t):
    h,w,n = map(int,input().split())

    fl = n % h
    ho = n // h + 1
    
    if fl == 0: # 나머지가 0인 경우 
        fl = h ; ho -= 1

    print(fl*100 + ho)

# 2775 부녀회장이 될테야
t = int(input())

for i in range(t):
    floor = int(input()) # 층
    num = int(input()) # 호
    ho = [x for x in range(1,num+1)] # 0층 리스트
    # 거주자 규칙이 없어서 각 층 호수별 거주 인원의 상태를 리스트로 저장하기
     
    for k in range(floor): # 층 수 만큼 반복
        for j in range(1, num): 
            ho[j] += ho[j-1]
        # print(ho) 1층부터 사는 사람 수 리스트 형태로 나옴
    print(ho[-1])

# 2839 설탕 배달
n = int(input())
bag = 0

while n >= 0:
    if n % 5 == 0:  # 5의 배수이면
        bag += (n //5) 
        print(bag)
        break
    n -= 3
    bag += 1
else:
    print(-1)

# 10757 큰 수 A + B
# C는 너무 커서 에러떠도 파이썬은 안뜸!
import sys
A, B = map(int, sys.stdin.readline().split())
print(A+B)

# 1011 Fly me to the Alpha Centauri
# 찾아봄!
# 1번 답
import math 

t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    distance = y-x
    cnt = 0

    num = math.floor(math.sqrt(distance)) 
    # math.floor()는 주어진 숫자와 같거나 작은 정수 중에 가장 큰 수 반환
    # math.sqrt()는 distance ** 1/2
    num_square = num ** 2
    increase_num = math.sqrt(num_square) # 이동횟수가 늘어나는 기점

    if distance > num_square + increase_num :
        cnt = 2 * num + 1
    elif distance > num_square and distance <= num_square + increase_num:
        cnt = 2 * num
    elif distance == num_square:
        cnt = 2 * num - 1

    if distance < 4:
        cnt = distance

    print(cnt)
# 2번 답
t = int(input())

for _ in range(t):
    x, y = map(int,input().split())
    distance = y - x
    count = 0  # 이동 횟수
    move = 1  # count별 이동 가능한 거리
    move_plus = 0  # 이동한 거리의 합

    while move_plus < distance :
        count += 1
        move_plus += move  # count 수에 해당하는 move를 더함
        
        if count % 2 == 0 :  # count가 2의 배수일 때, 
            move += 1  
    
    print(count)
