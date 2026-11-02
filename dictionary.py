#DICTIONARY






#Methods in dictionary

#1.  .keys()







#3.  .items() -> both keys and values 
print(d.items())

#4.  .pop() -> key and remove both key and value
d.pop("Rohan")
print(d)

#5. .get() - > agar key present hai in dictionary 
#so we will get value for that key otherwise NONE or ANY MESSAGE 

d = {1:10 , 2:20 ,3:30 ,4:40}
print(d.get(5,"not found"))

#6. .update() -> merge two dictionary
a = {1:10 , 2:20 , 3:30}
b = {4:40 , 5:50 , 6:60}
a.update(b)
print(a)

#Questions 

#1 print keys 
d = {"Ravi :70 , Abhishek :33 , Rohan :12"}
 #method -1
print(d.keys)
#method-2
for i in d:
    print(i)
#method-3
for key , value in d.items():
    print(key)

#2 find the total of marks without using the SUM()
d = { "Ravi" : 70 , "Abhishek" :88 , "Rohan" : 12}
total = 0
for i in d.values():
    total = total + i

print(total)

 #3 Print students name who scored more than 50

for name , marks in d.items():
    if marks >=50:
        print(name)
 
 #4 Find the student with the highest marks 

top = 0
highest = 0
for name , marks in d.items():
    if marks > highest :
        highest = marks
        top = name
print(top , highest)

#5 Add bonus 5 marks to every student 

for i in d:
    d[i] = d[i] + 5
    #d[Ravi] = 70+ 5
print(d)

#575
n = len(candyType)
maxeat = n//2
different = set(candyType)
differentCount = len(different)
return min(differentCount , maxeat)

#2273
i =1
while i< len(words):
    if sorted(words[i]) == sorted(words[i-1]):
        words.pop(i)
    else:
        i = i+1
return words

#
Index = 3
prefix = word[0:Index +1]
revprefix = [::-1]
last = word[Index+1 ; len(word)]
ans = revprefix + last
return ans

for i in range (len(word)):
    if ch == word[i]
    index = i
    break
if index == -1:
    return word 

