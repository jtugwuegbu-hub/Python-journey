import shutil

def copy_file():

    while True:

        source = input("Enter the file you want to copy: ")
        destination = input("Enter the name of the new file: ")

        try:
            shutil.copy2(source, destination)
            print("File copied successfully.")
            break

        except FileNotFoundError:
            print("File does not exist. Try again.")


def main():

    name = input("Enter customer name: ")
    id = input("Enter customer ID: ")
    balance = input("Enter starting bank balance: ")

    with open("customer_copy.txt", "w") as file:
        file.write(name + "\n")
        file.write(id + "\n")
        file.write(balance + "\n")

    copy_file()

main()
