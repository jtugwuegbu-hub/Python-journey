import os
import shutil
# path_Test_folder = r"/Users/justinugwuegbu/Desktop/Python-journey/Test_folder"
# path_empty_folder = r"/Users/justinugwuegbu/Desktop/Python-journey/empty _folder"

# try:
#     shutil.rmtree(path_Test_folder)
# except FileNotFoundError:
#     print("File not found")
# except OSError:
#     print("that function does no delete")
# except Exception as i:
#     print(f"Error is {i}")
# else:
#     print("folder deleted")

def move_file(file_name,destination):
    try:
        shutil.move(file_name,destination)
        print(f"file {file_name} moved")
    except FileNotFoundError:
        print("file not found")


try:
    user=int(input('1.move file\n2.delete file\n'))
except ValueError:
    print("enter a number")    

if user == 1:
    file_name=input("What file do you wish to move\n")
    destination=input("Where do you want to move it\n")
    move_file(file_name,destination)

elif user == 2:
    
    file_name=input("what file would you like to delete\n")
    path= os.getcwd()+f"/{file_name}"
    confirm=input(f"do you want to delete file {file_name} permanantly? 'y' or 'n' ")
    if confirm == "y":
        try:
            os.remove(path)
            print(f"file {file_name} deleted")
        except FileNotFoundError:
            print("File not found")
        except OSError:
            print("that function does no delete")
        except Exception as i:
            print(f"The error is {i}")
    elif confirm == "n":
        print("okay not permanatly deleted")
        destination="recycle"
        move_file(file_name,destination)
    else:
        print("enter valid input")