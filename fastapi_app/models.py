def count(N):
    dp = [0] * (N + 1)

    dp[1] = A[1]

    for i in range(2, N + 1):
        dp[i] = min(A[i] + dp[i-1], B[i-1] + dp[i-2], C[i-2] + dp[i-3])

    return dp[N]

N = int(input())
A = []
B = []
C = []
for i in range(N+1):
    A[i] = int(input())
    B[i] = int(input())
    C[i] = int(input())
print(count(N))