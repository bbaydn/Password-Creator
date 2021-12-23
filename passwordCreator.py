import random
import string
# We will use these two libraries for creating random passwords

strength = int(input("Please select the strength level of the password you want to create \n(1 for weak, 3 for strong)\n"))
length = int(input("Please select the length of the password you want to create\n "))
# User will give some information about password

passwordList = []
# While creating the password, random characters will be selected and a list  will be created with them.
# That list named as passwordList

def listToString(passwordList):
    str1 = ""
    for a in passwordList:
        str1+=a
    return str1
# This is a function that makes conversation from list to string


if strength == 1:
    for i in range(length):
        char=random.choice(string.ascii_letters)
        passwordList.append(char)
    print("Your level-1 password is: "+listToString(passwordList))
# If user wants a weak password, this loop will run
# in this loop, I use just letters for creating password
# string.ascii_letters will give just letters for program

elif strength ==2:
    for i in range(length):
        char=random.choice(string.hexdigits)
        passwordList.append(char)
    print("Your level-2 password is: "+listToString(passwordList))
# If user wants a mid-level password this loop will run
# in this loop, I use letters and numbers for creating password
# string.hexdigits has letters and numbers

elif strength ==3:
    for i in range(length):
        char=random.choice(string.ascii_letters + string.punctuation)
        passwordList.append(char)
    print("Your level-3 password is: "+listToString(passwordList))
# If user wants a high level password this loop will run
# in this loop, I use letters, numbers and special characters for creating password
# string.ascii_letters + string.punctuation has letters, numbers and special characters
     
else:
    print("This level password can not be created.")
# If something goes wrong this is program's output.
# Maybe later, If I want to change something in this program
# I can change this text message
# Maybe the text message could be "No can Dosville babydoll."
#



