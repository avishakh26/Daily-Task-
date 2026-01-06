string = str (input())

string.lower()

seperate = set(string)


count = len (seperate)



if count % 2 == 0:

    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")