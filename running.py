

a = int(input())


for _ in range(a):

    n = int(input())
    l = list(map(int, input().split()))
    
    
    if l[0] == 1 or l[-1] == 1:
        print("Alice")
    else:
        print("Bob")

