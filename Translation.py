s = str(input().lower())
t = str(input().lower())

result = "".join(reversed(t))

if result == s:
    print("YES")
elif s != t:
    print("NO")
elif s == t:
    print("NO")
else:
    ("NO")