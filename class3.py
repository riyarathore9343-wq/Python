#input and output operators

name= "harsh"
age = 24
#two ways of using variables inside print statement
print("hello your name is",name,"and your age is", age)

print(f"hello your name is {name} and your age is {age}")

#inputs
#make sure to use the type conversion while taking the inputs

input("what is your age : ")
age= int(input("what is your age : "))

print(f"your age after 10 years will be {age+10}")

#operators

a = intput("tell your first number :- ")
b = input("tell your second number:- ")

print(f"your sum is {a + b}")

print(a -b )
print(a*b)
print(int(a/b))
print(a//b) #floor divisin removes all the values after decimal point

print(5**2)
print(43%5)

#take inputs of three number P,R,T and calculate the simple interest

P = int(input("value of P"))
R = int(input("value of R"))
T = int(input("value of T"))

SI = (P*R*T)/100
print(f"your simple interest will be {SI}")

#now calculate compound interest
P = int(input("value pf p"))
R = int(input("value of r"))
T= int(input("value of T"))

ci =( P*(1+(R/100))**T)
ptint(f"your compound interest will be{ci}")


#assignment operators

#comparison operators

a = 12
b = 12
# (== , != , > , < , >= , <= )
print(a > b) 
print(a < b)

#strings

print("A">"B")

print("5" > "4")

#Logical operators
#(and , or , not )

print(12==12 , 12!= 34)

# and operator demANDS ONLY ONE THING THAT ALL THE COMPARISONS MUST BE TRUE
#THEN ONLY I WILL PROVIDE THE RESULT AS TRUE

print(12 ==12 and 34!= 34)

#OR OPERATORs - demands anyone comparison must be true then only i will provide true

print(12==13 or 45!= 45 or 23> 89 or 34== 34)

#not operators - it converts true to false and false to true

print(not 12 == 12)


