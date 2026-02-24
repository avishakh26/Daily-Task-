import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # Base contribution: all subarrays contribute at least 1
    ans = n * (n + 1) // 2

    # Add contributions from breaks
    for i in range(1, n):
        if a[i] != a[i - 1] + 1:
            ans += i * (n - i)

    print(ans)