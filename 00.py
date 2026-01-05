
A = int(input("Enter the date :"))

B = input("Enter the month name :")


today_spend = []


for info in range(500):

    time   = input("Enter the time: ")
    
    amount = input("Enter the amount: ")


    if time == "end":
        break
    today_spend.append(amount)


print(today_spend)


sum = 0
for i in today_spend:
    sum += int(i)


print(sum)

with open("00Calculator.txt","a") as saver:
    saver.write(f"{A} {B} = {sum} taka \n ")
    
