#LOOPS
#while loop
#automating a task
a = range(1,5,1)
print(a)

for i in a:
    print("hello world")

for i in range(1,5,1):
    print(i)

for i in range(10,81,1):
    print(i)

for i in range(-52,40,1):
    print(i)

for i in range(100,-101,-1):
    print(i)

for i in range(7,71,7):
    print(i)

n = int(input("tell your number :-"))
for i in range(n,n*10+1,n):
    print(i)

#take an input n print natural number upto n
n = int(input("tell your number"))
for i in range(1,n+1,):
    print(i)

#take n as the input and print numbers from n to 1

n = int(input("tell your number"))
for i in range(n,0,-1):
    print(i)

#take n as input print the sum of natural numbers till n

n = int(input("take your number"))
sum = 0
for i in range(1,n+1,1):
    sum = sum + i

print(sum)

#take iput n and print the factorial
n = int(input("tell your number"))
fact = 1
for i in range(1,n+1,1):
    fact = fact*i

print(fact)

#take n as the input print the factors of n

n = int(input("give your number"))

for i in range(1,n+1):
    if n % i ==0:
        print(i)

n = int(input("give your number"))

count = 0
for i in range(1,n+1): 
    if n% i == 0:
        count+= 1
print(f"factors on{n}are :{count}")

# check if a number is prime or not

n = int(input("give your number"))
#1 and number itself are factors.

for i in range(2,n):
    if n % i == 0:
        print(f"{n}is a composite number")
        break
else:
    print("{n} is a prime nuumber")

#upper and lower concept

name = "abhiSHEK"

upper = 0
lower = 0

for i in name:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower+= 1

print(f"upper case letters:{upper}")
print(f"lower case letters{lower}")

#while loop

"kaha se jaana hai -> kab takk jaana hai -> kaise jaaana hai"
" while jab tak yeh condition true hai:
    tab tak yeh code chlega.""


# print from 1 to 50 using while loop

i = 1
while i <= 10:
    print(i)
    i = i + 1

#print from 10 to 1 using while loop

i = 10
while >= 1:
    print(i)
    i = i - 1

# user se password mangte raho jab tak sahi passwoed "Abhishek123" nahi mil jaaaye 

password = ""
while password != "Abhishek123":
    password = input("enter password:"). #Abhishek123
print("access granted")


#print table of any number which user gives  using whilwe loop

n = int(input('enter your number'))
i = 1
while i <= 10:
    print(n* i)
    i = i + 1

#print even numbers from 2 to 20

i = 2
while i <= 20:
    print(i)
    i = i + 2

#sum of all even numbers from 2 to 20
i = 2
sum = 0
while sum <= 20:
    sum = sum + i
    print(i)
    i = i + 2
print(f"sum of even number from 2 to 20 is {sum}")

#print a number in reverse order
# %  last digit ko print krwana 
# // last digit permanent remove ho jayegi

n = 1234
while n != 0 :
    print(n % 10)
    n = n// 10

#
n = 1234
a = 0
while n > 0:
    last = n % 10
    a = a*10 + last
    n = n // 10
print(a)

n = 1234
a = 0 
count= 0
while n > 0:
    last =  n % 10 
    a = a*10 + last 
    count = count + 1
    n = n // 10
print(a)
print(count)











