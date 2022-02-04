import os
flag=0
lol=0
magnet = 0
def stop():
        quit()
print("Welcome to the menu.\nEnter a command or type ""help""")
while(flag==0):
        cmd=input("UserCommand:")
        lol
#Math Command
        if cmd=="math":
                os.system("start data\\math.py")

#Update Command
        if cmd=="update":
                os.system('start data\\verUpdate.py')
#Pyzip Command
        if cmd=="pyzip":
                os.system('start data\\pyzip.py')


#Quit command
                
        if cmd=="close" or cmd=="quit" or "exit" :
                exit and quit
#Password Deleter
        if cmd=="pwdel":
                if os.path.exists("data\\exa.dll"):
                        os.remove("data\\exa.dll")
                        print("Password Succesfully Reset!")
                else:
                        print("Password Already Reseted")
        

#B64 command
        if cmd == "base64":
                os.system("start data\\b64enc_dec.py")

#relauncher
        if cmd == "relaunch":
                os.system("start ..\\Launcher.py")
                

#EasterEggs
        if cmd == "engine_test":
                os.system("start data\\engine_data\\urs_engine.py")

#Cmd Command
                
        elif cmd == "cmd":
                os.system("start")
#Helloworld

        if cmd =="helloworld" and magnet == 0:
                print("Hello Operator what's your name ?")
                name = input()
                magnet +=1
                
        if cmd =="helloworld" and magnet >= 1:
                print(f"Hello {name}")
                
#Help Command
        if cmd=="help":
                print("math - a command to start the calculator API")
                print("close,exit,quit - quit the program (obsolete)")
                print("matrix - launch a little funny matrix program")
                print("relaunch - relaunch the program to verify files again (obsolete)")
                print("update - Update the program,(always in testing)")
                print("base64 - Open a Base64 Encoder and Decoder")
                print("pyzip - Open a API whom extract or ancrypt a zip file(no more use of winrar)")
                print("pwdel - Delete and reset the current password of the launcher")
#Matrix Command                
        if cmd=="matrix":
                os.system("start data\\Matrix.exe")
        
if lol == 1:                
        print("This is not a valid command, pls try again")
