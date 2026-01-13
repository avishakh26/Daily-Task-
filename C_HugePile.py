import sys

def solve():
    try:
        line = sys.stdin.readline()
        if not line: return
        n, k = map(int, line.split())
    except ValueError:
        return

    if n == k:
        print(0)
        return

    current_piles = {n}
    minutes = 0
    
    while current_piles:
        minutes += 1
        next_piles = set()
        
        for x in current_piles:
            if x < 2: 
                continue
        
            p1 = x // 2
            p2 = (x + 1) // 2
            
            if p1 == k or p2 == k:
                print(minutes)
                return
            
            if p1 > k:
                next_piles.add(p1)
            if p2 > k:
                next_piles.add(p2)
                
        current_piles = next_piles
        if not current_piles:
            break
            
    print("-1")

line = sys.stdin.readline()
if line:
    t_str = line.strip()
    if t_str:
        t = int(t_str)
        for _ in range(t):
            solve()