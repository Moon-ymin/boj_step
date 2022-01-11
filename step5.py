# 10818 최소, 최대

N = int(input())
nums = []

for i in range(N):
    nums = list(map(int, input().split()))
    break

print(min(nums), max(nums))

# 2562 최댓값

nums = []

for i in range(9):
    # 값 입력받고 리스트 내부에 추가하기
    a = int(input())
    nums.append(a)

max_nums = max(nums)

print(max_nums)
# 리스트 내부의 값의 인덱스 출력 리스트.index(값)
print(nums.index(max_nums)+1) 

# 2577 숫자의 개수

A = int(input())
B = int(input())
C = int(input())

final = A*B*C
nums = []

for i in str(final):
    nums.append(i)
    
for i in range(10):
    print(nums.count(str(i)))

# 3052 나머지

nums = []

for i in range(10):
    a = int(input())
    nums.append(a % 42)

nums = set(nums)
print(len(nums))

# 1546 평균

N = int(input())
score = list(map(int,input().split()))
max_score = max(score)

for i in range(N):    
    score[i] = score[i] / max_score * 100
    
total = sum(score)
avg = total/len(score)
print("%.2f"%avg)


# 8958 OX 퀴즈

T = int(input())

for i in range(T):
    result = input()
    score = 0
    sumscore = 0
    
    for j in result:
        if j == 'O':
            score += 1
        else:
            score = 0
            
        sumscore += score
    print(sumscore)
    
# 4344 평균은 넘겠지

C = int(input())


for i in range(C):
    students = list(map(int, input().split()))
    score = 0
    over_students = 0

    for j in range(1,len(students)):
        score = score + students[j]
        avg = score/students[i]
        
    for k in range(1,len(students)):
        if students[k] > avg:
            over_students += 1

        ratio = over_students /students[0] * 100
    print("%.3f"%ratio,"%")
