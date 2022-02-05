from zipfile import ZipFile
import time
from tkinter import filedialog


print("'Extract(1)' or 'Encrypt(2)'")
cmd = input()
if cmd == "1":
    print("specify the file")
    f = filedialog.askopenfilename(filetypes= (("zip archives","*.zip"),
                                                  ("all files","*.*")))
    with ZipFile(f,"r") as zip:
        zip.printdir()

        print(f"Extracting {f} contents files")
        zip.extractall(path="Extracted\\")
        print("Done")
        print("The Extracted file is in JipuSimulator 'Extracted' Directory")
    

