import re

message=("[1][25:30]",
"[1][32:33]",
"[0][2]",
"[0][6]",
"[0][35]",
"[0][13]",
"[4][13:15]",
"[6][0:3]",
"[3][15:18]",
"[5][24:32]")

with open("secret.txt") as file:
    whole_message=""
    lines=file.readlines()
    
    for code in message:
        code_index= list(map(int,re.findall(r'\d+',code)))
        if len(code_index)== 2:
            secret_message= lines[code_index[0]][code_index[1]]
        else:
            secret_message= lines[code_index[0]][code_index[1]:code_index[2]+ 1]
        whole_message+=secret_message + " "
    
    print(whole_message)
    