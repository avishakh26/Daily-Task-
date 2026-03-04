a = int(input())


years = a // 365

r_days = a % 365

month = r_days // 30

days = r_days % 30

print(years,"ano(s)")
print(month,"mes(es)")
print(days,"dia(s)")
    
