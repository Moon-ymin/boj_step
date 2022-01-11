# 10430 나머지
A, B, C = map(int, input().split())

print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)


# 2588 곱셈

A = int(input())
B = int(input())

C = A * (B%10)
D = A * ((B%100)//10)
E = A * (B//100)

print(C)
print(D)
print(E)
print(C + 10*D + 100*E)

