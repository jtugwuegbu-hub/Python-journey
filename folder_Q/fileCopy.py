import shutil
import os

path=os.getcwd()
print(path)
shutil.copy2("agenda.txt","folder_Q/agenda_copy.txt")


with open ("agenda_copy.txt") as file:
    agenda= file.read()

print(agenda)
    

