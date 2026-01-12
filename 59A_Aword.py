a = str(input())

upper = 0
lower = 0

for ch in a:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower +=1
        
# print(upper)
# print(lower)
    
    
if upper > lower:
    print(a.upper())
elif upper < lower:
    print(a.lower())
elif upper == lower:
    print(a.lower())