agenda_file="/Users/justinugwuegbu/Desktop/Python-journey/folder_Q/agenda.txt"
name = input("Who do you want to search for? ")

found = False

with open(agenda_file) as file:
    for line in file:
        date, person, time = line.strip().split(";")

        if person.lower() == name.lower():
            print(f"Date: {date}")
            print(f"Name: {person}")
            print(f"Time: {time}")
            found = True
            break

if not found:
    print("Person not found.")
    
    date = input("Enter date: ")
    time = input("Enter time: ")

    with open(agenda_file, "a") as file:
        file.write(f"{date};{name};{time}\n")

    print("Person added!")