import random

Digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  

Lower_Case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
  
Upper_Case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
  
Symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
           '*', '(', ')', '<']

prePass = random.choice(Digits) + random.choice(Lower_Case) + random.choice(Upper_Case) + random.choice(Symbols)

length = int(input("Enter the length of password(Min 4): "))

appendEnd = Digits + Lower_Case + Upper_Case + Symbols

if length >= 4:
    finalPassword = ""
    for i in range(length-4):
        finalPassword += random.choice(random.choice(appendEnd))
    print(finalPassword+ prePass)
else:
    print("Enter min length of 4")
