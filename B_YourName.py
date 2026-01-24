t = int(input())

for _ in range (t):
    
    a = int(input())
    b,c = map(str,input().split())
    
    
    if sorted(b) == sorted(c):
        print("YES")
    else:
        print("NO")
    

    # if a == c:
    #     print("YES")
        
    # else:
    #     print("NO")