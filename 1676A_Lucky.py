t = int(input())

for _ in range(t):
    s = input().strip()  
    
    first_sum = sum(int(d) for d in s[:3])
    last_sum  = sum(int(d) for d in s[3:])
    
    if first_sum == last_sum:
        print("YES")
    else:
        print("NO")
        
        
        