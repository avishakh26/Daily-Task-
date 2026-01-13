import sys

# Precompute combinations for efficiency (up to d=30 or 60)
MAX_D = 62
C = [[0] * MAX_D for _ in range(MAX_D)]
for i in range(MAX_D):
    C[i][0] = 1
    for j in range(1, i + 1):
        C[i][j] = C[i-1][j-1] + C[i-1][j]

def solve_bob():
    line = sys.stdin.readline().split()
    if not line: return
    n, k = map(int, line)
    
    # n = 2^d. Find d.
    d = n.bit_length() - 1
    
    # Alice can win if moves(a) <= k. 
    # We want to count a in [1, n] where moves(a) > k.
    # moves(a) = (highest_bit_index) + (count_of_set_bits)
    
    can_win_count = 0
    
    # Check all possible numbers from 1 to 2^d
    # 1. Check a = n (which is 2^d)
    # moves(2^d) = d + 1
    if d + 1 <= k:
        can_win_count += 1
        
    # 2. Check numbers a < 2^d
    # Iterate through each possible highest bit index 'i'
    for i in range(d):
        # a has highest bit at index i. moves(a) = i + 1 + (number of other set bits)
        # We need: i + 1 + (other_bits) <= k  =>  other_bits <= k - i - 1
        max_other_bits = k - i - 1
        if max_other_bits < 0:
            continue
            
        # From the 'i' available lower slots, choose 'j' bits
        for j in range(min(i, max_other_bits) + 1):
            can_win_count += C[i][j]
            
    # Result is total numbers minus those Alice can win with
    print(n - can_win_count)

line = sys.stdin.readline()
if line:
    t = int(line.strip())
    for _ in range(t):
        solve_bob()