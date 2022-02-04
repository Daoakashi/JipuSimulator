import pathlib
import time
from tkinter import *
from tkinter.ttk import *
import os
tasks = 0
#Def the password + password check
def pwC():
    print("New Password:")
    
    key=input()

    with open("data\\exa.dll","w") as verify_key: #Write a pasword file
                verify_key.write(f"{key}")
                
    with open("data\\exa.dll","r") as verify_key: #Read the file and see if the password is the same as typed
                key = verify_key.read()                

    flag = 3
    while flag > 0:
        print("Password ?")
        f = input()
    
        if key == f :
            print("Acces Granted")
            break

        else:
            flag -= 1
            print("Acces Denied")
            print(flag, "Attempt left")
        

        if (flag == 0):
            quit()


os.system('cls')   
def pwV():
    with open("data\\exa.dll","r") as verify_key: #Read the file and see if the password is the same as typed
                key = verify_key.read()                

    flag = 3
    while flag > 0:
        print("Password ?")
        f = input()
    
        if key == f :
            print("Acces Granted")
            break

        else:
            flag -= 1
            print("Acces Denied")
            print(flag, "Attempt left")
        

        if (flag == 0):
            quit()

#See if the password exists
os.system('cls')
pw = pathlib.Path("data\\exa.dll")
if pw.is_file():
    pwV() #Non Exist
else:
    pwC() #Exist   

#Interface
print("Program Created by OniQuinoxTeam")
print("###########################################")
print("#  ver 1.0.0                              #")
print("#        Welcome to                       #")
print("#             JIPU Interface              #")
print("#                                         #")
print("#                                         #")
print("###########################################")
time.sleep(0.5)
print("Verifying files...")


###Path Defined

path = pathlib.Path("data\\menu.py")

path_2 = pathlib.Path("data\\game.py")

path_3 = pathlib.Path("data\\verUpdate.py")

path_4 = pathlib.Path("data\\math.py")

path_5 = pathlib.Path("data\\broken.txt")

path_6 = pathlib.Path("data\\Matrix.bat")

path_7 = pathlib.Path("data\\Matrix.exe")

path_you = pathlib.Path("data\\malware\\YOU.bat") #Change to exe

path_8 = pathlib.Path("data\\b64enc_dec.py")

path_9 = pathlib.Path("data\\pyzip.py")

##Tasks files


if path.is_file():
    tasks += 1
    print("File",path,"Detected")
    
if path_2.is_file():
    tasks += 1
    print("File",path_2,"Detected")

if path_3.is_file():
    tasks += 1
    print("File",path_3,"Detected")

if path_4.is_file():
    tasks += 1
    print("File",path_4,"Detected")

if path_5.is_file():
    tasks += 1
    print("File",path_5,"Detected")

if path_6.is_file():
    tasks += 1
    print("File",path_6,"Detected")

if path_7.is_file():
    tasks += 1
    print("File",path_7,"Detected")

if path_you.is_file():
    tasks += 1
    print("File",path_you,"Detected")

if path_8.is_file():
    tasks += 1
    print("File",path_8,"Detected")

if path_9.is_file():
    tasks += 1
    print("File",path_9,"Detected")




   
#Waiting for response
time.sleep(1)

#Tasks are finished

if tasks == 10: #Change Task when i add a new file
    print("Files Verifyied")
    print("Opening menu.py in few seconds...")
    time.sleep(3)
    os.system("start data\\menu.py")
else:
    print("Some files are missing, pls download the Jipu Simulator and try again")
time.sleep(3)
