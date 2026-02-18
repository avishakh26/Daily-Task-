t = int(input())


for _ in range(t):
    
    
    n, k = map(int, input().split())
    s = input().strip()

    freq = [0] * 26
    for ch in s:
        freq[ord(ch) - ord('a')] += 1

  
    odd = 0
    for f in freq:
        if f % 2 == 1:
            odd += 1

 
    need = max(0, odd - 1)

    if k >= need:
        print("YES")
    else:
        print("NO")
