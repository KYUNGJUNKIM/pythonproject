
#1. 24262-알고리즘 수업
# print(1)
# print(0)


#2. 24263-알고리즘 수업2
# n = int(input())
# print(n)
# print(1)


#3. 24264-알고리즘 수업3
# n = int(input())
# print(n*n)
# print(2)


#4. 24265-알고리즘 수업4
# n = int(input())
# result = 0
# for i in range(1, n):
#     result += i
# print(result)
# print(2)


#5. 24266-알고리즘 수업5
# n = int(input())
# print(n**3)
# print(3)


#6. 24267-알고리즘 수업6
# n = int(input())
# tot = 0
# num = n-2
# for i in range(1, n-1):
#     tot += (num * i)
#     num -= 1
#
# print(tot)
# print(3)


#7. 24313-알고리즘 수업: 점근적 표기
x, y = map(int, input().split())
c = int(input())
n = int(input())

if (c-x) * n >= y and c >= x:
    print(1)
else:
    print(0)
