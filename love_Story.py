t = int(input())

for _ in range(t):
    
    s = str(input())
    
    a = "codeforces"
    
    b = s.lower()
    
    count = 0
    
    for i in range(10):
        
        if s[i] !=  a[i]:
            count += 1
            
    print(count)
        
