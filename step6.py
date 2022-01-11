# 4673 셀프 넘버
# set 함수 : 중복 제거
# sorted 함수 : 본체 리스트는 내버려두고, 정렬한 새로운 리스트 반환, 오름차순 정렬
# sort 함수 : 본체의 리스트를 정렬해서 변환

nums = set(range(1,10001))
generate_nums = set()

for i in range(1,10001):
    for j in str(i):        # str(i), 1234를 "1","2","3","4"로 받음
        i += int(j)         # 1234 + 1 + 2 + 3 + 4
    generate_nums.add(i)

self_nums = sorted(nums - generate_nums)
for i in self_nums:
    print(i)

# 1065 한수

N = int(input())
han = 0

for i in range(1,N+1):
    if i <= 99: # 1~99는 모두 한수
        han += 1
    else:
        # 숫자를 하나씩 분리하기
        Nums = list(map(int, str(n)))

        if Nums[0] - Nums[1] == Nums[1] - Nums[2]:
            han += 1
