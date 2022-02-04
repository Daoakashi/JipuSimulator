import base64
import os
import time
flag = 0
save1 = ""
save2 = ""

while flag == 0:
    print("Welcome to the B64Encoder_Decoder")
    print("Write 'str' to encode a string or 'img' to encode a image")
    cmd = input()

#String Encrypt Decrypt
    
    if cmd == "str":    
        print("Choose '1' to Encode or '2' to Decode")
        print("And press Enter to confirm selection")
        cmd = input()
        error = 0

    if cmd == "1":
        str_var = input("Enter your string:")
        str_var_ascii = str_var.encode("ascii")
        ans64_ascii = base64.b64encode(str_var_ascii)
        ans64 = ans64_ascii.decode("ascii")
        print(f"Base64String = {ans64}")
        print("Do you want to save this")
        print("write ""yes"" if you want to save")
        save1 = input()
    else:
        error +=1
    
    if cmd == "2":
        str_var = input("Enter your string:")
        str_var_ascii = str_var.encode("ascii")
        ans64_ascii = base64.b64decode(str_var_ascii)
        ans64 = ans64_ascii.decode("ascii")
        print(f"Base64String = {ans64}")
        print("Do you want to save this")
        print("write ""yes"" if you want to save")
        save2 = input()
        
        #os.system('cls')
        #print("Error, please try again")
        #time.sleep(2)
        #os.system('cls')

    if (error > 1):
        os.system('cls')
        print("Error, please try again")
        time.sleep(2)
        os.system('cls')

#Write in File
    if save1 == "yes":
        f = open("B64_Archive_Encoder.txt", "a")
        f.write(f"{ans64}")
        f.close()

    if save2 == "yes":
        f = open("B64_Archive_Decoder.txt", "a")
        f.write(f"{ans64}")
        f.close()

#Image Encrypt Decrypt
    if cmd == "img":
        print("")
    
    
    
