# 11654 아스키 코드
# ord : 입력받은 값을 아스키 코드 값으로 반환
# chr : 입력받은 아스키 코드를 값으로 반환
a = input()
print(ord(a))

# 11720 숫자의 합
N = int(input())
nums = input()
sum = 0

for i in range(N):
    sum += int(nums[i])

print(sum)

# 10809 알파벳 찾기
# 1번 방법
s = input()
abc = 'abcdefghijklmnopqrstuvwxyz'

for i in abc:
    if i in s:
        print(s.index(i), end=' ') # s에서의 위치를 반환
    else:
        print(-1, end = ' ')
# 2번 방법 : 아스키 코드 이용
S = input()
check = [-1]*26 # check는 리스트
 
for i in range(len(S)):
    if check[ord(S[i])-97] != -1: # 소문자 a의 아스키 코드 값 = 97
        continue
    else:
        check[ord(S[i])-97] = i
        
for i in range(26):
    print(check[i], end=' ')

# 2675 문자열 반복
T = int(input())

for i in range(T):
    R, S = input().split()
    text = ''

    for i in S:
        text = text + int(R) * i

    print(text)

# 1157 단어 공부
# 문자열 대문자로 변경하는거 ~ string.upper()

word = input().upper()
words = list(set(word)) # 입력받은 문자열에서 중복값을 제거
cnt_list = []

for i in words:
    cnt = word.count(i)
    cnt_list.append(cnt) # cnt 숫자를 cnt_list에 추가

if cnt_list.count(max(cnt_list))>1:
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))
    print(words[max_index])

# 1152 단어의 개수 
sentence = input().split()
print(len(sentence))

# 2908 상수 
A, B = input().split()

A1 = int(A[::-1])
B1 = int(B[::-1])

if A1 > B1 :
    print(A1)
else:
    print(B1)

# 5622 다이얼
word = input()
dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
cnt = 0

for i in range(len(word)):
    for j in dial:
        if word[i] in j :
            cnt = cnt + dial.index(j) + 3

print(cnt)

# 2941 크로아티아 알파벳
cro_alpha = [ 'c=', 'c-','dz=','d-','lj','nj','s=','z=']
word = input()

for i in cro_alpha:
    word = word.replace(i, '*') 
    # word안에 cro_alpha와 같은 글자 있으면 한글자 *로 바꿈

print(len(word))

# 1316 그룹 단어 체커
N = int(input())
total = 0

for i in range(N):
    word = input()
    for j in range(len(word)-1):
        if word[i] != word[i+1]:
            if word[i] in word[i+1:]:
                N -= 1
                break

print(N)