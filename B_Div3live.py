t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    
    
    
    for i in range(n):
        
        mx = max(p[i:])
        
        if mx > p[i]:
            
            j = n - 1
            while p[j] != mx:
                j -= 1
            
           
            p[i:j+1] = reversed(p[i:j+1])
            break
    
    print(*p)
