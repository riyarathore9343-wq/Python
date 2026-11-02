#loops questions

#
n = int(input("enter your number"))
count = 0
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 ==0 :
        count += 1
print(f"count: {count}")

#
n = int(input("enter your number"))
fact = 1
for i in range(1, n+1):
    fact = fact*i
print(f"{n}! is {fact}")

#
n = int(input("enter the number"))
temp = n
sum = 0
while n > 0:
    digit = n%10
    fact  = 1
    for i in range(1, digit+1):
        fact *=i
    sum += fact
    n = n//10
if temp == sum:
    print("strong number")
else:
    print("not a strong number")


#
n = int(input("enter your number"))
sum = 0
for i in range (1,n+1):
    if i %2 != 0:
        sum += i
print(f"sum of odd numbers from 1 to {n} is {sum}")

#fabonacci series
n = int(input("enter the number"))
a = 0 
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c

#
text = input("enter the text")
#Abhishek
count = 0

for ch in text:
    if ch in "aeiouAEIOU":
        count += 1
print(f"total words: {count}")

#
text = input("enter the string")
target = input("enter the target")
count = 0
for ch in text:
    if ch == target:
        count += 1
print(count)

#atm machine 

#input should be taken when user have left the attempts

attempts = 3
has_access_mainmenu = False
while attempt > 0:
    entered_pin = int(input("enter the pin"))
    if entered_pin == 1234:
        #main menu opens
        has_access_mainmenu = True
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"ncorrect pin! you have {attempts} ttempts remaining")
        else:
            print("card blocked")

if has_access_mainmenu == True:
    while True:
        print("ATM Menu")
        print("1 ->check balance")
        print("2 -> eposit cash")
        print("3 ->withdraw cash ")
        print("4 ->exit")
        choice = int(input("enter the choice"))

        if choice == 1:
            




