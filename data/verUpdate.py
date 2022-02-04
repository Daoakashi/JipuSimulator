from tkinter import *
from tkinter.ttk import *
import time
import sys

def start():
    tasks = 100
    x = 0
    while(x<tasks):
        time.sleep(0.03)
        bar['value']+=1
        x+=1
        percent.set(str(int((x/tasks)*100))+"%")
        #text.set(str(x)+"/"+(tasks)+" Tasks Completed")
        root.update_idletasks()

    else:
        exit()
            
            
root = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(root,orient=HORIZONTAL,length=300)
bar.pack(pady=10)

percentLabel = Label(root,textvariable=percent).pack()

button = Button(root,text="download",command=start).pack()

LabelAdvertise = Label(root,text="Please do not click again, that may make some files corrupted").pack()

root.mainloop()

#Why did i do this
#Why after 64 times that doesn't work
#Maybe "THE BEING" is the problem


