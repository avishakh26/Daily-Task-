import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    # Step 1: c[i] = max(a[i], b[i])
    c = [max(a[i], b[i]) for i in range(n)]
    
    # Step 2: suffix maximum
    suf = [0] * n
    suf[-1] = c[-1]
    for i in range(n - 2, -1, -1):
        suf[i] = max(c[i], suf[i + 1])
    
    # Step 3: prefix sum of suffix max
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + suf[i]
    
    # Step 4: answer queries
    ans = []
    for _ in range(q):
        l, r = map(int, input().split())
        ans.append(str(pref[r] - pref[l - 1]))
    
    print(" ".join(ans))
