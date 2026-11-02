#FUNCTIONS

a = 121
rev = 0 
copy = a
while a != 0 :
    rev = rev * 10 + a%10
    a = a//10

if copy == rev:
    print("pallindrome")
else:
    print("not a pallindrome")

#how functions are created
#inbuild function
#print()
#input()
#int()
#float()
#bool()
#range()
#str()
#len()

#user defined functions

#defining a function
def hello():
    print("how are you")

#calling a function
hello()

#return

def hey():  
    return "how are you" #return the value to the calling block

a = hey() #calling block captures the value
print(a)

#parameters and arguments

def addition(a,b):  #you accept the parameters
        print(a +b)

addition(10,20) #and you provide the arguments to the parameters
addition(50, 50)

def palindrome(a):
    rev = 0
    copy = a
    while a != 0:
        rev = rev *10 + a%10
        a = a//10

    if copy == rev :
        print(copy)
    

for i in range(1,1000):
    palindrome(i)

#default parameters
#when you assign any value to the parameters this is called default parameters

def hello(a,b,c,d,e = 30):
    print(a +b)

hello(50,50,20,56)

#default prameters
#you cannot write position or normal parameters after default parameters

def information(name, age, number):
    print("hello your info is")
    print(name)
    print(age)
    print(number)

information(number= 9343187450, name = "RIYA , age = 19")
information()

#print numbers from 1 to 30
#you cannot use for and while loop
#you cannot use print statement more than 1



#recursion - a function calling function itself
def numbers (n):
    if n == 999:
        return
    print(n)
    numbers(n+1)

numbers(1)

def number(n):
    if n == 31:
        return
    number(n+1)
    print(n)

numbers(1)








