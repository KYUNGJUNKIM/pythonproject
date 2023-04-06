#1.
# def fib(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     return fib(n-1) + fib(n-2)
#
#
# def fibonacci(n):
#     dp = [0] * (n+1)
#     dp[1], dp[2] = 1, 1
#     cnt = 0
#     for i in range(3, n+1):
#         cnt += 1
#         dp[i] = dp[i-1] + dp[i-2]
#     return cnt
#
#
# n = int(input())
# print(fib(n), fibonacci(n))

#2.
# import sys
# input = sys.stdin.readline
#
#
# def w(a, b, c):
#     if a <= 0 or b <= 0 or c <= 0:
#         return 1
#     if a > 20 or b > 20 or c > 20:
#         return w(20, 20, 20)
#     if dp[a][b][c]:
#         return dp[a][b][c]
#     if a < b < c:
#         dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
#         return dp[a][b][c]
#     dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
#     return dp[a][b][c]
#
#
# dp = [[[0]*21 for _ in range(21)] for _ in range(21)]
# while True:
#     a, b, c = map(int, input().split())
#     if a == -1 and b == -1 and c == -1:
#         break
#     print(f'w({a}, {b}, {c}) = {w(a, b, c)}')

#3.
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# dp = [0] * 1000001
# dp[1], dp[2] = 1, 2
#
# for i in range(3, n+1):
#     dp[i] = (dp[i-2] + dp[i-1]) % 15746
# print(dp[n])

#4.
# import sys
# input = sys.stdin.readline
#
# dp = [0] * 101
# dp[1], dp[2], dp[3] = 1, 1, 1
# for i in range(4, 101):
#     dp[i] = (dp[i - 2] + dp[i - 3])
#
# t = int(input())
# for j in range(t):
#     n = int(input())
#     print(dp[n])


#5.
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# nums = list(map(int, input().split()))
#
# dp = [0] * n
# dp[0] = nums[0]
# for i in range(1, n):
#     dp[i] = max(nums[i], dp[i-1]+nums[i])
# print(max(dp))


#6.
# import sys
#
# n = int(sys.stdin.readline())
# rgb = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
#
# # 반복문을 통해 각 집의 색을 칠할 수 있는 최소 비용에 경우의 수를 구한다.
# for i in range(n-1):
#     rgb[i+1][0] = min(rgb[i][1], rgb[i][2]) + rgb[i+1][0]
#     rgb[i+1][1] = min(rgb[i][0], rgb[i][2]) + rgb[i+1][1]
#     rgb[i+1][2] = min(rgb[i][0], rgb[i][1]) + rgb[i+1][2]
#
# # 마지막 집까지 색칠한 후 비용의 최솟값을 출력
# print(min(rgb[n-1]))

#-------------- 틀린코드
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# cost = [list(map(int, input().split())) for i in range(n)]
#
# dp = [0] * n
# idx = [4]
# for i in range(n):
#     minimum = 1001
#     for j in range(3):
#         if j != idx[-1]:
#             if cost[i][j] < minimum:
#                 minimum = cost[i][j]
#                 idx.append(j)
#     dp[i] = minimum
# print(sum(dp))


#7.
# import sys
# read = sys.stdin.readline
#
# n = int(read())
# graph = [list(map(int, read().split())) for i in range(n)]
#
# for i in range(1, n):
#     for j in range(i+1):
#         if j == 0:
#             graph[i][j] += graph[i-1][0]
#         elif j == i:
#             graph[i][j] += graph[i-1][-1]
#         else:
#             graph[i][j] += max(graph[i-1][j-1], graph[i-1][j])
# print(max(graph[-1]))

#----------------------풀이2
# import sys
# read = sys.stdin.readline
#
# n = int(read())
# cache = []
#
# for i in range(n):
#     floor = list(map(int, read().split()))
#     cache = [max(a+c, b+c) for a, b, c in zip([0]+cache, cache+[0], floor)]
# print(max(cache))


#8.
# import sys
# read = sys.stdin.readline
#
# n = int(read())
# nums = [int(read()) for i in range(n)]
# dp = [0] * n
#
# if len(nums) <= 2:
#     print(sum(nums))
# else:
#     dp[0] = nums[0]
#     dp[1] = nums[0] + nums[1]
#     for i in range(2, n):
#         dp[i] = max(dp[i-3]+nums[i-1]+nums[i], dp[i-2]+nums[i])
#     print(dp[-1])


#9.
# n = int(input())
# dp = [0] * (n+1)
# for i in range(2, n+1):
#     dp[i] = dp[i-1] + 1
#     if i % 2 == 0:
#         dp[i] = min(dp[i], dp[i//2]+1)
#     if i % 3 == 0:
#         dp[i] = min(dp[i], dp[i//3]+1)
# print(dp[n])


#10.
# n = int(input())
#
# dp = [[0]*10 for _ in range(n+1)]
# for i in range(1, 10):
#     dp[1][i] = 1
#
# MOD = 1000000000
#
# for i in range(2, n+1):
#     for j in range(10):
#         if j == 0:
#             dp[i][j] = dp[i-1][1]
#         elif j == 9:
#             dp[i][j] = dp[i-1][8]
#         else:
#             dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
#
# print(sum(dp[n]) % MOD)


#11.
# n = int(input())
# cost = [int(input()) for i in range(n)]
#
# dp = [0] * n
# dp[0] = cost[0]
#
# if n > 1:
#     dp[1] = cost[0] + cost[1]
# if n > 2:
#     dp[2] = max(cost[0]+cost[2], cost[1]+cost[2], dp[1])
# for i in range(3, n):
#     dp[i] = max(dp[i-3]+cost[i-1]+cost[i], dp[i-2]+cost[i])
#     dp[i] = max(dp[i-1], dp[i])
# print(dp[n-1])


#12.
# n = int(input())
# nums = list(map(int, input().split()))
#
# dp = [1] * n
# for i in range(1, n):
#     for j in range(i):
#         if nums[i] > nums[j]:
#             dp[i] = max(dp[i], dp[j] + 1)
# print(max(dp))


#13.
n = int(input())
nums = list(map(int, input().split()))
reverse = nums[::-1]

dp1 = [1] * n
dp2 = [1] * n
for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp1[i] = max(dp1[i], dp1[j]+1)
        if reverse[i] > reverse[j]:
            dp2[i] = max(dp2[i], dp2[j]+1)

result = [0] * n
for i in range(n):
    result[i] = dp1[i] + dp2[n-i-1] - 1

print(max(result))
