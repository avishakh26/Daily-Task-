a = input()

nums = sorted(map(int, a.split("+")))
sum = "+".join(map(str, nums))

print(sum)