
t = int(input())

for _ in range(t):
    a,b,c = map(int,input().split())
    
    anna_moves = a + (c+1) // 2
    katie_moves = b + c // 2
    
    if anna_moves > katie_moves:
        print("First")
    else:
        print("Second")
        
        
        