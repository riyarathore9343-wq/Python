#CONTROL FLOW STATEMENT

#if else statement

age = int(input("tell your age :-"))

if age >= 18:

    print("you can vote")
    print("thankyou visit again")

else:
    print("you cannot vote")

    #if elif ladder

money = int(input("whats the value:-"))

if money == 100:
    print("i will have sandwich")
elif money == 200:
    print("i will have chole kulche")
else:
    print("i will have full couse meal")
#1)
a = int(input("first number"))
b = int(input("second number"))

if a > b:
    print(f"{a}is greater than {b}")

elif b > a:
    print(f"{b} is grater than {a}")

else:
    print("both are equal")

#2)
m = int(input("enter your gender:- male"))
f = int(input("enter your gender:- female"))

if m is male:
    print("{m} is male")
else:
    print({f} is female)


gen = input("tell your gender in character (m or f)")
if gen == "M" or gen == "m":
    print("GOOD MORNING SIR")
else:
    print("GOOD MORNING MAM")

elif gen == "F" OR gen == "f":
    print("good morning others")
