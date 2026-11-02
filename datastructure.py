#data structure


























#. .remove() - remove any value from the list
a = [10,20,30,10,40,50]
a.remove(10)
print(a)

#5. .pop() - remone any value on the basis of index
a = [10,20,30,10,40,50]
a.pop(3)
print(a)

#6. .clear() - removes every element and gives empty list
a = [10,20,30,40]
a.clear()
print(a)


#
l = [10,20,30,40,50,60,70,80]
for i in range (len(l)):
    print(i , l[i])

#
l = [10,20,30,40,50,60,70,80]
for i in range (len(l)-1,-1,-1):
    print(i , l[i])

#
l = [10,20,30,40,50,60,70,80]
l2 = []
for i in range(len(l)-1,-1,-1):
    l2.append(l[i])
    # l2.insert(len(l2),l[i])
print(l2)

#print list elements inreverse order
#reverse the list using the two pointers approach

arr = [10,20,30,40,50]
n = len(arr)
mid = n//2
for i in range (mid):
    arr[i] , arr[n-i-1] = arr[n-i-1] , arr[i]
print(arr)


#Print positive and negative elements of a list
#Print positive and negative separately
#Ignore zero

print("positive:")
for elem in array:
    if elem>0:
        print(elem)

print("negative:")
for elem in array:
    if elem<0:
        print(elem)


#mean of list elements
#calculate the average of all elements in a list

arr = [10,20,30,40]
n = len(arr)
sum = 0
for elem in arr:
    sum += elem
print(f"mean is {sum/n}")

#Find the greatest element and its index

arr = [2,96,69,77,145,20]
max = arr[0]
index = 0
for i in range (1,len(arrr)):
    elem = arr[i]
    if elem > max:
        max = elem
        index= i
print(f"max is{max} at index {index}")

#find the missing number
#a list contains from 1 to N ,but one number is missing .
# Write a program to find the missing number


arr = [1,2,4,5]
n = len(arr)
og_n = n +1
og_sum = ((og_n)*(og_n+1)) //2
real_sum = 0
for elem in arr:
    real_sum += elem

misiing = og_sum - real_sum
print(missing)



#Check whether a list is sorted or not
#check if the list elelments are arrnged in ascending order

arr = [10,30,20,40,50]
is_sorted = True
n = len(arr)
for i in range(0,n-1):
    if arr[i] > arr[i+1]:
        is_sorted = False
        break

if is_sorted:
    print("list is sorted")
else:
    print("list is unsorted")

#Palindromis list
#Check whether the list reads rhe same from front and back

arr = [2,3,15,15,3,2]
n = len(arr)
is_palindrome = True
for i in range(n//2):
    if arr[i] != arr[n-i-1]:
        is_palindrome = False
        break
if is_palindrome:
    print("list is palindrome")
else:
    print("list is not palindrome")


#we can also do this using concatination method

#SPECIAL ALGORITHM
#sort a list in ascending order (bubble shot)

arr = [64,34,25,12,22,11,9]
n = len(arr)

for i in range (n):
    for j in range(n-i-1): #n-i-2 tkk jayenge pr range k liye n-i-2+1 tkk jayenge
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1] , arr[j]

print(arr)

#SELECTION SHORT




