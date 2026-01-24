t = int(input())

for _ in range(t):
    a = int(input())
    b = list(map(int, input().split()))
    
    
    even = []
    odd = []
    
    
    for i in b:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
            
            
    if even and odd:
            b.sort()
            
    
    
    print(*b)
    
