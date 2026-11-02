#FOLDER
#mkdir - to create a new folder/dictonary
#rmdir - to remove any folder/dictionary

import os

os.mkdir("Hello")
os.rmdir("Hello")

#FILES
X - this will only create the file and if already exists we will get an error back
W - agar file exist nhi kar rhi hai to this mode will create one and
 then insert the content inside the file
R -
w,a,r,x

#Mode 1:
x - just to create the FILES
open("Garba.txt", "x")

#Mode 2
w - if there is any content inside the file so the new one will replace the old one
file = open("Garba.txt","w")
file.write("khelo garba khub khelo")

#Mode 3
a - add the text at the last
file = open("Garba.txt","a")
file.write("\nThis message is newly added")
  
#Mode 4
r - read the content nside of the file
file = open("Garba.txt", "r")
print(file.read())

with open("sample.txt" , "w") as file:
    file.write("This is new file")

# file automatically open aur close ho jayegi is command se

#CRUD - CREATE , READ , UPDATE , DELETE
os.remove("sample.txt")

from pathlib import path
import os

def create_folder():
    name = input("Tell your folder name")
    p = path(name)

    if p.exists():
        print("this folder name is already exists please try again")
        create_folder()
    else:
        p.mkdir()
        print("folder created sucessfully !")

def read_folder():
    p = path("") #empty string will provide path for the existing file
    names = list(p.rglob("*"))


    for i in range(len(names)):
        print(f"{i+1} : {names[i]}")

def update_folder():
    read_folder()
    name = input("Which folder you want to update:- ")
    old_p = Path(name)

    if old_p.exists():
        new_name = input("Tell new folder name")
        new_p = Path(new_name)
        old_p.rename(new_p)
        print("folder name changes sucessfully")
    else:
        print("no such folder exists please try again")
        update_folder()

def delete_folder ()
    name = input("Tell your folder name")
    p = Path(name)

    if p.exists():
        p.rmdir()
        print("folder deleted successfully")
        create_folder()
    else:
        p.rmdirr()
        print("folder did not found")

def create_file():
    name = input("Tell your file name with extension")
    p = Path(name)

    if p.exists():
        print("file already exists please try again")
        create_file()
    else:
        with open(p,"w") as fs:
            data = input("Enter what you want to write")
            file.write(data)
            print("successfully ceated")

def read_file():
    name = input("Tell your file name with extensions")
    p = Path(name)
    if p.exists() and p.is_file():
        with open(p,"r") as file:
            data = file.read()
            print("\n\n\n Your file data is\n\n\n")
            print(data)

def update_file():
    names = read_folder()
    for i in names:
        i = str(i)
        p = Path(i)
        if p.is_file():
            print(i)

     name = input("which file you want to update:-")
     p = Path(name)

     if p.exists() and p.is_file():
        
    else:

def delete_file()
name = input("Tell your file name with extension")
    p = Path(name)

    if p.exists() and p.is_file() :
        os.remove(p)
        print("file deleted successfully")
    else:
        print("no such file exists please try again")
        delete_file()


    
        
    

print("Press 1 for Creating a new folder :")
print("Press 2 for Reading any folder:")
print("Press 3 for Updating any folder :")
print("Press 4 for deleting any folder:")

print("Press 5 for Creating a file :")
print("Press 6 for Reading any file:")
print("Press 7 for Updating any file :")
print("Press 8 for deleting any file :")



res = int(input("Tell your response:-"))

if res == 1:
    create_folder()

if res == 2:
    read_folder()

if res == 3:
    update_folder()

if res== 4:
    delete_folder()

if res == 5:
    create_file()

if res == 6:
    read_file()

if res == 7:
    update_file()

if res == 8:
    delete_file()
    