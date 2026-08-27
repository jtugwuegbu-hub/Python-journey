import os
import shutil

def create_file(file_name,data):
        with open(file_name, "w") as file:
            file.write(data)

def read_file(file_name):
    try:
        with open(file_name, "r") as file:
         print(file.read())
    except FileNotFoundError:
        print("file not found")
def move_file(file_name,destination):
    try:
        shutil.move(file_name,destination)
    except FileNotFoundError:
        print("file not found")
def copy_file(file_name,destination):
    try:
        shutil.copy2(file_name,destination)
    except FileNotFoundError:
        print("file not found")

def main():
    try:
        user=int(input("Select a number\n1.create\n2.read\n3.move\n4.copy\n"))
    except ValueError:
        print("enter a number")
        return
    if user == 1:
        file_name=input("What is the file you wish to create\n")
        data=input("What do you want to put in this file\n")
        create_file(file_name,data)
    elif user == 2:
        file_name=input("what file do you wish to read\n")
        read_file(file_name)
    elif user == 3:
        file_name=input("What file do you wish to move\n")
        destination=input("Where do you want to move it\n")
        move_file(file_name,destination)
    elif user == 4:
        file_name=input("What file do you wish to copy\n")
        destination=input("destination of copied file\n")
        copy_file(file_name,destination)
    else:
        print("invalid inpput")

main()