
# t = int(input())
# for _ in range(t):
#     s, k, m = map(int, input().split())
#     last_flip = (m // k) * k
#     print(max(0, last_flip + s - m))



# t = int(input())
# for _ in range(t):
#     s, k, m = map(int, input().split())
#     x = m % k
#     print(max(0, min(x, s - x)))


# t = int(input())
# for _ in range(t):
#     s, k, m = map(int, input().split())
#     x = m % k
#     if x == 0:
#         print(s)
#     else:
#         print(max(0, s - x))

import sys

def solve():
    # Read s, k, m
    try:
        line = sys.stdin.readline()
        if not line: return
        s, k, m = map(int, line.split())
    except ValueError:
        return

    num_flips = m // k
    time_since_last_flip = m % k
    
    if k >= s:
        # Sand always resets to s after every flip
        start_sand = s
    else:
        # Sand alternates between s and k
        # Flip 0: s, Flip 1: k, Flip 2: s, Flip 3: k...
        if num_flips % 2 == 0:
            start_sand = s
        else:
            start_sand = k
            
    print(max(0, start_sand - time_since_last_flip))

line = sys.stdin.readline()
if line:
    t = int(line)
    for _ in range(t):
        solve()