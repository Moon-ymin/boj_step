# 1330 두 수 비교하기

A, B = map(int, input().split())

if A > B :
    print('>')
elif A < B:
    print('<')
else:
    print('==')

# 9498 시험 성적

score = int(input())

if 90 <= score <= 100:
    print('A')
elif 80 <= score <= 89:
    print('B')
elif 70 <= score <= 79:
    print('C')
elif 60 <= score <= 69:
    print('D')
else:
    print('F')

# 2753 윤년

year = int(input())

# 4의 배수, 100의 배수가 아닐 때 
# 또는 400의 배수일때 


if (year % 4 == 0) & (year % 100 != 0):
        print('1')

elif year % 400 == 0:
        print('1')
else:
    print('0') 

# 14681 사분면 고르기

X = int(input())
Y = int(input())

if (X>0) & (Y>0):
    print('1')
elif (X>0) & (Y<0):
    print('4')
elif (X<0) & (Y>0):
    print('2')
else:
    print('3')

# 2884 알람 시계
H, M = map(int, input().split())

if (M-45 >= 0):
    print(H, M-45)
else:
    if (H-1 < 0):
        print(H-1+24, M-45+60)
    else:
        print(H-1, M-45+60)