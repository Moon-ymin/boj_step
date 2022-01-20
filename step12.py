# 2750 수 정렬하기 
n = int(input())
nums = []

for i in range(n):
    number = int(input())
    nums.append(number)
    
nums = sorted(nums, reverse=False) # 정렬함수 sorted, reverse = False는 오름차순

for i in range(n):
    print(nums[i])

# 2751 수 정렬하기 2
# 파이썬 기본 정렬 함수가 O(nlog(n))으로 잘 구성되어있어서 굳이 더 좋은 정렬사용 필요없음
# input()과 print()함수 대신 -> system input()과 system output을 사용

import sys # 파이썬의 표준 입출력은 sys 모듈 사용
n = int(input()) 
nums = []

for i in range(n):
    nums.append(int(sys.stdin.readline())) #sys.stdin : 입력 버퍼, 키보드 입력
for i in sorted(nums):
    sys.stdout.write(str(i)+'\n') # sys.stdout : 출력 버퍼, 표준 출력

# 10989 수 정렬하기 3
# 수의 범위가 작다면 카운팅 정렬을 사용
# for문에서 append하게되면 메모리 재할당이 이루어지면서 메모리를 효율적으로 사용 못함

import sys
n = int(input())
nums = [0] * 10001 # 리스트에 각 요소마다 0을 할당해놓고

for i in range(n):
    nums[int(sys.stdin.readline())] += 1 
    # 입력값을 받을 때마다 입력값과 같은 인덱스에 +1씩 해준다.
    
for i in range(10001): 
# 입력 끝나면 0보다 큰 요소를 갖는 인덱스들을 찾아서 그 수만큼 인덱스를 출력해준다.
    if nums[i] != 0:
        for j in range(nums[i]):
            print(i)

# 2108 통계학
import sys
from collections import Counter
n = int(sys.stdin.readline())
nums = []

for i in range(n):
    nums.append(int(sys.stdin.readline()))

nums.sort() # 오름차순 정렬
nums_s = Counter(nums).most_common() # 숫자별로 개수까지 세기

print(round(sum(nums) / n)) # 산술평균, 소수점 아래 첫째자리에서 반올림
print(nums[n // 2])         # 중앙값

if len(nums_s) > 1:         # 최빈값
    if nums_s[0][1] == nums_s[1][1]: # 최빈값 여러 개일때, 두 번째로 작은 값 출력
        print(nums_s[1][0])
    else:                   # 최빈값 하나일 때
        print(nums_s[0][0])
else:
    print(nums_s[0][0])

print(nums[-1] - nums[0])   # 범위

# 개수 체크에 Counter 라이브러리 사용
from collections import Counter

colors = Counter(['blue', 'green', 'red', 'blue','red','blue'])

print(colors)
# Counter({'blue': 3, 'red': 2, 'green': 1})

print(colors.most_common())
# [('red', 3), ('blue', 2), ('green', 1)]

print(colors.most_common(2))
# 가장 많은 것 부터 2개 출력
# [('red', 3), ('blue', 2)]

# 1427 소트인사이드
import sys

n = int(sys.stdin.readline())
nums = []

for i in str(n):          # 입력받은 숫자 한 자리씩 따로 리스트에 담기
    nums.append(int(i))

nums.sort(reverse = True) # reverse = True는 내림차순

for i in nums:
    print(i, end='')      # 정렬된 리스트 한 개씩 출력, end=''로 한줄에 출력

# 11650 좌표 정렬하기
import sys

n = int(sys.stdin.readline())
points = []

for i in range(n):
    points.append(list(map(int,sys.stdin.readline().split())))
    
points.sort(key = lambda x : (x[0],x[1]))

for i in points:
    print(i[0], i[1])

# sort()에서 key lambda 사용하기
# lambda 매개변수 : 표현식 
# sort(key = lambda x : (x[0], x[1]))
# sorted(points, key = lambda x : (x[0], x[1]))

# 11651 좌표 정렬하기2
import sys
n = int(sys.stdin.readline())
points = []

for i in range(n):
    points.append(list(map(int,sys.stdin.readline().split())))
points.sort(key = lambda x : (x[1], x[0]))

for i in points:
    print(i[0], i[1])

# 1181 단어 정렬
import sys

n = int(sys.stdin.readline())
words = []

for i in range(n):
    # words.append(sys.stdin.readline()) \n\포함되어있어 오류
    words.append(sys.stdin.readline().strip()) #.strip()
set_words = set(words) ## 중복된 단어 없애기
words = list(set_words)

# 정렬 순서
## 상위 조건 A, 하위 조건 B : B로 정렬하고 -> A로 정렬하기 
## sort()는 문자열에서도 통한다!
words.sort() ## 괄호 안에 아무 값도 넣지 않으면 알파벳 순서로 정렬해줌.
words.sort(key = len) ## 문자열 길이 순으로 정렬

for i in words:
    print(i)

# 10814 나이순 정렬
import sys
n = int(sys.stdin.readline())
members = []

for i in range(n):
    # 데이터 타입 다른 변수 한 번에 받기
    age, name = map(str, sys.stdin.readline().split())
    age = int(age)
    members.append((age, name))

# stable 정렬
# 1. 나이 순 2. 가입 순
members.sort(key = lambda x : x[0]) 

for i in members:
    print(i[0], i[1])

# 18870 좌표 압축
# 해당 값이 전체 집합에서 몇 번째로 낮은 숫자인지 반환하는 문제
n = int(input())
nums = list(map(int,input().split()))
# 순위를 내려면 정렬로 중복 없애고 순서대로~
nums_set = list(sorted(set(nums)))

# 정렬된 리스트에서 각 요소가 리스트의 몇 번째 요소인지 
# 태그를 다는 작업을 딕셔너리로 해서
nums_set = {nums_set[i] : i for i in range(len(nums_set))}

# nums = [2, 4, -10, 4, -9]
# nums_set = {-10: 0, -9: 1, 2: 2, 4: 3}

# 입력받은 좌표를 변환시켜 출력하면 됨!
# 딕셔너리 형태 : nums_set[key] = value
print(*[nums_set[i] for i in nums])
