A, S, B, Q, C = input().split()

A = int(A)
B = int(B)
C = int(C)



if S == '+':
    result = A+B
elif S == '-':
    result = A-B
elif S == '*':
    result = A*B
elif S == '/':
    result = A/B
    
    
if result == C:
    print("Yes")
else:
    print(result)
    