t = int(input())

for _ in range(t):
    a = int(input())
    b = str(input())
    c = "Timur"
    
    if a != 5:
        print("NO")
    else:
        if sorted(b) == sorted(c):
            print("YES")
        else:
            print("NO")